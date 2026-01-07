# Customization Guide: Client Onboarding Agent

This guide explains how to adapt the capstone project for your specific business needs, industry, and toolset.

---

## Table of Contents

1. [Industry Adaptations](#industry-adaptations)
2. [Swapping Services](#swapping-services)
3. [Adding Custom Steps](#adding-custom-steps)
4. [Removing Unnecessary Steps](#removing-unnecessary-steps)
5. [Testing Your Customizations](#testing-your-customizations)
6. [Common Customization Patterns](#common-customization-patterns)

---

## Industry Adaptations

### Real Estate Agency

**Modify the project types:**
```javascript
// In the Code node, update project types
const projectTypes = {
  'buyer-representation': 'Buyer Representation',
  'seller-listing': 'Seller Listing',
  'rental-management': 'Rental Management',
  'commercial': 'Commercial Real Estate'
};
```

**Update folder structure:**
```
[Client Name]/
  01-Contracts/
    Listing-Agreement/
    Purchase-Agreement/
  02-Property-Details/
    Photos/
    Virtual-Tours/
    Disclosures/
  03-Financials/
    Appraisals/
    Inspections/
  04-Communications/
    Buyer-Correspondence/
    Seller-Correspondence/
```

**Customize checklist items:**
- Property disclosure forms collected
- Pre-approval letter received (buyers)
- MLS listing prepared (sellers)
- Home inspection scheduled
- Title company selected

---

### Legal Firm

**Modify project types:**
```javascript
const projectTypes = {
  'litigation': 'Litigation',
  'corporate': 'Corporate Law',
  'family': 'Family Law',
  'estate-planning': 'Estate Planning',
  'real-estate': 'Real Estate Transactions'
};
```

**Update folder structure:**
```
[Client Name] - [Matter Number]/
  01-Engagement/
    Retainer-Agreement/
    Conflict-Check/
  02-Case-Files/
    Pleadings/
    Discovery/
    Correspondence/
  03-Evidence/
    Documents/
    Photos/
    Expert-Reports/
  04-Billing/
    Invoices/
    Time-Entries/
```

**Add legal-specific fields:**
- Matter number generation
- Conflict check status
- Statute of limitations tracking
- Court deadlines

---

### Healthcare / Medical Practice

**Modify project types:**
```javascript
const projectTypes = {
  'new-patient': 'New Patient Intake',
  'specialist-referral': 'Specialist Referral',
  'surgical': 'Surgical Consultation',
  'ongoing-care': 'Ongoing Care Management'
};
```

**HIPAA Compliance additions:**
- Remove PII from Slack notifications
- Encrypt folder contents
- Add audit logging
- Implement access controls

**Update welcome communication:**
- Include patient portal instructions
- HIPAA notice attachment
- Insurance verification steps

---

### Creative Agency

**Modify project types:**
```javascript
const projectTypes = {
  'branding': 'Brand Identity',
  'web-design': 'Web Design',
  'video-production': 'Video Production',
  'social-media': 'Social Media Campaign',
  'print': 'Print Design'
};
```

**Update folder structure:**
```
[Client Name]/
  01-Brief/
    Creative-Brief/
    Mood-Boards/
    References/
  02-Assets/
    Brand-Files/
    Stock-Media/
    Client-Provided/
  03-Work-In-Progress/
    Concepts/
    Revisions/
  04-Final-Deliverables/
    Print-Ready/
    Web-Optimized/
    Source-Files/
```

---

## Swapping Services

### Replace Google Drive with Dropbox

**1. Remove Google Drive nodes and add Dropbox:**

```json
{
  "parameters": {
    "operation": "folder",
    "name": "={{ $json.folderName }}",
    "path": "/Clients/"
  },
  "name": "Create Client Folder",
  "type": "n8n-nodes-base.dropbox",
  "credentials": {
    "dropboxApi": {
      "id": "dropbox-credentials",
      "name": "Dropbox Account"
    }
  }
}
```

**2. Update folder link references:**
```javascript
// Change from
$('Create Client Folder').item.json.webViewLink
// To
`https://www.dropbox.com/home${$('Create Client Folder').item.json.path_display}`
```

---

### Replace Google Sheets with Airtable

**1. Add Airtable node:**

```json
{
  "parameters": {
    "operation": "create",
    "application": {
      "__rl": true,
      "value": "YOUR_BASE_ID",
      "mode": "id"
    },
    "table": {
      "__rl": true,
      "value": "Clients",
      "mode": "name"
    },
    "columns": {
      "mappingMode": "defineBelow",
      "value": {
        "Name": "={{ $json.clientName }}",
        "Email": "={{ $json.clientEmail }}",
        "Company": "={{ $json.clientCompany }}",
        "Status": "Onboarding"
      }
    }
  },
  "name": "Add to Airtable",
  "type": "n8n-nodes-base.airtable",
  "credentials": {
    "airtableTokenApi": {
      "id": "airtable-credentials",
      "name": "Airtable Account"
    }
  }
}
```

---

### Replace Slack with Microsoft Teams

**1. Add Microsoft Teams node:**

```json
{
  "parameters": {
    "operation": "message",
    "teamId": "YOUR_TEAM_ID",
    "channelId": "YOUR_CHANNEL_ID",
    "contentType": "html",
    "message": "<h3>New Client Onboarded!</h3><p><strong>{{ $json.clientCompany }}</strong></p><ul><li>Contact: {{ $json.clientName }}</li><li>Project: {{ $json.projectType }}</li></ul>"
  },
  "name": "Notify Team on Teams",
  "type": "n8n-nodes-base.microsoftTeams",
  "credentials": {
    "microsoftTeamsOAuth2Api": {
      "id": "teams-credentials",
      "name": "Microsoft Teams Account"
    }
  }
}
```

---

### Replace Gmail with Outlook/Office 365

**1. Add Microsoft Outlook node:**

```json
{
  "parameters": {
    "operation": "send",
    "toRecipients": "={{ $json.clientEmail }}",
    "subject": "={{ $json.welcomeSubject }}",
    "bodyContent": "<html>...</html>",
    "bodyContentType": "html"
  },
  "name": "Send Welcome Email",
  "type": "n8n-nodes-base.microsoftOutlook",
  "credentials": {
    "microsoftOutlookOAuth2Api": {
      "id": "outlook-credentials",
      "name": "Outlook Account"
    }
  }
}
```

---

### Replace Google Calendar with Calendly

**1. Add HTTP Request node for Calendly API:**

```json
{
  "parameters": {
    "method": "POST",
    "url": "https://api.calendly.com/scheduling_links",
    "authentication": "genericCredentialType",
    "genericAuthType": "httpHeaderAuth",
    "sendHeaders": true,
    "headerParameters": {
      "parameters": [
        {
          "name": "Content-Type",
          "value": "application/json"
        }
      ]
    },
    "sendBody": true,
    "bodyParameters": {
      "parameters": [
        {
          "name": "max_event_count",
          "value": "1"
        },
        {
          "name": "owner",
          "value": "https://api.calendly.com/users/YOUR_USER_ID"
        },
        {
          "name": "owner_type",
          "value": "users"
        }
      ]
    }
  },
  "name": "Create Calendly Link",
  "type": "n8n-nodes-base.httpRequest"
}
```

---

## Adding Custom Steps

### Add CRM Integration (HubSpot)

**Insert after data preparation:**

```json
{
  "parameters": {
    "operation": "create",
    "additionalFields": {
      "company": "={{ $json.clientCompany }}",
      "email": "={{ $json.clientEmail }}",
      "firstname": "={{ $json.clientName.split(' ')[0] }}",
      "lastname": "={{ $json.clientName.split(' ').slice(1).join(' ') }}",
      "phone": "={{ $json.clientPhone }}"
    }
  },
  "name": "Create HubSpot Contact",
  "type": "n8n-nodes-base.hubspot",
  "credentials": {
    "hubspotApi": {
      "id": "hubspot-credentials",
      "name": "HubSpot Account"
    }
  }
}
```

---

### Add Contract Generation (PandaDoc)

**Add before sending welcome email:**

```json
{
  "parameters": {
    "operation": "create",
    "templateId": "YOUR_TEMPLATE_ID",
    "name": "Service Agreement - {{ $json.clientCompany }}",
    "recipients": [
      {
        "email": "={{ $json.clientEmail }}",
        "firstName": "={{ $json.clientName.split(' ')[0] }}",
        "lastName": "={{ $json.clientName.split(' ').slice(1).join(' ') }}",
        "role": "Client"
      }
    ],
    "tokens": [
      {
        "name": "client_company",
        "value": "={{ $json.clientCompany }}"
      },
      {
        "name": "project_type",
        "value": "={{ $json.projectType }}"
      },
      {
        "name": "budget",
        "value": "={{ $json.projectBudget }}"
      }
    ]
  },
  "name": "Generate Contract",
  "type": "n8n-nodes-base.pandaDoc"
}
```

---

### Add Invoice Creation (Stripe)

**Add for payment setup:**

```json
{
  "parameters": {
    "operation": "create",
    "resource": "customer",
    "email": "={{ $json.clientEmail }}",
    "name": "={{ $json.clientCompany }}",
    "metadata": {
      "client_id": "={{ $json.clientId }}",
      "project_type": "={{ $json.projectType }}"
    }
  },
  "name": "Create Stripe Customer",
  "type": "n8n-nodes-base.stripe"
}
```

---

### Add Task Management (Asana/Monday.com)

**Add project tasks automatically:**

```json
{
  "parameters": {
    "operation": "create",
    "workspace": "YOUR_WORKSPACE_ID",
    "name": "{{ $json.clientCompany }} - Onboarding",
    "projectId": "YOUR_PROJECT_ID",
    "otherProperties": {
      "assignee": "YOUR_USER_ID",
      "due_on": "={{ $json.projectStartDate }}",
      "notes": "New client onboarding for {{ $json.clientName }}"
    }
  },
  "name": "Create Asana Task",
  "type": "n8n-nodes-base.asana"
}
```

---

## Removing Unnecessary Steps

### Remove Slack Notification

1. Delete the "Notify Team on Slack" node
2. Connect "Send Welcome Email" directly to "Success Response"
3. Update the success response to remove Slack reference:

```javascript
// Remove this from success response
"slackNotified": true
```

---

### Remove Calendar Scheduling

1. Delete the "Schedule Kickoff Meeting" node
2. Update the Prepare Client Data node to remove meeting time calculation
3. Update welcome email to mention manual scheduling:

```html
<li><strong>Kickoff Meeting</strong> - We'll reach out shortly to find a time that works for you</li>
```

---

### Simplify Folder Structure

Replace multiple folder creation nodes with a single Code node:

```javascript
// Single node to create all folders
const folderId = $('Create Client Folder').item.json.id;
const folders = ['Contracts', 'Assets', 'Deliverables'];

// Return folder specs for batch creation
return folders.map(name => ({
  json: { parentId: folderId, name }
}));
```

---

## Testing Your Customizations

### 1. Create Test Payload

Save this as `test-payload.json`:

```json
{
  "client": {
    "name": "Test User",
    "email": "test@example.com",
    "company": "Test Company Inc"
  },
  "project": {
    "type": "web-development",
    "budget": "$5,000",
    "timeline": "2 weeks"
  }
}
```

### 2. Test Individual Nodes

In n8n, use "Execute Node" to test each node individually before running the full workflow.

### 3. Use Webhook Testing Tools

- **Webhook.site** - Get a temporary URL to inspect payloads
- **ngrok** - Expose local n8n for testing
- **Postman** - Send test requests with different payloads

### 4. Verify Each Integration

| Service | Verification Step |
|---------|-------------------|
| Google Drive | Check folder exists with correct structure |
| Google Sheets | Verify row added with all columns populated |
| Google Calendar | Confirm event appears with correct details |
| Gmail | Check sent folder for welcome email |
| Slack | Look for notification in correct channel |

### 5. Test Edge Cases

- Empty optional fields
- Special characters in company names
- Very long descriptions
- Invalid email formats
- Duplicate submissions

---

## Common Customization Patterns

### Pattern 1: Conditional Branching by Project Type

```javascript
// Add IF node after data preparation
{
  "conditions": {
    "conditions": [
      {
        "leftValue": "={{ $json.projectType }}",
        "rightValue": "enterprise",
        "operator": {
          "type": "string",
          "operation": "equals"
        }
      }
    ]
  }
}
```

Then create separate paths for enterprise vs. standard clients.

---

### Pattern 2: Rate Limiting

Add a Wait node to prevent API rate limits:

```json
{
  "parameters": {
    "amount": 1,
    "unit": "seconds"
  },
  "name": "Rate Limit",
  "type": "n8n-nodes-base.wait"
}
```

---

### Pattern 3: Error Notification

Add error handling that notifies you of failures:

```json
{
  "parameters": {
    "channel": "#alerts",
    "text": ":warning: Client onboarding failed for {{ $json.clientEmail }}\nError: {{ $json.error }}"
  },
  "name": "Alert on Error",
  "type": "n8n-nodes-base.slack"
}
```

---

### Pattern 4: Duplicate Prevention

Add a lookup before creating:

```json
{
  "parameters": {
    "operation": "search",
    "filter": {
      "email": "={{ $json.clientEmail }}"
    }
  },
  "name": "Check Existing Client",
  "type": "n8n-nodes-base.googleSheets"
}
```

Then use an IF node to skip if client exists.

---

## Quick Reference: Node Connections

When customizing, maintain these connection patterns:

```
[Trigger] -> [Validate] -> [Prepare Data] -> [Parallel Operations] -> [Sequential Completion] -> [Response]
```

- Parallel operations: Tasks that don't depend on each other (folder creation, sheet update, calendar)
- Sequential completion: Tasks that must happen in order (email before Slack, all before response)

---

## Need Help?

- **Launchpad Academy Discord**: #customization-help
- **n8n Community**: community.n8n.io
- **Documentation**: support-forge.com/docs/launchpad/customization

---

*Remember: Start with the default workflow working perfectly, then customize one piece at a time. Test after each change!*
