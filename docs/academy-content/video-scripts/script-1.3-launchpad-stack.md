# Script 1.3: Understanding the Launchpad Stack

**Duration:** 10 minutes (~1500-1700 words)
**Lesson:** Module 1, Lesson 3
**Purpose:** Full stack overview, how components connect, realistic cost expectations

---

## OPENING

[SCREEN: "The Launchpad Stack" title with architecture diagram teaser]

Now that you've got all your accounts created, let's step back and see the whole picture. What are we actually building here?

[PAUSE]

[SCREEN: Architecture diagram overview - all components]

In this lesson, I'm going to walk you through the complete Launchpad Stack. You'll understand what each component does, how they connect, and most importantly, why we're using each one.

[PAUSE]

By the end, you'll have a mental map of the entire system. Let's break it down.

[PAUSE]

---

## THE BIG PICTURE

[SCREEN: Three-layer architecture diagram]

Think of the stack in three layers. At the bottom, you've got your foundation layer, the core infrastructure. In the middle, you've got your intelligence layer, where AI does its work. And at the top, you've got your automation layer, where everything connects and triggers actions.

[PAUSE]

[SCREEN: Foundation layer highlighted]

Foundation layer handles storage, computing, and access. Intelligence layer handles thinking and creating. Automation layer handles connecting and executing.

[PAUSE]

Let's walk through each component.

[PAUSE]

---

## FOUNDATION LAYER

[SCREEN: GitHub logo with connection lines]

First: GitHub. This is your version control and collaboration hub. Even though you might not think of yourself as a coder, every project we build will live here.

[PAUSE]

Why GitHub? Because Claude Code integrates directly with it. When you're building automations, when you're creating scripts, everything gets version controlled automatically. That means you can always go back to a working version if something breaks.

[PAUSE]

[SCREEN: Git workflow visualization]

Think of it like Google Docs history, but for code and configuration. You make changes, they're tracked, you can compare versions, you can collaborate with others if needed.

[PAUSE]

[SCREEN: AWS and Google Cloud logos side by side]

Next: AWS and Google Cloud. These are your cloud infrastructure providers.

[PAUSE]

Why both? Because different services have different strengths. Google Cloud has excellent AI APIs (A-P-Is) and integrates seamlessly with Google Workspace if you're using Gmail, Drive, and Calendar. AWS has broader infrastructure options and is often where you'll deploy more complex applications.

[PAUSE]

[SCREEN: Specific services highlighted]

For this course, we're primarily using specific services within each. From Google Cloud, mainly their APIs (A-P-Is). From AWS, services like S3 (S-three) for storage, Lambda for serverless functions, and potentially Amplify for hosting if you build web applications.

[PAUSE]

You won't need to understand everything these platforms offer. We're cherry-picking the useful parts.

[PAUSE]

---

## INTELLIGENCE LAYER

[SCREEN: Anthropic/Claude logo prominently displayed]

The intelligence layer is where the magic happens, and Claude is the engine.

[PAUSE]

[SCREEN: Claude vs Claude Code comparison]

Let me clear up some confusion. Claude is the AI model. Claude Code is the development tool that lets you work with Claude in your terminal, integrated with your projects. You talk to Claude through Claude Code when you're building things.

[PAUSE]

[SCREEN: API visualization]

Under the hood, Claude Code is making API calls to Anthropic's servers. When you type a prompt, it goes to Claude, Claude thinks about it, and sends back a response. This all happens through the API key you'll set up in Module 2.

[PAUSE]

[SCREEN: Claude capabilities summary]

Claude can read and write code, analyze documents, understand context from your project files, make decisions, and generate content. It's not just answering questions. It's actively helping you build.

[PAUSE]

[SCREEN: Local + Cloud hybrid]

Here's the important part: Claude Code runs locally on your machine, but uses Claude's intelligence in the cloud. Your files stay on your computer. Only what you explicitly share in prompts goes to the API.

[PAUSE]

---

## AUTOMATION LAYER

[SCREEN: n8n and Zapier logos with workflow visualization]

The automation layer is where you connect everything and make it run without you.

[PAUSE]

[SCREEN: n8n interface preview]

n8n (n-eight-n) is our primary automation platform. It's open-source, which means more flexibility and a generous free tier. You can self-host it if you want full control, or use their cloud version, which is what I recommend for starting out.

[PAUSE]

[SCREEN: n8n workflow example - nodes connected]

In n8n, you build workflows by connecting nodes. Each node is an action: receive an email, call an API (A-P-I), update a database, send a message. You connect them together and define when they trigger.

[PAUSE]

[SCREEN: Zapier interface preview]

Zapier is your backup and sometimes your bridge. It has the largest library of pre-built integrations. Over five thousand apps. If something doesn't connect directly to n8n, Zapier probably has a connector for it.

[PAUSE]

[SCREEN: n8n vs Zapier comparison chart]

When do you use which? n8n for complex workflows where you need flexibility and control. Zapier for quick connections to apps that need ready-made integrations. We'll often use both in the same solution.

[PAUSE]

---

## HOW THEY CONNECT

[SCREEN: Full stack diagram with connection arrows animated]

Now let's see how these pieces work together.

[PAUSE]

[SCREEN: Example workflow: Customer email to automated response]

Let me give you a concrete example. A customer sends an email to your support address. Zapier or n8n detects the new email and triggers a workflow. The email content gets sent to Claude via API (A-P-I) for analysis. Claude determines what the customer needs, drafts a response, and maybe looks up information from a database on AWS. The response goes back through the automation platform and sends the email.

[PAUSE]

All of that can happen in seconds, automatically, while you're doing something else.

[PAUSE]

[SCREEN: Data flow visualization]

Data flows through the stack. GitHub stores your configuration and code. Cloud platforms store your data and provide services. Claude provides intelligence. Automation platforms connect everything and execute actions.

[PAUSE]

[SCREEN: You as the architect]

Your job is to be the architect. You design these flows, Claude helps you build them, and the automation platforms run them.

[PAUSE]

---

## REALISTIC COST EXPECTATIONS

[SCREEN: Cost breakdown chart]

Let's talk money. What does running this stack actually cost?

[PAUSE]

[SCREEN: Development phase costs]

During development and learning, you're mostly in free tiers. GitHub is free. Claude has free credits initially, then maybe five to twenty dollars per month for moderate API usage. Google Cloud free credits cover everything. AWS free tier covers everything. n8n free tier is generous. Zapier free tier is limited but workable.

[PAUSE]

[SCREEN: Production phase costs estimate]

When you're running real automations in production, costs go up but are usually reasonable. Claude API for a moderate business use case runs twenty to fifty dollars per month. n8n cloud plans start around twenty dollars per month. Zapier plans start around twenty dollars per month. AWS and Google Cloud for small-scale operations are typically under ten dollars per month.

[PAUSE]

[SCREEN: Total monthly estimate range]

Realistic total for a small business running meaningful automations: fifty to one hundred fifty dollars per month. Compare that to the time you're saving. If these automations save you ten hours per week, and your time is worth fifty dollars per hour, you're saving two thousand dollars per month in labor. The ROI (R-O-I) is obvious.

[PAUSE]

[SCREEN: Start free, scale as needed]

The beauty is you start free. You prove value before spending anything. Then you scale costs proportionally to the value you're getting.

[PAUSE]

---

## WHAT'S COMING NEXT

[SCREEN: Module roadmap with Module 2 highlighted]

You've now completed the Landscape phase. You understand where you are, what problems you're solving, what tools you have, and how they fit together.

[PAUSE]

[SCREEN: Module 2 preview - Claude Code Mastery]

Module 2 is where we get hands-on. Claude Code Mastery. This is the Architect phase. You'll install Claude Code, learn to work with it effectively, and start building real solutions.

[PAUSE]

[SCREEN: Skill progression visualization]

By the end of Module 2, you'll be having productive conversations with AI that result in actual working code and automation. Not just chatting, but collaborating.

[PAUSE]

---

## CLOSING

[SCREEN: Complete stack diagram with checkmark]

Take a moment to review the stack diagram in your resources. Understand how the pieces connect. When something makes more sense because you see how it fits into the bigger picture, the learning sticks better.

[PAUSE]

[SCREEN: Community prompt - share your audit results]

If you haven't already, share your AI Readiness Audit results in the community. Seeing what others are working on can spark ideas, and you might find someone with similar challenges to learn alongside.

[PAUSE]

[SCREEN: Fade to "Module 2: Claude Code Mastery" with Support Forge branding]

Congratulations on completing Module 1. I'll see you in Module 2, where we start building.

[PAUSE]

---

**END OF SCRIPT 1.3**

*Approximate word count: 1,550 words*
*Estimated runtime: 9:45-10:15*
