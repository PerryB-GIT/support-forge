# Design Tools MCP Integration Guide

> **Support Forge AI Launchpad Academy**
> Canva and Figma integration through Claude

---

## Overview

Design tools are essential for creating visual content, prototypes, and collaborative designs. With Zapier MCP, Claude can help you manage designs in Canva and Figma - from creating new designs to exporting assets and managing feedback.

**What you'll learn:**
- Create and manage Canva designs
- Export designs to various formats
- Search and interact with Figma files
- Create comments and dev resources in Figma

---

## Prerequisites

- [ ] Zapier MCP configured ([see setup guide](./zapier-mcp-setup.md))
- [ ] Canva account (Pro for full features)
- [ ] Figma account (with appropriate access)
- [ ] Both accounts connected in Zapier

---

## Canva Integration

### Available Tools

| Tool | Description |
|------|-------------|
| `canva_create_design` | Create a new design |
| `canva_find_design` | Search for designs |
| `canva_export_design` | Export design to file |
| `canva_upload_asset` | Upload asset to Canva |
| `canva_import_design` | Import design from file |
| `canva_move_folder_item` | Organize designs |
| `canva_get_design_export_job` | Check export status |
| `canva_get_asset_upload_job` | Check upload status |

### Example: Create a New Design

```
Create a new Instagram post design in Canva titled "Product Launch Announcement"
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__canva_create_design",
  "parameters": {
    "instructions": "Create an Instagram post design titled Product Launch Announcement",
    "title": "Product Launch Announcement",
    "design_type__type": "InstagramPost"
  }
}
```

### Design Type Reference

| Type | Dimensions | Use Case |
|------|------------|----------|
| `InstagramPost` | 1080x1080 | Social square posts |
| `InstagramStory` | 1080x1920 | Vertical stories |
| `FacebookPost` | 1200x630 | Facebook feed |
| `TwitterPost` | 1600x900 | Twitter/X posts |
| `LinkedInPost` | 1200x1200 | LinkedIn feed |
| `Presentation` | 1920x1080 | Slide decks |
| `Poster` | Various | Print posters |
| `Logo` | 500x500 | Brand logos |
| `BusinessCard` | 3.5x2 in | Business cards |
| `YouTubeThumbnail` | 1280x720 | Video thumbnails |

### Example: Find Existing Designs

```
Find my Canva designs that contain "marketing" in the name
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__canva_find_design",
  "parameters": {
    "instructions": "Find designs with marketing in the name",
    "query": "marketing",
    "ownership": "owned"
  }
}
```

### Example: Export Design as PNG

```
Export my "Product Launch Announcement" design as a PNG file
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__canva_export_design",
  "parameters": {
    "instructions": "Export design as PNG",
    "design_id": "[design_id_from_find]",
    "format__type": "png"
  }
}
```

### Export Format Options

| Format | Description |
|--------|-------------|
| `png` | High-quality image with transparency |
| `jpg` | Compressed image |
| `pdf_standard` | Standard PDF |
| `pdf_print` | Print-quality PDF |
| `gif` | Animated GIF |
| `mp4` | Video export |
| `pptx` | PowerPoint format |

### Example: Export Specific Pages

```
Export only pages 1 and 3 of my presentation as PDF
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__canva_export_design",
  "parameters": {
    "instructions": "Export pages 1 and 3 as PDF",
    "design_id": "[design_id]",
    "format__type": "pdf_standard",
    "format__pages": "1,3"
  }
}
```

### Example: Upload Asset to Canva

```
Upload a logo image to my Canva brand assets
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__canva_upload_asset",
  "parameters": {
    "instructions": "Upload logo to brand assets",
    "name": "Company Logo 2026",
    "file": "https://example.com/logo.png"
  }
}
```

### Example: Check Export Status

```
Check the status of my design export job
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__canva_get_design_export_job",
  "parameters": {
    "instructions": "Check export job status",
    "job_id": "[job_id_from_export]"
  }
}
```

### Example: Import Design

```
Import a PSD file as a new Canva design
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__canva_import_design",
  "parameters": {
    "instructions": "Import PSD as Canva design",
    "title": "Imported Design from Photoshop",
    "file": "https://example.com/design.psd"
  }
}
```

### Example: Organize Designs

```
Move my "Q1 Campaign" design to the "Archive" folder
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__canva_move_folder_item",
  "parameters": {
    "instructions": "Move Q1 Campaign to Archive folder",
    "item_id": "[design_id]",
    "from_folder_id": "[current_folder_id]",
    "to_folder_id": "[archive_folder_id]"
  }
}
```

---

## Figma Integration

### Available Tools

| Tool | Description |
|------|-------------|
| `figma_search_file` | Search for file by key |
| `figma_search_file_meta` | Get file metadata |
| `figma_create_comment` | Add comment to file |
| `figma_delete_comment` | Remove a comment |
| `figma_react_to_comment` | React with emoji |
| `figma_create_image` | Export nodes as images |
| `figma_create_dev_resource` | Add dev resources |
| `figma_create_variable` | Create design variables (Enterprise) |
| `figma_update_variable` | Update variables (Enterprise) |

### Getting Your Figma File Key

The file key is found in your Figma file URL:
```
https://www.figma.com/file/ABC123xyz/My-Design
                          ^^^^^^^^^
                          This is the file key
```

### Example: Search for a File

```
Get details about my Figma file with key "ABC123xyz"
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__figma_search_file",
  "parameters": {
    "instructions": "Get file details",
    "file_key": "ABC123xyz",
    "depth": "1"
  }
}
```

### Example: Get File Metadata

```
Get metadata for my design file including last modified date and version
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__figma_search_file_meta",
  "parameters": {
    "instructions": "Get file metadata",
    "file_key": "ABC123xyz"
  }
}
```

### Example: Create a Comment

```
Add a comment to my Figma file saying "This button needs to be larger
for mobile accessibility"
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__figma_create_comment",
  "parameters": {
    "instructions": "Add comment about button accessibility",
    "file_key": "ABC123xyz",
    "message": "This button needs to be larger for mobile accessibility"
  }
}
```

### Example: Reply to a Comment

```
Reply to comment ID 12345 in my Figma file
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__figma_create_comment",
  "parameters": {
    "instructions": "Reply to existing comment",
    "file_key": "ABC123xyz",
    "message": "Good point! I'll update this in the next iteration.",
    "parent_id": "12345"
  }
}
```

### Example: React to a Comment

```
Add a thumbs up reaction to comment 12345
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__figma_react_to_comment",
  "parameters": {
    "instructions": "Add thumbs up reaction",
    "file_key": "ABC123xyz",
    "comment_id": "12345",
    "emoji": ":thumbsup:"
  }
}
```

### Example: Delete a Comment

```
Delete comment 12345 from my Figma file
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__figma_delete_comment",
  "parameters": {
    "instructions": "Delete comment 12345",
    "file_key": "ABC123xyz",
    "comment_id": "12345"
  }
}
```

### Example: Export Node as Image

```
Export the frame with ID "123:456" from my Figma file as PNG at 2x scale
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__figma_create_image",
  "parameters": {
    "instructions": "Export frame as PNG at 2x",
    "file_key": "ABC123xyz",
    "ids": ["123:456"],
    "format": "png",
    "scale": "2"
  }
}
```

### Image Export Options

| Parameter | Options | Description |
|-----------|---------|-------------|
| `format` | `png`, `jpg`, `svg`, `pdf` | Output format |
| `scale` | `0.5` to `4` | Export scale factor |

### Example: Create Dev Resource

```
Add a dev resource link to the button component pointing to its React
component documentation
```

**Tool Call:**
```json
{
  "tool": "mcp__zapier__figma_create_dev_resource_requires_dev_seat",
  "parameters": {
    "instructions": "Add dev resource for button component",
    "file_key": "ABC123xyz",
    "node_id": "123:456",
    "name": "React Button Component",
    "url": "https://docs.company.com/components/button"
  }
}
```

---

## Common Errors and Fixes

### Canva Errors

#### Error: "Design type not supported"

**Cause:** Invalid design type specified

**Fix:**
- Use exact type names from the reference table
- Check Canva documentation for new types
- Try creating through Canva first to verify type name

#### Error: "Export job failed"

**Cause:** Design has elements that can't be exported

**Fix:**
- Check for unsupported fonts or elements
- Try a different export format
- Export individual pages instead of all

#### Error: "Asset upload failed"

**Cause:** File format or size not supported

**Fix:**
- Supported formats: PNG, JPG, SVG, GIF, MP4, WEBM
- Check file size limits (varies by account type)
- Ensure URL is publicly accessible

### Figma Errors

#### Error: "File not found"

**Cause:** Invalid file key or no access

**Fix:**
- Verify file key from URL
- Check that connected account has access
- File may have been deleted or moved

#### Error: "Cannot create comment"

**Cause:** Permissions issue

**Fix:**
- Verify edit access to the file
- Check if commenting is disabled on file
- Ensure connected account has appropriate permissions

#### Error: "Node not found"

**Cause:** Invalid node ID for export

**Fix:**
- Node IDs change when elements are recreated
- Use the latest node ID from the file
- Check if element still exists in file

#### Error: "Dev resource requires Dev seat"

**Cause:** Account doesn't have Figma Dev Mode

**Fix:**
- Upgrade to a plan with Dev Mode
- Use a different account with Dev Mode access

---

## Pro Tips

### Canva Tips

#### 1. Use Templates for Consistency

When creating designs programmatically:
```
Create a design using my "Social Post Template" as a base
```

#### 2. Batch Exports

Export multiple formats at once by making parallel requests:
```
Export design as both PNG and PDF for web and print
```

#### 3. Asset Organization

Create a folder structure for assets:
```
Brand Assets/
  Logos/
  Icons/
  Photos/
Campaigns/
  Q1 2026/
  Q2 2026/
```

#### 4. Design Naming Convention

Use consistent naming:
```
[Client] - [Project] - [Type] - [Version]
Acme Corp - Spring Sale - Instagram Post - v2
```

### Figma Tips

#### 1. Node ID Structure

Figma node IDs follow this format:
```
123:456
^^^
Frame number and element number
```

#### 2. Comment Threads

Keep feedback organized:
```
Main comment: Describe the issue
Reply: Discuss solutions
Final reply: Mark as resolved
```

#### 3. Dev Resources Strategy

Link components to:
- Documentation pages
- Storybook instances
- GitHub component files
- Design system references

#### 4. Export at Multiple Scales

For responsive designs:
```
Export at 1x for web
Export at 2x for retina
Export at 3x for high-DPI mobile
```

---

## Workflow Examples

### Social Media Campaign Workflow

```
1. Create Instagram Post design in Canva
2. Create Twitter Post design using same branding
3. Create LinkedIn Post design for professional audience
4. Export all three as PNG
5. Upload to respective platforms (via other integrations)
```

### Design Review Workflow

```
1. Search for Figma file by key
2. Get file metadata to verify version
3. Add review comments on specific elements
4. React to existing comments with feedback
5. Export approved frames as images
```

### Asset Handoff Workflow

```
1. Find completed design in Canva
2. Export as PDF for stakeholder review
3. Export as PNG for developer handoff
4. Add dev resource links in Figma
5. Create comment notifying team of completion
```

### Brand Asset Update Workflow

```
1. Upload new logo to Canva assets
2. Find all designs using old logo
3. Update designs with new asset
4. Export updated designs
5. Move old designs to archive folder
```

---

## Integration Scenarios

### Canva + Google Drive

```
1. Create design in Canva
2. Export as PDF
3. Upload to Google Drive folder
4. Share Drive folder with stakeholders
```

### Figma + GitHub

```
1. Export component from Figma as SVG
2. Create/update file in GitHub repo
3. Open pull request with new assets
4. Add dev resource in Figma linking to PR
```

### Canva + Gmail

```
1. Find design for email campaign
2. Export as PNG
3. Create draft email with design attached
4. Send for approval
```

---

## Next Steps

- [Google Workspace MCP Guide](./google-workspace-mcp.md) - Store and share designs
- [GitHub MCP Guide](./github-mcp.md) - Version control for assets
- [Marketing MCP Guide](./marketing-mcp.md) - Use designs in campaigns

---

*Support Forge AI Launchpad Academy - Building the Future of AI Integration*
