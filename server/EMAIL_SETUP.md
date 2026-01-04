# Email Notification System - Setup Guide

## Overview

The Support Forge email notification system provides automated email notifications for contact form submissions and consultation bookings. Built with Nodemailer, it supports professional HTML email templates with the copper/dark theme.

## Features

- **Contact Form Notifications**: Sends confirmation emails to users and notifications to admins
- **Schedule Confirmations**: Sends booking confirmations with appointment details
- **Professional Templates**: HTML email templates matching the Support Forge brand
- **Error Handling**: Comprehensive error handling and logging
- **Test Endpoints**: Built-in testing functionality

## File Structure

```
server/
├── email.js                          # Email service module
├── routes/
│   └── email.js                      # Email API routes
├── templates/
│   ├── contact-notification.html     # Contact form email template
│   ├── schedule-confirmation.html    # Booking confirmation template
│   └── admin-notification.html       # Admin alert template
├── test-email.js                     # Email testing script
└── .env.example                      # Environment configuration example
```

## Setup Instructions

### 1. Install Dependencies

```bash
cd server
npm install
```

This will install `nodemailer` along with other dependencies.

### 2. Configure Environment Variables

Create a `.env` file in the server directory:

```bash
cp .env.example .env
```

Edit `.env` and configure your SMTP settings:

```env
# Email Configuration (SMTP)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password

# Email Addresses
ADMIN_EMAIL=admin@support-forge.com
FROM_EMAIL=noreply@support-forge.com
```

### 3. Gmail Setup (Recommended)

If using Gmail:

1. Enable 2-Factor Authentication on your Google account
2. Generate an App Password:
   - Go to https://myaccount.google.com/security
   - Click "2-Step Verification"
   - Scroll to "App passwords"
   - Generate a new app password for "Mail"
3. Use the generated 16-character password as `SMTP_PASS`

### 4. Test the Email System

Run the test script to verify everything works:

```bash
npm run test-email
```

Or directly:

```bash
node test-email.js
```

This will:
- Verify SMTP configuration
- Test connection to email server
- Send test emails using all templates
- Send emails to the configured SMTP_USER address

## API Endpoints

### Test Email

Send a test email to verify configuration:

```http
POST /api/email/test
Content-Type: application/json

{
  "recipient": "test@example.com"
}
```

### Contact Form Notification

Send contact form notification:

```http
POST /api/email/contact
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "subject": "Inquiry about services",
  "message": "I would like to know more..."
}
```

### Schedule Confirmation

Send booking confirmation:

```http
POST /api/email/schedule
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "date": "2024-12-15",
  "time": "14:00",
  "service": "IT Support Consultation",
  "notes": "Discuss network infrastructure"
}
```

### Email Service Status

Check email service status:

```http
GET /api/email/status
```

## Email Service Functions

### `sendContactNotification(formData)`

Sends a confirmation email to the user who submitted the contact form.

**Parameters:**
- `name`: User's name
- `email`: User's email address
- `subject`: Contact subject
- `message`: Contact message

**Returns:** `{ success: true, messageId: string }`

### `sendScheduleConfirmation(bookingData)`

Sends a booking confirmation email with appointment details.

**Parameters:**
- `name`: Client name
- `email`: Client email
- `date`: Consultation date
- `time`: Consultation time
- `service`: Service type
- `notes`: Additional notes (optional)

**Returns:** `{ success: true, messageId: string }`

### `sendAdminNotification(type, data)`

Sends notification to admin about new submissions.

**Parameters:**
- `type`: 'contact' or 'booking'
- `data`: Submission data object

**Returns:** `{ success: true, messageId: string }`

### `sendTestEmail(recipient)`

Sends a test email to verify configuration.

**Parameters:**
- `recipient`: Email address to send test to

**Returns:** `{ success: true, messageId: string }`

## Email Templates

All templates use the Support Forge copper/dark theme with professional styling:

### Contact Notification Template
- Confirms receipt of contact form
- Displays message summary
- Shows expected response time (24 hours)

### Schedule Confirmation Template
- Confirms consultation booking
- Shows appointment details
- Includes confirmation number
- Lists what to expect
- Add to calendar button

### Admin Notification Template
- Alerts admin of new submissions
- Shows all submission details
- Displays priority and status
- Quick action buttons

## SMTP Providers

The system works with any SMTP provider:

### Gmail
```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
```

### Outlook/Office365
```env
SMTP_HOST=smtp.office365.com
SMTP_PORT=587
```

### SendGrid
```env
SMTP_HOST=smtp.sendgrid.net
SMTP_PORT=587
SMTP_USER=apikey
SMTP_PASS=your-api-key
```

### AWS SES
```env
SMTP_HOST=email-smtp.us-east-1.amazonaws.com
SMTP_PORT=587
```

## Troubleshooting

### Authentication Failed (EAUTH)

**Problem:** Email authentication fails

**Solutions:**
- Verify SMTP username and password are correct
- For Gmail, use App Password (not regular password)
- Check if 2FA is enabled on your email account

### Connection Failed (ESOCKET)

**Problem:** Cannot connect to SMTP server

**Solutions:**
- Verify SMTP host and port are correct
- Check firewall settings
- Ensure internet connectivity
- Try port 465 with `secure: true` for SSL

### Emails Not Arriving

**Problem:** Emails sent but not received

**Solutions:**
- Check spam/junk folder
- Verify recipient email address is correct
- Check email provider's sending limits
- Review SMTP provider's logs

### Template Errors

**Problem:** Template loading fails

**Solutions:**
- Verify template files exist in `server/templates/`
- Check file permissions
- Ensure template placeholders match data keys

## Security Best Practices

1. **Never commit `.env` file** - Keep credentials secure
2. **Use App Passwords** - Don't use main email password
3. **Limit Admin Email Access** - Only send to verified admin addresses
4. **Validate Input** - Always sanitize user input before sending
5. **Rate Limiting** - Implement rate limiting on email endpoints (recommended)

## Integration with Frontend

To integrate with the existing contact and schedule forms:

1. Import the email service in your route handlers
2. Call email functions after successful form submission
3. Handle email errors gracefully

Example:

```javascript
import emailService from './email.js';

// In your contact route
app.post('/api/contact', async (req, res) => {
  // ... validate and save submission ...

  try {
    // Send customer notification
    await emailService.sendContactNotification(formData);

    // Send admin notification
    await emailService.sendAdminNotification('contact', formData);
  } catch (error) {
    console.error('Email send failed:', error);
    // Don't fail the request if email fails
  }

  res.json({ success: true });
});
```

## Performance Considerations

- Email sending is asynchronous and may take 1-3 seconds
- Consider using a queue system for high-volume applications
- HTML templates are loaded from disk (consider caching for production)
- SMTP connection is reused for efficiency

## Future Enhancements

Potential improvements:

- [ ] Email queue system (Bull, BeeQueue)
- [ ] Template caching
- [ ] Email tracking (open rates, clicks)
- [ ] Attachment support
- [ ] Multi-language templates
- [ ] Email scheduling
- [ ] Unsubscribe management

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review Nodemailer documentation: https://nodemailer.com
3. Verify SMTP provider's documentation
4. Test with the included test script

---

**Version:** 1.0.0
**Last Updated:** December 2024
