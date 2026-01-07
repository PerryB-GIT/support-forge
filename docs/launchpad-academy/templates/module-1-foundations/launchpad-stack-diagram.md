# Launchpad Academy Stack Diagram

This document illustrates the core architecture of the AI-powered automation stack taught in Launchpad Academy.

---

## High-Level Architecture Overview

```
+==============================================================================+
|                           YOUR WORKSPACE                                      |
|                                                                               |
|   +------------------+    +------------------+    +------------------+        |
|   |   Your Code      |    |   Your Data      |    |   Your Docs      |        |
|   |   & Projects     |    |   & Databases    |    |   & Content      |        |
|   +--------+---------+    +--------+---------+    +--------+---------+        |
|            |                       |                       |                  |
+============|=======================|=======================|==================+
             |                       |                       |
             v                       v                       v
+==============================================================================+
|                                                                               |
|                         +-------------------------+                           |
|                         |                         |                           |
|                         |      CLAUDE CODE        |                           |
|                         |     (AI Assistant)      |                           |
|                         |                         |                           |
|                         |  - Code Generation      |                           |
|                         |  - Analysis & Debug     |                           |
|                         |  - Task Automation      |                           |
|                         |  - Documentation        |                           |
|                         |                         |                           |
|                         +-----------+-------------+                           |
|                                     |                                         |
|                    +----------------+----------------+                        |
|                    |                                 |                        |
|              MCP Protocol                      Direct API                     |
|                    |                                 |                        |
|     +--------------+--------------+                  |                        |
|     |              |              |                  |                        |
|     v              v              v                  v                        |
| +-------+    +---------+    +--------+    +------------------+               |
| |Zapier |    | GitHub  |    | Google |    | Anthropic API    |               |
| | MCP   |    |  MCP    |    |  MCP   |    | (Claude Models)  |               |
| +---+---+    +----+----+    +----+---+    +------------------+               |
|     |             |              |                                            |
+==============================================================================+
      |             |              |
      v             v              v
+==============================================================================+
|                        AUTOMATION LAYER                                       |
|                                                                               |
|    +----------------+                      +----------------+                  |
|    |                |                      |                |                  |
|    |     n8n        |<-------------------->|    Zapier      |                  |
|    |                |                      |                |                  |
|    | - Visual       |                      | - No-Code      |                  |
|    |   Workflows    |                      |   Automation   |                  |
|    | - Self-hosted  |                      | - 5000+ Apps   |                  |
|    |   Option       |                      | - Quick Setup  |                  |
|    | - Custom Code  |                      | - Templates    |                  |
|    |   Nodes        |                      |                |                  |
|    +-------+--------+                      +-------+--------+                  |
|            |                                       |                          |
|            +-------------------+-------------------+                          |
|                                |                                              |
+================================|=============================================+
                                 |
                                 v
+==============================================================================+
|                        EXTERNAL SERVICES                                      |
|                                                                               |
|  +------------+  +------------+  +------------+  +------------+              |
|  |            |  |            |  |            |  |            |              |
|  |   Gmail    |  |  Google    |  |  Google    |  |   Slack    |              |
|  |            |  |  Calendar  |  |  Sheets    |  |            |              |
|  +------------+  +------------+  +------------+  +------------+              |
|                                                                               |
|  +------------+  +------------+  +------------+  +------------+              |
|  |            |  |            |  |            |  |            |              |
|  |  GitHub    |  |  Notion    |  |   CRM      |  |  Database  |              |
|  |            |  |            |  | (HubSpot)  |  | (Postgres) |              |
|  +------------+  +------------+  +------------+  +------------+              |
|                                                                               |
+==============================================================================+
                                 |
                                 v
+==============================================================================+
|                        CLOUD DEPLOYMENT LAYER                                 |
|                                                                               |
|    +---------------------------+    +---------------------------+            |
|    |          AWS              |    |     Google Cloud          |            |
|    |                           |    |                           |            |
|    |  +-------+  +--------+   |    |  +-------+  +--------+    |            |
|    |  |  S3   |  |Amplify |   |    |  |  GCS  |  |Cloud   |    |            |
|    |  |Storage|  |Hosting |   |    |  |       |  |Run     |    |            |
|    |  +-------+  +--------+   |    |  +-------+  +--------+    |            |
|    |                           |    |                           |            |
|    |  +-------+  +--------+   |    |  +-------+  +--------+    |            |
|    |  |Lambda |  |  EC2   |   |    |  |Cloud  |  |Firebase|    |            |
|    |  |       |  |        |   |    |  |Funct. |  |        |    |            |
|    |  +-------+  +--------+   |    |  +-------+  +--------+    |            |
|    +---------------------------+    +---------------------------+            |
|                                                                               |
|    +---------------------------+    +---------------------------+            |
|    |        Vercel             |    |      Cloudflare           |            |
|    |                           |    |                           |            |
|    |  - Next.js Hosting        |    |  - CDN                    |            |
|    |  - Edge Functions         |    |  - DNS Management         |            |
|    |  - Preview Deployments    |    |  - Workers                |            |
|    +---------------------------+    +---------------------------+            |
|                                                                               |
+==============================================================================+
```

---

## Data Flow Diagram

```
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|   USER INPUT     |---->|   CLAUDE CODE    |---->|   PROCESSED      |
|                  |     |                  |     |   OUTPUT         |
|  - Commands      |     |  - Understands   |     |                  |
|  - Questions     |     |  - Plans         |     |  - Code          |
|  - Files         |     |  - Executes      |     |  - Answers       |
|                  |     |                  |     |  - Actions       |
+------------------+     +--------+---------+     +------------------+
                                  |
                                  | MCP
                                  | Connections
                                  v
         +------------------------+------------------------+
         |                        |                        |
         v                        v                        v
+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  Zapier MCP      |     |  GitHub MCP      |     |  Custom MCP      |
|                  |     |                  |     |                  |
|  - Triggers      |     |  - Repos         |     |  - Your APIs     |
|  - Actions       |     |  - Issues        |     |  - Internal      |
|  - 5000+ Apps    |     |  - PRs           |     |    Tools         |
|                  |     |  - Actions       |     |                  |
+--------+---------+     +--------+---------+     +--------+---------+
         |                        |                        |
         v                        v                        v
+==============================================================================+
|                          EXTERNAL WORLD                                       |
|                                                                               |
|   Email    Calendar    Spreadsheets    Databases    APIs    Websites         |
|                                                                               |
+==============================================================================+
```

---

## MCP (Model Context Protocol) Architecture

```
+==============================================================================+
|                                                                               |
|                           CLAUDE CODE RUNTIME                                 |
|                                                                               |
|   +---------------------------------------------------------------------+    |
|   |                         MCP CLIENT                                   |    |
|   |                                                                      |    |
|   |   Manages connections to MCP servers                                |    |
|   |   Routes tool calls to appropriate servers                          |    |
|   |   Handles authentication and security                               |    |
|   +---------------------------------------------------------------------+    |
|                                    |                                          |
|              +---------------------+---------------------+                    |
|              |                     |                     |                    |
|              v                     v                     v                    |
|   +------------------+  +------------------+  +------------------+            |
|   |   MCP Server 1   |  |   MCP Server 2   |  |   MCP Server 3   |            |
|   |   (Zapier)       |  |   (GitHub)       |  |   (Google)       |            |
|   |                  |  |                  |  |                  |            |
|   |  Tools:          |  |  Tools:          |  |  Tools:          |            |
|   |  - send_email    |  |  - create_issue  |  |  - read_sheet    |            |
|   |  - create_event  |  |  - create_pr     |  |  - send_email    |            |
|   |  - update_sheet  |  |  - list_repos    |  |  - create_event  |            |
|   |  - trigger_zap   |  |  - get_file      |  |  - upload_file   |            |
|   +------------------+  +------------------+  +------------------+            |
|              |                     |                     |                    |
+==============|=====================|=====================|====================+
               |                     |                     |
               v                     v                     v
        +-----------+         +-----------+         +-----------+
        |  Zapier   |         |  GitHub   |         |  Google   |
        |   API     |         |   API     |         |   APIs    |
        +-----------+         +-----------+         +-----------+
```

---

## Automation Workflow Example

```
TRIGGER                    PROCESS                      ACTION
   |                          |                            |
   v                          v                            v

+--------+              +----------+                 +----------+
| New    |              | Claude   |                 | Create   |
| Email  |------------->| Analyzes |---------------->| Task in  |
| Arrives|              | Content  |                 | Notion   |
+--------+              +----------+                 +----------+
                              |
                              | If urgent
                              v
                        +----------+                 +----------+
                        | Generate |                 | Send     |
                        | Response |---------------->| Slack    |
                        | Draft    |                 | Alert    |
                        +----------+                 +----------+
                              |
                              | If needs data
                              v
                        +----------+                 +----------+
                        | Query    |                 | Update   |
                        | Database |---------------->| Google   |
                        |          |                 | Sheet    |
                        +----------+                 +----------+


n8n Workflow Visual:

    [Gmail Trigger]
          |
          v
    [Claude AI Node]----+
          |             |
          v             v
    [IF Urgent?]   [Log to Sheet]
      /     \
     v       v
  [Slack]  [Create Draft]
     |
     v
  [Notion Task]
```

---

## Security Layers

```
+==============================================================================+
|                              SECURITY ARCHITECTURE                            |
|                                                                               |
|  Layer 1: Authentication                                                      |
|  +---------------------------------------------------------------------+     |
|  |  - API Keys (stored in environment variables)                        |     |
|  |  - OAuth 2.0 tokens (managed by MCP servers)                        |     |
|  |  - SSH keys (for Git operations)                                    |     |
|  +---------------------------------------------------------------------+     |
|                                                                               |
|  Layer 2: Authorization                                                       |
|  +---------------------------------------------------------------------+     |
|  |  - Scoped API permissions (least privilege)                         |     |
|  |  - IAM roles (AWS/GCP)                                              |     |
|  |  - OAuth scopes (limited access)                                    |     |
|  +---------------------------------------------------------------------+     |
|                                                                               |
|  Layer 3: Encryption                                                          |
|  +---------------------------------------------------------------------+     |
|  |  - TLS/HTTPS for all API communications                             |     |
|  |  - Encrypted secrets storage                                        |     |
|  |  - Encrypted database connections                                   |     |
|  +---------------------------------------------------------------------+     |
|                                                                               |
|  Layer 4: Monitoring                                                          |
|  +---------------------------------------------------------------------+     |
|  |  - Audit logs                                                       |     |
|  |  - Usage monitoring                                                 |     |
|  |  - Anomaly detection                                                |     |
|  +---------------------------------------------------------------------+     |
|                                                                               |
+==============================================================================+
```

---

## Component Responsibilities

| Component | Primary Purpose | Key Capabilities |
|-----------|----------------|------------------|
| **Claude Code** | AI-powered development assistant | Code generation, analysis, debugging, documentation |
| **MCP Servers** | Bridge to external services | Tool execution, authentication, data access |
| **n8n** | Complex workflow automation | Visual workflows, custom code, self-hosted |
| **Zapier** | Simple, no-code automation | Quick integrations, templates, 5000+ apps |
| **AWS** | Enterprise cloud infrastructure | Compute, storage, serverless, databases |
| **Google Cloud** | Cloud services + Google integrations | APIs, hosting, AI/ML services |
| **Vercel** | Frontend deployment | Next.js hosting, edge functions, preview |
| **Cloudflare** | Edge network services | CDN, DNS, security, workers |

---

## Getting Started Checklist

- [ ] Claude Code installed and configured
- [ ] MCP servers connected (Zapier, GitHub, Google)
- [ ] n8n Cloud or self-hosted instance running
- [ ] Zapier account with test Zaps created
- [ ] AWS account with CLI configured
- [ ] Google Cloud project with APIs enabled
- [ ] First automation workflow tested end-to-end

---

## Next Steps

1. **Module 2:** Build your first Claude Code + MCP integration
2. **Module 3:** Create n8n workflows with AI nodes
3. **Module 4:** Deploy to AWS/GCP
4. **Module 5:** Advanced automation patterns
