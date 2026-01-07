# Claude Code to n8n Integration Guide

Connect Claude Code to n8n for powerful AI-driven automation workflows.

---

## Overview

This integration allows Claude to:
- Trigger n8n workflows via webhooks
- Pass data to automations
- Receive workflow results
- Orchestrate complex multi-step processes

---

## Architecture

```
┌─────────────┐    Webhook    ┌─────────────┐    Actions    ┌──────────────┐
│ Claude Code │──────────────►│    n8n      │──────────────►│ External     │
│             │◄──────────────│  Workflow   │◄──────────────│ Services     │
└─────────────┘   Response    └─────────────┘   Results     └──────────────┘
```

---

## Method 1: Webhook Integration

### Step 1: Create n8n Webhook Workflow

1. In n8n, create a new workflow
2. Add **Webhook** trigger node
3. Configure:
   - HTTP Method: POST
   - Path: `/claude-trigger`
   - Authentication: Header Auth (recommended)
   - Response: "Last Node"

4. Add your processing nodes
5. End with **Respond to Webhook** node
6. Activate workflow and copy webhook URL

### Step 2: Configure Claude Code

Add to your CLAUDE.md or system prompt:

```markdown
## Available Automations

### n8n Webhooks
- **Lead Processing**: POST to https://your-n8n.com/webhook/lead-process
- **Report Generation**: POST to https://your-n8n.com/webhook/generate-report
- **Notification**: POST to https://your-n8n.com/webhook/notify

### Headers Required
Authorization: Bearer YOUR_WEBHOOK_SECRET
Content-Type: application/json
```

### Step 3: Trigger from Claude

```
Trigger the lead processing workflow with:
{
  "name": "John Smith",
  "email": "john@example.com",
  "source": "website"
}
```

Claude will execute:
```bash
curl -X POST https://your-n8n.com/webhook/lead-process \
  -H "Authorization: Bearer YOUR_WEBHOOK_SECRET" \
  -H "Content-Type: application/json" \
  -d '{"name":"John Smith","email":"john@example.com","source":"website"}'
```

---

## Method 2: MCP Integration (Recommended)

### Step 1: Configure n8n MCP Server

Add to `~/.claude/claude_mcp_config.json`:

```json
{
  "mcpServers": {
    "n8n": {
      "command": "npx",
      "args": ["-y", "@n8n/mcp-server"],
      "env": {
        "N8N_API_URL": "https://your-n8n.com/api/v1",
        "N8N_API_KEY": "your-api-key"
      }
    }
  }
}
```

### Step 2: Available n8n Tools

After configuration, Claude has access to:

| Tool | Description |
|------|-------------|
| `n8n_list_workflows` | List all workflows |
| `n8n_execute_workflow` | Run a specific workflow |
| `n8n_get_executions` | View execution history |
| `n8n_create_workflow` | Create new workflows |

### Step 3: Usage Examples

```
List my n8n workflows

Execute the "Daily Report" workflow

Show me the last 5 executions of workflow ID 123
```

---

## Common Integration Patterns

### Pattern 1: Data Processing Pipeline

```
User: Process this CSV data and add to our CRM

Claude:
1. Reads CSV file
2. Validates and transforms data
3. Triggers n8n webhook with clean data
4. n8n: Adds to CRM, sends confirmation

Flow:
Claude (prep) → n8n webhook → CRM API → Notification
```

### Pattern 2: Multi-Step Orchestration

```
User: Onboard new client "Acme Corp"

Claude orchestrates:
1. Trigger n8n: Create Drive folder
2. Trigger n8n: Add to CRM
3. Trigger n8n: Send welcome email
4. Trigger n8n: Create Slack channel
5. Report completion

n8n handles each step as separate workflows or one complex workflow
```

### Pattern 3: Scheduled + On-Demand

```
n8n: Runs daily report at 8 AM (scheduled)
Claude: "Generate a report for client X now" (on-demand via webhook)

Both use same report generation logic in n8n
```

---

## Example n8n Workflows for Claude

### 1. AI Content Generator

```json
{
  "trigger": "Webhook (POST /generate-content)",
  "input": {
    "topic": "string",
    "type": "blog|social|email",
    "length": "short|medium|long"
  },
  "steps": [
    "Receive webhook",
    "Call OpenAI/Claude API",
    "Format output",
    "Return to webhook caller"
  ],
  "output": {
    "content": "Generated text",
    "wordCount": 500
  }
}
```

### 2. Data Enrichment

```json
{
  "trigger": "Webhook (POST /enrich-contact)",
  "input": {
    "email": "user@company.com"
  },
  "steps": [
    "Receive webhook",
    "Query Clearbit/Hunter API",
    "Merge data",
    "Update CRM",
    "Return enriched data"
  ],
  "output": {
    "company": "Company Inc",
    "title": "CEO",
    "linkedin": "url"
  }
}
```

### 3. Approval Workflow

```json
{
  "trigger": "Webhook (POST /request-approval)",
  "input": {
    "type": "expense|purchase|leave",
    "amount": 500,
    "requestor": "user@company.com"
  },
  "steps": [
    "Receive webhook",
    "Create approval record",
    "Send Slack message to approver",
    "Wait for response (or timeout)",
    "Update record",
    "Notify requestor"
  ]
}
```

---

## Security Best Practices

### 1. Webhook Authentication

```javascript
// In n8n Code node - validate webhook
const authHeader = $input.first().json.headers.authorization;
const expectedToken = $env.WEBHOOK_SECRET;

if (authHeader !== `Bearer ${expectedToken}`) {
  throw new Error('Unauthorized');
}
```

### 2. Input Validation

```javascript
// Validate required fields
const data = $input.first().json.body;

if (!data.email || !data.email.includes('@')) {
  throw new Error('Invalid email');
}

if (!data.name || data.name.length < 2) {
  throw new Error('Name required');
}
```

### 3. Rate Limiting

```javascript
// Simple rate limit check
const lastExecution = $getWorkflowStaticData('global').lastRun;
const now = Date.now();

if (lastExecution && (now - lastExecution) < 1000) {
  throw new Error('Rate limited');
}

$getWorkflowStaticData('global').lastRun = now;
```

---

## Troubleshooting

### Webhook not responding

1. Check workflow is active (green indicator)
2. Verify webhook URL is correct
3. Check n8n logs for errors
4. Test with curl directly

### Authentication failures

1. Verify API key/token is correct
2. Check header format matches config
3. Ensure n8n instance is accessible

### Timeout issues

1. Increase webhook timeout in n8n
2. Use async pattern for long operations
3. Return quick acknowledgment, process async

### Data not passing correctly

1. Log incoming data in n8n
2. Check Content-Type header
3. Verify JSON structure matches expected

---

## Quick Reference

### Trigger Workflow from Claude

```
Run n8n workflow "Report Generator" with parameters:
- client: "Acme Corp"
- period: "Q4 2025"
- format: "PDF"
```

### Check Workflow Status

```
Check the status of n8n execution ID 12345
```

### List Available Workflows

```
Show me all active n8n workflows
```

---

## Environment Setup Checklist

- [ ] n8n instance running and accessible
- [ ] API key generated in n8n settings
- [ ] MCP config added to Claude Code
- [ ] Webhook URLs documented in CLAUDE.md
- [ ] Authentication configured
- [ ] Test workflow created and verified
- [ ] Error handling in place

---

*AI Launchpad Academy - Support Forge*
