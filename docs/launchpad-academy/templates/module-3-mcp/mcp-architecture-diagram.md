# MCP Architecture Diagram

This document provides visual representations of how Claude Code connects to and communicates with MCP (Model Context Protocol) servers.

---

## High-Level Architecture Overview

```
+------------------------------------------------------------------+
|                         YOUR COMPUTER                             |
|                                                                   |
|  +-------------------+         +-----------------------------+    |
|  |                   |         |       MCP SERVER LAYER      |    |
|  |   CLAUDE CODE     |         |                             |    |
|  |                   |   JSON  |  +----------------------+   |    |
|  |   +----------+    |   RPC   |  |   GitHub MCP Server  |   |    |
|  |   |  Claude  |<-->|-------->|  |   (Node.js process)  |   |    |
|  |   |   AI     |    |         |  +----------+-----------+   |    |
|  |   +----------+    |         |             |               |    |
|  |                   |         |  +----------+-----------+   |    |
|  |   +----------+    |         |  |   Zapier MCP Server  |   |    |
|  |   |   MCP    |<-->|-------->|  |   (Node.js process)  |   |    |
|  |   |  Client  |    |         |  +----------+-----------+   |    |
|  |   +----------+    |         |             |               |    |
|  |                   |         |  +----------+-----------+   |    |
|  |   +----------+    |         |  | Filesystem MCP Server|   |    |
|  |   |  Config  |    |-------->|  |   (Node.js process)  |   |    |
|  |   |  Parser  |    |         |  +----------------------+   |    |
|  |   +----------+    |         |                             |    |
|  +-------------------+         +-----------------------------+    |
|                                              |                    |
+----------------------------------------------|--------------------+
                                               |
                                               | HTTPS/API Calls
                                               |
+----------------------------------------------|--------------------+
|                      INTERNET                |                    |
|                                              v                    |
|  +----------------+  +----------------+  +----------------+       |
|  |                |  |                |  |                |       |
|  |  GitHub API   |  |  Zapier API    |  |  Google APIs   |       |
|  |  api.github   |  |  mcp.zapier    |  |  googleapis    |       |
|  |    .com       |  |    .com        |  |    .com        |       |
|  |                |  |                |  |                |       |
|  +----------------+  +----------------+  +----------------+       |
|                                                                   |
+-------------------------------------------------------------------+
```

---

## Request/Response Flow

### Step-by-Step Communication

```
+-------------+     +-------------+     +-------------+     +-------------+
|   You       |     | Claude Code |     | MCP Server  |     | External    |
|  (User)     |     |  (Client)   |     | (Bridge)    |     | Service API |
+------+------+     +------+------+     +------+------+     +------+------+
       |                   |                   |                   |
       | 1. "Create issue" |                   |                   |
       |------------------>|                   |                   |
       |                   |                   |                   |
       |                   | 2. Parse request  |                   |
       |                   |    Identify tool  |                   |
       |                   |                   |                   |
       |                   | 3. JSON-RPC call  |                   |
       |                   |------------------>|                   |
       |                   |                   |                   |
       |                   |                   | 4. Transform to   |
       |                   |                   |    API request    |
       |                   |                   |                   |
       |                   |                   | 5. HTTPS request  |
       |                   |                   |------------------>|
       |                   |                   |                   |
       |                   |                   | 6. API response   |
       |                   |                   |<------------------|
       |                   |                   |                   |
       |                   | 7. JSON-RPC       |                   |
       |                   |    response       |                   |
       |                   |<------------------|                   |
       |                   |                   |                   |
       | 8. Formatted      |                   |                   |
       |    response       |                   |                   |
       |<------------------|                   |                   |
       |                   |                   |                   |


EXAMPLE FLOW: Creating a GitHub Issue
=====================================

1. User: "Create an issue in myrepo titled 'Bug fix needed'"

2. Claude Code:
   - Understands intent
   - Selects github_create_issue tool
   - Prepares parameters: {repo: "myrepo", title: "Bug fix needed"}

3. JSON-RPC call to GitHub MCP Server:
   {
     "jsonrpc": "2.0",
     "method": "tools/call",
     "params": {
       "name": "create_issue",
       "arguments": {"repo": "myrepo", "title": "Bug fix needed"}
     }
   }

4. MCP Server transforms to GitHub API format

5. HTTPS POST to api.github.com/repos/user/myrepo/issues
   Headers: Authorization: token ghp_xxxxx
   Body: {"title": "Bug fix needed"}

6. GitHub responds: {id: 123, url: "...", ...}

7. MCP Server returns JSON-RPC response

8. Claude Code: "Created issue #123 in myrepo"
```

---

## Security Architecture

```
+------------------------------------------------------------------------+
|                          SECURITY LAYERS                                |
+------------------------------------------------------------------------+

Layer 1: User Authentication
+----------------------------+
|     Claude Code Login      |
|  (Anthropic Account Auth)  |
+----------------------------+
            |
            v

Layer 2: MCP Server Security
+----------------------------+
|   Local Process Sandbox    |
|   - Runs under your user   |
|   - Limited file access    |
|   - Network restrictions   |
+----------------------------+
            |
            v

Layer 3: API Authentication
+----------------------------+
|   Per-Service Credentials  |
|   - API Keys / Tokens      |
|   - OAuth 2.0 Tokens       |
|   - Stored in env vars     |
+----------------------------+
            |
            v

Layer 4: Transport Security
+----------------------------+
|   HTTPS / TLS Encryption   |
|   - All API calls encrypted|
|   - Certificate validation |
+----------------------------+
            |
            v

Layer 5: Service Authorization
+----------------------------+
|   External Service Perms   |
|   - OAuth scopes           |
|   - API key permissions    |
|   - Resource-level access  |
+----------------------------+


CREDENTIAL FLOW
===============

+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Configuration   |---->|  Environment     |---->|  MCP Server      |
|  File (JSON)     |     |  Variables       |     |  Process         |
|                  |     |                  |     |                  |
|  References env  |     |  GITHUB_TOKEN=   |     |  Reads env,      |
|  var names only  |     |  ghp_xxxxx       |     |  uses for auth   |
|                  |     |                  |     |                  |
+------------------+     +------------------+     +------------------+

SECURITY BEST PRACTICES:
- Never store credentials in config files
- Use environment variables
- Rotate tokens regularly
- Use minimum required permissions
- Audit access periodically
```

---

## MCP Server Types and Connections

```
+------------------------------------------------------------------------+
|                     MCP SERVER ECOSYSTEM                                |
+------------------------------------------------------------------------+

CATEGORY 1: REMOTE API BRIDGES
==============================
These MCP servers connect to external cloud services

    Claude Code
         |
         v
+------------------+         HTTPS          +------------------+
|  Zapier MCP      |----------------------->|  Zapier Cloud    |
|  Server          |                        |  (6000+ apps)    |
+------------------+                        +------------------+
         |
         +----------------------------------------+
         |                    |                   |
         v                    v                   v
+----------------+   +----------------+   +----------------+
| Google Sheets  |   | Google Cal    |   | Slack          |
| Gmail, Drive   |   | Events        |   | Messages       |
+----------------+   +----------------+   +----------------+


+------------------+         HTTPS          +------------------+
|  GitHub MCP      |----------------------->|  GitHub API      |
|  Server          |                        |  api.github.com  |
+------------------+                        +------------------+
         |
         +------------------+------------------+
         |                  |                  |
         v                  v                  v
+----------------+   +----------------+   +----------------+
| Repositories   |   | Issues & PRs   |   | Actions        |
+----------------+   +----------------+   +----------------+


CATEGORY 2: LOCAL SYSTEM ACCESS
===============================
These MCP servers interact with your local machine

    Claude Code
         |
         v
+------------------+         Local          +------------------+
|  Filesystem MCP  |----------------------->|  Your Files      |
|  Server          |   (sandboxed paths)    |  & Directories   |
+------------------+                        +------------------+


+------------------+         Local          +------------------+
|  Database MCP    |----------------------->|  PostgreSQL/     |
|  Server          |      (TCP/Unix)        |  MySQL/SQLite    |
+------------------+                        +------------------+


CATEGORY 3: BROWSER/AUTOMATION
==============================
These MCP servers control browsers or other applications

    Claude Code
         |
         v
+------------------+         Local          +------------------+
|  Puppeteer MCP   |----------------------->|  Chrome/         |
|  Server          |    (DevTools Protocol) |  Chromium        |
+------------------+                        +------------------+
         |
         v
+------------------+
|  Web Pages       |
|  Screenshots     |
|  DOM Extraction  |
+------------------+
```

---

## Configuration File Structure

```
CONFIG FILE: mcp_config.json (or claude_desktop_config.json)
============================================================

{
  "mcpServers": {
    |
    +-- "server-name-1": {
    |       |
    |       +-- "command": "npx"           <-- Executable to run
    |       |
    |       +-- "args": [                  <-- Command arguments
    |       |       "-y",
    |       |       "@package/server"
    |       |   ]
    |       |
    |       +-- "env": {                   <-- Environment variables
    |               "API_KEY": "..."           passed to the process
    |           }
    |   }
    |
    +-- "server-name-2": {
            ...
        }
  }
}


EXAMPLE PARSED CONFIG:
======================

+------------------------------------------------------------------+
|  mcpServers                                                       |
+------------------------------------------------------------------+
|                                                                   |
|  +------------------------+    +------------------------+         |
|  | github                 |    | zapier                 |         |
|  +------------------------+    +------------------------+         |
|  | command: npx           |    | command: npx           |         |
|  | args:                  |    | args:                  |         |
|  |   - -y                 |    |   - -y                 |         |
|  |   - @mcp/server-github |    |   - @anthropic/mcp-    |         |
|  | env:                   |    |     client             |         |
|  |   GITHUB_PAT: ghp_xxx  |    |   - https://mcp.zap... |         |
|  +------------------------+    | env:                   |         |
|                                |   ZAPIER_KEY: zap_xxx  |         |
|                                +------------------------+         |
|                                                                   |
+------------------------------------------------------------------+
                |                              |
                v                              v
        +---------------+              +---------------+
        | Node Process  |              | Node Process  |
        | PID: 12345    |              | PID: 12346    |
        | Port: dynamic |              | Port: dynamic |
        +---------------+              +---------------+
```

---

## Data Flow Security Diagram

```
+------------------------------------------------------------------------+
|                      WHAT DATA GOES WHERE                               |
+------------------------------------------------------------------------+

YOUR REQUEST: "Show my GitHub issues"

+-------------------+
|  Claude Code      |
|  +--------------+ |
|  | Your prompt  | |     1. Prompt processed locally
|  | stored here  | |        (sent to Anthropic for AI)
|  +--------------+ |
+--------+----------+
         |
         | 2. Tool call generated
         v
+-------------------+
|  MCP Server       |
|  +--------------+ |
|  | API params   | |     3. Only necessary parameters
|  | - repo name  | |        sent to external service
|  | - filters    | |
|  +--------------+ |
+--------+----------+
         |
         | 4. HTTPS request
         v
+-------------------+
|  GitHub API       |
|  +--------------+ |
|  | Your data    | |     5. GitHub returns only
|  | - issues     | |        requested data
|  | - titles     | |
|  +--------------+ |
+--------+----------+
         |
         | 6. Response
         v
+-------------------+
|  MCP Server       |
|  +--------------+ |
|  | Formats data | |     7. Data transformed
|  | for Claude   | |        for display
|  +--------------+ |
+--------+----------+
         |
         | 8. Display
         v
+-------------------+
|  Claude Code      |
|  +--------------+ |
|  | Shows you    | |     9. Results displayed
|  | the issues   | |        in your session
|  +--------------+ |
+-------------------+


WHAT IS SENT WHERE:
===================

TO ANTHROPIC (Claude AI):
- Your prompts and questions
- Conversation context
- Tool results (for reasoning)

TO MCP SERVERS (Local):
- Specific tool parameters
- Environment variables (credentials)

TO EXTERNAL APIS:
- Only data needed for the request
- Authentication tokens
- API-specific parameters

STORED LOCALLY:
- Conversation history
- MCP configuration
- Log files
```

---

## Troubleshooting Visual Guide

```
MCP CONNECTION DIAGNOSTIC PATH
==============================

START: MCP tool not working
            |
            v
+------------------------+
| Is Claude Code running |----NO----> Start Claude Code
| and responsive?        |
+------------------------+
            |
           YES
            v
+------------------------+
| Can you see the MCP    |----NO----> Check config file:
| server in tools list?  |            - Valid JSON?
+------------------------+            - Correct path?
            |                         - No comments?
           YES
            v
+------------------------+
| Does the MCP server    |----NO----> Check:
| start without errors?  |            - Node.js installed?
+------------------------+            - npx working?
            |                         - Package exists?
           YES
            v
+------------------------+
| Is authentication      |----YES---> Check:
| failing? (401/403)     |            - API key valid?
+------------------------+            - Correct env var?
            |                         - Proper scopes?
            NO
            v
+------------------------+
| Is connection timing   |----YES---> Check:
| out?                   |            - Network connection
+------------------------+            - Firewall rules
            |                         - VPN issues
            NO
            v
+------------------------+
| Check logs for         |
| specific error message |
| See: Log File Locations|
+------------------------+
```

---

## Quick Reference: Port and Protocol Map

```
+------------------------------------------------------------------------+
|                    COMMON MCP CONNECTIONS                               |
+------------------------------------------------------------------------+

SERVICE          PROTOCOL    PORT    ENDPOINT
-----------      --------    ----    --------
GitHub API       HTTPS       443     api.github.com
Zapier MCP       HTTPS       443     mcp.zapier.com
Google APIs      HTTPS       443     *.googleapis.com
Local Postgres   TCP         5432    localhost
Local MySQL      TCP         3306    localhost
Local Files      N/A         N/A     File system paths

MCP INTERNAL COMMUNICATION:
- Claude Code <-> MCP Server: stdio (standard input/output)
- Alternative: HTTP on localhost (some servers)

```

---

## Summary Diagram: Complete System

```
+========================================================================+
||                    CLAUDE CODE + MCP ARCHITECTURE                    ||
+========================================================================+

   +------------------+
   |      YOU         |
   |  (Human User)    |
   +--------+---------+
            |
            | Natural language
            v
+====================================================================================+
||                              YOUR COMPUTER                                       ||
||                                                                                  ||
||  +------------------------+          +-------------------------------------+     ||
||  |     CLAUDE CODE        |          |         MCP SERVER LAYER            |     ||
||  |                        |          |                                     |     ||
||  |  +----------------+    |  stdio   |  +------------+    +------------+   |     ||
||  |  |  Claude AI     |<===|==========>  | GitHub MCP |    | Zapier MCP |   |     ||
||  |  |  (via API)     |    |          |  +-----+------+    +-----+------+   |     ||
||  |  +----------------+    |          |        |                 |          |     ||
||  |                        |          |  +-----+------+    +-----+------+   |     ||
||  |  +----------------+    |          |  | Files MCP  |    | DB MCP     |   |     ||
||  |  | Tool Executor  |<===|==========>  +-----+------+    +-----+------+   |     ||
||  |  +----------------+    |          |        |                 |          |     ||
||  |                        |          +--------|-----------------|----------+     ||
||  |  +----------------+    |                   |                 |                ||
||  |  | Response       |    |                   |                 |                ||
||  |  | Formatter      |    |                   |                 |                ||
||  |  +----------------+    |                   |                 |                ||
||  +------------------------+                   |                 |                ||
||                                               |                 |                ||
+===============================================|=================|=================+
                                                |                 |
                                                |  HTTPS          | Local
                                                v                 v
            +---------------------------+   +----------+   +----------+
            |        INTERNET           |   | Your     |   | Your     |
            |                           |   | Files    |   | Database |
            |  +---------+ +---------+  |   +----------+   +----------+
            |  | GitHub  | | Google  |  |
            |  | API     | | APIs    |  |
            |  +---------+ +---------+  |
            |                           |
            |  +---------+ +---------+  |
            |  | Zapier  | | Others  |  |
            |  | Cloud   | | ...     |  |
            |  +---------+ +---------+  |
            +---------------------------+
```

---

*Last updated: Module 3 - MCP Server Deep Dive*
