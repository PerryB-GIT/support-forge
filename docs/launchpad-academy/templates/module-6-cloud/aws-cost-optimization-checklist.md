# AWS Cost Optimization Checklist

Use this checklist monthly to keep AWS costs under control. Check off items as you verify them.

---

## Billing Alerts Setup

### Initial Configuration (Do Once)

- [ ] **Enable Cost Explorer**
  - AWS Console > Billing > Cost Explorer > Enable
  - Takes 24 hours to populate data

- [ ] **Create Budget Alerts**
  - AWS Console > Billing > Budgets > Create Budget
  - Set monthly budget amount
  - Configure alerts at 50%, 80%, 100%
  - Add email recipients

- [ ] **Enable Free Tier Alerts**
  - AWS Console > Billing > Billing Preferences
  - Check "Receive Free Tier Usage Alerts"
  - Enter email address

- [ ] **Set Up CloudWatch Billing Alarm**
  ```bash
  aws cloudwatch put-metric-alarm \
    --alarm-name "MonthlyBillingAlarm" \
    --metric-name EstimatedCharges \
    --namespace AWS/Billing \
    --statistic Maximum \
    --period 21600 \
    --threshold 50 \
    --comparison-operator GreaterThanThreshold \
    --dimensions Name=Currency,Value=USD \
    --evaluation-periods 1 \
    --alarm-actions arn:aws:sns:us-east-1:ACCOUNT_ID:billing-alerts
  ```

---

## Monthly Review Checklist

### EC2 Optimization

- [ ] **Review running instances**
  ```bash
  aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,LaunchTime]' --output table
  ```

- [ ] **Check for stopped instances (still incur EBS costs)**
  ```bash
  aws ec2 describe-instances --filters "Name=instance-state-name,Values=stopped" --query 'Reservations[*].Instances[*].[InstanceId,InstanceType]' --output table
  ```

- [ ] **Review CPU utilization (right-sizing)**
  - Check CloudWatch metrics for average CPU < 20% = oversized
  - Consider t3/t3a instances for variable workloads

- [ ] **Check unattached EBS volumes**
  ```bash
  aws ec2 describe-volumes --filters "Name=status,Values=available" --query 'Volumes[*].[VolumeId,Size,CreateTime]' --output table
  ```

- [ ] **Review EBS snapshots**
  ```bash
  aws ec2 describe-snapshots --owner-ids self --query 'Snapshots[*].[SnapshotId,VolumeSize,StartTime]' --output table
  ```

- [ ] **Check Elastic IPs not in use**
  ```bash
  aws ec2 describe-addresses --query 'Addresses[?AssociationId==null].[PublicIp,AllocationId]' --output table
  ```

### S3 Optimization

- [ ] **Review bucket sizes**
  ```bash
  # Get total size per bucket
  for bucket in $(aws s3api list-buckets --query 'Buckets[*].Name' --output text); do
    size=$(aws s3api list-objects-v2 --bucket $bucket --query "sum(Contents[].Size)" --output text 2>/dev/null)
    echo "$bucket: $size bytes"
  done
  ```

- [ ] **Implement lifecycle policies for old objects**
  - Move to Glacier after 90 days
  - Delete incomplete multipart uploads after 7 days
  - Example lifecycle policy:
  ```json
  {
    "Rules": [{
      "ID": "Move to Glacier",
      "Status": "Enabled",
      "Filter": {"Prefix": ""},
      "Transitions": [{
        "Days": 90,
        "StorageClass": "GLACIER"
      }],
      "AbortIncompleteMultipartUpload": {
        "DaysAfterInitiation": 7
      }
    }]
  }
  ```

- [ ] **Enable S3 Intelligent-Tiering for unknown access patterns**

- [ ] **Check for versioned buckets with excessive versions**

### Lambda Optimization

- [ ] **Review function memory allocation**
  - Use AWS Lambda Power Tuning for optimization
  - Over-provisioned memory = wasted cost

- [ ] **Check for unused functions**
  ```bash
  aws lambda list-functions --query 'Functions[*].[FunctionName,LastModified]' --output table
  ```

- [ ] **Review provisioned concurrency (expensive if unused)**

### RDS Optimization

- [ ] **Check for idle databases**
  - Review connection count in CloudWatch
  - Consider stopping dev/test instances when not in use

- [ ] **Review storage provisioned vs used**

- [ ] **Consider Reserved Instances for production databases**

### CloudFront Optimization

- [ ] **Review data transfer costs**
  - Enable compression for text-based content
  - Use appropriate cache TTLs

- [ ] **Check invalidation requests (first 1000/month free)**

### General Cleanup

- [ ] **Check for unused NAT Gateways ($0.045/hour each)**
  ```bash
  aws ec2 describe-nat-gateways --query 'NatGateways[*].[NatGatewayId,State,SubnetId]' --output table
  ```

- [ ] **Review load balancers**
  ```bash
  aws elbv2 describe-load-balancers --query 'LoadBalancers[*].[LoadBalancerName,State.Code,Type]' --output table
  ```

- [ ] **Check for unused Secrets Manager secrets ($0.40/secret/month)**
  ```bash
  aws secretsmanager list-secrets --query 'SecretList[*].[Name,LastAccessedDate]' --output table
  ```

---

## Reserved Instances Evaluation

### When to Consider Reserved Instances

- [ ] Instance running 24/7 for at least 6 months
- [ ] Predictable, steady-state workloads
- [ ] Production databases

### Savings Comparison

| Commitment | Savings | Best For |
|------------|---------|----------|
| No commitment | 0% | Variable workloads |
| 1-year All Upfront | ~40% | Confident 1-year need |
| 3-year All Upfront | ~60% | Long-term production |

### Evaluation Checklist

- [ ] Review current on-demand spend in Cost Explorer
- [ ] Identify consistent running instances
- [ ] Calculate break-even point
- [ ] Consider Savings Plans (more flexible than Reserved Instances)

---

## Free Tier Maximization

### Always Free Services

| Service | Free Amount |
|---------|-------------|
| Lambda | 1M requests/month, 400,000 GB-seconds |
| DynamoDB | 25 GB storage, 25 WCU, 25 RCU |
| CloudWatch | 10 custom metrics, 10 alarms |
| SNS | 1M publishes |
| SQS | 1M requests |
| API Gateway | 1M REST API calls |

### 12-Month Free Tier (New Accounts)

| Service | Free Amount |
|---------|-------------|
| EC2 | 750 hours/month t2.micro |
| S3 | 5 GB storage |
| RDS | 750 hours/month db.t2.micro |
| CloudFront | 50 GB data transfer |

### Tips to Stay in Free Tier

- [ ] Use t2.micro or t3.micro for EC2
- [ ] Set up billing alerts at $1 threshold
- [ ] Stop dev instances when not in use
- [ ] Delete test resources immediately after use
- [ ] Use single AZ for non-production RDS

---

## Quick Wins Checklist

### Immediate Savings (< 30 minutes)

- [ ] Delete unattached EBS volumes
- [ ] Release unused Elastic IPs
- [ ] Delete old EBS snapshots
- [ ] Stop unused EC2 instances
- [ ] Delete unused Lambda functions
- [ ] Remove old CloudWatch log groups

### Medium-Term Savings (1-2 hours)

- [ ] Implement S3 lifecycle policies
- [ ] Right-size EC2 instances
- [ ] Enable S3 Intelligent-Tiering
- [ ] Review and consolidate RDS instances

### Strategic Savings (Planning Required)

- [ ] Evaluate Reserved Instances / Savings Plans
- [ ] Implement auto-scaling
- [ ] Consider spot instances for fault-tolerant workloads
- [ ] Move to serverless where appropriate

---

## Cost Tracking Commands

```bash
# Get current month costs by service
aws ce get-cost-and-usage \
  --time-period Start=$(date -d "$(date +%Y-%m-01)" +%Y-%m-%d),End=$(date +%Y-%m-%d) \
  --granularity MONTHLY \
  --metrics "UnblendedCost" \
  --group-by Type=DIMENSION,Key=SERVICE \
  --query 'ResultsByTime[0].Groups[*].[Keys[0],Metrics.UnblendedCost.Amount]' \
  --output table

# Get daily costs for current month
aws ce get-cost-and-usage \
  --time-period Start=$(date -d "$(date +%Y-%m-01)" +%Y-%m-%d),End=$(date +%Y-%m-%d) \
  --granularity DAILY \
  --metrics "UnblendedCost" \
  --output table

# Forecast for current month
aws ce get-cost-forecast \
  --time-period Start=$(date +%Y-%m-%d),End=$(date -d "$(date +%Y-%m-01) +1 month -1 day" +%Y-%m-%d) \
  --granularity MONTHLY \
  --metric UNBLENDED_COST
```

---

## Monthly Review Schedule

| Week | Task |
|------|------|
| 1st | Review billing dashboard, check alerts |
| 2nd | EC2 and EBS cleanup |
| 3rd | S3 and data transfer review |
| 4th | Reserved Instances evaluation, plan for next month |

---

## Resources

- [AWS Cost Explorer](https://console.aws.amazon.com/cost-management/)
- [AWS Trusted Advisor](https://console.aws.amazon.com/trustedadvisor/) (cost optimization checks)
- [AWS Pricing Calculator](https://calculator.aws/)
- [Savings Plans](https://console.aws.amazon.com/savingsplans/)
