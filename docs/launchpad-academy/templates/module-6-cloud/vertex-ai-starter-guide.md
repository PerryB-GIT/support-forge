# Google Cloud Vertex AI Starter Guide

Get started with Vertex AI for business automation and AI workloads.

---

## What is Vertex AI?

Vertex AI is Google Cloud's unified AI platform for:
- Using pre-trained AI models (Gemini, PaLM)
- Training custom models
- Deploying AI applications
- Managing ML pipelines

---

## Initial Setup

### Step 1: Enable Vertex AI API

```bash
# Using gcloud CLI
gcloud services enable aiplatform.googleapis.com

# Or via Cloud Console:
# 1. Go to APIs & Services
# 2. Click "Enable APIs"
# 3. Search "Vertex AI API"
# 4. Click Enable
```

### Step 2: Create Service Account

```bash
# Create service account
gcloud iam service-accounts create vertex-ai-user \
    --display-name="Vertex AI User"

# Grant permissions
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:vertex-ai-user@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/aiplatform.user"

# Download credentials
gcloud iam service-accounts keys create vertex-ai-key.json \
    --iam-account=vertex-ai-user@YOUR_PROJECT_ID.iam.gserviceaccount.com
```

### Step 3: Set Environment Variables

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/vertex-ai-key.json"
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_REGION="us-central1"
```

---

## Quick Start: Text Generation with Gemini

### Python SDK Setup

```bash
pip install google-cloud-aiplatform
```

### Basic Text Generation

```python
from google.cloud import aiplatform
from vertexai.generative_models import GenerativeModel

# Initialize
aiplatform.init(project="your-project-id", location="us-central1")

# Load model
model = GenerativeModel("gemini-1.5-flash")

# Generate text
response = model.generate_content("Explain AI in simple terms for a business owner")

print(response.text)
```

### With Custom Parameters

```python
from vertexai.generative_models import GenerativeModel, GenerationConfig

model = GenerativeModel("gemini-1.5-flash")

config = GenerationConfig(
    temperature=0.7,
    top_p=0.95,
    top_k=40,
    max_output_tokens=1024,
)

response = model.generate_content(
    "Write a professional email to reschedule a meeting",
    generation_config=config
)

print(response.text)
```

---

## Business Use Cases

### 1. Document Summarization

```python
def summarize_document(text: str, max_words: int = 200) -> str:
    """Summarize a document for executive review."""
    model = GenerativeModel("gemini-1.5-flash")

    prompt = f"""Summarize the following document in {max_words} words or less.
    Focus on key points, decisions needed, and action items.

    Document:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text
```

### 2. Email Response Generator

```python
def generate_email_response(
    original_email: str,
    tone: str = "professional",
    action: str = "accept"
) -> str:
    """Generate an appropriate email response."""
    model = GenerativeModel("gemini-1.5-flash")

    prompt = f"""Generate a {tone} email response.
    Action to take: {action}

    Original email:
    {original_email}

    Write a response that is clear, concise, and maintains good business relationships.
    """

    response = model.generate_content(prompt)
    return response.text
```

### 3. Data Extraction

```python
import json

def extract_contact_info(text: str) -> dict:
    """Extract contact information from unstructured text."""
    model = GenerativeModel("gemini-1.5-flash")

    prompt = f"""Extract contact information from this text and return as JSON.
    Include: name, email, phone, company, title (if available).
    Return null for missing fields.

    Text:
    {text}

    Return only valid JSON, no explanation.
    """

    response = model.generate_content(prompt)

    # Parse JSON response
    try:
        return json.loads(response.text)
    except json.JSONDecodeError:
        return {"error": "Could not parse response"}
```

### 4. Content Classification

```python
def classify_support_ticket(ticket_text: str) -> dict:
    """Classify a support ticket by category and priority."""
    model = GenerativeModel("gemini-1.5-flash")

    prompt = f"""Analyze this support ticket and classify it.

    Ticket:
    {ticket_text}

    Return JSON with:
    - category: (billing, technical, feature-request, complaint, other)
    - priority: (low, medium, high, urgent)
    - sentiment: (positive, neutral, negative)
    - suggested_action: brief recommendation

    Return only valid JSON.
    """

    response = model.generate_content(prompt)
    return json.loads(response.text)
```

---

## Integration Patterns

### REST API Integration

```python
import requests
import google.auth
from google.auth.transport.requests import Request

def call_vertex_api(prompt: str) -> str:
    """Call Vertex AI via REST API."""
    credentials, project = google.auth.default()
    credentials.refresh(Request())

    endpoint = f"https://us-central1-aiplatform.googleapis.com/v1/projects/{project}/locations/us-central1/publishers/google/models/gemini-1.5-flash:generateContent"

    headers = {
        "Authorization": f"Bearer {credentials.token}",
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 1024
        }
    }

    response = requests.post(endpoint, headers=headers, json=payload)
    result = response.json()

    return result["candidates"][0]["content"]["parts"][0]["text"]
```

### Flask Web Service

```python
from flask import Flask, request, jsonify
from google.cloud import aiplatform
from vertexai.generative_models import GenerativeModel

app = Flask(__name__)
aiplatform.init(project="your-project", location="us-central1")
model = GenerativeModel("gemini-1.5-flash")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    response = model.generate_content(prompt)
    return jsonify({"response": response.text})

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    text = data.get("text", "")

    prompt = f"Summarize this text in 3 bullet points:\n\n{text}"
    response = model.generate_content(prompt)

    return jsonify({"summary": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

---

## Cost Management

### Pricing Overview (as of 2025)

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|-------|----------------------|------------------------|
| Gemini 1.5 Flash | $0.075 | $0.30 |
| Gemini 1.5 Pro | $1.25 | $5.00 |

### Cost Optimization Tips

```python
# 1. Use Flash for simple tasks
model = GenerativeModel("gemini-1.5-flash")  # Cheaper

# 2. Use Pro for complex reasoning
model = GenerativeModel("gemini-1.5-pro")    # More capable

# 3. Limit output tokens
config = GenerationConfig(max_output_tokens=256)  # Reduce costs

# 4. Cache responses when appropriate
from functools import lru_cache

@lru_cache(maxsize=100)
def cached_generation(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text
```

### Budget Alerts

```bash
# Set up budget alert
gcloud billing budgets create \
    --billing-account=BILLING_ACCOUNT_ID \
    --display-name="Vertex AI Budget" \
    --budget-amount=100USD \
    --threshold-rules=percent=50 \
    --threshold-rules=percent=90 \
    --threshold-rules=percent=100
```

---

## Security Best Practices

### 1. Use Service Accounts (Not User Credentials)

```python
# Good: Service account
from google.cloud import aiplatform
aiplatform.init(project="my-project", location="us-central1")

# Avoid: User credentials in code
```

### 2. Implement Rate Limiting

```python
from ratelimit import limits, sleep_and_retry

@sleep_and_retry
@limits(calls=60, period=60)  # 60 calls per minute
def rate_limited_generation(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text
```

### 3. Input Validation

```python
def safe_generate(prompt: str) -> str:
    # Validate input
    if len(prompt) > 10000:
        raise ValueError("Prompt too long")

    if not prompt.strip():
        raise ValueError("Empty prompt")

    # Generate response
    response = model.generate_content(prompt)
    return response.text
```

---

## Monitoring & Logging

### Enable Logging

```python
import logging
from google.cloud import logging as cloud_logging

# Initialize Cloud Logging
client = cloud_logging.Client()
client.setup_logging()

logger = logging.getLogger(__name__)

def logged_generation(prompt: str) -> str:
    logger.info(f"Generation request: {prompt[:100]}...")

    try:
        response = model.generate_content(prompt)
        logger.info(f"Generation success: {len(response.text)} chars")
        return response.text
    except Exception as e:
        logger.error(f"Generation failed: {e}")
        raise
```

### View Logs

```bash
# View recent logs
gcloud logging read "resource.type=aiplatform.googleapis.com" --limit=50

# Or use Cloud Console:
# Logging → Logs Explorer → Filter by "aiplatform"
```

---

## Quick Reference

### Available Models

| Model | Use Case |
|-------|----------|
| `gemini-1.5-flash` | Fast, cost-effective tasks |
| `gemini-1.5-pro` | Complex reasoning |
| `text-embedding-004` | Text embeddings |
| `imagen-3.0` | Image generation |

### Common Regions

| Region | Location |
|--------|----------|
| `us-central1` | Iowa (recommended) |
| `us-east1` | South Carolina |
| `europe-west1` | Belgium |
| `asia-northeast1` | Tokyo |

---

## Resources

- [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
- [Gemini API Reference](https://cloud.google.com/vertex-ai/generative-ai/docs)
- [Pricing Calculator](https://cloud.google.com/products/calculator)
- [Python SDK](https://github.com/googleapis/python-aiplatform)

---

*AI Launchpad Academy - Support Forge*
