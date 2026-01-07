# Video Automation Workflow Guide

**Support Forge AI Launchpad Academy**
**Last Updated:** January 6, 2026

---

## Overview

This guide explains how to set up and use the n8n video production automation workflow for generating AI avatar videos from script files. The workflow integrates Google Drive, HeyGen API, Google Sheets, and Slack to create a fully automated video production pipeline.

---

## Architecture

```
Webhook Request (Script File ID)
       |
       v
Google Drive (Read Script)
       |
       v
Parse Script (Extract Narration)
       |
       v
Validate Content
       |
   [Valid?]
   /     \
  Yes     No
  |       |
  v       v
HeyGen   Error
API      Response
  |
  v
Check Status
  |
  [Ready?]
  /     \
 Yes    No (Processing)
  |       |
  v       v
Log to   Log Status
Sheets   & Respond
  |
  v
Slack Notification
  |
  v
Return Video URL
```

---

## Prerequisites

### Required Accounts

1. **n8n Instance**
   - Self-hosted (Docker) or n8n Cloud
   - Workflow located: `module-5-automation/n8n-workflows/video-production-workflow.json`

2. **HeyGen Account**
   - Sign up at [heygen.com](https://www.heygen.com/)
   - Requires paid plan for API access ($29+/month Creator plan)
   - API documentation: [docs.heygen.com](https://docs.heygen.com/)

3. **Google Cloud Project**
   - Google Drive API enabled
   - Google Sheets API enabled
   - OAuth 2.0 credentials configured

4. **Slack Workspace**
   - Slack app with `chat:write` permission
   - OAuth token for your workspace

---

## Required API Keys & Credentials

### 1. HeyGen API Key

**How to obtain:**
1. Log into [HeyGen](https://app.heygen.com/)
2. Navigate to Settings > API
3. Generate a new API key
4. Copy the key (format: `hg_xxxxxxxxxxxxx`)

**n8n credential setup:**
- Type: HTTP Header Auth
- Header Name: `X-Api-Key`
- Header Value: Your HeyGen API key

### 2. Google OAuth2 (Drive & Sheets)

**How to obtain:**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create or select a project
3. Enable Google Drive API and Google Sheets API
4. Configure OAuth consent screen
5. Create OAuth 2.0 Client ID (Web application type)
6. Add n8n redirect URI: `https://your-n8n-instance/rest/oauth2-credential/callback`

**n8n credential setup:**
- Type: Google Drive OAuth2 API
- Client ID: Your OAuth client ID
- Client Secret: Your OAuth client secret

### 3. Slack OAuth Token

**How to obtain:**
1. Go to [Slack API](https://api.slack.com/apps)
2. Create a new app or select existing
3. Under OAuth & Permissions, add scopes:
   - `chat:write`
   - `chat:write.public` (optional, for public channels)
4. Install app to workspace
5. Copy Bot User OAuth Token

**n8n credential setup:**
- Type: Slack OAuth2 API
- Access Token: Your bot token (starts with `xoxb-`)

---

## Setup Instructions

### Step 1: Import the Workflow

1. Open your n8n instance
2. Click **Workflows** > **Import from File**
3. Select `video-production-workflow.json`
4. Workflow will appear in draft mode

### Step 2: Configure Credentials

Replace placeholder credential IDs in these nodes:

| Node | Credential Type |
|------|-----------------|
| Google Drive - Read Script | Google Drive OAuth2 API |
| Google Sheets - Log Completed Video | Google Sheets OAuth2 API |
| Google Sheets - Log Processing | Google Sheets OAuth2 API |
| Google Sheets - Log Error | Google Sheets OAuth2 API |
| HTTP - HeyGen Generate Video | HTTP Header Auth |
| HTTP - Check Video Status | HTTP Header Auth |
| Slack - Notify Video Ready | Slack OAuth2 API |
| Slack - Notify Error | Slack OAuth2 API |

### Step 3: Create Tracking Spreadsheet

Create a Google Sheet with two tabs:

**Tab 1: VideoProduction**
| Column | Description |
|--------|-------------|
| LessonID | Lesson identifier (e.g., "2.3") |
| ModuleID | Module identifier (e.g., "module-2") |
| Title | Video title |
| VideoID | HeyGen video ID |
| VideoURL | Download URL for completed video |
| ThumbnailURL | Video thumbnail URL |
| Duration | Video duration in seconds |
| Status | "processing" or "completed" |
| CreatedAt | Request timestamp |
| CompletedAt | Completion timestamp |
| CharacterCount | Script character count |
| SegmentCount | Number of narration segments |

**Tab 2: VideoErrors**
| Column | Description |
|--------|-------------|
| LessonID | Lesson identifier |
| Title | Video title |
| Error | Error description |
| CharacterCount | Script character count |
| Timestamp | Error timestamp |

### Step 4: Update Configuration Values

1. Replace `YOUR_TRACKING_SHEET_ID` with your Google Sheet ID
   - Find it in the Sheet URL: `docs.google.com/spreadsheets/d/{SHEET_ID}/edit`

2. Update Slack channel name (default: `#video-production`)

3. Set environment variables (optional):
   - `HEYGEN_AVATAR_ID`: Your custom avatar ID
   - `HEYGEN_VOICE_ID`: Your preferred voice ID

### Step 5: Configure Avatar & Voice

Default values in the workflow:
- Avatar: `Kristin_public_3_20240108` (HeyGen public avatar)
- Voice: `2d5b0e6cf36f460aa7fc47e3eee4ba54` (Professional female voice)

To use your custom "Sparky" avatar:
1. Create avatar in HeyGen studio
2. Note the avatar ID from API settings
3. Update the HTTP Request node or set environment variable

### Step 6: Activate Workflow

1. Review all connections
2. Test with a sample script
3. Click **Active** toggle to enable webhook

---

## How to Trigger Video Production

### Via HTTP Request

**Webhook URL:** `https://your-n8n-instance/webhook/video-production`

**Method:** POST

**Headers:**
```
Content-Type: application/json
```

**Body:**
```json
{
  "scriptFileId": "1abc123def456_google_drive_file_id",
  "lessonId": "2.3",
  "moduleId": "module-2",
  "title": "Advanced Prompting Techniques"
}
```

### Via cURL

```bash
curl -X POST https://your-n8n-instance/webhook/video-production \
  -H "Content-Type: application/json" \
  -d '{
    "scriptFileId": "1abc123def456",
    "lessonId": "2.3",
    "moduleId": "module-2",
    "title": "Advanced Prompting Techniques"
  }'
```

### Via Claude Code

You can trigger video production directly from Claude Code using the Zapier MCP:

```
Create a video for lesson 2.3 using the script file 1abc123def456
```

Or create a custom skill that wraps the webhook call.

### Script File Format

The workflow parses Markdown scripts. Supported formats:

**Option A: Marked Narration**
```markdown
# Lesson Title

[NARRATION]
Welcome to this lesson on advanced prompting techniques.
Today we'll explore how to get better results from AI assistants.
[/NARRATION]

[SCREEN]
// Code demonstration here
[/SCREEN]

[AVATAR]
Let's wrap up what we learned today.
[/AVATAR]
```

**Option B: Plain Paragraphs**
```markdown
# Lesson Title

Welcome to this lesson. This paragraph will be extracted as narration.

Another paragraph of explanation that will become avatar speech.

- Bullet points are included
- As part of the narration

```code blocks are excluded```

| Tables | Are | Excluded |
```

---

## Tracking Production Status

### Google Sheets Dashboard

Your tracking spreadsheet serves as the production dashboard:

1. **VideoProduction tab** - Shows all videos and their status
2. **VideoErrors tab** - Lists failed attempts for debugging

Filter by Status column to see:
- `processing` - HeyGen is generating the video
- `completed` - Video is ready for download

### Slack Notifications

The workflow sends notifications to `#video-production` channel:

**Success:**
```
:movie_camera: Video Ready!

Advanced Prompting Techniques
Module: module-2
Lesson: 2.3

:stopwatch: Duration: ~45 seconds
:link: Download Video

Generated via Support Forge Video Pipeline
```

**Error:**
```
:warning: Video Production Failed

Advanced Prompting Techniques
Lesson: 2.3

:x: Error: Script validation failed - only 30 characters found

Please check the script file and try again.
```

### Manual Status Check

If the workflow returns "processing" status, you can manually check HeyGen:

1. Note the `videoId` from the response
2. Call HeyGen status endpoint:
   ```
   GET https://api.heygen.com/v1/video_status.get?video_id={videoId}
   ```

---

## Troubleshooting

### Common Issues

**1. "Script validation failed"**
- Script has less than 50 characters of narration
- Check that markdown isn't all code blocks or tables
- Ensure file is readable from Google Drive

**2. "HeyGen API error"**
- Verify API key is valid
- Check HeyGen account has credits remaining
- Ensure avatar ID exists in your account

**3. "Google Drive access denied"**
- Re-authorize OAuth credentials
- Ensure file is shared with service account
- Check Drive API is enabled

**4. "Slack notification failed"**
- Verify bot is added to channel
- Check OAuth token hasn't expired
- Ensure channel name matches exactly

### Debug Mode

Enable execution logging in n8n:
1. Open workflow
2. Click Settings gear
3. Enable "Save Manual Executions"
4. Run test and check Executions tab

---

## Batch Processing

For processing multiple scripts, create a wrapper workflow:

```
Schedule Trigger (daily)
       |
       v
Google Sheets (Read pending scripts)
       |
       v
Split In Batches
       |
       v
HTTP Request (Call video-production webhook)
       |
       v
Wait (rate limiting)
       |
       v
Loop back for next batch
```

---

## Cost Considerations

### HeyGen Pricing (2026)

| Plan | Monthly Cost | Credits |
|------|--------------|---------|
| Creator | $29 | 15 min/month |
| Business | $89 | 60 min/month |
| Enterprise | Custom | Unlimited |

**Estimate for 9-hour course:**
- ~3 hours of avatar video needed
- Business plan for 3 months: ~$270
- Or Creator plan for ~12 months: ~$350

### n8n Execution Costs

- Self-hosted: Free (server costs only)
- n8n Cloud Starter: $20/month (2,500 executions)

---

## Related Resources

- [n8n Video Production Workflow](/docs/launchpad-academy/templates/module-5-automation/n8n-workflows/video-production-workflow.json)
- [AI Video Production Plan](/docs/plans/2026-01-06-ai-video-production-plan.md)
- [HeyGen API Documentation](https://docs.heygen.com/)
- [n8n Documentation](https://docs.n8n.io/)

---

## Next Steps

1. **Import and configure** the workflow in your n8n instance
2. **Create test script** in Google Drive
3. **Run test production** with a short script
4. **Verify tracking** in Google Sheets
5. **Scale up** to batch processing when ready

---

*Support Forge AI Launchpad Academy - Video Production Pipeline*
