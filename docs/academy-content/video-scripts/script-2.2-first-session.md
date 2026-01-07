# Script 2.2: Your First Claude Code Session

**Duration:** 20 minutes (~3000-3400 words)
**Lesson:** Module 2, Lesson 2
**Purpose:** Interface overview, essential commands, basic operations

---

## OPENING

[SCREEN: Terminal with Claude Code ready]

Alright, Claude Code is installed. Now let's actually use it.

[PAUSE]

[SCREEN: "Your First Claude Code Session" title]

In this lesson, we're going to explore the interface, learn the commands you'll use every day, and complete some basic operations. By the end, you'll be comfortable having productive conversations with Claude Code.

[PAUSE]

Let's dive in.

[PAUSE]

---

## LAUNCHING CLAUDE CODE

[SCREEN: Terminal navigation]

First, open your terminal. On Windows, that's Ubuntu through WSL. On Mac and Linux, your regular terminal.

[PAUSE]

[SCREEN: Navigate to project directory]

Navigate to a folder where you want to work. For now, let's create a practice folder. Type: mkdir claude-practice

[PAUSE]

Then: cd claude-practice

[PAUSE]

[SCREEN: Launch command]

Now launch Claude Code by simply typing: claude

[PAUSE]

[SCREEN: Claude Code interface appears]

You'll see the Claude Code interface load. There's a prompt waiting for your input. This is your workspace.

[PAUSE]

---

## THE INTERFACE

[SCREEN: Interface elements labeled]

Let's break down what you're looking at.

[PAUSE]

[SCREEN: Input prompt highlighted]

At the bottom, you've got your input prompt. This is where you type your messages, questions, and instructions. Claude reads everything you type here.

[PAUSE]

[SCREEN: Response area highlighted]

Above that, you'll see Claude's responses appear. The conversation flows from top to bottom, with your messages and Claude's replies alternating.

[PAUSE]

[SCREEN: Context indicator]

You might notice some context information, like what directory you're in, or what files Claude is aware of. This helps you understand what Claude can "see" when you're working.

[PAUSE]

[SCREEN: Status indicators]

Status indicators show when Claude is thinking, when it's writing a file, or when it's waiting for your input. Pay attention to these so you know what's happening.

[PAUSE]

---

## ESSENTIAL COMMANDS

[SCREEN: Commands reference card]

Claude Code has built-in commands that start with a forward slash. These are your shortcuts for common operations.

[PAUSE]

[SCREEN: /help command]

The most important command to remember: /help

[PAUSE]

Type that now. You'll see a list of all available commands with brief descriptions. When in doubt, help.

[PAUSE]

[SCREEN: /clear command]

/clear wipes the current conversation. Useful when you want to start fresh or when the context is getting cluttered.

[PAUSE]

[SCREEN: /exit command]

/exit closes Claude Code and returns you to your regular terminal.

[PAUSE]

[SCREEN: /model command]

/model shows you which AI model you're using. Claude Code defaults to the latest Claude model.

[PAUSE]

[SCREEN: /cost command]

/cost shows your current session cost and estimated API usage. Keep an eye on this while you're learning.

[PAUSE]

[SCREEN: /memory command]

/memory lets you view what Claude remembers about your project. We'll explore this more in later lessons.

[PAUSE]

---

## YOUR FIRST CONVERSATION

[SCREEN: Ready for first prompt]

Let's have a real conversation. Don't overthink it, just type naturally.

[PAUSE]

[SCREEN: Simple greeting example]

Type: Hi Claude. I'm new to this. Can you tell me what you can help me with?

[PAUSE]

[SCREEN: Claude's response]

Claude will respond with an overview of its capabilities. Notice how it's conversational but informative. This is how interactions work: you ask or instruct, Claude responds.

[PAUSE]

[SCREEN: Follow-up question]

Now let's go deeper. Type: I'm trying to automate parts of my business. I do marketing consulting. What kinds of things could we build together?

[PAUSE]

[SCREEN: Claude's detailed response]

See how Claude adapts to your specific context? It's not giving generic advice. It's thinking about what makes sense for a marketing consultant.

[PAUSE]

This is key: the more context you give, the better the responses. Claude doesn't read your mind. Tell it what you're working on.

[PAUSE]

---

## WORKING WITH FILES

[SCREEN: File operations intro]

Claude Code can read, create, and modify files. This is where it becomes more than a chatbot.

[PAUSE]

[SCREEN: Create a file prompt]

Type: Create a simple Python script that prints "Hello, World!"

[PAUSE]

[SCREEN: Claude creates the file]

Watch what happens. Claude will create a file, usually hello.py (hello dot P-Y), and show you its contents. It'll ask for confirmation before actually writing to your filesystem.

[PAUSE]

[SCREEN: Confirmation prompt]

This confirmation step is important. Always read what Claude's about to do before saying yes. It prevents accidents.

[PAUSE]

[SCREEN: File created confirmation]

Once you confirm, the file exists in your directory. You can verify by typing: ls

[PAUSE]

That's a Linux command that lists files. You should see hello.py there.

[PAUSE]

[SCREEN: Read a file prompt]

Now let's read it back. Type: Show me what's in hello.py

[PAUSE]

[SCREEN: Claude displays file contents]

Claude reads the file and shows you its contents. You can also ask it to explain the code, modify it, or add features.

[PAUSE]

[SCREEN: Modify a file prompt]

Try this: Modify the script to ask for the user's name and then greet them personally

[PAUSE]

[SCREEN: Claude shows modification plan]

Claude will show you the changes it wants to make. It'll typically show the new code and ask for confirmation before applying.

[PAUSE]

[SCREEN: Confirming changes]

Confirm, and the file is updated. This workflow, ask, review, confirm, is how you'll work with Claude Code on real projects.

[PAUSE]

---

## ASKING FOR EXPLANATIONS

[SCREEN: Learning mode]

Claude isn't just for doing. It's for learning too.

[PAUSE]

[SCREEN: Explain prompt]

Type: Explain what each line of that Python script does. I'm new to programming.

[PAUSE]

[SCREEN: Claude's explanation]

Claude breaks down the code line by line, explaining concepts at the level you indicated. Notice I said "I'm new to programming." That context helps Claude calibrate its explanation.

[PAUSE]

[SCREEN: Follow-up for deeper understanding]

If something doesn't make sense, ask follow-ups: What does 'input()' mean exactly? Why do we use 'f' before the string?

[PAUSE]

[SCREEN: Interactive learning]

This back-and-forth is how you learn effectively. Don't just nod along. Ask questions until it clicks.

[PAUSE]

---

## CONTEXT AND MEMORY

[SCREEN: Context concept visualization]

Here's something crucial to understand: Claude Code has context awareness.

[PAUSE]

[SCREEN: Directory context]

It knows what directory you're in. It can see the files in that directory. When you reference "the script" or "that file," it knows what you mean based on your recent conversation.

[PAUSE]

[SCREEN: Conversation context]

It also remembers your conversation within the session. If you mentioned you're a marketing consultant earlier, it carries that context forward.

[PAUSE]

[SCREEN: Context limitations]

But context has limits. If you exit and restart Claude Code, the conversation resets. If your project has hundreds of files, Claude might not be aware of all of them unless you specifically reference them.

[PAUSE]

[SCREEN: Explicit context is best]

Best practice: be explicit about context. Instead of "fix the bug," say "in the hello.py file, there's an error on line 5. Fix it." Specific beats vague.

[PAUSE]

---

## RUNNING CODE

[SCREEN: Code execution]

Claude Code can also run code for you.

[PAUSE]

[SCREEN: Run command prompt]

Type: Run the hello.py script

[PAUSE]

[SCREEN: Execution output]

Claude executes the script and shows you the output. If it requires input, like our modified script asking for a name, you'll see that interactive prompt.

[PAUSE]

[SCREEN: Error handling]

If there's an error, Claude shows you the error message and typically offers to help fix it. Try intentionally breaking the code and see how Claude responds.

[PAUSE]

[SCREEN: Safety note]

Important safety note: Claude Code can execute code on your machine. That's powerful but requires trust. Always review what you're running, especially if it came from somewhere else.

[PAUSE]

---

## MULTI-STEP TASKS

[SCREEN: Complex task example]

Let's try something more complex. A multi-step task.

[PAUSE]

[SCREEN: Multi-step prompt]

Type: Create a simple web page that shows the current time. It should refresh automatically every second. Include an HTML file and a CSS file to make it look nice.

[PAUSE]

[SCREEN: Claude's plan]

Claude will often break this down into steps. First, it'll create the HTML. Then the CSS. Then it might suggest JavaScript for the auto-refresh functionality.

[PAUSE]

[SCREEN: Multiple file creation]

You'll confirm each file creation. Watch how Claude handles multiple files that need to work together. It understands the relationships.

[PAUSE]

[SCREEN: Testing the result]

Once the files are created, you can open the HTML file in a browser to see the result. On most systems: open index.html or just double-click the file in your file explorer.

[PAUSE]

[SCREEN: Iteration]

If it's not quite right, iterate: Make the background darker and center the time on the page

[PAUSE]

Claude modifies the CSS. You confirm. The result updates. This is the development workflow.

[PAUSE]

---

## PRACTICAL EXERCISE

[SCREEN: Hands-on practice]

Time for you to practice. Here's your exercise.

[PAUSE]

[SCREEN: Exercise instructions]

Create a new folder called "practice-project." Navigate into it. Ask Claude to create a simple to-do list application that runs in the terminal. It should let you add tasks, list tasks, and mark tasks as complete.

[PAUSE]

[SCREEN: Exercise goals]

Goals for this exercise: practice navigating and creating projects, experience multi-file creation, practice iterating on a solution, experience the confirm workflow multiple times.

[PAUSE]

[SCREEN: Time estimate]

This should take about fifteen to twenty minutes. Take your time. Explore. Ask Claude questions when you're stuck.

[PAUSE]

[SCREEN: Bonus challenge]

Bonus challenge: once it works, ask Claude to add a feature. Maybe saving tasks to a file so they persist between sessions. See how Claude handles adding to existing code.

[PAUSE]

---

## TIPS FOR EFFECTIVE SESSIONS

[SCREEN: Pro tips list]

Before we wrap up, here are some tips for effective Claude Code sessions.

[PAUSE]

[SCREEN: Tip 1 - Be specific]

Tip one: be specific. "Make it better" is weak. "Reduce the code duplication in the validate function" is strong.

[PAUSE]

[SCREEN: Tip 2 - One thing at a time]

Tip two: tackle one thing at a time. Don't ask Claude to build an entire application in one prompt. Break it into pieces.

[PAUSE]

[SCREEN: Tip 3 - Review before confirming]

Tip three: always review before confirming. Read the code Claude is about to write. Understand what it does. You're responsible for what runs on your machine.

[PAUSE]

[SCREEN: Tip 4 - Use /clear strategically]

Tip four: use /clear when context gets confusing. If your conversation has gone in circles, sometimes a fresh start is faster than trying to correct course.

[PAUSE]

[SCREEN: Tip 5 - Save good patterns]

Tip five: when Claude does something useful, save it somewhere. Copy interesting prompts or solutions to a notes file. Build your personal library of patterns.

[PAUSE]

---

## CLOSING

[SCREEN: Session summary]

You've just had your first real Claude Code session. You know the interface, the essential commands, and the basic workflow: ask, review, confirm, iterate.

[PAUSE]

[SCREEN: Next lesson preview]

Next up, we're going deeper into prompting. Not just asking questions, but crafting prompts that get exactly what you need for real business tasks. That's where the productivity gains really kick in.

[PAUSE]

Complete the practice exercise, then I'll see you in the next lesson.

[PAUSE]

[SCREEN: Fade to "Next: Prompting for Business Tasks" with Support Forge branding]

---

**END OF SCRIPT 2.2**

*Approximate word count: 2,000 words*
*Estimated runtime: 19:00-21:00*
