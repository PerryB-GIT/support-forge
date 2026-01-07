# Script 2.1: Installing Claude Code

**Duration:** 15 minutes (~2250-2550 words)
**Lesson:** Module 2, Lesson 1
**Purpose:** Windows/WSL, Mac, and Linux installation procedures

---

## OPENING

[SCREEN: "Module 2: ARCHITECT Phase" title card]

Welcome to Module 2, the Architect phase. This is where we master Claude Code, your AI development partner.

[PAUSE]

[SCREEN: "Installing Claude Code" lesson title]

Before we can use it, we need to install it. In this lesson, I'll walk you through installation on Windows with WSL (W-S-L), Mac, and Linux. Find your operating system section and follow along.

[PAUSE]

By the end, you'll have Claude Code running and authenticated. Let's get it set up.

[PAUSE]

---

## PREREQUISITES CHECK

[SCREEN: Prerequisites checklist]

Before we start, let's make sure you've got what you need.

[PAUSE]

[SCREEN: Node.js requirement]

You need Node.js (node-J-S) version eighteen or higher installed. If you're not sure, open a terminal and type node dash dash version. If you see a version number starting with eighteen or higher, you're good.

[PAUSE]

[SCREEN: Node.js installation page]

If you don't have Node, go to nodejs.org (node-J-S dot org) and download the LTS (L-T-S) version. That stands for Long Term Support, which means it's stable. Run the installer, accept the defaults.

[PAUSE]

[SCREEN: Anthropic account reminder]

You also need your Anthropic account ready. You created this in Module 1. We'll grab an API (A-P-I) key during this installation.

[PAUSE]

---

## WINDOWS INSTALLATION (WITH WSL)

[SCREEN: Windows logo with WSL callout]

Let's start with Windows. We're going to use WSL, the Windows Subsystem for Linux. This gives you a proper Linux environment inside Windows, which makes development work much smoother.

[PAUSE]

[SCREEN: PowerShell admin window]

First, open PowerShell as Administrator. Right-click the Start menu, select "Windows Terminal (Admin)" or "PowerShell (Admin)."

[PAUSE]

[SCREEN: WSL install command]

Type this command: wsl dash dash install

[PAUSE]

Hit Enter. Windows will download and install WSL with Ubuntu (oo-BOON-too) as the default Linux distribution. This might take a few minutes depending on your internet speed.

[PAUSE]

[SCREEN: Restart prompt]

When it's done, you'll probably need to restart your computer. Do that.

[PAUSE]

[SCREEN: Ubuntu first-time setup]

After restart, open Ubuntu from your Start menu. First time launching, it'll ask you to create a username and password. This is your Linux user, separate from Windows. Pick something simple you'll remember.

[PAUSE]

[SCREEN: Ubuntu terminal ready]

Now you've got a Linux terminal running inside Windows. This is where we'll install Claude Code.

[PAUSE]

[SCREEN: npm install command]

In the Ubuntu terminal, type: npm install dash g at anthropic slash claude-code

[PAUSE]

The dash g flag installs it globally so you can run it from anywhere. npm will download the package and its dependencies.

[PAUSE]

[SCREEN: Installation progress]

You'll see a progress bar as packages download. When it finishes without errors, you're ready to authenticate.

[PAUSE]

[SCREEN: Authentication command]

Type: claude

[PAUSE]

This launches Claude Code for the first time. It'll prompt you to authenticate.

[PAUSE]

[SCREEN: Browser authentication flow]

A browser window should open automatically, taking you to Anthropic's login page. If it doesn't, copy the URL (U-R-L) from the terminal and paste it into your browser.

[PAUSE]

[SCREEN: Anthropic login]

Sign in with your Anthropic account. Authorize the connection when prompted.

[PAUSE]

[SCREEN: Success message in terminal]

Back in your terminal, you should see a success message. Claude Code is now installed and authenticated.

[PAUSE]

[SCREEN: Quick test]

Let's verify it works. Type: claude "Hello, are you working?"

[PAUSE]

If Claude responds, you're all set. Windows users, you can skip to the end of this lesson.

[PAUSE]

---

## MAC INSTALLATION

[SCREEN: Apple logo]

Mac users, you've got the smoothest installation process.

[PAUSE]

[SCREEN: Terminal application]

Open Terminal. You can find it in Applications, then Utilities, or just search for "Terminal" using Spotlight.

[PAUSE]

[SCREEN: Check Node version command]

First, verify Node is installed. Type: node dash dash version

[PAUSE]

If you see version 18 or higher, you're good. If not, or if you get an error, install Node.

[PAUSE]

[SCREEN: Homebrew installation option]

The easiest way on Mac is using Homebrew (home-brew). If you don't have Homebrew, install it first by going to brew.sh (brew dot S-H) and running the command they show.

[PAUSE]

[SCREEN: Node install via Homebrew]

Once Homebrew is ready, type: brew install node

[PAUSE]

That'll get you the latest Node version.

[PAUSE]

[SCREEN: npm install command for Mac]

Now install Claude Code. Type: npm install dash g at anthropic slash claude-code

[PAUSE]

[SCREEN: Possible permission error]

If you get a permission error, you might need to prefix with sudo. Type: sudo npm install dash g at anthropic slash claude-code

[PAUSE]

Enter your Mac password when prompted. This gives npm temporary administrator privileges to install globally.

[PAUSE]

[SCREEN: Authentication]

Once installed, authenticate by typing: claude

[PAUSE]

[SCREEN: Browser authentication flow]

Your default browser opens to Anthropic's authentication page. Sign in with your Anthropic account and authorize the connection.

[PAUSE]

[SCREEN: Verification]

Back in Terminal, verify it works: claude "Hello, are you working?"

[PAUSE]

If Claude responds, you're done. Mac users, skip to the end.

[PAUSE]

---

## LINUX INSTALLATION

[SCREEN: Linux penguin logo]

Linux users, you're probably comfortable in the terminal already, so this will be quick.

[PAUSE]

[SCREEN: Terminal prompt]

Open your terminal. Verify Node.js is installed: node dash dash version

[PAUSE]

[SCREEN: Installing Node on Linux]

If you need Node, use your distribution's package manager. For Ubuntu or Debian (deb-ee-an), you'll want to use NodeSource (node-source) for the latest version. Commands are in your lesson resources.

[PAUSE]

For Fedora (feh-DOR-ah) or Red Hat, use dnf. For Arch, use pacman. Check the resources for your specific distribution.

[PAUSE]

[SCREEN: npm install command]

Once Node is ready: npm install dash g at anthropic slash claude-code

[PAUSE]

If you get permission issues, you can use sudo, or better yet, configure npm to install global packages in your home directory. The safer approach avoids permission issues long-term. Instructions are in the resources.

[PAUSE]

[SCREEN: Authentication]

Authenticate: claude

[PAUSE]

[SCREEN: Browser may not open automatically]

Depending on your setup, the browser might not open automatically. If not, copy the URL (U-R-L) from the terminal output and paste it into your browser.

[PAUSE]

[SCREEN: Login and authorize]

Log in to Anthropic, authorize the connection, and you're done.

[PAUSE]

[SCREEN: Verification]

Verify: claude "Hello, are you working?"

[PAUSE]

---

## API KEY SETUP (ALTERNATIVE METHOD)

[SCREEN: API Key option callout]

Quick aside: there's an alternative authentication method using an API key directly. Some advanced users prefer this.

[PAUSE]

[SCREEN: Anthropic Console API Keys section]

Go to console.anthropic.com (console dot anthropic dot com). Navigate to API Keys. Click "Create Key."

[PAUSE]

[SCREEN: Key creation]

Name it something descriptive like "Claude Code Local." Copy the key immediately. You won't be able to see it again.

[PAUSE]

[SCREEN: Environment variable setup]

Set it as an environment variable. On Mac or Linux: export ANTHROPIC underscore API underscore KEY equals your-key-here

[PAUSE]

Add that line to your shell configuration file, dot bashrc (dot bash-R-C) or dot zshrc (dot Z-S-H-R-C), to make it permanent.

[PAUSE]

[SCREEN: Windows environment variable]

On Windows with WSL, same process in your Ubuntu terminal.

[PAUSE]

This method is useful if you're using Claude Code in CI/CD (C-I-C-D) pipelines or automated scripts where browser login isn't practical.

[PAUSE]

---

## TROUBLESHOOTING COMMON ISSUES

[SCREEN: Troubleshooting header]

Let's cover common issues people run into.

[PAUSE]

[SCREEN: Issue 1 - npm not found]

Issue one: "npm not found." This means Node.js isn't installed or isn't in your PATH (path). Reinstall Node and make sure to restart your terminal after installation.

[PAUSE]

[SCREEN: Issue 2 - Permission denied]

Issue two: "Permission denied" on global install. Either use sudo, which works but isn't ideal, or configure npm to use a different directory for global packages. Search for "npm global without sudo" for guides.

[PAUSE]

[SCREEN: Issue 3 - Browser doesn't open]

Issue three: Browser doesn't open during authentication. Copy the URL (U-R-L) manually from the terminal. It'll be printed in the output.

[PAUSE]

[SCREEN: Issue 4 - Authentication fails]

Issue four: Authentication fails. Check that you're logged into the correct Anthropic account. Check that your account has API access enabled. Free credits should be available for new accounts.

[PAUSE]

[SCREEN: Issue 5 - WSL specific issues]

Issue five, Windows-specific: WSL won't install. Make sure virtualization is enabled in your BIOS (BY-ose). This is a hardware setting that some computers have disabled by default. Search for your computer model plus "enable virtualization" for instructions.

[PAUSE]

[SCREEN: Community support callout]

If you hit something not covered here, post in the community forum with your operating system, the exact error message, and what you've tried. We'll help you through it.

[PAUSE]

---

## CLOSING

[SCREEN: All platforms checkmark graphic]

Whether you're on Windows, Mac, or Linux, you should now have Claude Code installed and authenticated.

[PAUSE]

[SCREEN: Quick verification command]

Run that quick test one more time: claude "Tell me a short joke."

[PAUSE]

If Claude responds with something at least mildly amusing, you're ready for the next lesson.

[PAUSE]

[SCREEN: Next lesson preview]

Coming up: Your First Claude Code Session. We'll explore the interface, learn the essential commands, and start having productive conversations with your new AI development partner.

[PAUSE]

[SCREEN: Fade to "Next: Your First Claude Code Session" with Support Forge branding]

---

**END OF SCRIPT 2.1**

*Approximate word count: 1,750 words*
*Estimated runtime: 14:30-15:30*
