// ===== SUPPORT FORGE - AI & IT CONSULTING =====

// Smooth scrolling
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

// Header scroll effect
const header = document.querySelector('header');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 50) {
        header.style.background = 'rgba(12, 12, 15, 0.98)';
    } else {
        header.style.background = 'rgba(12, 12, 15, 0.9)';
    }

    lastScroll = currentScroll;
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const fadeInObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Apply fade-in animation to elements
document.querySelectorAll('.service-card, .solution-item, .stat-card, .about-content, .contact-info, .contact-form').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    fadeInObserver.observe(el);
});

// Animate stat bars
const statBars = document.querySelectorAll('.stat-fill');
const statObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const width = entry.target.style.width;
            entry.target.style.width = '0';
            setTimeout(() => {
                entry.target.style.width = width;
            }, 100);
            statObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

statBars.forEach(bar => statObserver.observe(bar));

// Chart bar animation
const chartBars = document.querySelectorAll('.chart-bar');
const chartObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            chartBars.forEach((bar, index) => {
                const height = bar.style.height;
                bar.style.height = '0';
                setTimeout(() => {
                    bar.style.transition = 'height 0.6s ease';
                    bar.style.height = height;
                }, index * 100);
            });
            chartObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.3 });

const visualChart = document.querySelector('.visual-chart');
if (visualChart) {
    chartObserver.observe(visualChart);
}

// Contact form handling
const contactForm = document.getElementById('contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(this);
        const name = formData.get('name');
        const email = formData.get('email');

        // Create success modal
        const overlay = document.createElement('div');
        overlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(12, 12, 15, 0.95);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 10000;
            opacity: 0;
            transition: opacity 0.3s ease;
        `;

        const modal = document.createElement('div');
        modal.style.cssText = `
            background: #141419;
            border: 1px solid #2a2a35;
            border-radius: 12px;
            padding: 40px;
            max-width: 420px;
            text-align: center;
            transform: scale(0.9);
            transition: transform 0.3s ease;
        `;

        modal.innerHTML = `
            <div style="
                width: 56px;
                height: 56px;
                border-radius: 50%;
                background: rgba(220, 38, 38, 0.1);
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 20px;
            ">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2">
                    <polyline points="20 6 9 17 4 12"></polyline>
                </svg>
            </div>
            <h3 style="
                font-family: 'Space Grotesk', sans-serif;
                font-size: 1.25rem;
                font-weight: 600;
                color: #f9fafb;
                margin-bottom: 8px;
            ">Message Sent</h3>
            <p style="color: #9ca3af; font-size: 0.95rem; margin-bottom: 24px; line-height: 1.6;">
                Thank you, ${name}. We've received your inquiry and will respond to ${email} within 24 hours.
            </p>
            <button onclick="this.parentElement.parentElement.remove()" style="
                font-family: 'Inter', sans-serif;
                background: #dc2626;
                border: none;
                color: white;
                padding: 12px 28px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 0.95rem;
                font-weight: 500;
                transition: background 0.2s ease;
            " onmouseover="this.style.background='#ef4444'" onmouseout="this.style.background='#dc2626'">
                Got it
            </button>
        `;

        overlay.appendChild(modal);
        document.body.appendChild(overlay);

        // Trigger animations
        setTimeout(() => {
            overlay.style.opacity = '1';
            modal.style.transform = 'scale(1)';
        }, 10);

        // Close on overlay click
        overlay.addEventListener('click', (e) => {
            if (e.target === overlay) {
                overlay.style.opacity = '0';
                modal.style.transform = 'scale(0.9)';
                setTimeout(() => overlay.remove(), 300);
            }
        });

        this.reset();
    });
}

// Mobile menu toggle
const mobileMenu = document.querySelector('.mobile-menu');
const navLinks = document.querySelector('.nav-links');

if (mobileMenu) {
    mobileMenu.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        mobileMenu.classList.toggle('active');
    });
}

// Active nav link highlighting
const sections = document.querySelectorAll('section[id]');
const navItems = document.querySelectorAll('.nav-links a:not(.nav-cta)');

window.addEventListener('scroll', () => {
    let current = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (pageYOffset >= sectionTop - 150) {
            current = section.getAttribute('id');
        }
    });

    navItems.forEach(link => {
        link.style.color = '';
        if (link.getAttribute('href') === `#${current}`) {
            link.style.color = '#f9fafb';
        }
    });
});

// Service card hover effect enhancement
document.querySelectorAll('.service-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.querySelector('.service-link span')?.style.setProperty('transform', 'translateX(4px)');
    });
    card.addEventListener('mouseleave', function() {
        this.querySelector('.service-link span')?.style.setProperty('transform', 'translateX(0)');
    });
});

// Schedule form handling
const scheduleForm = document.getElementById('schedule-form');
if (scheduleForm) {
    const dateInput = document.getElementById('schedule-date');
    if (dateInput) {
        const today = new Date().toISOString().split('T')[0];
        dateInput.setAttribute('min', today);
    }

    scheduleForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(this);
        const name = formData.get('name');
        const email = formData.get('email');
        const date = formData.get('date');
        const time = formData.get('time');

        const dateObj = new Date(date);
        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        const formattedDate = dateObj.toLocaleDateString('en-US', options);

        const timeDisplay = time.replace('09:', '9:').replace('10:', '10:').replace('11:', '11:')
            .replace('13:', '1:').replace('14:', '2:').replace('15:', '3:').replace('16:', '4:') + ' EST';

        const overlay = document.createElement('div');
        overlay.className = 'modal-overlay';
        overlay.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(12,12,15,0.95);display:flex;justify-content:center;align-items:center;z-index:10000;opacity:0;transition:opacity 0.3s ease;';

        const modal = document.createElement('div');
        modal.style.cssText = 'background:#141419;border:1px solid #2a2a35;border-radius:12px;padding:40px;max-width:480px;text-align:center;transform:scale(0.9);transition:transform 0.3s ease;';

        modal.innerHTML = '<div style="width:64px;height:64px;border-radius:50%;background:rgba(220,38,38,0.1);display:flex;align-items:center;justify-content:center;margin:0 auto 24px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/><path d="M9 16l2 2 4-4"/></svg></div>' +
            '<h3 style="font-family:Space Grotesk,sans-serif;font-size:1.5rem;font-weight:600;color:#f9fafb;margin-bottom:12px;">Consultation Scheduled!</h3>' +
            '<p style="color:#9ca3af;font-size:1rem;margin-bottom:8px;">Thank you, ' + name + '!</p>' +
            '<p style="color:#f9fafb;font-size:1.1rem;font-weight:500;margin-bottom:8px;">' + formattedDate + ' at ' + timeDisplay + '</p>' +
            '<p style="color:#9ca3af;font-size:0.95rem;margin-bottom:28px;">A confirmation email has been sent to <strong style="color:#f9fafb;">' + email + '</strong></p>' +
            '<button onclick="this.parentElement.parentElement.remove()" style="font-family:Inter,sans-serif;background:#dc2626;border:none;color:white;padding:14px 32px;border-radius:8px;cursor:pointer;font-size:1rem;font-weight:500;">Got it</button>';

        overlay.appendChild(modal);
        document.body.appendChild(overlay);

        setTimeout(() => {
            overlay.style.opacity = '1';
            modal.style.transform = 'scale(1)';
        }, 10);

        overlay.addEventListener('click', (e) => {
            if (e.target === overlay) {
                overlay.style.opacity = '0';
                modal.style.transform = 'scale(0.9)';
                setTimeout(() => overlay.remove(), 300);
            }
        });

        this.reset();
    });
}

// Add schedule section to fade-in animations
document.querySelectorAll('.schedule-info, .schedule-form-container').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    fadeInObserver.observe(el);
});
