# AI Launchpad Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add AI Launchpad as a flagship service section on support-forge.com with two tiers (Academy $997, Pro $7,500-15k) and the proprietary LAUNCH Method.

**Architecture:** New dedicated page (`/launchpad` or `launchpad.html`) with sections for hero, tiers, methodology, stack, credentials, and CTAs. Follows existing site patterns (custom CSS variables, section-header structure, 2-column grids). Adds new styles in existing `styles.css`.

**Tech Stack:** HTML5, Custom CSS (existing variables), Vanilla JS, Express server (existing)

---

## Phase 1: Foundation & Navigation

### Task 1.1: Create Launchpad HTML File

**Files:**
- Create: `launchpad.html`

**Step 1: Create base HTML structure**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Launchpad | Support Forge - Your Complete AI Stack Installed</title>
    <meta name="description" content="Stop paying for AI you don't use. AI Launchpad installs your complete AI stack—Claude Code, MCP servers, automations—in days, not months.">

    <!-- Open Graph -->
    <meta property="og:title" content="AI Launchpad | Support Forge">
    <meta property="og:description" content="Your entire AI stack—installed, configured, and working—in days, not months.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://support-forge.com/launchpad">

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

    <!-- Styles -->
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="launchpad.css">

    <!-- Favicons -->
    <link rel="icon" type="image/x-icon" href="favicon.ico">
    <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
</head>
<body>
    <!-- Header (same as index.html) -->
    <header class="header" id="header">
        <div class="container">
            <a href="index.html" class="logo">
                <svg class="logo-icon" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M20 4L4 12V28L20 36L36 28V12L20 4Z" stroke="currentColor" stroke-width="2" fill="none"/>
                    <path d="M20 8L8 14V26L20 32L32 26V14L20 8Z" fill="currentColor" opacity="0.3"/>
                    <path d="M14 18L20 14L26 18V24L20 28L14 24V18Z" fill="currentColor"/>
                </svg>
                <span>Support Forge</span>
            </a>
            <nav class="nav" id="nav">
                <a href="index.html">Home</a>
                <a href="index.html#services">Services</a>
                <a href="#tiers">Pricing</a>
                <a href="#method">Method</a>
                <a href="index.html#contact">Contact</a>
            </nav>
            <button class="mobile-menu-toggle" id="mobileMenuToggle" aria-label="Toggle menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </header>

    <main>
        <!-- Sections will be added in subsequent tasks -->
    </main>

    <!-- Footer (same as index.html) -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand">
                    <a href="index.html" class="logo">
                        <svg class="logo-icon" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M20 4L4 12V28L20 36L36 28V12L20 4Z" stroke="currentColor" stroke-width="2" fill="none"/>
                            <path d="M20 8L8 14V26L20 32L32 26V14L20 8Z" fill="currentColor" opacity="0.3"/>
                            <path d="M14 18L20 14L26 18V24L20 28L14 24V18Z" fill="currentColor"/>
                        </svg>
                        <span>Support Forge</span>
                    </a>
                    <p>AI-powered solutions that actually work.</p>
                </div>
                <div class="footer-links">
                    <div class="footer-column">
                        <h4>Services</h4>
                        <a href="index.html#services">AI Integration</a>
                        <a href="launchpad.html">AI Launchpad</a>
                        <a href="index.html#services">Cloud Solutions</a>
                    </div>
                    <div class="footer-column">
                        <h4>Company</h4>
                        <a href="index.html#about">About</a>
                        <a href="index.html#contact">Contact</a>
                        <a href="index.html#schedule">Schedule</a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Support Forge. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
    <script src="launchpad.js"></script>
</body>
</html>
```

**Step 2: Verify file created**

Run: `ls -la ~/support-forge/launchpad.html`
Expected: File exists with correct size

**Step 3: Commit**

```bash
cd ~/support-forge
git add launchpad.html
git commit -m "feat(launchpad): create base HTML structure"
```

---

### Task 1.2: Create Launchpad CSS File

**Files:**
- Create: `launchpad.css`

**Step 1: Create CSS file with launchpad-specific styles**

```css
/* ===========================================
   AI Launchpad Page Styles
   =========================================== */

/* Hero Section */
.launchpad-hero {
    min-height: 90vh;
    display: flex;
    align-items: center;
    padding: 120px 0 80px;
    background: linear-gradient(135deg, var(--bg-dark) 0%, rgba(201, 124, 75, 0.05) 100%);
    position: relative;
    overflow: hidden;
}

.launchpad-hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 70% 30%, rgba(201, 124, 75, 0.1) 0%, transparent 50%);
    pointer-events: none;
}

.launchpad-hero .container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
}

.launchpad-hero-content {
    position: relative;
    z-index: 1;
}

.launchpad-hero-tag {
    display: inline-block;
    background: rgba(201, 124, 75, 0.15);
    color: var(--accent);
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 0.875rem;
    font-weight: 600;
    margin-bottom: 24px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.launchpad-hero h1 {
    font-family: 'DM Serif Display', serif;
    font-size: 3.5rem;
    line-height: 1.1;
    margin-bottom: 24px;
    color: var(--text-primary);
}

.launchpad-hero h1 .highlight {
    color: var(--accent);
}

.launchpad-hero .lead {
    font-size: 1.25rem;
    color: var(--text-secondary);
    margin-bottom: 32px;
    line-height: 1.7;
}

.launchpad-hero-cta {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
}

.launchpad-hero-visual {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Tiers Section */
.launchpad-tiers {
    padding: 100px 0;
    background: var(--forge-navy);
}

.tiers-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 32px;
    margin-top: 60px;
}

.tier-card {
    background: var(--bg-card);
    border: 1px solid rgba(201, 124, 75, 0.2);
    border-radius: 16px;
    padding: 40px;
    position: relative;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.tier-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}

.tier-card.featured {
    border-color: var(--accent);
    background: linear-gradient(135deg, var(--bg-card) 0%, rgba(201, 124, 75, 0.08) 100%);
}

.tier-card.featured::before {
    content: 'MOST POPULAR';
    position: absolute;
    top: -12px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--accent);
    color: var(--bg-dark);
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 1px;
}

.tier-name {
    font-family: 'DM Serif Display', serif;
    font-size: 1.75rem;
    color: var(--text-primary);
    margin-bottom: 8px;
}

.tier-tagline {
    color: var(--text-secondary);
    font-size: 1rem;
    margin-bottom: 24px;
}

.tier-price {
    margin-bottom: 24px;
}

.tier-price .amount {
    font-family: 'DM Serif Display', serif;
    font-size: 3rem;
    color: var(--accent);
}

.tier-price .period {
    color: var(--text-secondary);
    font-size: 1rem;
}

.tier-price .alt-price {
    color: var(--text-muted);
    font-size: 0.875rem;
    margin-top: 4px;
}

.tier-features {
    list-style: none;
    padding: 0;
    margin: 0 0 32px 0;
}

.tier-features li {
    padding: 12px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    color: var(--text-secondary);
    display: flex;
    align-items: flex-start;
    gap: 12px;
}

.tier-features li::before {
    content: '✓';
    color: var(--accent);
    font-weight: 700;
    flex-shrink: 0;
}

.tier-features li:last-child {
    border-bottom: none;
}

.tier-cta {
    width: 100%;
}

/* LAUNCH Method Section */
.launchpad-method {
    padding: 100px 0;
    background: var(--bg-dark);
}

.method-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    margin-top: 60px;
}

.method-card {
    background: var(--bg-card);
    border: 1px solid rgba(201, 124, 75, 0.15);
    border-radius: 12px;
    padding: 32px;
    text-align: center;
    transition: transform 0.3s ease, border-color 0.3s ease;
}

.method-card:hover {
    transform: translateY(-4px);
    border-color: var(--accent);
}

.method-letter {
    font-family: 'DM Serif Display', serif;
    font-size: 3rem;
    color: var(--accent);
    margin-bottom: 8px;
}

.method-name {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 12px;
}

.method-desc {
    color: var(--text-secondary);
    font-size: 0.9rem;
    line-height: 1.6;
}

/* Stack Section */
.launchpad-stack {
    padding: 100px 0;
    background: var(--forge-navy);
}

.stack-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    margin-top: 60px;
}

.stack-item {
    background: var(--bg-card);
    border: 1px solid rgba(201, 124, 75, 0.1);
    border-radius: 12px;
    padding: 24px;
    text-align: center;
    transition: transform 0.3s ease, border-color 0.3s ease;
}

.stack-item:hover {
    transform: translateY(-2px);
    border-color: var(--accent);
}

.stack-icon {
    font-size: 2rem;
    margin-bottom: 12px;
}

.stack-name {
    font-weight: 600;
    color: var(--text-primary);
    font-size: 0.9rem;
}

.stack-category {
    color: var(--text-muted);
    font-size: 0.75rem;
    margin-top: 4px;
}

/* ROI Section */
.launchpad-roi {
    padding: 100px 0;
    background: var(--bg-dark);
}

.roi-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
    margin-top: 60px;
}

.roi-card {
    background: var(--bg-card);
    border: 1px solid rgba(201, 124, 75, 0.15);
    border-radius: 12px;
    padding: 32px;
    text-align: center;
}

.roi-number {
    font-family: 'DM Serif Display', serif;
    font-size: 3rem;
    color: var(--accent);
    margin-bottom: 8px;
}

.roi-label {
    color: var(--text-secondary);
    font-size: 1rem;
}

/* Credentials Section */
.launchpad-credentials {
    padding: 100px 0;
    background: var(--forge-navy);
}

.credentials-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 40px;
    margin-top: 60px;
}

.credential-group h3 {
    font-family: 'DM Serif Display', serif;
    font-size: 1.5rem;
    color: var(--text-primary);
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 12px;
}

.credential-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.credential-list li {
    padding: 12px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    color: var(--text-secondary);
    display: flex;
    align-items: center;
    gap: 12px;
}

.credential-list li::before {
    content: '🏅';
}

/* CTA Section */
.launchpad-cta {
    padding: 100px 0;
    background: linear-gradient(135deg, var(--bg-dark) 0%, rgba(201, 124, 75, 0.15) 100%);
    text-align: center;
}

.launchpad-cta h2 {
    font-family: 'DM Serif Display', serif;
    font-size: 2.5rem;
    color: var(--text-primary);
    margin-bottom: 16px;
}

.launchpad-cta p {
    color: var(--text-secondary);
    font-size: 1.25rem;
    margin-bottom: 32px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

.launchpad-cta .cta-buttons {
    display: flex;
    gap: 16px;
    justify-content: center;
    flex-wrap: wrap;
}

/* Responsive */
@media (max-width: 1024px) {
    .launchpad-hero .container {
        grid-template-columns: 1fr;
        text-align: center;
    }

    .launchpad-hero-cta {
        justify-content: center;
    }

    .launchpad-hero-visual {
        display: none;
    }

    .tiers-grid {
        grid-template-columns: 1fr;
        max-width: 500px;
        margin-left: auto;
        margin-right: auto;
    }

    .method-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .stack-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .credentials-grid {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 768px) {
    .launchpad-hero h1 {
        font-size: 2.5rem;
    }

    .method-grid {
        grid-template-columns: 1fr;
    }

    .roi-grid {
        grid-template-columns: 1fr;
    }

    .stack-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 480px) {
    .launchpad-hero h1 {
        font-size: 2rem;
    }

    .tier-card {
        padding: 24px;
    }

    .tier-price .amount {
        font-size: 2.5rem;
    }
}
```

**Step 2: Verify file created**

Run: `ls -la ~/support-forge/launchpad.css`
Expected: File exists

**Step 3: Commit**

```bash
cd ~/support-forge
git add launchpad.css
git commit -m "feat(launchpad): add launchpad-specific CSS styles"
```

---

### Task 1.3: Create Launchpad JavaScript File

**Files:**
- Create: `launchpad.js`

**Step 1: Create JS file with launchpad-specific functionality**

```javascript
/* ===========================================
   AI Launchpad Page Scripts
   =========================================== */

document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe elements for animation
    const animateElements = document.querySelectorAll(
        '.tier-card, .method-card, .stack-item, .roi-card, .credential-group'
    );

    animateElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = `opacity 0.5s ease ${index * 0.05}s, transform 0.5s ease ${index * 0.05}s`;
        observer.observe(el);
    });

    // Add visible class styles
    const style = document.createElement('style');
    style.textContent = `
        .tier-card.visible,
        .method-card.visible,
        .stack-item.visible,
        .roi-card.visible,
        .credential-group.visible {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    `;
    document.head.appendChild(style);

    // Track CTA clicks (for analytics)
    document.querySelectorAll('.tier-cta, .launchpad-cta .btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const tierName = this.closest('.tier-card')?.querySelector('.tier-name')?.textContent || 'CTA';
            console.log('Launchpad CTA clicked:', tierName);
            // Add analytics tracking here if needed
        });
    });
});
```

**Step 2: Verify file created**

Run: `ls -la ~/support-forge/launchpad.js`
Expected: File exists

**Step 3: Commit**

```bash
cd ~/support-forge
git add launchpad.js
git commit -m "feat(launchpad): add launchpad JavaScript functionality"
```

---

### Task 1.4: Update Main Navigation

**Files:**
- Modify: `index.html` (nav section, approximately lines 20-30)

**Step 1: Add Launchpad link to navigation**

Find the nav element and add AI Launchpad link:

```html
<nav class="nav" id="nav">
    <a href="#services">Services</a>
    <a href="launchpad.html" class="nav-highlight">AI Launchpad</a>
    <a href="#about">About</a>
    <a href="#schedule">Schedule</a>
    <a href="#contact">Contact</a>
</nav>
```

**Step 2: Add CSS for nav-highlight (in styles.css)**

Add after existing nav styles:

```css
.nav-highlight {
    color: var(--accent) !important;
    font-weight: 600;
}
```

**Step 3: Test navigation**

Run: `curl -s http://localhost:3000 | grep -o 'launchpad.html'`
Expected: `launchpad.html`

**Step 4: Commit**

```bash
cd ~/support-forge
git add index.html styles.css
git commit -m "feat(nav): add AI Launchpad link to main navigation"
```

---

## Phase 2: Hero Section

### Task 2.1: Build Hero Section Content

**Files:**
- Modify: `launchpad.html` (inside `<main>` tag)

**Step 1: Add hero section HTML**

```html
<!-- Hero Section -->
<section class="launchpad-hero" id="hero">
    <div class="container">
        <div class="launchpad-hero-content">
            <span class="launchpad-hero-tag">AI Launchpad</span>
            <h1>Stop Paying for AI <span class="highlight">You Don't Use</span></h1>
            <p class="lead">
                Most businesses collect AI subscriptions like unused gym memberships.
                We install a complete, connected AI system that actually runs your operations.
            </p>
            <p class="lead">
                <strong>Your entire AI stack—installed, configured, and working—in days, not months.</strong>
            </p>
            <div class="launchpad-hero-cta">
                <a href="#tiers" class="btn btn-primary btn-large">See Pricing</a>
                <a href="#method" class="btn btn-secondary btn-large">How It Works</a>
            </div>
        </div>
        <div class="launchpad-hero-visual">
            <!-- Rocket/Launch SVG illustration -->
            <svg viewBox="0 0 400 400" width="400" height="400" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="200" cy="200" r="150" stroke="currentColor" stroke-width="2" opacity="0.1"/>
                <circle cx="200" cy="200" r="100" stroke="currentColor" stroke-width="2" opacity="0.2"/>
                <circle cx="200" cy="200" r="50" stroke="currentColor" stroke-width="2" opacity="0.3"/>
                <!-- Rocket body -->
                <path d="M200 80 L230 180 L230 280 L200 320 L170 280 L170 180 Z" fill="var(--accent)" opacity="0.9"/>
                <!-- Rocket fins -->
                <path d="M170 250 L140 300 L170 280 Z" fill="var(--accent)" opacity="0.7"/>
                <path d="M230 250 L260 300 L230 280 Z" fill="var(--accent)" opacity="0.7"/>
                <!-- Rocket window -->
                <circle cx="200" cy="160" r="20" fill="var(--bg-dark)" stroke="var(--accent)" stroke-width="3"/>
                <!-- Flame -->
                <path d="M185 320 L200 380 L215 320" fill="#ff6b35" opacity="0.8">
                    <animate attributeName="d"
                        values="M185 320 L200 380 L215 320;M185 320 L200 360 L215 320;M185 320 L200 380 L215 320"
                        dur="0.5s"
                        repeatCount="indefinite"/>
                </path>
            </svg>
        </div>
    </div>
</section>
```

**Step 2: Verify hero displays**

Run: Open `http://localhost:3000/launchpad.html` in browser
Expected: Hero section visible with headline, copy, and rocket visual

**Step 3: Commit**

```bash
cd ~/support-forge
git add launchpad.html
git commit -m "feat(launchpad): add hero section with messaging"
```

---

## Phase 3: Pricing Tiers Section

### Task 3.1: Build Tiers Section

**Files:**
- Modify: `launchpad.html` (after hero section)

**Step 1: Add tiers section HTML**

```html
<!-- Pricing Tiers Section -->
<section class="launchpad-tiers" id="tiers">
    <div class="container">
        <div class="section-header">
            <span class="section-tag">Pricing</span>
            <h2>Two Ways to Launch</h2>
            <p class="section-description">
                Learn to build it yourself, or let us build it for you. Both include our proven LAUNCH Method.
            </p>
        </div>

        <div class="tiers-grid">
            <!-- Academy Tier -->
            <div class="tier-card">
                <h3 class="tier-name">Launchpad Academy</h3>
                <p class="tier-tagline">Learn to build your own AI-powered operations</p>
                <div class="tier-price">
                    <span class="amount">$997</span>
                    <span class="period">one-time</span>
                    <p class="alt-price">or $127/mo for 12 months</p>
                </div>
                <ul class="tier-features">
                    <li>Complete video course library</li>
                    <li>Step-by-step LAUNCH Method playbooks</li>
                    <li>Pre-configured templates & config files</li>
                    <li>Private community access</li>
                    <li>Monthly group Q&A calls</li>
                    <li>Certificate of completion</li>
                    <li>Responsible AI certification</li>
                    <li>Lifetime updates</li>
                </ul>
                <a href="#schedule" class="btn btn-secondary btn-full tier-cta">Enroll Now</a>
            </div>

            <!-- Pro Tier -->
            <div class="tier-card featured">
                <h3 class="tier-name">Launchpad Pro</h3>
                <p class="tier-tagline">We build your AI command center while you run your business</p>
                <div class="tier-price">
                    <span class="amount">$7,500</span>
                    <span class="period">starting at</span>
                    <p class="alt-price">Custom quote based on complexity</p>
                </div>
                <ul class="tier-features">
                    <li>Full LAUNCH Method execution</li>
                    <li>Complete stack installation & configuration</li>
                    <li>3-5 custom automation workflows</li>
                    <li>Industry-specific skills installed</li>
                    <li>Security audit & hardening</li>
                    <li>Team training session (2-3 hours)</li>
                    <li>30-day post-launch support</li>
                    <li>Full Academy access included</li>
                </ul>
                <a href="#schedule" class="btn btn-primary btn-full tier-cta">Book Consultation</a>
            </div>
        </div>
    </div>
</section>
```

**Step 2: Verify tiers display**

Run: Refresh browser, scroll to tiers section
Expected: Two tier cards with pricing, features, and CTAs

**Step 3: Commit**

```bash
cd ~/support-forge
git add launchpad.html
git commit -m "feat(launchpad): add pricing tiers section"
```

---

## Phase 4: LAUNCH Method Section

### Task 4.1: Build Method Section

**Files:**
- Modify: `launchpad.html` (after tiers section)

**Step 1: Add LAUNCH method section HTML**

```html
<!-- LAUNCH Method Section -->
<section class="launchpad-method" id="method">
    <div class="container">
        <div class="section-header">
            <span class="section-tag">Our Process</span>
            <h2>The LAUNCH Method</h2>
            <p class="section-description">
                Our proprietary 6-phase methodology ensures your AI implementation succeeds.
                No guesswork. No wasted time. Just results.
            </p>
        </div>

        <div class="method-grid">
            <div class="method-card">
                <div class="method-letter">L</div>
                <h4 class="method-name">Landscape</h4>
                <p class="method-desc">Audit your current tools, workflows, and pain points. Know where you stand before you leap.</p>
            </div>

            <div class="method-card">
                <div class="method-letter">A</div>
                <h4 class="method-name">Architect</h4>
                <p class="method-desc">Design your AI stack blueprint. Select the right tools for your specific needs and budget.</p>
            </div>

            <div class="method-card">
                <div class="method-letter">U</div>
                <h4 class="method-name">Unlock</h4>
                <p class="method-desc">Set up all accounts, API keys, and permissions. Remove every blocker before the build.</p>
            </div>

            <div class="method-card">
                <div class="method-letter">N</div>
                <h4 class="method-name">Network</h4>
                <p class="method-desc">Connect everything into one system. Claude Code, MCP servers, automations—all talking to each other.</p>
            </div>

            <div class="method-card">
                <div class="method-letter">C</div>
                <h4 class="method-name">Configure</h4>
                <p class="method-desc">Customize for your business. Install skills, build automations, tailor to your industry.</p>
            </div>

            <div class="method-card">
                <div class="method-letter">H</div>
                <h4 class="method-name">Harden</h4>
                <p class="method-desc">Secure it, document it, own it. Security audit, responsible AI training, and full handoff.</p>
            </div>
        </div>
    </div>
</section>
```

**Step 2: Verify method section displays**

Run: Refresh browser, scroll to method section
Expected: 6 cards spelling LAUNCH with descriptions

**Step 3: Commit**

```bash
cd ~/support-forge
git add launchpad.html
git commit -m "feat(launchpad): add LAUNCH Method section"
```

---

## Phase 5: Stack & Credentials Sections

### Task 5.1: Build Stack Section

**Files:**
- Modify: `launchpad.html` (after method section)

**Step 1: Add stack section HTML**

```html
<!-- Stack Section -->
<section class="launchpad-stack" id="stack">
    <div class="container">
        <div class="section-header">
            <span class="section-tag">The Launchpad Stack</span>
            <h2>Everything You Need, Connected</h2>
            <p class="section-description">
                A complete ecosystem of AI tools, automations, and integrations—configured to work together.
            </p>
        </div>

        <div class="stack-grid">
            <div class="stack-item">
                <div class="stack-icon">🤖</div>
                <div class="stack-name">Claude Code</div>
                <div class="stack-category">AI Core</div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">🔌</div>
                <div class="stack-name">MCP Servers</div>
                <div class="stack-category">Connectors</div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">✨</div>
                <div class="stack-name">Gemini</div>
                <div class="stack-category">Google AI</div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">🧠</div>
                <div class="stack-name">Vertex AI</div>
                <div class="stack-category">Google AI</div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">📊</div>
                <div class="stack-name">BigQuery</div>
                <div class="stack-category">Analytics</div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">⚡</div>
                <div class="stack-name">n8n</div>
                <div class="stack-category">Automation</div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">🔗</div>
                <div class="stack-name">Zapier</div>
                <div class="stack-category">Automation</div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">☁️</div>
                <div class="stack-name">AWS</div>
                <div class="stack-category">Cloud</div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">🌐</div>
                <div class="stack-name">Google Cloud</div>
                <div class="stack-category">Cloud</div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">🐙</div>
                <div class="stack-name">GitHub</div>
                <div class="stack-category">Dev Tools</div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">🐳</div>
                <div class="stack-name">Docker</div>
                <div class="stack-category">Dev Tools</div>
            </div>
            <div class="stack-item">
                <div class="stack-icon">📧</div>
                <div class="stack-name">Google Workspace</div>
                <div class="stack-category">Productivity</div>
            </div>
        </div>
    </div>
</section>
```

**Step 2: Commit**

```bash
cd ~/support-forge
git add launchpad.html
git commit -m "feat(launchpad): add stack section with tools"
```

---

### Task 5.2: Build ROI Section

**Files:**
- Modify: `launchpad.html` (after stack section)

**Step 1: Add ROI section HTML**

```html
<!-- ROI Section -->
<section class="launchpad-roi" id="roi">
    <div class="container">
        <div class="section-header">
            <span class="section-tag">The Business Case</span>
            <h2>ROI That Justifies Itself</h2>
            <p class="section-description">
                The average SMB wastes $15,000-30,000 annually on unused AI tools and manual tasks that should be automated.
            </p>
        </div>

        <div class="roi-grid">
            <div class="roi-card">
                <div class="roi-number">500%+</div>
                <div class="roi-label">First-Year ROI (Academy)</div>
            </div>
            <div class="roi-card">
                <div class="roi-number">2-4 mo</div>
                <div class="roi-label">Payback Period (Pro)</div>
            </div>
            <div class="roi-card">
                <div class="roi-number">40-80 hrs</div>
                <div class="roi-label">Monthly Time Saved</div>
            </div>
        </div>
    </div>
</section>
```

**Step 2: Commit**

```bash
cd ~/support-forge
git add launchpad.html
git commit -m "feat(launchpad): add ROI section"
```

---

### Task 5.3: Build Credentials Section

**Files:**
- Modify: `launchpad.html` (after ROI section)

**Step 1: Add credentials section HTML**

```html
<!-- Credentials Section -->
<section class="launchpad-credentials" id="credentials">
    <div class="container">
        <div class="section-header">
            <span class="section-tag">Expertise</span>
            <h2>Certified, Not Just Self-Taught</h2>
            <p class="section-description">
                Our team holds official certifications from Google AI and Google Cloud.
            </p>
        </div>

        <div class="credentials-grid">
            <div class="credential-group">
                <h3>🎓 Google AI Certifications</h3>
                <ul class="credential-list">
                    <li>Google AI Essentials</li>
                    <li>Design Prompts for Everyday Work Tasks</li>
                    <li>Discover the Art of Prompting</li>
                    <li>Maximize Productivity With AI Tools</li>
                    <li>Start Writing Prompts like a Pro</li>
                    <li>Use AI Responsibly</li>
                    <li>Use AI as a Creative or Expert Partner</li>
                    <li>Speed Up Data Analysis and Presentation Building</li>
                </ul>
            </div>

            <div class="credential-group">
                <h3>☁️ Google Cloud Certifications</h3>
                <ul class="credential-list">
                    <li>Introduction to Large Language Models</li>
                    <li>Introduction to Responsible AI</li>
                </ul>

                <h3 style="margin-top: 32px;">🏆 Company Track Record</h3>
                <ul class="credential-list">
                    <li>10+ Years Experience (Est. 2005)</li>
                    <li>150+ Projects Delivered</li>
                    <li>98% Client Satisfaction</li>
                </ul>
            </div>
        </div>
    </div>
</section>
```

**Step 2: Commit**

```bash
cd ~/support-forge
git add launchpad.html
git commit -m "feat(launchpad): add credentials section"
```

---

## Phase 6: CTA & Final Polish

### Task 6.1: Build Final CTA Section

**Files:**
- Modify: `launchpad.html` (after credentials section, before footer)

**Step 1: Add CTA section HTML**

```html
<!-- Final CTA Section -->
<section class="launchpad-cta" id="schedule">
    <div class="container">
        <h2>Ready to Launch?</h2>
        <p>
            Stop collecting AI subscriptions. Start running AI operations.
        </p>
        <div class="cta-buttons">
            <a href="mailto:hello@support-forge.com?subject=Launchpad%20Academy%20Inquiry" class="btn btn-primary btn-large">
                Enroll in Academy ($997)
            </a>
            <a href="https://calendly.com/support-forge/consultation" class="btn btn-secondary btn-large" target="_blank">
                Book Pro Consultation
            </a>
        </div>
    </div>
</section>
```

**Step 2: Commit**

```bash
cd ~/support-forge
git add launchpad.html
git commit -m "feat(launchpad): add final CTA section"
```

---

### Task 6.2: Add Structured Data for SEO

**Files:**
- Modify: `launchpad.html` (in `<head>` section)

**Step 1: Add JSON-LD structured data**

```html
<!-- Structured Data -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "AI Launchpad",
    "description": "Complete AI stack installation and configuration service. Get Claude Code, MCP servers, and automations working in days.",
    "brand": {
        "@type": "Organization",
        "name": "Support Forge"
    },
    "offers": [
        {
            "@type": "Offer",
            "name": "Launchpad Academy",
            "price": "997",
            "priceCurrency": "USD",
            "description": "Self-service course to learn AI implementation"
        },
        {
            "@type": "Offer",
            "name": "Launchpad Pro",
            "priceRange": "$7,500 - $15,000",
            "priceCurrency": "USD",
            "description": "Done-for-you AI stack implementation"
        }
    ]
}
</script>
```

**Step 2: Commit**

```bash
cd ~/support-forge
git add launchpad.html
git commit -m "feat(launchpad): add structured data for SEO"
```

---

### Task 6.3: Update Server Routes

**Files:**
- Modify: `server/server.js`

**Step 1: Ensure launchpad.html is served correctly**

The existing Express setup with static file serving should work automatically. Verify by testing:

Run: `curl -I http://localhost:3000/launchpad.html`
Expected: `HTTP/1.1 200 OK`

**Step 2: Commit if changes needed**

```bash
cd ~/support-forge
git add server/server.js
git commit -m "chore(server): ensure launchpad route works"
```

---

### Task 6.4: Final Testing & Deployment

**Step 1: Local testing checklist**

Run through manually:
- [ ] Hero section displays correctly
- [ ] Tiers section shows both cards
- [ ] LAUNCH method shows 6 cards
- [ ] Stack section shows all tools
- [ ] ROI numbers display
- [ ] Credentials list displays
- [ ] CTA buttons work
- [ ] Mobile responsive (test at 768px, 480px)
- [ ] Animations trigger on scroll

**Step 2: Deploy to production**

```bash
cd ~/support-forge
ssh -i ~/.ssh/support-forge-key.pem ubuntu@35.172.150.179 "cd /var/www/support-forge && git pull && docker-compose build --no-cache web && docker-compose up -d"
```

**Step 3: Verify production**

Run: `curl -I https://support-forge.com/launchpad.html`
Expected: `HTTP/1.1 200 OK`

**Step 4: Final commit**

```bash
cd ~/support-forge
git add .
git commit -m "feat(launchpad): complete AI Launchpad page implementation"
git push origin main
```

---

## Phase 7: Post-Launch (Future Tasks)

These tasks are documented for future implementation:

### Task 7.1: Course Platform Setup
- Choose platform (Teachable, Kajabi, or self-hosted)
- Create course structure matching Academy modules
- Set up payment processing
- Integrate with website

### Task 7.2: Academy Content Creation
- Record video walkthroughs for each LAUNCH phase
- Create downloadable templates
- Build community platform (Discord/Slack)
- Create certification quiz

### Task 7.3: Pro Delivery Process
- Create intake form
- Build proposal templates
- Set up project tracking
- Create handoff documentation

### Task 7.4: Analytics & Tracking
- Add conversion tracking to CTAs
- Set up Google Analytics events
- Create dashboard for lead tracking

---

## Summary

| Phase | Tasks | Est. Time |
|-------|-------|-----------|
| 1. Foundation | 4 tasks | Core files, navigation |
| 2. Hero | 1 task | Hero section |
| 3. Tiers | 1 task | Pricing cards |
| 4. Method | 1 task | LAUNCH methodology |
| 5. Stack/Credentials | 3 tasks | Tools, ROI, certs |
| 6. CTA/Polish | 4 tasks | CTA, SEO, deploy |
| 7. Post-Launch | 4 tasks | Future content |

**Total: 18 implementation tasks**

---

*Plan created: January 4, 2026*
