# Google Cloud Platform Quick Start Guide

Getting started with GCP for developers already familiar with AWS. Focus on AI/ML services and when to choose GCP over AWS.

---

## Table of Contents

1. [Console Navigation](#console-navigation)
2. [Project Setup](#project-setup)
3. [Billing Configuration](#billing-configuration)
4. [Key Services Overview](#key-services-overview)
5. [When to Use GCP vs AWS](#when-to-use-gcp-vs-aws)
6. [Quick Start Commands](#quick-start-commands)

---

## Console Navigation

### Accessing GCP

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Sign in with your Google account
3. Accept terms of service (first time only)

### Console Layout

| Area | Purpose |
|------|---------|
| **Navigation Menu** (hamburger icon) | Access all services |
| **Project Selector** (top bar) | Switch between projects |
| **Search Bar** | Find services, resources, docs |
| **Cloud Shell** (terminal icon) | Browser-based CLI |
| **Notifications** (bell icon) | Alerts and updates |

### Quick Navigation Tips

- Press `/` to focus search bar
- Pin frequently used services to sidebar
- Use Cloud Shell for quick CLI tasks without local setup
- Bookmark specific project URLs for fast access

### AWS to GCP Service Mapping

| AWS Service | GCP Equivalent |
|-------------|----------------|
| EC2 | Compute Engine |
| Lambda | Cloud Functions / Cloud Run |
| S3 | Cloud Storage |
| RDS | Cloud SQL |
| DynamoDB | Firestore / Bigtable |
| Route53 | Cloud DNS |
| CloudFront | Cloud CDN |
| IAM | Cloud IAM |
| CloudWatch | Cloud Monitoring |
| SageMaker | Vertex AI |
| Athena | BigQuery |

---

## Project Setup

### Understanding GCP Projects

GCP uses **Projects** as the primary organizational unit (similar to AWS Accounts). Each project:
- Has its own billing
- Contains isolated resources
- Has unique project ID (globally unique, cannot be changed)
- Can be organized into Folders and Organizations

### Creating a New Project

**Via Console:**
1. Click project selector (top bar)
2. Click **"New Project"**
3. Enter:
   - **Project name**: Human-readable name
   - **Project ID**: Auto-generated, can customize (must be unique)
   - **Organization**: Select if applicable
   - **Location**: Folder or organization
4. Click **"Create"**

**Via CLI:**
```bash
# Create project
gcloud projects create my-project-id --name="My Project"

# Set as active project
gcloud config set project my-project-id

# Enable billing (required for most services)
gcloud beta billing projects link my-project-id --billing-account=BILLING_ACCOUNT_ID
```

### Project Best Practices

- Use descriptive project IDs (cannot change later)
- Create separate projects for dev/staging/prod
- Use labels for cost tracking
- Delete unused projects to avoid confusion

### Enabling APIs

Most GCP services require API enablement:

```bash
# Enable specific API
gcloud services enable compute.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable aiplatform.googleapis.com

# List enabled APIs
gcloud services list --enabled

# Enable multiple APIs
gcloud services enable \
  compute.googleapis.com \
  storage.googleapis.com \
  bigquery.googleapis.com
```

---

## Billing Configuration

### Setting Up Billing Account

1. Go to **Navigation Menu** > **Billing**
2. Click **"Manage billing accounts"**
3. Click **"Create Account"**
4. Enter billing details and payment method
5. Link projects to billing account

### Budget Alerts

**Create budget:**
1. Go to **Billing** > **Budgets & alerts**
2. Click **"Create Budget"**
3. Configure:
   - Budget name
   - Projects to include
   - Budget amount
   - Alert thresholds (50%, 90%, 100%)

**Via CLI:**
```bash
gcloud billing budgets create \
  --billing-account=BILLING_ACCOUNT_ID \
  --display-name="Monthly Budget" \
  --budget-amount=100USD \
  --threshold-rules=percent=0.5 \
  --threshold-rules=percent=0.9 \
  --threshold-rules=percent=1.0
```

### Free Tier

GCP offers:
- **$300 credit** for new accounts (90 days)
- **Always Free** tier for many services

| Service | Free Amount |
|---------|-------------|
| Compute Engine | 1 e2-micro instance/month |
| Cloud Storage | 5 GB-months |
| Cloud Functions | 2M invocations/month |
| BigQuery | 1 TB queries/month |
| Firestore | 1 GB storage |
| Cloud Run | 2M requests/month |

### Cost Management Tips

```bash
# View current spend
gcloud billing accounts list

# Export billing to BigQuery for analysis
# (Configure in Console > Billing > Billing export)
```

---

## Key Services Overview

### Vertex AI

GCP's unified AI/ML platform. **This is where GCP shines over AWS.**

**Key Features:**
- Gemini models (Google's latest LLMs)
- AutoML (no-code model training)
- Custom model training
- Model deployment and serving
- AI pipelines

**When to Use:**
- Building AI-powered applications
- Need access to Gemini models
- Want managed ML infrastructure
- Require multimodal AI (text, image, video)

**Quick Start:**
```bash
# Enable Vertex AI
gcloud services enable aiplatform.googleapis.com

# Using Gemini via REST API
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/gemini-pro:generateContent" \
  -d '{
    "contents": [{
      "parts": [{"text": "Explain cloud computing in one sentence."}]
    }]
  }'
```

**Pricing:**
- Gemini Pro: ~$0.0025 per 1K characters input
- Custom training: Per compute hour
- Predictions: Per node hour

### BigQuery

Serverless data warehouse for analytics. **GCP's flagship data service.**

**Key Features:**
- Petabyte-scale analytics
- SQL interface
- Built-in ML (BigQuery ML)
- Real-time analytics
- Federated queries (query external data)

**When to Use:**
- Large-scale data analytics
- SQL-based machine learning
- Business intelligence dashboards
- Log analysis at scale

**Quick Start:**
```bash
# Enable BigQuery
gcloud services enable bigquery.googleapis.com

# Run query from CLI
bq query --use_legacy_sql=false \
  'SELECT * FROM `bigquery-public-data.samples.shakespeare` LIMIT 10'

# Create dataset
bq mk --dataset my-project:my_dataset

# Load data
bq load --source_format=CSV my_dataset.my_table gs://bucket/data.csv schema.json
```

**Pricing:**
- Storage: $0.02/GB/month
- Queries: $5/TB processed (first 1TB/month free)
- Streaming inserts: $0.01/200MB

### Cloud Run

Serverless containers. **Simpler than AWS Fargate, more flexible than Lambda.**

**Key Features:**
- Deploy any container
- Scale to zero
- Pay per request
- HTTPS endpoints
- Custom domains

**When to Use:**
- Containerized applications
- APIs and microservices
- Serverless backends
- Any language/framework

**Quick Start:**
```bash
# Enable Cloud Run
gcloud services enable run.googleapis.com

# Deploy from source (auto-builds container)
gcloud run deploy my-service \
  --source . \
  --region us-central1 \
  --allow-unauthenticated

# Deploy existing container
gcloud run deploy my-service \
  --image gcr.io/my-project/my-image \
  --region us-central1 \
  --allow-unauthenticated

# View services
gcloud run services list

# Get URL
gcloud run services describe my-service --region us-central1 --format='value(status.url)'
```

**Pricing:**
- CPU: $0.00002400/vCPU-second
- Memory: $0.00000250/GiB-second
- Requests: $0.40/million
- Free tier: 2M requests/month

### Cloud Functions

Event-driven serverless functions (like AWS Lambda).

**Quick Start:**
```bash
# Enable Cloud Functions
gcloud services enable cloudfunctions.googleapis.com

# Deploy function (Node.js example)
gcloud functions deploy helloWorld \
  --runtime nodejs20 \
  --trigger-http \
  --allow-unauthenticated \
  --entry-point helloWorld

# Deploy with Pub/Sub trigger
gcloud functions deploy processMessage \
  --runtime python311 \
  --trigger-topic my-topic
```

### Cloud Storage

Object storage (like S3).

**Quick Start:**
```bash
# Create bucket
gsutil mb gs://my-unique-bucket-name

# Upload file
gsutil cp file.txt gs://my-bucket/

# Sync directory
gsutil rsync -r ./local-dir gs://my-bucket/remote-dir

# Make public
gsutil iam ch allUsers:objectViewer gs://my-bucket

# List buckets
gsutil ls
```

---

## When to Use GCP vs AWS

### Choose GCP When:

| Use Case | Why GCP |
|----------|---------|
| **AI/ML Projects** | Vertex AI, Gemini models, better ML tooling |
| **Big Data Analytics** | BigQuery is superior to Athena/Redshift for ease of use |
| **Containerized Apps** | Cloud Run is simpler than Fargate |
| **Kubernetes** | GKE is the gold standard (Google created Kubernetes) |
| **Real-time Analytics** | BigQuery streaming, Dataflow |
| **Google Workspace Integration** | Native integration with Gmail, Drive, etc. |
| **Cost-Conscious ML** | Often cheaper for AI workloads |

### Choose AWS When:

| Use Case | Why AWS |
|----------|---------|
| **Enterprise Features** | More compliance certifications, services |
| **Existing AWS Investment** | Keep skills and infrastructure together |
| **Specific Services** | Lambda@Edge, DynamoDB, many AWS-only services |
| **Global Reach** | More regions worldwide |
| **Mature Tooling** | Better CLI, CloudFormation, more documentation |
| **Team Expertise** | Team already knows AWS |

### Multi-Cloud Strategy

Consider using both:
- **AWS**: Primary infrastructure, hosting, compute
- **GCP**: AI/ML workloads, BigQuery analytics

Example architecture:
```
AWS (Primary)              GCP (AI/ML)
├── EC2/ECS (compute)      ├── Vertex AI (models)
├── S3 (storage)           ├── BigQuery (analytics)
├── RDS (database)         └── Cloud Run (ML APIs)
└── CloudFront (CDN)
```

---

## Quick Start Commands

### Install gcloud CLI

**macOS:**
```bash
brew install --cask google-cloud-sdk
```

**Windows:**
Download from: https://cloud.google.com/sdk/docs/install

**Linux:**
```bash
curl https://sdk.cloud.google.com | bash
```

### Initial Setup

```bash
# Initialize and authenticate
gcloud init

# Set default project
gcloud config set project PROJECT_ID

# Set default region
gcloud config set compute/region us-central1

# View current configuration
gcloud config list

# Switch accounts
gcloud auth login

# Use service account
gcloud auth activate-service-account --key-file=key.json
```

### Common Operations

```bash
# List all projects
gcloud projects list

# Get current project
gcloud config get-value project

# List compute instances
gcloud compute instances list

# List Cloud Run services
gcloud run services list

# View logs
gcloud logging read "resource.type=cloud_run_revision" --limit 50

# Get access token (for API calls)
gcloud auth print-access-token
```

### Service Account Setup

```bash
# Create service account
gcloud iam service-accounts create my-service-account \
  --display-name="My Service Account"

# Grant permissions
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:my-service-account@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer"

# Create key file
gcloud iam service-accounts keys create key.json \
  --iam-account=my-service-account@PROJECT_ID.iam.gserviceaccount.com
```

---

## Quick Reference Card

### URLs

| Resource | URL |
|----------|-----|
| Console | console.cloud.google.com |
| Billing | console.cloud.google.com/billing |
| Vertex AI | console.cloud.google.com/vertex-ai |
| BigQuery | console.cloud.google.com/bigquery |
| Cloud Run | console.cloud.google.com/run |
| Documentation | cloud.google.com/docs |
| Pricing Calculator | cloud.google.com/products/calculator |

### Key CLI Commands

| Task | Command |
|------|---------|
| Set project | `gcloud config set project PROJECT_ID` |
| Deploy container | `gcloud run deploy SERVICE --image IMAGE` |
| Query BigQuery | `bq query 'SELECT ...'` |
| Upload to storage | `gsutil cp file gs://bucket/` |
| View logs | `gcloud logging read FILTER` |
| Enable API | `gcloud services enable API_NAME` |

---

## Next Steps

1. **Get free credits**: Sign up at cloud.google.com/free
2. **Try Vertex AI**: Build a simple AI app with Gemini
3. **Explore BigQuery**: Query public datasets
4. **Deploy to Cloud Run**: Deploy a container in under 5 minutes
5. **Connect services**: Build an end-to-end data pipeline
