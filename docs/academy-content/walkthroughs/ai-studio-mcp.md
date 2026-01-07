# Google AI Studio / Gemini MCP Integration Guide

> **Support Forge AI Launchpad Academy**
> Leverage Google's AI capabilities through Claude

---

## Overview

Google AI Studio provides access to Gemini models - Google's most capable AI. With Zapier MCP, you can use Gemini's multimodal capabilities to generate text, understand documents, analyze audio/video, and create images.

**What you'll learn:**
- Send prompts to Gemini models
- Analyze documents, audio, and video
- Generate images with Imagen
- Build conversational AI with memory

---

## Prerequisites

- [ ] Zapier MCP configured ([see setup guide](./zapier-mcp-setup.md))
- [ ] Google AI Studio / Google Cloud account
- [ ] API access enabled for Gemini
- [ ] Connected in Zapier

---

## Available Tools

| Tool | Description |
|------|-------------|
| `google_ai_studio_gemini_send_prompt` | Generate text response |
| `google_ai_studio_gemini_conversation` | Chat with memory |
| `google_ai_studio_gemini_understand_document` | Analyze documents |
| `google_ai_studio_gemini_understand_audio` | Transcribe/analyze audio |
| `google_ai_studio_gemini_understand_video` | Analyze video content |
| `google_ai_studio_gemini_understand_youtube_video` | Analyze YouTube videos |
| `google_ai_studio_gemini_generate_image` | Create images |
| `google_ai_studio_gemini_generate_audio` | Text-to-speech |
| `google_ai_studio_gemini_generate_video` | Create videos |

---

## Text Generation

### Example: Basic Prompt

```
Use Gemini to write a product description for a smart water bottle
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_send_prompt",
  "parameters": {
    "instructions": "Generate product description for smart water bottle",
    "prompt": "Write a compelling product description for a smart water bottle that tracks hydration, syncs with fitness apps, and reminds users to drink water. Keep it under 150 words.",
    "model": "gemini-1.5-pro"
  }
}
```

### Available Models

| Model | Description | Best For |
|-------|-------------|----------|
| `gemini-1.5-pro` | Most capable, multimodal | Complex tasks, analysis |
| `gemini-1.5-flash` | Fast, efficient | Quick responses |
| `gemini-1.0-pro` | Balanced | General use |

### Example: With System Instructions

```
Generate marketing copy as if you were a luxury brand copywriter
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_send_prompt",
  "parameters": {
    "instructions": "Generate luxury marketing copy",
    "prompt": "Write a tagline for a premium leather handbag collection.",
    "model": "gemini-1.5-pro",
    "systemInstructions": "You are a copywriter for a luxury fashion brand. Your tone is sophisticated, elegant, and aspirational. Use evocative language that appeals to discerning customers."
  }
}
```

### Example: Controlled Output with Temperature

```
Generate three creative taglines (high creativity)
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_send_prompt",
  "parameters": {
    "instructions": "Generate creative taglines",
    "prompt": "Generate 3 creative and unexpected taglines for a sustainable clothing brand.",
    "model": "gemini-1.5-flash",
    "temperature": "0.9",
    "maxOutputTokens": "200"
  }
}
```

### Temperature Guide

| Value | Effect | Use Case |
|-------|--------|----------|
| `0.0-0.3` | Deterministic, focused | Factual, consistent |
| `0.4-0.6` | Balanced | General content |
| `0.7-0.9` | Creative, varied | Brainstorming |
| `1.0+` | Highly random | Experimental |

### Example: With Google Search Grounding

```
Get current information about a topic using Gemini with search
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_send_prompt",
  "parameters": {
    "instructions": "Get current market information",
    "prompt": "What are the latest trends in sustainable packaging for e-commerce in 2026?",
    "model": "gemini-1.5-pro",
    "googleSearchGrounding": "true"
  }
}
```

---

## Conversational AI

### Example: Start a Conversation

```
Start a conversation with Gemini about project planning
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_conversation",
  "parameters": {
    "instructions": "Start project planning conversation",
    "message": "I'm starting a new software project. Can you help me create a project plan?",
    "model": "gemini-1.5-pro",
    "memoryKey": "project-planning-session-001",
    "systemInstructions": "You are a helpful project management assistant. Ask clarifying questions and provide structured recommendations."
  }
}
```

### Example: Continue Conversation

```
Continue the previous conversation with more details
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_conversation",
  "parameters": {
    "instructions": "Continue project planning with details",
    "message": "It's a web application for task management. We have 3 developers and a 3-month timeline.",
    "model": "gemini-1.5-pro",
    "memoryKey": "project-planning-session-001"
  }
}
```

### Memory Key Best Practices

- Use unique keys per conversation thread
- Include identifiers: `user-123-support-ticket-456`
- Memory persists across calls with same key

---

## Document Understanding

### Example: Analyze a PDF

```
Use Gemini to summarize the key points from a contract PDF
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_understand_document",
  "parameters": {
    "instructions": "Summarize contract key points",
    "fileUrl": "https://example.com/contract.pdf",
    "prompt": "Summarize the key terms, obligations, and important dates in this contract. Highlight any unusual clauses.",
    "model": "gemini-1.5-pro"
  }
}
```

### Example: Extract Data from Document

```
Extract all invoice details from a scanned document
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_understand_document",
  "parameters": {
    "instructions": "Extract invoice details",
    "fileUrl": "https://example.com/invoice.pdf",
    "prompt": "Extract the following from this invoice and format as JSON:\n- Invoice number\n- Date\n- Vendor name\n- Line items with quantities and prices\n- Total amount\n- Payment terms",
    "model": "gemini-1.5-pro"
  }
}
```

### Supported Document Formats

- PDF (`.pdf`)
- Word (`.docx`, `.doc`)
- Text (`.txt`)
- Images of documents (`.png`, `.jpg`)

---

## Audio Understanding

### Example: Transcribe Audio

```
Transcribe a meeting recording
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_understand_audio",
  "parameters": {
    "instructions": "Transcribe meeting recording",
    "fileUrl": "https://example.com/meeting-recording.mp3",
    "prompt": "Transcribe this meeting recording. Include speaker labels if you can distinguish different speakers.",
    "model": "gemini-1.5-pro"
  }
}
```

### Example: Summarize Audio Content

```
Summarize the key points from a podcast episode
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_understand_audio",
  "parameters": {
    "instructions": "Summarize podcast episode",
    "fileUrl": "https://example.com/podcast-episode.mp3",
    "prompt": "Summarize the main topics discussed in this podcast. List the key takeaways and any actionable advice mentioned.",
    "model": "gemini-1.5-pro"
  }
}
```

### Example: Extract Action Items

```
Find action items from a recorded meeting
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_understand_audio",
  "parameters": {
    "instructions": "Extract meeting action items",
    "fileUrl": "https://example.com/team-meeting.wav",
    "prompt": "Listen to this meeting recording and extract:\n1. All action items mentioned\n2. Who is responsible for each\n3. Any deadlines mentioned\n\nFormat as a bulleted list.",
    "model": "gemini-1.5-pro"
  }
}
```

### Supported Audio Formats

- MP3 (`.mp3`)
- WAV (`.wav`)
- FLAC (`.flac`)
- OGG (`.ogg`)
- M4A (`.m4a`)

---

## Video Understanding

### Example: Analyze Video Content

```
Analyze a product demo video and describe what's shown
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_understand_video",
  "parameters": {
    "instructions": "Analyze product demo video",
    "fileUrl": "https://example.com/product-demo.mp4",
    "prompt": "Watch this product demo and describe:\n1. What product is being demonstrated\n2. Key features shown\n3. Any problems it solves\n4. Suggested improvements for the demo",
    "model": "gemini-1.5-pro"
  }
}
```

### Example: Generate Video Summary

```
Create a summary with timestamps for a training video
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_understand_video",
  "parameters": {
    "instructions": "Create timestamped summary",
    "fileUrl": "https://example.com/training-video.mp4",
    "prompt": "Create a summary of this training video with timestamps for each major section. Format like:\n[0:00] Introduction\n[2:30] Topic 1\netc.",
    "model": "gemini-1.5-pro"
  }
}
```

---

## YouTube Video Analysis

### Example: Analyze YouTube Video

```
Summarize the key points from a YouTube video about productivity
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_understand_youtube_video",
  "parameters": {
    "instructions": "Summarize YouTube productivity video",
    "videoUrl": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "prompt": "Summarize the main productivity tips from this video. List them as actionable bullet points.",
    "model": "gemini-1.5-pro"
  }
}
```

### Example: Analyze Specific Section

```
Analyze only minutes 5-10 of a YouTube tutorial
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_understand_youtube_video",
  "parameters": {
    "instructions": "Analyze specific video section",
    "videoUrl": "https://www.youtube.com/watch?v=example",
    "prompt": "What are the key steps demonstrated in this section of the tutorial?",
    "startOffset": "300",
    "endOffset": "600",
    "model": "gemini-1.5-pro"
  }
}
```

### Offset Values

- Values are in seconds
- `startOffset`: Where to begin analysis
- `endOffset`: Where to stop analysis

---

## Image Generation

### Example: Generate Image from Text

```
Create an image of a futuristic city skyline at sunset
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_generate_image",
  "parameters": {
    "instructions": "Generate futuristic city image",
    "prompt": "A futuristic city skyline at sunset with flying cars, neon lights reflecting on glass buildings, and a vibrant orange and purple sky. Photorealistic style.",
    "model": "imagen-3.0-generate-001"
  }
}
```

### Example: Generate with Style Control

```
Create a product mockup in a specific style
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_generate_image",
  "parameters": {
    "instructions": "Generate styled product image",
    "prompt": "A minimalist product photo of a ceramic coffee mug on a marble surface with soft natural lighting. Clean, modern aesthetic with subtle shadows.",
    "model": "imagen-3.0-generate-001",
    "temperature": "0.7"
  }
}
```

### Example: Generate with Reference Image

```
Create a variation of an existing design
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_generate_image",
  "parameters": {
    "instructions": "Generate image variation",
    "prompt": "Create a variation of this logo design but with a blue color scheme and more geometric shapes.",
    "model": "imagen-3.0-generate-001",
    "files": ["https://example.com/original-logo.png"]
  }
}
```

### Image Generation Tips

- Be specific about style, lighting, composition
- Include negative prompts: "without text", "no people"
- Specify aspect ratio in prompt if needed

---

## Audio Generation (Text-to-Speech)

### Example: Generate Voice Audio

```
Convert text to speech for a voiceover
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_generate_audio",
  "parameters": {
    "instructions": "Generate voiceover audio",
    "prompt": "Welcome to our product tour. In this video, we'll show you how our platform can transform your workflow and save you hours every week.",
    "model": "gemini-2.0-flash-exp",
    "voiceName": "Kore"
  }
}
```

### Available Voices

| Voice | Characteristics |
|-------|-----------------|
| `Puck` | Youthful, energetic |
| `Charon` | Deep, authoritative |
| `Kore` | Warm, friendly |
| `Fenrir` | Strong, confident |
| `Aoede` | Calm, soothing |

---

## Video Generation

### Example: Generate Video from Prompt

```
Create a short video clip of waves on a beach
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__google_ai_studio_gemini_generate_video",
  "parameters": {
    "instructions": "Generate beach waves video",
    "prompt": "Gentle ocean waves rolling onto a sandy beach at golden hour. Calm, peaceful, cinematic quality. 5 seconds.",
    "model": "veo-2.0-generate-001"
  }
}
```

---

## Common Errors and Fixes

### Error: "Model not found"

**Cause:** Invalid or deprecated model name

**Fix:**
- Check current model names in Google AI Studio
- Use supported models: `gemini-1.5-pro`, `gemini-1.5-flash`
- For images: `imagen-3.0-generate-001`

### Error: "Content blocked"

**Cause:** Safety filters triggered

**Fix:**
- Review prompt for potentially problematic content
- Rephrase to be more neutral
- Add context to clarify intent

### Error: "File too large"

**Cause:** Media file exceeds size limits

**Fix:**
- Compress audio/video files
- Use lower resolution
- Split into smaller segments

### Error: "Unsupported file format"

**Cause:** Media format not supported

**Fix:**
- Convert to supported format
- Check format list for each tool
- Ensure file extension matches content

### Error: "Rate limit exceeded"

**Cause:** Too many requests

**Fix:**
- Implement delays between requests
- Upgrade API tier if needed
- Use caching for repeated requests

---

## Pro Tips

### 1. Prompt Engineering

Structure prompts clearly:
```
Role: You are a professional copywriter
Task: Write a product description
Context: For a sustainable fashion brand
Format: 3 paragraphs, under 200 words
Tone: Sophisticated but accessible
```

### 2. Multi-step Analysis

For complex documents:
```
Step 1: Send document for structure overview
Step 2: Ask specific questions about sections
Step 3: Request summary or action items
```

### 3. Consistent Output Formats

Request structured output:
```
"Format your response as JSON with keys:
- summary (string)
- keyPoints (array)
- recommendations (array)"
```

### 4. Use Memory Keys Strategically

```
user-[id]-[context]-[session]
user-123-support-ticket-456
user-123-project-planning-789
```

### 5. Optimize for Cost

- Use `gemini-1.5-flash` for simple tasks
- Use `gemini-1.5-pro` for complex analysis
- Set `maxOutputTokens` to limit response length

### 6. Video Analysis Efficiency

For long videos:
- Analyze in segments using offsets
- Ask targeted questions
- Request timestamps for reference

---

## Workflow Examples

### Content Research Workflow

```
1. Analyze YouTube video about industry trends
2. Extract key insights with Gemini prompt
3. Generate blog post outline
4. Create featured image with Imagen
```

### Meeting Processing Workflow

```
1. Transcribe meeting audio
2. Extract action items and decisions
3. Generate summary email
4. Create follow-up tasks in Sheets
```

### Document Processing Workflow

```
1. Analyze incoming document (contract, invoice)
2. Extract structured data as JSON
3. Validate against business rules
4. Add to Google Sheets for tracking
```

### Content Creation Workflow

```
1. Research topic with grounded search
2. Generate article draft
3. Create supporting images
4. Generate audio version for podcast
```

---

## Integration Scenarios

### AI Studio + Google Sheets

```
1. Read document for data extraction
2. Parse JSON response
3. Create rows in spreadsheet
```

### AI Studio + Gmail

```
1. Analyze email attachment
2. Generate response summary
3. Draft reply with recommendations
```

### AI Studio + Canva

```
1. Generate image with Imagen
2. Upload to Canva assets
3. Create design using asset
```

---

## Next Steps

- [Code Execution MCP Guide](./code-execution-mcp.md) - Process AI outputs
- [Google Workspace MCP Guide](./google-workspace-mcp.md) - Store results
- [Marketing MCP Guide](./marketing-mcp.md) - Use AI content

---

*Support Forge AI Launchpad Academy - Building the Future of AI Integration*
