// ===== SUPPORT FORGE - TRON: ARES THEME =====

// Smooth scrolling for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Header scroll effect
const header = document.querySelector('header');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 100) {
        header.style.background = 'rgba(10, 10, 10, 0.98)';
        header.style.borderBottomColor = 'rgba(255, 0, 64, 0.4)';
    } else {
        header.style.background = 'linear-gradient(180deg, rgba(10, 10, 10, 0.98) 0%, rgba(10, 10, 10, 0.9) 100%)';
        header.style.borderBottomColor = 'rgba(255, 0, 64, 0.2)';
    }

    lastScroll = currentScroll;
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

// Animate elements on scroll
document.querySelectorAll('.service-card, .stat-card, .about-text').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
});

// Add visible class styles dynamically
const style = document.createElement('style');
style.textContent = `
    .service-card.visible,
    .stat-card.visible,
    .about-text.visible {
        opacity: 1 !important;
        transform: translateY(0) !important;
    }
`;
document.head.appendChild(style);

// Animate stat bars on scroll
const statBars = document.querySelectorAll('.stat-fill');
const statObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const width = entry.target.style.width;
            entry.target.style.width = '0';
            setTimeout(() => {
                entry.target.style.transition = 'width 1.5s ease-out';
                entry.target.style.width = width;
            }, 200);
            statObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

statBars.forEach(bar => statObserver.observe(bar));

// Contact form handling
document.getElementById('contact-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    const name = formData.get('name');
    const email = formData.get('email');
    const service = formData.get('service');
    const message = formData.get('message');

    // Create a futuristic alert
    const overlay = document.createElement('div');
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(10, 10, 10, 0.95);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 10000;
        animation: fadeIn 0.3s ease;
    `;

    const modal = document.createElement('div');
    modal.style.cssText = `
        background: #141418;
        border: 1px solid #ff0040;
        padding: 3rem;
        max-width: 500px;
        text-align: center;
        position: relative;
        box-shadow: 0 0 50px rgba(255, 0, 64, 0.3);
    `;

    modal.innerHTML = `
        <div style="
            width: 60px;
            height: 60px;
            border: 2px solid #ff0040;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.5rem;
            animation: pulse 1.5s infinite;
        ">
            <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#ff0040" stroke-width="2">
                <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
        </div>
        <h3 style="
            font-family: 'Orbitron', sans-serif;
            color: #ff0040;
            font-size: 1.2rem;
            letter-spacing: 3px;
            margin-bottom: 1rem;
        ">TRANSMISSION RECEIVED</h3>
        <p style="color: #a0a0a0; margin-bottom: 0.5rem;">Thank you, <span style="color: #fff;">${name}</span></p>
        <p style="color: #606060; font-size: 0.9rem; margin-bottom: 2rem;">
            We will establish contact at<br>
            <span style="color: #8b00ff;">${email}</span>
        </p>
        <button onclick="this.parentElement.parentElement.remove()" style="
            font-family: 'Orbitron', sans-serif;
            background: transparent;
            border: 1px solid #ff0040;
            color: #ff0040;
            padding: 0.75rem 2rem;
            cursor: pointer;
            letter-spacing: 2px;
            font-size: 0.8rem;
            transition: all 0.3s ease;
        " onmouseover="this.style.background='#ff0040';this.style.color='#0a0a0a'" onmouseout="this.style.background='transparent';this.style.color='#ff0040'">
            ACKNOWLEDGE
        </button>
    `;

    // Add pulse animation
    const pulseStyle = document.createElement('style');
    pulseStyle.textContent = `
        @keyframes pulse {
            0%, 100% { box-shadow: 0 0 0 0 rgba(255, 0, 64, 0.4); }
            50% { box-shadow: 0 0 0 15px rgba(255, 0, 64, 0); }
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    `;
    document.head.appendChild(pulseStyle);

    overlay.appendChild(modal);
    document.body.appendChild(overlay);

    // Close on overlay click
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) {
            overlay.remove();
        }
    });

    this.reset();
});

// Add subtle parallax to hero
const hero = document.querySelector('.hero');
const heroVisual = document.querySelector('.hero-visual');

window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    if (heroVisual && scrolled < window.innerHeight) {
        heroVisual.style.transform = `translateY(${scrolled * 0.1}px)`;
    }
});

// Service card hover sound effect (visual feedback)
document.querySelectorAll('.service-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
        card.style.borderColor = 'rgba(255, 0, 64, 0.5)';
    });
    card.addEventListener('mouseleave', () => {
        card.style.borderColor = 'transparent';
    });
});

// Active nav link on scroll
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
    let current = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
            link.style.color = '#ff0040';
        } else {
            link.style.color = '';
        }
    });
});

// Console Easter egg
console.log('%c⚒️ SUPPORT FORGE', 'font-size: 24px; font-weight: bold; color: #ff0040; text-shadow: 0 0 10px #ff0040;');
console.log('%cBuilding solutions. Forging success.', 'font-size: 12px; color: #8b00ff;');
console.log('%c─────────────────────────────────', 'color: #303030;');
