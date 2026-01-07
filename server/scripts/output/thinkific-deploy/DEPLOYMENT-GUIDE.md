# AI Launchpad Academy - Thinkific Deployment Guide

## Videos Ready for Upload

| File | Lesson | Duration | Size |
|------|--------|----------|------|
| Module7-Lesson1-Security-Part1.mp4 | 7.1 Credential Security (Part 1) | ~2 min | 6.7 MB |
| Module7-Lesson1-Security-Part2.mp4 | 7.1 Credential Security (Part 2) | ~2 min | 6.5 MB |
| Module7-Lesson1-Security-Part3.mp4 | 7.1 Credential Security (Part 3) | ~1 min | 2.9 MB |
| Module7-Lesson1-Security-Part4.mp4 | 7.1 Credential Security (Part 4) | ~15 sec | 0.5 MB |
| Module8-Lesson1-Capstone-Overview.mp4 | 8.1 Capstone Project Overview | ~4 min | 13.2 MB |
| Module8-Lesson2-Onboarding-Part1.mp4 | 8.2 Building Onboarding Agent (Part 1) | ~2 min | 6.8 MB |
| Module8-Lesson2-Onboarding-Part2.mp4 | 8.2 Building Onboarding Agent (Part 2) | ~3 min | 16.0 MB |

**Total: 7 videos, ~52.6 MB**

---

## Thinkific Upload Instructions

### Option 1: Video Library (Recommended)

1. Log into your Thinkific admin dashboard
2. Go to **Manage Learning Content** > **Video Library**
3. Click **Upload videos**
4. Drag all 7 MP4 files or click to browse
5. Wait for processing (may take a few minutes per video)
6. Videos will be available to add to any lesson

### Option 2: Direct Lesson Upload

1. Go to **Manage Learning Content** > **Courses**
2. Select your course (AI Launchpad Academy)
3. Navigate to the appropriate lesson
4. Click **Add Content** > **Video**
5. Upload the corresponding video file
6. Set video settings (autoplay, completion tracking)

---

## Course Structure Mapping

```
Module 7: Security & Best Practices
└── Lesson 7.1: Credential Security & API Key Management
    ├── Part 1: Introduction to Credential Security
    ├── Part 2: Environment Variables & Secrets
    ├── Part 3: n8n Credential Management
    └── Part 4: Best Practices Summary

Module 8: Capstone Projects
├── Lesson 8.1: Capstone Project Overview
│   └── Overview video (single part)
└── Lesson 8.2: Building a Client Onboarding Agent
    ├── Part 1: Project Setup & Webhook Triggers
    └── Part 2: Google Services Integration
```

---

## Video Settings Recommendations

- **Autoplay**: Disabled (let students control)
- **Completion Required**: Yes (for course progress)
- **Downloadable**: Optional (for premium tier)
- **Thumbnail**: Auto-generated or custom upload

---

## Production Status

### Completed (7 videos)
- 7.1 Credential Security (4 parts)
- 8.1 Capstone Overview (1 video)
- 8.2 Onboarding Agent (2 parts)

### Pending (HeyGen credits needed)
- Remaining 117 video scripts awaiting avatar generation
- Scripts are ready at: `output/parsed-scripts/`
- Audio needs to be generated via HeyGen API

---

## Technical Specs

- **Resolution**: 1920x1080 (Full HD)
- **Format**: MP4 (H.264)
- **Audio**: AAC, synchronized with avatar
- **Slides**: Auto-generated with brand colors
- **Transitions**: 0.3s crossfade between segments
