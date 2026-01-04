# Email System - Quick Start Guide

## 3-Minute Setup

### Step 1: Install Dependencies (30 seconds)
```bash
cd server
npm install
```

### Step 2: Configure Email (1 minute)

Create `.env` file:
```bash
cp .env.example .env
```

**For Gmail users**, edit `.env`:
```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-16-char-app-password
ADMIN_EMAIL=your-email@gmail.com
FROM_EMAIL=noreply@support-forge.com
```

**Get Gmail App Password:**
1. Go to https://myaccount.google.com/apppasswords
2. Create password for "Mail"
3. Copy the 16-character password
4. Paste into `SMTP_PASS`

### Step 3: Test (30 seconds)
```bash
node test-email.js
```

✅ If successful, check your email inbox!

---

## What You Built

### Email Service (`email.js`)
- ✅ `sendContactNotification()` - Send contact form confirmation
- ✅ `sendScheduleConfirmation()` - Send booking confirmation
- ✅ `sendAdminNotification()` - Alert admin of submissions
- ✅ `sendTestEmail()` - Test configuration

### API Endpoints (`routes/email.js`)
- ✅ `POST /api/email/test` - Send test email
- ✅ `POST /api/email/contact` - Contact notification
- ✅ `POST /api/email/schedule` - Schedule confirmation
- ✅ `GET /api/email/status` - Check email status

### Email Templates (`templates/`)
- ✅ `contact-notification.html` - Professional contact form email
- ✅ `schedule-confirmation.html` - Booking confirmation email
- ✅ `admin-notification.html` - Admin alert email

All templates use the Support Forge copper/dark theme!

---

## Next: Integrate with Forms

Add to your existing routes in `index.js`:

```javascript
import emailService from './email.js';

// After successful contact form submission:
await emailService.sendContactNotification(formData);
await emailService.sendAdminNotification('contact', formData);

// After successful schedule submission:
await emailService.sendScheduleConfirmation(bookingData);
await emailService.sendAdminNotification('booking', bookingData);
```

See `EMAIL_SETUP.md` for complete integration examples.

---

## Troubleshooting

**Gmail authentication failed?**
- Use App Password, not your regular password
- Enable 2-Factor Authentication first
- Visit: https://myaccount.google.com/apppasswords

**Can't connect to SMTP server?**
- Check firewall settings
- Verify SMTP_HOST and SMTP_PORT
- Try port 465 for SSL

**Emails not arriving?**
- Check spam/junk folder
- Verify email addresses are correct
- Run `node test-email.js` for diagnostics

---

## Files Created

```
server/
├── email.js                          # Email service
├── routes/email.js                   # API endpoints
├── templates/
│   ├── contact-notification.html
│   ├── schedule-confirmation.html
│   └── admin-notification.html
├── test-email.js                     # Test script
├── EMAIL_SETUP.md                    # Full documentation
├── EMAIL_IMPLEMENTATION_REPORT.md    # Implementation details
└── QUICK_START.md                    # This file
```

---

## Ready to Go!

Your email notification system is ready. Just configure `.env` and test it!

**Need help?** See `EMAIL_SETUP.md` for detailed documentation.
