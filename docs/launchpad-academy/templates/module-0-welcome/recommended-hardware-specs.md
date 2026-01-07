# AI Launchpad - Recommended Hardware & Software Specifications

This guide outlines the hardware and software requirements for the AI Launchpad Academy course, from minimum specs to optimal setups.

---

## Hardware Requirements

### Minimum Requirements
| Component | Specification |
|-----------|---------------|
| **Processor** | Intel i5 (8th gen+) / AMD Ryzen 5 / Apple M1 |
| **RAM** | 8GB |
| **Storage** | 20GB free space (SSD recommended) |
| **Display** | 1920x1080 resolution |
| **Internet** | 10 Mbps download / 5 Mbps upload |

### Recommended Specifications
| Component | Specification |
|-----------|---------------|
| **Processor** | Intel i7 (10th gen+) / AMD Ryzen 7 / Apple M1 Pro+ |
| **RAM** | 16GB or more |
| **Storage** | 50GB+ free on SSD |
| **Display** | 1920x1080 or higher (dual monitors ideal) |
| **Internet** | 50+ Mbps download |

### Optimal Setup (Power Users)
| Component | Specification |
|-----------|---------------|
| **Processor** | Intel i9 / AMD Ryzen 9 / Apple M2 Pro/Max |
| **RAM** | 32GB+ |
| **Storage** | 100GB+ free on NVMe SSD |
| **Display** | 4K or ultrawide (dual monitors) |
| **Internet** | 100+ Mbps download |

---

## Operating System Support

### Windows
- **Minimum:** Windows 10 (version 1903+)
- **Recommended:** Windows 11
- **Note:** WSL2 (Windows Subsystem for Linux) required for optimal experience

### macOS
- **Minimum:** macOS 10.15 (Catalina)
- **Recommended:** macOS 12 (Monterey) or newer
- **Note:** Apple Silicon (M1/M2/M3) chips work great

### Linux
- **Minimum:** Ubuntu 20.04 LTS or equivalent
- **Recommended:** Ubuntu 22.04 LTS or newer
- **Also Supported:** Debian 11+, Fedora 36+, other major distributions

---

## Software Requirements

### Essential Software
| Software | Version | Purpose | Download |
|----------|---------|---------|----------|
| **Git** | 2.30+ | Version control | [git-scm.com](https://git-scm.com/) |
| **Node.js** | 18 LTS+ | Runtime for tools | [nodejs.org](https://nodejs.org/) |
| **VS Code** | Latest | Code editor | [code.visualstudio.com](https://code.visualstudio.com/) |
| **Browser** | Chrome/Firefox/Edge | Web access | - |

### Recommended Software
| Software | Purpose | Download |
|----------|---------|----------|
| **Docker Desktop** | Container management | [docker.com](https://www.docker.com/products/docker-desktop/) |
| **Postman** | API testing | [postman.com](https://www.postman.com/downloads/) |
| **1Password/Bitwarden** | Credential management | [1password.com](https://1password.com/) / [bitwarden.com](https://bitwarden.com/) |

### VS Code Extensions (Recommended)
```
- GitHub Copilot (optional, paid)
- ESLint
- Prettier
- Thunder Client (API testing)
- Docker
- GitLens
```

---

## Cloud Service Accounts

### Required (Free Tiers)
| Service | Free Tier Includes | Sign Up |
|---------|-------------------|---------|
| **GitHub** | Unlimited public repos | [github.com/signup](https://github.com/signup) |
| **Anthropic (Claude)** | $5 free credits | [console.anthropic.com](https://console.anthropic.com/) |
| **AWS** | 12 months free tier | [aws.amazon.com/free](https://aws.amazon.com/free/) |
| **Google Cloud** | $300 free credits | [cloud.google.com/free](https://cloud.google.com/free) |

### Recommended
| Service | Free Tier | Sign Up |
|---------|-----------|---------|
| **n8n Cloud** | 5 workflows free | [n8n.io](https://n8n.io/) |
| **Zapier** | 100 tasks/month | [zapier.com](https://zapier.com/) |

---

## Estimated Monthly Costs

### During the Course
| Service | Estimated Cost |
|---------|----------------|
| Claude API | $10-20/month |
| AWS (within free tier) | $0-5/month |
| Google Cloud (within free tier) | $0/month |
| n8n Cloud (free tier) | $0/month |
| **Total** | **~$15-30/month** |

### After Course (Production Use)
| Service | Estimated Cost |
|---------|----------------|
| Claude API | $20-100/month |
| AWS services | $10-50/month |
| n8n/Zapier | $0-30/month |
| **Total** | **~$30-180/month** |

*Costs vary significantly based on usage. Start with free tiers and scale as needed.*

---

## Network Requirements

### Ports That Should Be Open
- **443** (HTTPS) - Required for all web services
- **22** (SSH) - Git operations
- **3000-3999** - Local development servers
- **8080-8090** - Alternative local ports

### VPN/Firewall Considerations
- Some corporate networks block API calls
- If using VPN, ensure it doesn't interfere with cloud services
- Consider a dedicated network for development if issues arise

---

## Performance Tips

### Speed Up Your Setup
1. **Use an SSD** - Dramatically improves tool installation and file operations
2. **Close unnecessary apps** - Free up RAM for Docker and AI tools
3. **Use wired internet** - More stable for API calls and uploads
4. **Dual monitors** - Reference materials while coding

### Reduce API Costs
1. **Use caching** - Store API responses when possible
2. **Batch requests** - Combine multiple operations
3. **Monitor usage** - Set up billing alerts early
4. **Use appropriate models** - Haiku for simple tasks, Sonnet/Opus for complex

---

## Quick Environment Test

Run this script to verify your setup:

```bash
#!/bin/bash
echo "=== AI Launchpad Environment Check ==="
echo ""

echo "Operating System:"
uname -a
echo ""

echo "Git Version:"
git --version 2>/dev/null || echo "Git NOT INSTALLED"
echo ""

echo "Node.js Version:"
node --version 2>/dev/null || echo "Node.js NOT INSTALLED"
echo ""

echo "npm Version:"
npm --version 2>/dev/null || echo "npm NOT INSTALLED"
echo ""

echo "Docker Version:"
docker --version 2>/dev/null || echo "Docker not installed (optional)"
echo ""

echo "=== Check Complete ==="
```

Save as `check-environment.sh` and run with `bash check-environment.sh`

---

## Need Help?

- **Course Discord** - Post in #tech-support channel
- **Office Hours** - Weekly live Q&A sessions
- **Email** - support@support-forge.com

---

*AI Launchpad Academy - Support Forge*
