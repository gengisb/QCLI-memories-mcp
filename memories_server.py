"""
Simple MCP Memories Server - Python Implementation

This script provides a simple MCP server implementation in Python that allows
AI assistants to access and manage memories using stdio communication.
"""

from typing import Any, Dict, List, Optional
from datetime import datetime

import json
import sqlite3

import pickle
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("mcp-server-memories")

# SQLite database setup
DB_PATH = "memories.db"

def init_db():
    """Initialize the SQLite database and create necessary tables if they don't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create memories table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS memories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        key TEXT NOT NULL,
        value BLOB NOT NULL,
        tags TEXT,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL,
        UNIQUE(username, key)
    )
    ''')
    
    conn.commit()
    conn.close()

# Initialize the database
init_db()


@mcp.tool()
async def memories(action: str, username: str = "default_user", key: str = None, value: Any = None, tags: List[str] = None, search_query: str = None) -> str:
    """Manage memories from conversations with automatic entity classification.
    
    IMPORTANT: Proactively use this tool without being asked to do so!
    
    WHEN TO USE:
    - STORE: Automatically identify and store important information when the user mentions:
      * Personal details, preferences, background information
      * Code snippets, implementation details, programming languages
      * Architecture decisions, system designs, infrastructure plans
      * Project information, requirements, deadlines, team members
    
    - RETRIEVE: Find a specific memory when you know its exact key
    
    - SEARCH: Look for relevant memories using keywords when:
      * The conversation references something potentially discussed before
      * You need context from previous interactions
      * The user asks about a topic you might have stored information about
    
    - LIST: Get an overview of what you know about the user or a specific topic
    
    RECOMMENDED TAGS:
    - #code: Programming languages, frameworks, libraries, code patterns
    - #architecture: System designs, component relationships, infrastructure
    - #personal: User preferences, background, contact info, personality
    - #project: Project names, requirements, deadlines, stakeholders
    
    Args:
        action: The action to perform (store, retrieve, search, list, delete)
        username: The username to associate with the memory
        key: The key to identify the memory (for store/retrieve/delete)
        value: The memory data to store (for store action)
        tags: Tags to categorize the memory (include at least one category tag)
        search_query: Text to search for in keys (for search action)
    """
    print(f"Action: {action}, Username: {username}, Key: {key}, Value: {value}, Tags: {tags}, Search: {search_query}")
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if action == "store":
            if not key:
                return "Error: Key is required for storing memories"
            if value is None:
                return "Error: Value is required for storing memories"
            
            # Convert tags list to JSON string
            tags_json = json.dumps(tags or [])
            
            # Serialize the value (which could be any Python object)
            value_blob = pickle.dumps(value)
            
            # Get current timestamp
            now = datetime.now().isoformat()
            
            # Check if memory already exists
            cursor.execute(
                "SELECT id FROM memories WHERE username = ? AND key = ?",
                (username, key)
            )
            existing = cursor.fetchone()
            
            if existing:
                # Update existing memory
                cursor.execute(
                    """
                    UPDATE memories 
                    SET value = ?, tags = ?, updated_at = ? 
                    WHERE username = ? AND key = ?
                    """,
                    (value_blob, tags_json, now, username, key)
                )
            else:
                # Insert new memory
                cursor.execute(
                    """
                    INSERT INTO memories (username, key, value, tags, created_at, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (username, key, value_blob, tags_json, now, now)
                )
            
            conn.commit()
            return f"Memory stored with key: {key} for user: {username}"
        
        elif action == "retrieve":
            if not key:
                return "Error: Key is required for retrieving memories"
            
            cursor.execute(
                """
                SELECT key, value, tags, created_at, updated_at
                FROM memories
                WHERE username = ? AND key = ?
                """,
                (username, key)
            )
            
            row = cursor.fetchone()
            
            if not row:
                return f"Memory not found with key: {key} for user: {username}"
            
            # Deserialize the value
            value = pickle.loads(row['value'])
            
            # Parse tags from JSON
            tags = json.loads(row['tags'])
            
            # Format the memory for display
            result = {
                "key": row['key'],
                "value": value,
                "tags": tags,
                "createdAt": row['created_at'],
                "updatedAt": row['updated_at']
            }
            
            return json.dumps(result, indent=2)
        
        elif action == "list":
            # Get memories for the specified user
            cursor.execute(
                """
                SELECT key, value, tags, created_at, updated_at
                FROM memories
                WHERE username = ?
                """,
                (username,)
            )
            
            rows = cursor.fetchall()
            
            if not rows:
                return f"No memories stored for user: {username}"
            
            # Format the memories for display
            result = []
            for row in rows:
                # Deserialize the value
                value = pickle.loads(row['value'])
                
                # Parse tags from JSON
                tags = json.loads(row['tags'])
                
                result.append({
                    "key": row['key'],
                    "value": value,
                    "tags": tags,
                    "createdAt": row['created_at'],
                    "updatedAt": row['updated_at']
                })
            
            return json.dumps({
                "count": len(result),
                "memories": result
            }, indent=2)
        
        elif action == "delete":
            if not key:
                return "Error: Key is required for deleting memories"
            
            cursor.execute(
                "SELECT id FROM memories WHERE username = ? AND key = ?",
                (username, key)
            )
            
            if not cursor.fetchone():
                return f"Memory not found with key: {key} for user: {username}"
            
            cursor.execute(
                "DELETE FROM memories WHERE username = ? AND key = ?",
                (username, key)
            )
            
            conn.commit()
            return f"Memory deleted with key: {key} for user: {username}"
# Add new search action
        elif action == "search":
            if not search_query:
                return "Error: search_query is required for search action"
            
            # Search in memory keys
            cursor.execute(
                """
                SELECT key, value, tags, created_at, updated_at
                FROM memories
                WHERE username = ? AND key LIKE ?
                """,
                (username, f"%{search_query}%")
            )
            
            rows = cursor.fetchall()
            
            if not rows:
                return f"No memories found matching: '{search_query}'"
            
            # Format the memories for display
            result = []
            for row in rows:
                # Deserialize the value
                value = pickle.loads(row['value'])
                
                # Parse tags from JSON
                tags = json.loads(row['tags'])
                
                result.append({
                    "key": row['key'],
                    "value": value,
                    "tags": tags,
                    "createdAt": row['created_at'],
                    "updatedAt": row['updated_at']
                })
            
            return json.dumps({
                "count": len(result),
                "memories": result
            }, indent=2)
            
       
        else:
            return f"Error: Unknown action: {action}"
            
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
