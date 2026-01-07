# Support Forge - Usage Monitoring Checklist

## Daily Usage Tracking Spreadsheet
**URL:** https://docs.google.com/spreadsheets/d/1xUkmlYZEMMR1k9vwoRVKP7aFRixcIl6JKi50oEJ9Sfo/edit

## Free Tier Limits - Quick Reference

### Gemini API (Google AI Studio)
| Model | Requests/Min | Tokens/Min (Input) | Requests/Day |
|-------|-------------|-------------------|--------------|
| Gemini 2.0 Flash | 10 | 4M | 1,500 |
| Gemini 1.5 Flash | 15 | 1M | 1,500 |
| Gemini 1.5 Pro | 2 | 32K | 50 |

### BigQuery
- **Queries:** 1TB free/month
- **Storage:** 10GB free
- **BigQuery ML:** Included in query quota

### Google Cloud
- **$300 credit** for 90 days (new accounts)
- **Always Free:**
  - f1-micro VM (1 per month, US regions)
  - 5GB Cloud Storage
  - 1GB Pub/Sub

### Zapier MCP
- No additional charges
- Uses your connected Google account quotas

---

## Weekly Monitoring Tasks

### Monday Morning Check
- [ ] Review last week's API usage in tracking sheet
- [ ] Check GCP billing dashboard
- [ ] Verify no unexpected charges

### Check GCP Usage
```bash
# View current billing
gcloud billing accounts list

# View project costs
gcloud billing projects describe PROJECT_ID
```

### Check Gemini Usage
- Visit: https://aistudio.google.com/app/apikey
- Check usage statistics

---

## Billing Alerts Setup

### Create $1 Alert
```bash
gcloud billing budgets create \
  --billing-account=YOUR_BILLING_ACCOUNT \
  --display-name="Support Forge MCP Alert" \
  --budget-amount=1.00USD \
  --threshold-rules=percent=50,basis=CURRENT_SPEND \
  --threshold-rules=percent=90,basis=CURRENT_SPEND \
  --threshold-rules=percent=100,basis=CURRENT_SPEND
```

### Email Notifications
1. Go to: https://console.cloud.google.com/billing
2. Select billing account
3. Budgets & alerts
4. Create budget
5. Set $1 threshold
6. Enable email notifications

---

## Cost Avoidance Strategies

### 1. Use Gemini 2.0 Flash by Default
- Most generous free tier
- 10 requests/min, 1,500/day
- 4M tokens input

### 2. Avoid Vertex AI Unless Necessary
- Costs accumulate quickly
- Use only for paying client projects
- Always estimate costs first

### 3. BigQuery Best Practices
- Use LIMIT clauses
- Preview queries before running
- Partition large tables
- Use dry-run to estimate bytes

### 4. Rotate API Keys Monthly
- Security best practice
- Helps track usage per period
- Easy to revoke if compromised

---

## Emergency: Unexpected Charges

### Immediate Actions
1. **Disable affected API**
   ```bash
   gcloud services disable SERVICE_NAME.googleapis.com
   ```

2. **Revoke API keys**
   - https://console.cloud.google.com/apis/credentials

3. **Check for runaway jobs**
   ```bash
   gcloud compute instances list
   gcloud functions list
   ```

4. **Contact GCP Support**
   - Request billing adjustment for accidental usage

---

## Monthly Review Template

### Date: ___________

| Service | Usage | Free Limit | Status |
|---------|-------|------------|--------|
| Gemini API | ___ calls | 1,500/day | ✅/⚠️/❌ |
| BigQuery | ___ TB | 1 TB/mo | ✅/⚠️/❌ |
| Cloud Storage | ___ GB | 5 GB | ✅/⚠️/❌ |
| Cloud Run | ___ hrs | 2M req/mo | ✅/⚠️/❌ |

### Actions Taken:
-
-

### Next Month Focus:
-
-

---

*Keep this checklist updated and review weekly*
