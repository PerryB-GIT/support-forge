# Claude Code Installation Guide

A complete guide to installing Claude Code on your system.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Windows Installation (with WSL)](#windows-installation-with-wsl)
3. [Mac Installation (Homebrew)](#mac-installation-homebrew)
4. [Linux Installation](#linux-installation)
5. [Verification Steps](#verification-steps)
6. [Common Troubleshooting](#common-troubleshooting)

---

## Prerequisites

Before installing Claude Code, ensure you have:

- **Node.js 18+** installed (check with `node --version`)
- **npm** or **yarn** package manager
- **Git** installed and configured
- An **Anthropic API key** or **Claude Pro/Max subscription**
- A terminal/command line environment

---

## Windows Installation (with WSL)

### Step 1: Install WSL (if not already installed)

Open PowerShell as Administrator and run:

```powershell
wsl --install
```

Restart your computer when prompted.

### Step 2: Set Up Ubuntu in WSL

1. Open the Microsoft Store and install **Ubuntu** (latest LTS version)
2. Launch Ubuntu and complete the initial setup (username/password)
3. Update packages:

```bash
sudo apt update && sudo apt upgrade -y
```

### Step 3: Install Node.js in WSL

```bash
# Install nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# Reload shell configuration
source ~/.bashrc

# Install Node.js LTS
nvm install --lts
nvm use --lts

# Verify installation
node --version
npm --version
```

### Step 4: Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### Step 5: Authenticate

```bash
claude
```

On first run, you'll be prompted to authenticate. Choose one of:
- **Anthropic API Key**: Enter your API key from console.anthropic.com
- **Claude Pro/Max**: Sign in with your Anthropic account

### Windows-Specific Notes

- Use WSL terminal for best experience (Windows Terminal recommended)
- Access Windows files at `/mnt/c/Users/YourUsername/`
- VS Code with WSL extension provides excellent integration
- Run `code .` in WSL to open VS Code in current directory

---

## Mac Installation (Homebrew)

### Step 1: Install Homebrew (if not already installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Step 2: Install Node.js

```bash
# Install Node.js via Homebrew
brew install node

# Or use nvm for version management
brew install nvm
mkdir ~/.nvm
echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.zshrc
echo '[ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \. "/opt/homebrew/opt/nvm/nvm.sh"' >> ~/.zshrc
source ~/.zshrc
nvm install --lts
```

### Step 3: Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### Step 4: Authenticate

```bash
claude
```

Follow the authentication prompts to connect your Anthropic account or API key.

### Mac-Specific Notes

- For M1/M2/M3 Macs, ensure you're using the ARM version of Node.js
- Terminal.app or iTerm2 both work well
- Homebrew installs to `/opt/homebrew/` on Apple Silicon Macs

---

## Linux Installation

### Debian/Ubuntu

```bash
# Update package list
sudo apt update

# Install Node.js (using NodeSource repository for latest version)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Verify installation
node --version
npm --version

# Install Claude Code
npm install -g @anthropic-ai/claude-code
```

### Fedora/RHEL/CentOS

```bash
# Install Node.js
sudo dnf install nodejs npm

# Or use NodeSource for latest version
curl -fsSL https://rpm.nodesource.com/setup_20.x | sudo bash -
sudo dnf install nodejs

# Install Claude Code
npm install -g @anthropic-ai/claude-code
```

### Arch Linux

```bash
# Install Node.js
sudo pacman -S nodejs npm

# Install Claude Code
npm install -g @anthropic-ai/claude-code
```

### Authenticate

```bash
claude
```

---

## Verification Steps

After installation, verify everything is working correctly:

### 1. Check Claude Code Installation

```bash
claude --version
```

Expected output: Version number (e.g., `1.x.x`)

### 2. Check Node.js Version

```bash
node --version
```

Expected output: `v18.x.x` or higher

### 3. Test Claude Code Launch

```bash
claude
```

You should see the Claude Code interface with a prompt to enter your message.

### 4. Test Basic Functionality

In Claude Code, try:

```
/help
```

This should display available commands and confirm the tool is working.

### 5. Check Authentication Status

```bash
claude --status
```

Or within Claude Code:

```
/status
```

---

## Common Troubleshooting

### Issue: "command not found: claude"

**Cause**: npm global bin directory not in PATH

**Solution (Linux/Mac/WSL)**:
```bash
# Find npm global bin directory
npm config get prefix

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$PATH:$(npm config get prefix)/bin"

# Reload shell
source ~/.bashrc  # or source ~/.zshrc
```

**Solution (Windows native)**:
```powershell
# Run as Administrator
npm config set prefix "$env:APPDATA\npm"
# Restart terminal
```

### Issue: "EACCES permission denied"

**Cause**: npm trying to install globally without permissions

**Solution 1 - Use nvm (Recommended)**:
```bash
# Install nvm and reinstall Node.js
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install --lts
npm install -g @anthropic-ai/claude-code
```

**Solution 2 - Fix npm permissions**:
```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
npm install -g @anthropic-ai/claude-code
```

### Issue: Authentication Failed

**Cause**: Invalid API key or expired session

**Solution**:
```bash
# Clear authentication and re-authenticate
claude --logout
claude
```

Or check your API key at: https://console.anthropic.com/

### Issue: WSL Network Issues

**Cause**: WSL networking not configured properly

**Solution**:
```bash
# In PowerShell as Admin
wsl --shutdown
# Wait 10 seconds, then reopen WSL
```

### Issue: "Node.js version too old"

**Cause**: System Node.js is outdated

**Solution**:
```bash
# Use nvm to install latest LTS
nvm install --lts
nvm use --lts
nvm alias default node
```

### Issue: Slow Startup on Windows

**Cause**: Antivirus scanning npm packages

**Solution**:
1. Add exclusion for npm cache: `%APPDATA%\npm-cache`
2. Add exclusion for node_modules in your projects
3. Consider using WSL for better performance

### Issue: "SSL Certificate Error"

**Cause**: Corporate proxy or certificate issues

**Solution**:
```bash
# Temporarily disable strict SSL (not recommended for production)
npm config set strict-ssl false

# Or configure proxy
npm config set proxy http://proxy.company.com:8080
npm config set https-proxy http://proxy.company.com:8080
```

### Issue: Claude Code Crashes Immediately

**Cause**: Corrupted installation or cache

**Solution**:
```bash
# Uninstall
npm uninstall -g @anthropic-ai/claude-code

# Clear npm cache
npm cache clean --force

# Reinstall
npm install -g @anthropic-ai/claude-code
```

---

## Getting Help

If you continue to experience issues:

1. Check the [Claude Code GitHub Issues](https://github.com/anthropics/claude-code/issues)
2. Visit the [Anthropic Discord](https://discord.gg/anthropic)
3. Review the [official documentation](https://docs.anthropic.com/claude-code)
4. Contact Anthropic support at support@anthropic.com

---

## Next Steps

Once installed, proceed to:

1. Create your first `CLAUDE.md` configuration file
2. Learn the slash commands (`/help`, `/clear`, `/compact`)
3. Practice with business prompt templates
4. Connect MCP servers for extended functionality
