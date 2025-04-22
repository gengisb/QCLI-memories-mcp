# QCLI-memories-mcp

A Contextual Memory System for Developer Tools
MCP Memory Server is a powerful contextual memory system designed specifically for CLI tools supporting developers and cloud engineers. It provides intelligent memory capabilities that persist across sessions, helping AI assistants remember critical information about users, their preferences, code, and architecture decisions.



Overview
This MCP-based memory system allows AI assistants to build a rich understanding of users and their work over time. As users interact with the tool, it intelligently remembers key details from previous sessions, including:

Personal preferences and information
Preferred programming languages and frameworks
AWS infrastructure patterns and configurations
Code formatting preferences
Previous errors and their solutions
Project-specific requirements
The result is a progressively more personalized experience that adapts to individual workflows, eliminating the need to repeatedly explain technical context.

Features
🧠 Intelligent Memory Storage
The system automatically identifies and stores important information from conversations, categorizing it appropriately with tags like:

#code: Programming languages, frameworks, coding patterns
#architecture: System designs, component relationships, infrastructure decisions
#personal: User preferences, background information
#project: Project details, requirements, deadlines
🔍 Contextual Retrieval
Memories can be retrieved through:

Exact key lookup
Keyword search
Context-based inference
👥 Multi-User Support
The system intelligently:

Identifies users from conversation context
Maintains separate memory spaces for different users
Allows potential for shared project contexts across users
🔄 Progressive Learning
Memory builds over time, creating a continuously improving understanding of the user's:

Technical preferences
Project requirements
Common workflows
Recurring challenges
Installation
# Clone the repository
git clone https://github.com/yourusername/mcp-memory-server.git

# Navigate to the directory
cd mcp-memory-server

# Install dependencies
pip install -r requirements.txt

# Run the server
python3 mcp_memory_server.py
Usage
Explicit Memory Storage
You can explicitly instruct the assistant to remember important information:

"Remember that I use TypeScript with the AWS Cloudscape style guide for all frontend projects"

"Remember that our AWS infrastructure uses multi-account strategy with Organizations."
Querying Stored Memories
To review what information the assistant has stored:

"What do you remember about me?"

"What do you remember about my projects?"

"What do you remember about my AWS infrastructure?"
Sample User Journeys
User Journey 1: Gengis - Project Continuity
Gengis can resume work on his migration project without repeating context:

"Hi, I'm Gengis. Let's continue with the migration project we discussed last time."

"What were the next steps for implementing the POC?"

"By the way, do you remember that issue I had with my toddler yesterday? Any update on that solution?"
User Journey 2: Jeremy - Skill-Based Development
Jeremy provides his background and receives progressively more tailored assistance:

"Hi, I'm Jeremy. I'm skilled in React and serverless architecture."

"I'd like to build a new e-commerce platform that leverages my expertise."

"Remember this project will need to handle high traffic during sales events."
Technical Implementation
The MCP Memory Server is built as a Python-based FastMCP server that:

Provides standardized memory management tools
Uses SQLite for persistent storage
Implements a flexible tagging system for categorization
Offers keyword search capabilities
Core components:

Memory storage with automatic serialization
Memory retrieval by key
Memory search by keywords
Memory listing and deletion capabilities
Fun Facts & Insights
User Identification: The system can identify users from context clues in the terminal (e.g., recognizing "Gengis" from /Users/gengis in pwd output)
Proactive Storage: The tool automatically stores information it deems relevant without being explicitly instructed
Future Potential: While currently lacking security features, there's potential for implementing shared project contexts with user-specific private memories
Value Proposition
MCP Memory Server introduces a powerful, context-aware memory system that fundamentally transforms how developers, architects, and solutions architects interact with AI tools. By capturing, storing, and retrieving both technical and personalized context across sessions, the feature eliminates repetitive explanations of preferences, environments, and project details.

This persistent knowledge enables practitioners to maintain continuity in their workflows, resulting in more personalized, relevant, and efficient assistance that adapts to individual working patterns over time.
