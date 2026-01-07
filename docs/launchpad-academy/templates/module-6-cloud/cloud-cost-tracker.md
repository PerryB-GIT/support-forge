# Cloud Cost Tracker

Monthly tracking template for AWS/cloud costs. Copy this template for each month.

---

## Month: [MONTH YEAR]

**Review Date:** [DATE]
**Reviewed By:** [NAME]
**Total Budget:** $[AMOUNT]
**Total Actual:** $[AMOUNT]
**Variance:** $[AMOUNT] ([+/-]%)

---

## Summary Dashboard

| Metric | Value |
|--------|-------|
| Total AWS Spend | $ |
| Budget | $ |
| Variance | $ (%) |
| Previous Month | $ |
| Month-over-Month Change | $ (%) |
| Year-to-Date Total | $ |
| Projected Annual | $ |

---

## Cost by Service

| Service | Category | Budget | Actual | Variance | Notes |
|---------|----------|--------|--------|----------|-------|
| EC2 | Compute | $ | $ | $ | |
| EBS | Storage | $ | $ | $ | |
| S3 | Storage | $ | $ | $ | |
| RDS | Database | $ | $ | $ | |
| Lambda | Compute | $ | $ | $ | |
| CloudFront | Network | $ | $ | $ | |
| Route53 | Network | $ | $ | $ | |
| Amplify | Hosting | $ | $ | $ | |
| API Gateway | Network | $ | $ | $ | |
| CloudWatch | Monitoring | $ | $ | $ | |
| Data Transfer | Network | $ | $ | $ | |
| Other | - | $ | $ | $ | |
| **TOTAL** | | **$** | **$** | **$** | |

---

## Cost by Project/Client

| Project/Client | Budget | Actual | Variance | Primary Services |
|----------------|--------|--------|----------|------------------|
| | $ | $ | $ | |
| | $ | $ | $ | |
| | $ | $ | $ | |
| | $ | $ | $ | |
| | $ | $ | $ | |
| Internal/Overhead | $ | $ | $ | |
| **TOTAL** | **$** | **$** | **$** | |

---

## Cost by Environment

| Environment | Budget | Actual | Variance |
|-------------|--------|--------|----------|
| Production | $ | $ | $ |
| Staging | $ | $ | $ |
| Development | $ | $ | $ |
| Testing | $ | $ | $ |
| **TOTAL** | **$** | **$** | **$** |

---

## Month-over-Month Comparison

| Service | 3 Months Ago | 2 Months Ago | Last Month | This Month | Trend |
|---------|--------------|--------------|------------|------------|-------|
| EC2 | $ | $ | $ | $ | |
| S3 | $ | $ | $ | $ | |
| RDS | $ | $ | $ | $ | |
| Lambda | $ | $ | $ | $ | |
| CloudFront | $ | $ | $ | $ | |
| Other | $ | $ | $ | $ | |
| **TOTAL** | **$** | **$** | **$** | **$** | |

---

## Data Transfer Breakdown

| Transfer Type | GB | Cost |
|---------------|-----|------|
| Internet to AWS | | $ |
| AWS to Internet | | $ |
| Inter-Region | | $ |
| CloudFront | | $ |
| **TOTAL** | | **$** |

---

## Reserved Instances / Savings Plans Status

| Type | Service | Term | Expiration | Monthly Savings | Status |
|------|---------|------|------------|-----------------|--------|
| | | | | $ | |
| | | | | $ | |

**Reserved Capacity Utilization:** [%]
**Potential Additional Savings:** $[AMOUNT]

---

## Free Tier Usage

| Service | Free Limit | Used | Remaining | % Used |
|---------|------------|------|-----------|--------|
| Lambda Requests | 1M | | | % |
| Lambda GB-seconds | 400K | | | % |
| S3 Storage | 5 GB* | | | % |
| EC2 Hours | 750* | | | % |
| DynamoDB | 25 GB | | | % |

*12-month free tier only

---

## Anomalies & Unexpected Costs

| Date | Service | Expected | Actual | Cause | Resolution |
|------|---------|----------|--------|-------|------------|
| | | $ | $ | | |
| | | $ | $ | | |

---

## Optimization Actions Taken

| Action | Service | Savings | Status |
|--------|---------|---------|--------|
| | | $ | |
| | | $ | |
| | | $ | |

**Total Monthly Savings from Optimizations:** $[AMOUNT]

---

## Planned Actions for Next Month

| Action | Expected Savings | Priority | Owner |
|--------|------------------|----------|-------|
| | $ | High/Med/Low | |
| | $ | High/Med/Low | |
| | $ | High/Med/Low | |

---

## Budget Forecast

| Month | Budget | Projected | Confidence |
|-------|--------|-----------|------------|
| Current + 1 | $ | $ | |
| Current + 2 | $ | $ | |
| Current + 3 | $ | $ | |

---

## Notes & Observations

### What Went Well
-

### Concerns
-

### Action Items
- [ ]
- [ ]
- [ ]

---

## Quick CLI Commands for Data Collection

```bash
# Get current month costs by service
aws ce get-cost-and-usage \
  --time-period Start=YYYY-MM-01,End=YYYY-MM-DD \
  --granularity MONTHLY \
  --metrics "UnblendedCost" \
  --group-by Type=DIMENSION,Key=SERVICE

# Get costs by tag (if using cost allocation tags)
aws ce get-cost-and-usage \
  --time-period Start=YYYY-MM-01,End=YYYY-MM-DD \
  --granularity MONTHLY \
  --metrics "UnblendedCost" \
  --group-by Type=TAG,Key=Project

# Get daily breakdown
aws ce get-cost-and-usage \
  --time-period Start=YYYY-MM-01,End=YYYY-MM-DD \
  --granularity DAILY \
  --metrics "UnblendedCost"
```

---

## Appendix: Cost Allocation Tags

Ensure these tags are applied to all resources for accurate tracking:

| Tag Key | Required | Example Values |
|---------|----------|----------------|
| Project | Yes | client-website, internal-api |
| Environment | Yes | production, staging, development |
| Owner | Yes | team-name, developer-name |
| CostCenter | Optional | marketing, engineering |

---

*Template Version: 1.0*
*Last Updated: [DATE]*
