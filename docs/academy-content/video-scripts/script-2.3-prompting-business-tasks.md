# Script 2.3: Prompting for Business Tasks

**Duration:** 25 minutes (~3750-4250 words)
**Lesson:** Module 2, Lesson 3
**Purpose:** Context-rich prompting, multi-step workflows, practical business examples

---

## OPENING

[SCREEN: "Prompting for Business Tasks" title]

You know how to have a conversation with Claude Code. Now let's make those conversations actually productive for your business.

[PAUSE]

[SCREEN: Prompt quality spectrum]

Here's the reality: the quality of what you get from AI is directly proportional to the quality of what you put in. Vague prompts give vague results. Precise prompts give useful results.

[PAUSE]

In this lesson, I'll teach you to prompt like a pro. We're covering context-building, multi-step instructions, and we'll work through real business examples you can adapt to your own needs.

[PAUSE]

Let's level up your prompting game.

[PAUSE]

---

## PART 1: THE ANATOMY OF A GOOD PROMPT

[SCREEN: Prompt structure diagram]

Every effective prompt has three components: context, instruction, and constraints.

[PAUSE]

[SCREEN: Context component highlighted]

Context tells Claude what it needs to know to help you. Who you are, what you're working on, what's already been done, what the situation is.

[PAUSE]

[SCREEN: Instruction component highlighted]

Instruction tells Claude what you want it to do. This is the action, the task, the deliverable.

[PAUSE]

[SCREEN: Constraints component highlighted]

Constraints tell Claude how to do it. Formatting requirements, length limits, things to include or avoid, style preferences.

[PAUSE]

[SCREEN: Full prompt example]

Let me show you a bad prompt versus a good prompt.

[PAUSE]

[SCREEN: Bad prompt example]

Bad prompt: "Write me an email."

[PAUSE]

What email? To who? About what? In what tone? Claude could write anything. You'll spend more time fixing it than if you'd started from scratch.

[PAUSE]

[SCREEN: Good prompt example]

Good prompt: "I run a web design agency. A potential client named Sarah inquired about redesigning her bakery website. Write a professional but warm follow-up email confirming our discovery call tomorrow at 2pm EST. Keep it under 150 words."

[PAUSE]

Context: web design agency, potential client Sarah, bakery website inquiry. Instruction: write follow-up email confirming call at 2pm EST. Constraints: professional but warm, under 150 words.

[PAUSE]

[SCREEN: Comparison of outputs]

The difference in output quality is night and day. Context plus instruction plus constraints equals useful results.

[PAUSE]

---

## PART 2: CONTEXT LOADING TECHNIQUES

[SCREEN: Context loading header]

Let's dive deeper into context. There are several ways to give Claude the information it needs.

[PAUSE]

[SCREEN: Technique 1 - Direct context in prompt]

Technique one: direct context in your prompt. Just tell Claude what it needs to know. "I'm a financial advisor. My client is retiring in 5 years with a $500,000 portfolio..."

[PAUSE]

This works for one-off tasks where the context fits in a few sentences.

[PAUSE]

[SCREEN: Technique 2 - Reference files]

Technique two: reference files. Claude Code can read files in your project. You might say: "Read the client-brief.txt file and summarize the key requirements."

[PAUSE]

This is powerful when you have existing documentation, emails, specifications, or data.

[PAUSE]

[SCREEN: Technique 3 - Role assignment]

Technique three: role assignment. Tell Claude to adopt a specific perspective. "Act as an experienced copywriter who specializes in luxury brands."

[PAUSE]

This shapes how Claude thinks about the task, what vocabulary it uses, and what standards it applies.

[PAUSE]

[SCREEN: Technique 4 - Example-driven context]

Technique four: example-driven context. Show Claude what good looks like. "Here's an example of how we format proposals at my company: [example]. Now create a similar proposal for..."

[PAUSE]

Examples are incredibly effective for matching specific styles or formats.

[PAUSE]

[SCREEN: Combining techniques]

The best prompts often combine these techniques. Reference a file for data, assign a role for perspective, and give examples for formatting.

[PAUSE]

---

## PART 3: MULTI-STEP INSTRUCTIONS

[SCREEN: Multi-step workflow concept]

Some tasks are too complex for a single instruction. That's where multi-step prompting comes in.

[PAUSE]

[SCREEN: Option 1 - Sequential prompts]

Option one: sequential prompts. Break the task into steps and execute them one at a time.

[PAUSE]

[SCREEN: Sequential example]

For example: First prompt, "Analyze this competitor website and list their key features." Review the output. Second prompt, "Now compare those features to our current offering and identify gaps." Review. Third prompt, "Suggest three features we could add to address the biggest gaps."

[PAUSE]

Each step builds on the previous. You can review and redirect between steps.

[PAUSE]

[SCREEN: Option 2 - Numbered instructions]

Option two: numbered instructions in a single prompt. Tell Claude to do multiple things in sequence.

[PAUSE]

[SCREEN: Numbered example]

"Help me create a content calendar. 1) First, brainstorm 12 blog post topics relevant to small business marketing. 2) For each topic, suggest a catchy title. 3) Organize them by month, putting seasonal topics in appropriate months. 4) Output as a simple table I can paste into a spreadsheet."

[PAUSE]

Claude executes each step, building toward the final output.

[PAUSE]

[SCREEN: When to use which]

When to use which? Sequential prompts when you want to review and adjust between steps. Numbered instructions when the steps are straightforward and you trust Claude to chain them together.

[PAUSE]

---

## PART 4: BUSINESS PROMPT EXAMPLES

[SCREEN: Practical examples header]

Let's work through some real business examples. I'll show you the prompt and explain why each element is there.

[PAUSE]

[SCREEN: Example 1 - Client Email Response]

Example one: responding to a client email.

[PAUSE]

[SCREEN: The prompt text]

"I'm a freelance graphic designer. A client named Tom just emailed asking why the logo revisions are taking so long. The reality is he keeps changing requirements, and that's caused delays. Write a professional email that: 1) acknowledges his frustration, 2) diplomatically explains that scope changes have extended the timeline, 3) proposes a brief call to align on final direction, 4) maintains a positive, solution-focused tone. Keep it under 200 words."

[PAUSE]

[SCREEN: Prompt breakdown]

Context: freelance designer, client Tom, frustration about delays, real cause is changing requirements. Instruction: write email covering four specific points. Constraints: professional, diplomatic, solution-focused, under 200 words.

[PAUSE]

[SCREEN: Why this works]

This prompt gives Claude everything it needs to write an email you could actually send. No guessing about tone or content.

[PAUSE]

[SCREEN: Example 2 - Process Documentation]

Example two: creating process documentation.

[PAUSE]

[SCREEN: The prompt text]

"I manage a small e-commerce business. We just hired our first employee who'll handle order fulfillment. Create a step-by-step process document for shipping orders. Include: checking the order queue, printing packing slips, packaging standards, label printing using ShipStation, and end-of-day reporting. Format it as a numbered checklist with brief explanations. Assume they have no prior experience."

[PAUSE]

[SCREEN: Prompt breakdown]

Context: e-commerce business, new employee, order fulfillment role. Instruction: create process document for shipping. Constraints: numbered checklist, brief explanations, assumes no experience, covers specific steps.

[PAUSE]

[SCREEN: The output potential]

This produces documentation you can hand to a new hire. It's actionable, specific, and properly formatted.

[PAUSE]

[SCREEN: Example 3 - Data Analysis Request]

Example three: analyzing data.

[PAUSE]

[SCREEN: The prompt text]

"Read the sales-report.csv file in this directory. Analyze the data and provide: 1) Total revenue for each month, 2) Top 5 best-selling products, 3) Any noticeable trends or patterns, 4) Two actionable recommendations based on what you find. Present the findings in a clear, executive-summary format suitable for a non-technical business owner."

[PAUSE]

[SCREEN: Prompt breakdown]

Context: file reference provides the data. Instruction: analyze and provide four specific outputs. Constraints: executive-summary format, suitable for non-technical audience.

[PAUSE]

[SCREEN: File integration power]

Notice how referencing the file gives Claude direct access to the data. No copy-pasting needed.

[PAUSE]

[SCREEN: Example 4 - Technical Task with Business Context]

Example four: a technical task with business context.

[PAUSE]

[SCREEN: The prompt text]

"I run a small marketing agency. We send weekly email newsletters to about 2,000 subscribers using Mailchimp. We also use Airtable to track client projects. Create a Python script that: 1) Connects to the Airtable API to fetch projects completed this week, 2) Formats them as a 'Recent Wins' section with client name and project description, 3) Outputs HTML that I can paste into our Mailchimp newsletter template. Include comments explaining each section of the code since I'm not a developer."

[PAUSE]

[SCREEN: Prompt breakdown]

Context: marketing agency, Mailchimp, Airtable, weekly newsletter to 2,000 subscribers. Instruction: create Python script doing three specific things. Constraints: include explanatory comments, output pasteable HTML.

[PAUSE]

[SCREEN: Technical + accessible]

Even though this is a coding task, the business context helps Claude understand the purpose. The constraint about comments makes the code accessible to a non-developer.

[PAUSE]

---

## PART 5: ITERATION AND REFINEMENT

[SCREEN: Iteration concept]

Getting a perfect result on the first try is rare. Iteration is part of the process.

[PAUSE]

[SCREEN: Refinement prompts]

When the output isn't quite right, refine it. Here are some refinement patterns:

[PAUSE]

[SCREEN: Pattern 1 - More specific]

"Make the tone more casual. This feels too formal for our brand."

[PAUSE]

[SCREEN: Pattern 2 - Add or remove]

"Add a section about pricing. Remove the part about enterprise features, we don't offer that."

[PAUSE]

[SCREEN: Pattern 3 - Restructure]

"Reorganize this with the most important points first. Busy readers might not finish the whole thing."

[PAUSE]

[SCREEN: Pattern 4 - Match a reference]

"Make this match the style of the email I showed you earlier. It's too different."

[PAUSE]

[SCREEN: Iteration is normal]

Don't feel like you've failed if the first output isn't perfect. Two or three rounds of refinement is normal. It's still way faster than starting from scratch.

[PAUSE]

---

## PART 6: COMMON PROMPTING MISTAKES

[SCREEN: Mistakes to avoid]

Let's cover some common prompting mistakes so you can avoid them.

[PAUSE]

[SCREEN: Mistake 1 - Too vague]

Mistake one: being too vague. "Help me with marketing" tells Claude almost nothing. What aspect of marketing? For what business? What format do you need?

[PAUSE]

[SCREEN: Mistake 2 - Assuming knowledge]

Mistake two: assuming Claude knows your specifics. Claude doesn't know your business, your clients, your products, or your preferences unless you tell it. Provide context.

[PAUSE]

[SCREEN: Mistake 3 - Asking too much at once]

Mistake three: asking too much at once. "Create my entire business plan, marketing strategy, and financial projections" is overwhelming. Break it into focused tasks.

[PAUSE]

[SCREEN: Mistake 4 - No constraints]

Mistake four: no constraints. Without constraints, Claude makes its own choices about length, format, tone, and depth. You might not like those choices. Be specific about what you want.

[PAUSE]

[SCREEN: Mistake 5 - Not reviewing output]

Mistake five: not reviewing output before using it. Claude is good, but it's not perfect. Always read what it produces. Check facts. Verify that code works. Ensure the tone is right.

[PAUSE]

---

## PART 7: BUILDING YOUR PROMPT LIBRARY

[SCREEN: Prompt library concept]

Here's a productivity hack: build a personal prompt library.

[PAUSE]

[SCREEN: Saving effective prompts]

When you craft a prompt that works well, save it. Create a document or folder where you keep your best prompts.

[PAUSE]

[SCREEN: Template with blanks]

Turn them into templates with blanks. "I run a [type of business]. A client named [name] just [situation]. Write a [format] that [accomplishes goal]. Keep it [constraint]."

[PAUSE]

[SCREEN: Categories]

Organize by category. Client communication. Content creation. Data analysis. Process documentation. Technical tasks.

[PAUSE]

[SCREEN: Reuse and refine]

Next time you need something similar, grab the template, fill in the blanks, and you're ready. Over time, you'll develop a collection of proven prompts that consistently deliver good results.

[PAUSE]

---

## PRACTICAL EXERCISE

[SCREEN: Exercise instructions]

Time for practice. Here's your exercise.

[PAUSE]

[SCREEN: Exercise scenario]

Scenario: You run a consulting business. A potential client named Jennifer reached out interested in your services. You had an initial call and want to send a follow-up proposal outline.

[PAUSE]

[SCREEN: Your task]

Your task: Write a prompt that asks Claude to create this proposal outline. Include context about your consulting business, make it a fictional one if needed, details about Jennifer's needs, and constraints about format and tone.

[PAUSE]

[SCREEN: Quality criteria]

A good prompt will include: who you are, who Jennifer is and what she needs, what the proposal should cover, format preferences, and tone guidance.

[PAUSE]

[SCREEN: Test your prompt]

Then run your prompt in Claude Code and see the result. Iterate if needed until you're happy with the output.

[PAUSE]

[SCREEN: Bonus challenge]

Bonus: Save your polished prompt as a template for future proposal outlines.

[PAUSE]

---

## CLOSING

[SCREEN: Key takeaways]

Let's recap. Effective prompts have context, instruction, and constraints. Load context through direct statements, file references, role assignment, or examples. Use multi-step approaches for complex tasks. Iterate, it's part of the process. Build a prompt library to reuse what works.

[PAUSE]

[SCREEN: Practice makes permanent]

The more you prompt, the better you'll get. It becomes second nature to think in terms of context, instruction, and constraints.

[PAUSE]

[SCREEN: Next lesson preview]

Next up, we're going to configure Claude Code to work even better for you. Custom settings, your personal CLAUDE.md file, and other configurations that make Claude feel like it actually knows your business.

[PAUSE]

Complete the exercise, then I'll see you there.

[PAUSE]

[SCREEN: Fade to "Next: Configuring Settings" with Support Forge branding]

---

**END OF SCRIPT 2.3**

*Approximate word count: 2,450 words*
*Estimated runtime: 24:00-26:00*
