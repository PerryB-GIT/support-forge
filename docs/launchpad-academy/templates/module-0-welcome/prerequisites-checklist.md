# AI Launchpad - Prerequisites Checklist

Complete this checklist before starting the course to ensure you have everything you need for a smooth learning experience.

---

## Required Items

### Computer Requirements
- [ ] Computer running Windows 10/11, macOS 10.15+, or Linux (Ubuntu 20.04+ recommended)
- [ ] At least 8GB RAM (16GB recommended)
- [ ] 20GB free disk space
- [ ] Stable internet connection (10+ Mbps recommended)

### Software Prerequisites
- [ ] Modern web browser (Chrome, Firefox, Edge, or Safari)
- [ ] Terminal/Command Line access
  - Windows: PowerShell or WSL2 (Windows Subsystem for Linux)
  - Mac: Terminal.app
  - Linux: Any terminal emulator
- [ ] Text editor or IDE (VS Code recommended - it's free)
- [ ] Git installed ([Download Git](https://git-scm.com/downloads))
- [ ] Node.js 18+ installed ([Download Node.js](https://nodejs.org/))

### Accounts to Create (Free Tiers Available)
- [ ] GitHub account ([Sign up](https://github.com/signup))
- [ ] Anthropic account for Claude API ([Sign up](https://console.anthropic.com/))
- [ ] Google account (for Google Cloud, Calendar, Drive integrations)
- [ ] AWS account ([Sign up](https://aws.amazon.com/free/))

### Financial Requirements
- [ ] Credit card for cloud service signups (free tiers are available, but card required)
- [ ] Budget for API usage (~$20-50/month estimated during learning)

---

## Recommended (But Not Required)

### Technical Skills
- [ ] Basic command line familiarity (cd, ls, mkdir commands)
- [ ] Basic understanding of file systems and paths
- [ ] Familiarity with JSON format
- [ ] Any programming experience (helpful but not required)

### Additional Software
- [ ] Password manager (1Password, Bitwarden, or similar)
- [ ] Docker Desktop (needed for Module 5 self-hosted options)
- [ ] Postman or similar API testing tool

### Additional Accounts
- [ ] n8n Cloud account ([Sign up](https://n8n.io/))
- [ ] Zapier account ([Sign up](https://zapier.com/))
- [ ] Discord account (for community access)

---

## Pre-Course Setup Tasks

### 1. Verify Terminal Access
Open your terminal and run:
```bash
echo "Terminal is working!"
```
You should see the message displayed.

### 2. Verify Git Installation
```bash
git --version
```
Expected output: `git version 2.x.x`

### 3. Verify Node.js Installation
```bash
node --version
npm --version
```
Expected: Node v18+ and npm v9+

### 4. Create a Test Directory
```bash
mkdir ~/ai-launchpad-workspace
cd ~/ai-launchpad-workspace
```
This will be your working directory for the course.

---

## Troubleshooting Common Issues

### Windows Users
- **WSL not installed?** Run `wsl --install` in PowerShell as Administrator
- **Node.js path issues?** Reinstall using the official installer with "Add to PATH" checked

### Mac Users
- **Permission denied errors?** You may need to use `sudo` or fix permissions
- **Homebrew not installed?** Visit [brew.sh](https://brew.sh/) for installation

### Linux Users
- **Package manager issues?** Update first: `sudo apt update && sudo apt upgrade`
- **Node.js outdated?** Use nvm for version management

---

## Ready to Start?

Once you've completed all **Required Items**, you're ready to begin Module 1!

If you're missing any recommended items, don't worry - we'll cover installations as needed throughout the course.

**Questions?** Post in the Discord community channel for help.

---

*AI Launchpad Academy - Support Forge*
