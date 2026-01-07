# OAuth Troubleshooting Guide

Resolve common OAuth authentication issues with Google services and other MCP integrations.

---

## Understanding OAuth Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ Claude Code │────►│ OAuth Server│────►│ Google/Svc  │
│   (Client)  │◄────│  (Auth)     │◄────│   (API)     │
└─────────────┘     └─────────────┘     └─────────────┘
      │                   │                    │
      │  1. Request Auth  │                    │
      │──────────────────►│                    │
      │                   │  2. Redirect to    │
      │                   │     Login          │
      │  3. User Logs In ─┼───────────────────►│
      │                   │  4. Auth Code      │
      │                   │◄───────────────────│
      │  5. Access Token  │                    │
      │◄──────────────────│                    │
      │                   │                    │
      │  6. API Requests ─┼───────────────────►│
      │◄──────────────────┼────────────────────│
      │                   │                    │
```

---

## Common OAuth Errors

### Error: "OAuth consent screen not configured"

**Cause:** Google Cloud project missing OAuth setup

**Solution:**
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Select your project
3. Navigate to **APIs & Services** → **OAuth consent screen**
4. Choose "External" user type
5. Fill in required fields:
   - App name
   - User support email
   - Developer contact email
6. Add scopes for services you need
7. Add test users (your email)
8. Save and publish (or keep in testing mode)

---

### Error: "Access token expired"

**Cause:** OAuth tokens have limited lifespan (usually 1 hour)

**Solution:**
```bash
# Clear cached credentials
rm -rf ~/.claude/google-credentials/
rm -rf ~/.claude/oauth-tokens/

# Restart Claude Code and re-authenticate
claude
```

**Prevention:**
- MCP servers should auto-refresh tokens
- Check refresh token hasn't been revoked
- Ensure offline access scope is granted

---

### Error: "Invalid client"

**Cause:** OAuth client credentials incorrect or deleted

**Solution:**
1. Go to Google Cloud Console
2. Navigate to **APIs & Services** → **Credentials**
3. Find your OAuth 2.0 Client ID
4. Download new credentials JSON
5. Update MCP configuration with new client ID/secret

```json
{
  "mcpServers": {
    "google": {
      "env": {
        "GOOGLE_CLIENT_ID": "xxxx.apps.googleusercontent.com",
        "GOOGLE_CLIENT_SECRET": "GOCSPX-xxxxxxxxxxxx"
      }
    }
  }
}
```

---

### Error: "Redirect URI mismatch"

**Cause:** Redirect URL in config doesn't match Google Console

**Solution:**
1. In Google Cloud Console → Credentials
2. Click on your OAuth Client
3. Under "Authorized redirect URIs", add:
   - `http://localhost:3000/oauth/callback`
   - `http://127.0.0.1:3000/oauth/callback`
4. Save changes
5. Wait 5 minutes for propagation

---

### Error: "Access denied" or "Insufficient permissions"

**Cause:** Required scopes not granted

**Solution:**
1. Check which scopes your integration needs:

| Service | Required Scopes |
|---------|-----------------|
| Gmail | `gmail.readonly`, `gmail.send` |
| Calendar | `calendar.readonly`, `calendar.events` |
| Drive | `drive.readonly`, `drive.file` |
| Sheets | `spreadsheets` |

2. Re-authenticate with full scopes:
```bash
# Clear credentials and re-auth
rm -rf ~/.claude/google-credentials/
claude "Connect to my Google Calendar"
```

3. When prompted, check ALL required permission boxes

---

### Error: "User rate limit exceeded"

**Cause:** Too many authentication attempts

**Solution:**
1. Wait 15-30 minutes
2. Check for authentication loops
3. Don't retry repeatedly on failures

**Prevention:**
- Cache tokens properly
- Don't re-authenticate unnecessarily
- Check for infinite auth loops in code

---

### Error: "This app isn't verified"

**Cause:** OAuth app in testing mode or unverified

**Solution (Development):**
1. Click "Advanced" on the warning screen
2. Click "Go to [App Name] (unsafe)"
3. Continue with authentication

**Solution (Production):**
1. Submit app for Google verification
2. Complete OAuth consent screen fully
3. Add privacy policy URL
4. Wait for Google review (can take weeks)

---

## Google-Specific Troubleshooting

### Gmail Integration

**Common Issues:**
- "Gmail API not enabled"
  - Go to APIs & Services → Enable Gmail API

- "Cannot send email"
  - Need `gmail.send` scope
  - Re-authenticate with send permission

### Calendar Integration

**Common Issues:**
- "Calendar not found"
  - Verify calendar ID (usually your email)
  - Check calendar is shared properly

- "Cannot create events"
  - Need `calendar.events` scope (not just readonly)

### Drive Integration

**Common Issues:**
- "File not found"
  - Check file sharing permissions
  - May need `drive.readonly` for shared files

- "Cannot upload"
  - Need `drive.file` scope

### Sheets Integration

**Common Issues:**
- "Spreadsheet not accessible"
  - Share sheet with service account email
  - Check spreadsheet ID is correct

---

## Diagnostic Steps

### Step 1: Check Token Status

```bash
# List stored credentials
ls -la ~/.claude/google-credentials/

# Check token expiry
cat ~/.claude/google-credentials/token.json | python -m json.tool
```

### Step 2: Verify API Enablement

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Navigate to **APIs & Services** → **Enabled APIs**
3. Verify these are enabled:
   - Gmail API
   - Google Calendar API
   - Google Drive API
   - Google Sheets API

### Step 3: Test Credentials

```bash
# Use curl to test token
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  https://www.googleapis.com/oauth2/v1/tokeninfo

# Expected output includes scopes and expiry
```

### Step 4: Check MCP Logs

```bash
# View MCP server logs
cat ~/.claude/logs/mcp-google.log

# Look for error patterns
grep -i "error\|fail\|denied" ~/.claude/logs/mcp-google.log
```

---

## Re-Authentication Process

### Complete Reset

```bash
# 1. Clear all credentials
rm -rf ~/.claude/google-credentials/
rm -rf ~/.claude/oauth-tokens/

# 2. Clear MCP cache
rm -rf ~/.claude/mcp-cache/

# 3. Restart Claude Code
pkill -f claude
claude

# 4. Trigger re-authentication
# In Claude Code:
"Connect to my Google Calendar"
```

### Selective Reset (One Service)

```bash
# Clear only Gmail credentials
rm ~/.claude/google-credentials/gmail-token.json

# Restart and re-auth just Gmail
claude "Check my Gmail inbox"
```

---

## Prevention Best Practices

### 1. Credential Management
- Store tokens securely
- Never commit credentials to git
- Use environment variables for secrets

### 2. Scope Management
- Request minimum necessary scopes
- Document which scopes you need and why
- Re-auth when adding new features

### 3. Token Refresh
- Implement automatic token refresh
- Handle refresh token expiration
- Monitor token status

### 4. Error Handling
- Catch auth errors gracefully
- Provide clear re-auth instructions
- Log authentication issues for debugging

---

## Quick Reference

| Symptom | Likely Cause | Quick Fix |
|---------|--------------|-----------|
| "Login required" | Token expired | Re-authenticate |
| "Invalid grant" | Refresh token revoked | Full re-auth |
| "Access denied" | Missing scope | Re-auth with scope |
| "Rate limited" | Too many attempts | Wait 30 min |
| "Not verified" | Dev mode app | Click "Advanced" |
| "Invalid client" | Wrong credentials | Update config |

---

## Getting Help

If issues persist:

1. **Check Google Status:** [status.google.com](https://status.google.com)
2. **Review API Quotas:** Console → APIs → Quotas
3. **Ask in Discord:** #tech-support channel
4. **Email Support:** support@support-forge.com

Include in your support request:
- Error message (exact text)
- Steps to reproduce
- MCP config (redact secrets)
- Claude Code version

---

*AI Launchpad Academy - Support Forge*
