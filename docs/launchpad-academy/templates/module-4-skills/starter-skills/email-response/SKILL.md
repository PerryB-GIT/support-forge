# Email Response

Analyze an incoming email and draft a professional response with appropriate tone and content.

## Trigger

- /email-response
- /draft-email
- /reply-email
- "help me respond to this email"
- "draft an email response"
- "write a reply to this email"

## Context

This skill helps users craft professional email responses. It analyzes the incoming email for tone, urgency, and key points, then drafts an appropriate response. The goal is to save time while maintaining professional communication standards.

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| email_content | string | Yes | The email to respond to (pasted or from Gmail) |
| tone | string | No | Desired tone: formal, friendly, brief, detailed |
| action | string | No | What the response should accomplish |

## Instructions

1. **Receive the Email**
   - Ask the user to paste the email they want to respond to
   - Alternatively, if Gmail MCP is available, offer to fetch their latest unread email
   - Parse the email for: sender, subject, main content, any questions asked

2. **Analyze the Email**
   - Identify the sender's tone (formal, casual, urgent, frustrated, etc.)
   - Extract key points and questions that need addressing
   - Note any action items or requests
   - Determine urgency level
   - Present this analysis to the user

3. **Determine Response Strategy**
   - Ask the user: "What would you like to accomplish with your response?"
   - Options might include:
     - Answer questions
     - Provide information
     - Decline a request
     - Schedule a meeting
     - Acknowledge and buy time
     - Escalate or redirect
   - Ask about preferred tone if not specified

4. **Gather Response Details**
   - Ask for any specific information to include
   - Confirm key points the user wants to make
   - Check if there are any attachments to reference

5. **Draft the Response**
   - Create a draft email matching the appropriate tone
   - Address all questions/points from the original email
   - Include clear next steps or call to action
   - Keep it concise unless detail is requested

6. **Review and Refine**
   - Present the draft to the user
   - Offer variations: "Would you like me to make it more/less formal?"
   - Make requested edits
   - Offer to shorten or expand specific sections

7. **Finalize**
   - Once approved, offer to:
     - Copy to clipboard
     - Open in Gmail draft (if MCP available)
     - Save as template for future use

## Output Format

```markdown
## Email Analysis

**From**: [Sender name and email]
**Subject**: [Email subject]
**Tone**: [Detected tone]
**Urgency**: [Low/Medium/High]

**Key Points**:
- [Point 1]
- [Point 2]

**Questions to Address**:
1. [Question 1]
2. [Question 2]

**Action Items Requested**:
- [Action 1]

---

## Draft Response

**Subject**: Re: [Original subject]

[Email body]

---

**Tone**: [Tone used]
**Word Count**: [X words]
**Reading Time**: [~X seconds]
```

## Examples

### Example: Responding to Client Request

**User**: /email-response

**Claude**: Please paste the email you'd like to respond to, or I can check your Gmail for recent messages.

**User**:
```
From: john@acmecorp.com
Subject: Dashboard Update - Urgent

Hi,

We reviewed the latest dashboard mockups and have some concerns. The color scheme doesn't match our brand guidelines, and we're worried about the timeline.

Can you:
1. Revise the colors to match our brand (I'll send the style guide)
2. Confirm we're still on track for the Feb 15 launch
3. Schedule a call this week to discuss?

Thanks,
John
```

**Claude**:
## Email Analysis

**From**: John (john@acmecorp.com)
**Subject**: Dashboard Update - Urgent
**Tone**: Professional but concerned
**Urgency**: High (marked urgent, mentions timeline worry)

**Key Points**:
- Color scheme doesn't match brand guidelines
- Concern about project timeline

**Questions to Address**:
1. Can you revise colors to match brand guidelines?
2. Are we on track for Feb 15 launch?
3. Can we schedule a call this week?

**Action Items Requested**:
- Color revision (pending style guide)
- Timeline confirmation
- Meeting scheduling

---

What would you like to accomplish with your response?
- Reassure and confirm everything is on track
- Set expectations about potential delays
- Something else?

**User**: Reassure them, we can definitely hit the date

**Claude**: Here's your draft response:

---

**Subject**: Re: Dashboard Update - Urgent

Hi John,

Thanks for the feedback on the mockups.

Regarding your points:

1. **Colors**: Absolutely, we'll update the color scheme once you send the style guide. This is a quick change on our end.

2. **Timeline**: We're on track for the Feb 15 launch. The color updates won't impact our schedule.

3. **Call**: I'm available Thursday at 2 PM or Friday at 10 AM. Would either work for you?

Let me know if you have any other concerns.

Best,
[Your name]

---

**Tone**: Professional, reassuring
**Word Count**: 82 words
**Reading Time**: ~20 seconds

Would you like me to adjust anything? I can make it more formal, add more detail, or modify the available times.

## Dependencies

- Gmail MCP (optional, for fetching emails directly)

## Notes

- Always maintain professional language even if the incoming email is terse or frustrated
- When declining requests, offer alternatives when possible
- For sensitive topics (complaints, negotiations), suggest the user review carefully before sending
- Default to being concise - most email responses should be under 150 words
- Match formality level to the sender's style unless user specifies otherwise
