# MCP Memory Server

## A Contextual Memory System for Developer Tools

MCP Memory Server is a powerful contextual memory system designed specifically for CLI tools supporting developers and cloud engineers. It provides intelligent memory capabilities that persist across sessions, helping AI assistants remember critical information about users, their preferences, code, and architecture decisions.

## Overview

This MCP-based memory system allows AI assistants to build a rich understanding of users and their work over time. As users interact with the tool, it intelligently remembers key details from previous sessions, including:

- Personal preferences and information
- Preferred programming languages and frameworks
- AWS infrastructure patterns and configurations
- Code formatting preferences
- Previous errors and their solutions
- Project-specific requirements

The result is a progressively more personalized experience that adapts to individual workflows, eliminating the need to repeatedly explain technical context.

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/mcp-memory-server.git

# Navigate to the directory
cd mcp-memory-server

# Install dependencies
pip install -r requirements.txt

# Run the server
python3 mcp_memory_server.py
```
## Configure MCP Server
Add the following configuration to your mcp.json file:
```json
{
    "mcp-server-memories": {
        "command": "python",
        "args": [
            "PATH_TO_YOUR_FILE/memories_server.py"
        ],
        "env": {}
    }
}
Note: Replace PATH_TO_YOUR_FILE with the actual path to your memories_server.py file.


## Features

### 🧠 Intelligent Memory Storage

The system automatically identifies and stores important information from conversations, categorizing it appropriately with tags like:
- `#code`: Programming languages, frameworks, coding patterns
- `#architecture`: System designs, component relationships, infrastructure decisions
- `#personal`: User preferences, background information
- `#project`: Project details, requirements, deadlines

### 🔍 Contextual Retrieval

Memories can be retrieved through:
- Exact key lookup
- Keyword search
- Context-based inference

### 👥 Multi-User Support

The system intelligently:
- Identifies users from conversation context
- Maintains separate memory spaces for different users
- Allows potential for shared project contexts across users

### 🔄 Progressive Learning

Memory builds over time, creating a continuously improving understanding of the user's:
- Technical preferences
- Project requirements
- Common workflows
- Recurring challenges

