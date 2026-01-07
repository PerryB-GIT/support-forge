# AI Video Producer

## Overview

**Problem Solved:** Video production involves extensive pre-production work - scriptwriting, shot planning, and asset organization - that delays project timelines. Post-production documentation and publishing workflows are manual and error-prone. Teams struggle to maintain organized video libraries and consistent publishing schedules.

**Solution:** An AI video producer that generates scripts using Gemini, organizes production assets in Drive, analyzes video content for summaries and transcripts, and manages the publishing workflow - streamlining video projects from concept to distribution.

## Tools Used

| Tool | Purpose |
|------|---------|
| Gemini | Script writing, video analysis, content generation |
| Google Drive | Asset organization, project files, deliverables |
| Google Sheets | Production tracking, content calendar, asset inventory |
| Gmail | Team communication, stakeholder updates |
| n8n | Workflow orchestration |

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                     AI VIDEO PRODUCER WORKFLOW                       │
└─────────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │          PRE-PRODUCTION                  │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Trigger: New video project initiated             │
              │ (Sheet entry or form submission)                 │
              └───────────────────────┬─────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ PROJECT       │           │ SCRIPT            │           │ SHOT LIST     │
│ SETUP         │           │ GENERATION        │           │ CREATION      │
│               │           │                   │           │               │
│ Create folder │           │ Gemini:           │           │ Based on      │
│ structure in  │           │ - Generate script │           │ script:       │
│ Drive         │           │ - Multiple takes  │           │ - Scene list  │
│               │           │ - Format options  │           │ - B-roll needs│
│               │           │                   │           │ - Graphics    │
└───────────────┘           └───────────────────┘           └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │          PRODUCTION TRACKING             │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Track in Sheets:                                 │
              │ - Filming status                                 │
              │ - Asset collection                               │
              │ - Team assignments                               │
              │ - Timeline milestones                            │
              └─────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────┐
                    │          POST-PRODUCTION                 │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Trigger: Video file uploaded to Drive            │
              └───────────────────────┬─────────────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────────┐
        ▼                             ▼                                 ▼
┌───────────────┐           ┌───────────────────┐           ┌───────────────┐
│ VIDEO         │           │ TRANSCRIPT        │           │ METADATA      │
│ ANALYSIS      │           │ GENERATION        │           │ CREATION      │
│               │           │                   │           │               │
│ Gemini:       │           │ Gemini:           │           │ Generate:     │
│ - Summary     │           │ - Full transcript │           │ - Title       │
│ - Key moments │           │ - Timestamps      │           │ - Description │
│ - Topics      │           │ - Speaker labels  │           │ - Tags        │
└───────────────┘           └───────────────────┘           │ - Thumbnails  │
                                                            └───────────────┘

                    ┌─────────────────────────────────────────┐
                    │          PUBLISHING & DISTRIBUTION       │
                    └─────────────────────────────────────────┘
                                      │
                                      ▼
              ┌─────────────────────────────────────────────────┐
              │ Prepare for platforms:                           │
              │ - Export in required formats                     │
              │ - Create platform-specific descriptions          │
              │ - Generate promotional assets                    │
              │ - Schedule publishing                            │
              │ - Distribute to stakeholders                     │
              └─────────────────────────────────────────────────┘
```

## Step-by-Step Implementation

### Step 1: Set Up Video Production Tracking

**Sheet 1: Video Projects**
| Column | Description |
|--------|-------------|
| A: Project ID | Unique identifier |
| B: Title | Video title |
| C: Type | Tutorial/Interview/Promo/Testimonial |
| D: Status | Concept/Pre-Prod/Production/Post/Complete |
| E: Priority | High/Medium/Low |
| F: Client/Audience | Who it's for |
| G: Due Date | Deadline |
| H: Length Target | Target duration |
| I: Script Status | Draft/Review/Approved |
| J: Filming Status | Not Started/In Progress/Complete |
| K: Edit Status | Not Started/Rough/Fine/Final |
| L: Drive Folder | Project folder link |
| M: Assigned To | Team member |
| N: Notes | Project notes |

**Sheet 2: Asset Inventory**
| Column | Description |
|--------|-------------|
| A: Asset ID | Unique identifier |
| B: Project ID | Related project |
| C: Asset Name | File name |
| D: Type | Raw/Edited/Graphics/Audio/Other |
| E: Format | MP4/MOV/PNG/MP3/etc. |
| F: Duration | Length if video |
| G: Resolution | Video resolution |
| H: Status | Ingested/Used/Archived |
| I: Location | Drive link |
| J: Uploaded | Upload date |
| K: Notes | Asset notes |

**Sheet 3: Content Calendar**
| Column | Description |
|--------|-------------|
| A: Date | Publish date |
| B: Platform | YouTube/LinkedIn/Website/etc. |
| C: Project ID | Video project |
| D: Title | Post title |
| E: Description | Platform description |
| F: Status | Scheduled/Published |
| G: Link | Published link |
| H: Performance | View count, engagement |

**Sheet 4: Script Library**
| Column | Description |
|--------|-------------|
| A: Script ID | Unique identifier |
| B: Project ID | Related project |
| C: Version | Script version |
| D: Status | Draft/Review/Approved/Final |
| E: Word Count | Script length |
| F: Est. Duration | Estimated video length |
| G: Script Link | Drive document link |
| H: Created | Creation date |
| I: Updated | Last update |

### Step 2: Configure Pre-Production Workflow

**Workflow: Project Initialization**
```yaml
Trigger: New project added to Video Projects sheet
  │
  ├─ Node 1: Create Folder Structure
  │    - Main project folder
  │    - /Scripts/
  │    - /Assets/
  │    -   /Raw/
  │    -   /Graphics/
  │    -   /Audio/
  │    - /Exports/
  │    - /Deliverables/
  │
  ├─ Node 2: Generate Project Brief
  │    - Template document
  │    - Fill with project details
  │    - Save to project folder
  │
  ├─ Node 3: Update Sheet
  │    - Add folder link
  │    - Set initial status
  │
  └─ Node 4: Notify Team
       - Email with project details
       - Links to folder and brief
```

**Workflow: Script Generation**
```yaml
Trigger: Project status = "Pre-Prod" AND Script Status = "Needed"
  │
  ├─ Node 1: Get Project Brief
  │    - Topic/subject
  │    - Target audience
  │    - Key messages
  │    - Desired tone
  │    - Length target
  │
  ├─ Node 2: Gemini - Generate Script
  │    - Create full script
  │    - Include visual cues
  │    - Add timing estimates
  │    - Create multiple variations
  │
  ├─ Node 3: Save Script
  │    - Create Google Doc
  │    - Format professionally
  │    - Save to /Scripts/
  │
  ├─ Node 4: Generate Shot List
  │    - Based on script
  │    - List each scene
  │    - Note required B-roll
  │    - Identify graphics needs
  │
  ├─ Node 5: Update Tracking
  │    - Script Status = "Draft"
  │    - Add script link
  │    - Add to Script Library
  │
  └─ Node 6: Request Review
       - Email to stakeholder
       - Include script preview
```

### Step 3: Asset Organization

**Workflow: Asset Ingestion**
```yaml
Trigger: New file uploaded to project /Assets/ folder
  │
  ├─ Node 1: Analyze File
  │    - Determine type
  │    - Get metadata (duration, resolution)
  │    - Parse filename for context
  │
  ├─ Node 2: Organize
  │    - Move to appropriate subfolder
  │    - Standardize filename
  │
  ├─ Node 3: If Video
  │    - Gemini: Quick content analysis
  │    - Generate brief description
  │    - Identify key moments
  │
  ├─ Node 4: Add to Inventory
  │    - Create row in Asset Inventory
  │    - Link to file
  │    - Add metadata
  │
  └─ Node 5: Notify Producer
       - Daily digest of new assets
       - Or immediate if priority
```

### Step 4: Post-Production Documentation

**Workflow: Video Analysis**
```yaml
Trigger: Final video uploaded to /Exports/
  │
  ├─ Node 1: Gemini Video Analysis
  │    │
  │    ├─ Generate Summary
  │    │    - 2-3 sentence overview
  │    │    - Key takeaways
  │    │
  │    ├─ Identify Key Moments
  │    │    - Timestamps of important points
  │    │    - Quotable moments
  │    │
  │    └─ Extract Topics
  │         - Main themes covered
  │         - Keywords and tags
  │
  ├─ Node 2: Generate Transcript
  │    - Full transcript with timestamps
  │    - Speaker identification if multiple
  │    - Format for readability
  │
  ├─ Node 3: Create Documentation
  │    │
  │    ├─ Video Summary Doc
  │    │    - Summary, key moments, topics
  │    │
  │    ├─ Full Transcript Doc
  │    │    - Formatted transcript
  │    │
  │    └─ Chapter Markers
  │         - For platform uploads
  │
  ├─ Node 4: Generate Platform Content
  │    │
  │    ├─ YouTube Description
  │    │    - Optimized for SEO
  │    │    - With chapters
  │    │
  │    ├─ LinkedIn Post
  │    │    - Teaser content
  │    │
  │    └─ Website Copy
  │         - Blog post or landing page
  │
  └─ Node 5: Save All to Drive
       - Organize in /Deliverables/
       - Update project status
```

### Step 5: Publishing Workflow

**Workflow: Distribution Prep**
```yaml
Trigger: Project status = "Complete" AND distribution requested
  │
  ├─ Node 1: Export for Platforms
  │    - Verify format requirements
  │    - Check resolution/compression
  │    - Create platform-specific versions
  │
  ├─ Node 2: Prepare Metadata
  │    - Title (platform-optimized)
  │    - Description
  │    - Tags/keywords
  │    - Thumbnail suggestions
  │
  ├─ Node 3: Schedule Distribution
  │    - Add to Content Calendar
  │    - Set publish dates per platform
  │
  ├─ Node 4: Create Social Assets
  │    - Teaser clips
  │    - Quote graphics
  │    - Promotional posts
  │
  └─ Node 5: Stakeholder Package
       - Final video links
       - All supporting docs
       - Distribution schedule
       - Email to stakeholders
```

## Example Prompts/Commands

### Script Generation
```
Write a video script for:

Topic: [TOPIC]
Video Type: [TUTORIAL/INTERVIEW/PROMO/EXPLAINER]
Target Audience: [AUDIENCE_DESCRIPTION]
Key Messages:
- [MESSAGE_1]
- [MESSAGE_2]
- [MESSAGE_3]
Target Length: [X] minutes
Tone: [PROFESSIONAL/CASUAL/ENERGETIC/EDUCATIONAL]

Create a script that includes:

1. HOOK (first 10 seconds)
   - Attention-grabbing opening
   - Why viewer should keep watching

2. INTRO (15-30 seconds)
   - Introduce topic
   - Set expectations
   - Quick speaker intro if needed

3. MAIN CONTENT (body)
   - Organized into clear sections
   - Each section with:
     - Headline/transition
     - Key points
     - Examples or demonstrations
     - Visual cues [B-ROLL: ...] or [GRAPHIC: ...]

4. CONCLUSION (30-60 seconds)
   - Summary of key points
   - Clear CTA (what should viewer do next)
   - Outro/sign-off

Format with:
- [ON CAMERA] for speaking parts
- [VOICEOVER] for narration
- [B-ROLL: description] for visuals
- [GRAPHIC: description] for text/graphics
- [MUSIC: description] for audio cues
- Estimated timing for each section
```

### Video Analysis
```
Analyze this video and provide:

Video: [VIDEO_URL or description of content]
Duration: [LENGTH]
Type: [TYPE]

Generate:

1. Executive Summary (2-3 sentences)
   - What the video covers
   - Key takeaway

2. Key Moments with Timestamps
   - [00:00] - Topic/moment
   - [00:45] - Topic/moment
   - etc.

3. Chapter Markers (for YouTube)
   - Formatted for copy/paste
   - Clear, descriptive titles

4. Main Topics Covered
   - Bullet list of subjects

5. Quotable Moments
   - Direct quotes with timestamps
   - Good for social media

6. SEO Keywords
   - Primary keyword
   - 10-15 secondary keywords/phrases

7. Recommended Tags
   - Platform-appropriate tags

8. Content Warnings/Notes
   - Anything noteworthy
   - Quality issues if any
```

### Platform Description Generation
```
Create platform-specific descriptions for this video:

Video Title: [TITLE]
Summary: [BRIEF_SUMMARY]
Key Topics: [TOPICS]
Call to Action: [DESIRED_CTA]
Links to Include: [RELEVANT_LINKS]

Generate descriptions for:

1. YouTube Description
   - First 2 lines appear in search (most important)
   - Full description with chapters
   - Links and resources
   - Subscribe CTA
   - Standard end screen with related videos
   - Character limit: 5000

2. LinkedIn Post
   - Hook (first line stops scroll)
   - Value proposition
   - Conversational tone
   - Include video link
   - Character limit: 3000 (optimal under 1300)

3. Website/Blog
   - SEO-optimized headline
   - Meta description (160 chars)
   - Intro paragraph
   - Key takeaways section
   - Embedded video instructions

4. Email Newsletter
   - Subject line options (3)
   - Preview text (90 chars)
   - Body copy introducing video
   - Clear CTA to watch

Each should match platform best practices and audience expectations.
```

## Automation Triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| New project created | Create folder structure, generate brief | Real-time |
| Project in pre-prod, needs script | Generate script draft | Real-time |
| File uploaded to Assets | Analyze, organize, inventory | Real-time |
| Video uploaded to Exports | Full analysis, transcription, docs | Real-time |
| Project marked complete | Generate distribution package | Real-time |
| Scheduled publish date | Reminder to publish | Daily check |
| Weekly Monday | Production status report | Weekly |

## Expected Outcomes

### Quantitative Results
- **Script drafting time:** 80% reduction (hours to minutes)
- **Post-production documentation:** 90% automated
- **Asset organization:** 100% consistent structure
- **Platform optimization:** All content properly formatted
- **Production tracking:** Real-time visibility

### Qualitative Benefits
- Consistent video quality
- Faster concept-to-publish timeline
- Professional documentation
- Better team collaboration
- Searchable video library

## ROI Estimate

### Assumptions
- Video Producer salary: $70,000/year ($35/hour)
- Editor salary: $60,000/year ($30/hour)
- Videos produced: 4/month
- Pre-production time: 8 hours per video
- Post-production documentation: 4 hours per video
- Post-automation: 2 hours pre-prod, 1 hour post-prod

### Calculation
| Metric | Value |
|--------|-------|
| Pre-prod time saved/video | 6 hours |
| Post-prod doc time saved/video | 3 hours |
| Total time saved/video | 9 hours |
| Monthly time saved (4 videos) | 36 hours |
| Monthly labor savings | $1,170 |
| Annual savings | $14,040 |
| Tool costs (estimated) | $50/month |
| **Net annual ROI** | **$13,440** |

### Additional Value
- Faster turnaround wins more projects
- Better SEO from optimized descriptions
- Repurposable content from transcripts

## Advanced Extensions

1. **Thumbnail Generation:** AI-suggested thumbnails
2. **Multi-Language:** Auto-translation of scripts/captions
3. **Performance Analytics:** Track video performance across platforms
4. **Content Repurposing:** Auto-create clips, quotes, blog posts
5. **Voice Generation:** AI voiceover for certain content types

## Sample Project Folder Structure

```
/Video_Projects/
└── [Project_Name]_[Date]/
    ├── 00_Brief/
    │   └── Project_Brief.docx
    ├── 01_Scripts/
    │   ├── Script_v1_Draft.docx
    │   ├── Script_v2_Review.docx
    │   └── Script_FINAL.docx
    ├── 02_Assets/
    │   ├── Raw_Footage/
    │   │   ├── A_Cam/
    │   │   └── B_Cam/
    │   ├── Graphics/
    │   │   ├── Lower_Thirds/
    │   │   └── Titles/
    │   ├── Audio/
    │   │   ├── Music/
    │   │   └── SFX/
    │   └── Stock/
    ├── 03_Exports/
    │   ├── Rough_Cut_v1.mp4
    │   ├── Fine_Cut_v1.mp4
    │   └── FINAL_MASTER.mp4
    ├── 04_Deliverables/
    │   ├── YouTube/
    │   │   ├── Video.mp4
    │   │   └── Description.txt
    │   ├── LinkedIn/
    │   ├── Transcript.docx
    │   └── Video_Summary.docx
    └── 05_Archive/
        └── Project_Files.zip
```
