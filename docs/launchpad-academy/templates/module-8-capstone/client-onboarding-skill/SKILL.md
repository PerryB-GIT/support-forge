# Client Onboarding Agent

## Metadata
- **name**: client-onboarding
- **version**: 1.0.0
- **description**: Automates client onboarding by analyzing client information, generating personalized communications, creating project structures, and providing onboarding checklists.

## Triggers

This skill activates when:
- User mentions "onboard", "new client", or "client onboarding"
- Processing client intake form data
- Setting up a new client project
- Generating welcome communications
- Creating client folder structures

## Input Schema

The skill expects client information in the following format:

```json
{
  "client": {
    "name": "string (required) - Full name of primary contact",
    "email": "string (required) - Primary email address",
    "company": "string (required) - Company or organization name",
    "phone": "string (optional) - Contact phone number",
    "website": "string (optional) - Company website URL"
  },
  "project": {
    "type": "string (required) - Service type: web-development | consulting | marketing | support | custom",
    "name": "string (optional) - Project name, defaults to company name",
    "budget": "string (optional) - Budget range or amount",
    "timeline": "string (optional) - Expected timeline or deadline",
    "startDate": "string (optional) - Preferred start date (ISO format)",
    "description": "string (optional) - Project description or requirements"
  },
  "preferences": {
    "communicationMethod": "string (optional) - email | phone | slack | teams",
    "meetingPreference": "string (optional) - morning | afternoon | evening",
    "timezone": "string (optional) - Client timezone",
    "specialRequests": "string (optional) - Any special accommodations or notes"
  }
}
```

## Workflow

### Phase 1: Client Analysis

When triggered, first analyze the client information:

1. **Validate Required Fields** - Verify client name, email, and company are present
2. **Client Profile Analysis** - Determine segment, industry, and complexity
3. **Generate Client Summary** with all relevant details

### Phase 2: Personalized Welcome Email

Generate a welcome email tailored to the client based on project type (web-development, consulting, marketing, support, or custom).

### Phase 3: Folder Structure Creation

Generate specification for:
- 01-Contracts/
- 02-Project-Brief/
- 03-Assets/ (with subfolders)
- 04-Deliverables/ (with subfolders)
- 05-Communications/
- README.md

### Phase 4: Onboarding Checklist

Generate comprehensive checklist with universal items plus project-type specific additions.

### Phase 5: Output Generation

Return structured JSON response with all outputs.

## Error Handling

1. **Missing Required Fields** - Return specific validation errors
2. **Invalid Email Format** - Flag issue and continue with warning
3. **Unknown Project Type** - Default to custom type
4. **Empty Optional Fields** - Use sensible defaults

## Usage Examples

### Example 1: Basic Onboarding
```
User: Onboard new client - John Smith, john@acmecorp.com, Acme Corporation, web development project

Response: [Skill generates complete onboarding package]
```

### Example 2: Full Data Onboarding
```
User: Process this client intake:
{
  "client": {
    "name": "Sarah Johnson",
    "email": "sarah@techstartup.io",
    "company": "TechStartup Inc",
    "phone": "+1-555-123-4567",
    "website": "https://techstartup.io"
  },
  "project": {
    "type": "web-development",
    "budget": "$15,000-$25,000",
    "timeline": "3 months",
    "startDate": "2024-02-01",
    "description": "Complete website redesign with e-commerce functionality"
  },
  "preferences": {
    "communicationMethod": "slack",
    "meetingPreference": "afternoon",
    "timezone": "America/Los_Angeles"
  }
}

Response: [Skill generates personalized onboarding with all customizations]
```

### Example 3: Generating Specific Output
```
User: Generate just the welcome email for consulting client: Mike Chen, mike@bigcorp.com, BigCorp Enterprises

Response: [Skill generates only the welcome email component]
```

## Integration Points

This skill integrates with:

- **n8n Workflows**: Receives data from webhook triggers
- **Google Drive**: Folder structure creation
- **Google Sheets**: Client tracking
- **Google Calendar**: Meeting scheduling
- **Gmail**: Welcome email delivery
- **Slack**: Team notifications

## Configuration

Set these environment variables for full functionality:

```
COMPANY_NAME=Your Company Name
COMPANY_EMAIL=contact@yourcompany.com
COMPANY_PHONE=+1-555-000-0000
COMPANY_WEBSITE=https://yourcompany.com
DEFAULT_ACCOUNT_MANAGER=Account Manager Name
SLACK_CHANNEL=#new-clients
```

## Version History

- **1.0.0** - Initial release with full onboarding automation
