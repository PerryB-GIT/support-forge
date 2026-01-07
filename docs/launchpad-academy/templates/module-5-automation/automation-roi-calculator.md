# Automation ROI Calculator

Use this template to evaluate whether automating a task is worth the investment. Fill in the values for each task you're considering automating.

## Configuration

| Setting | Value |
|---------|-------|
| **Your Hourly Rate** | $____ /hour |
| **Analysis Period** | 12 months |

---

## ROI Calculation Table

| # | Task Description | Manual Time (hrs/week) | Frequency (times/week) | Total Weekly Hours | Setup Time (hrs) | Maintenance (hrs/month) | Break-Even (weeks) | Annual Time Saved (hrs) | Annual $ Saved |
|---|------------------|------------------------|------------------------|--------------------|--------------------|-------------------------|--------------------|-----------------------|----------------|
| 1 | _Example: Data entry from forms to spreadsheet_ | 0.5 | 10 | 5 | 2 | 0.5 | 0.5 | 254 | $12,700 |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |
| 4 | | | | | | | | | |
| 5 | | | | | | | | | |
| 6 | | | | | | | | | |
| 7 | | | | | | | | | |
| 8 | | | | | | | | | |
| 9 | | | | | | | | | |
| 10 | | | | | | | | | |

---

## Formulas

### Total Weekly Hours
```
Total Weekly Hours = Manual Time per Instance x Frequency per Week
```

### Break-Even Point (in weeks)
```
Break-Even = Setup Time / (Total Weekly Hours - (Maintenance Hours / 4))
```

### Annual Time Saved
```
Annual Time Saved = (Total Weekly Hours x 52) - (Setup Time + Maintenance Hours x 12)
```

### Annual Dollar Value Saved
```
Annual $ Saved = Annual Time Saved x Hourly Rate
```

---

## Priority Scoring Matrix

Rate each task 1-5 for the following criteria:

| Task # | Time Saved (1-5) | Error Reduction (1-5) | Scalability (1-5) | Complexity (1-5 inverse) | **Total Score** |
|--------|------------------|----------------------|-------------------|--------------------------|-----------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Scoring Guide:**
- **Time Saved**: 5 = saves 5+ hrs/week, 1 = saves < 30 min/week
- **Error Reduction**: 5 = eliminates critical errors, 1 = minimal error impact
- **Scalability**: 5 = handles 10x volume easily, 1 = no scalability benefit
- **Complexity**: 5 = simple to automate, 1 = very complex

**Prioritize tasks with scores of 15+**

---

## Quick Decision Guide

### Automate Immediately (Score 15+)
- [ ] Task: _________________ | Score: ___
- [ ] Task: _________________ | Score: ___

### Automate Soon (Score 10-14)
- [ ] Task: _________________ | Score: ___
- [ ] Task: _________________ | Score: ___

### Evaluate Later (Score 5-9)
- [ ] Task: _________________ | Score: ___
- [ ] Task: _________________ | Score: ___

### Keep Manual (Score < 5)
- [ ] Task: _________________ | Score: ___

---

## Common Automation Candidates

Check if any of these apply to your workflow:

- [ ] Form submissions to spreadsheet/CRM
- [ ] Email notifications for specific events
- [ ] Social media posting
- [ ] Invoice generation
- [ ] Report compilation
- [ ] File organization/backup
- [ ] Calendar scheduling
- [ ] Lead capture and routing
- [ ] Customer onboarding emails
- [ ] Data synchronization between apps
- [ ] Backup and archival tasks
- [ ] Monitoring and alerts

---

## Notes & Next Steps

### Tasks to Automate First:
1.
2.
3.

### Estimated Total Annual Savings:
- **Time**: _____ hours
- **Value**: $_____

### Platform Choice:
- [ ] n8n (self-hosted, complex workflows)
- [ ] Zapier (quick setup, simpler workflows)
- [ ] Make.com (visual, mid-complexity)
- [ ] Custom code (maximum flexibility)

---

*Template by Launchpad Academy - Module 5: Automation Engines*
