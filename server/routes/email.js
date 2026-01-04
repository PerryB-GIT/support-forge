import express from 'express';
import emailService from '../email.js';

const router = express.Router();

/**
 * POST /api/email/test
 * Send a test email to verify email configuration
 *
 * Body:
 * {
 *   "recipient": "test@example.com"
 * }
 */
router.post('/test', async (req, res) => {
  try {
    const { recipient } = req.body;

    // Validate recipient email
    if (!recipient) {
      return res.status(400).json({
        success: false,
        error: 'Recipient email is required'
      });
    }

    // Basic email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(recipient)) {
      return res.status(400).json({
        success: false,
        error: 'Invalid email format'
      });
    }

    // Verify email service connection first
    const isConnected = await emailService.verifyConnection();
    if (!isConnected) {
      return res.status(503).json({
        success: false,
        error: 'Email service is not properly configured. Please check your SMTP settings.'
      });
    }

    // Send test email
    const result = await emailService.sendTestEmail(recipient);

    res.json({
      success: true,
      message: `Test email sent successfully to ${recipient}`,
      messageId: result.messageId
    });

  } catch (error) {
    console.error('Error sending test email:', error);

    // Provide more specific error messages
    let errorMessage = 'Failed to send test email';

    if (error.code === 'EAUTH') {
      errorMessage = 'Email authentication failed. Please check your SMTP credentials.';
    } else if (error.code === 'ESOCKET') {
      errorMessage = 'Could not connect to email server. Please check your SMTP host and port.';
    } else if (error.message) {
      errorMessage = error.message;
    }

    res.status(500).json({
      success: false,
      error: errorMessage
    });
  }
});

/**
 * POST /api/email/contact
 * Send contact form notification email
 *
 * Body:
 * {
 *   "name": "John Doe",
 *   "email": "john@example.com",
 *   "subject": "Inquiry about services",
 *   "message": "I would like to know more..."
 * }
 */
router.post('/contact', async (req, res) => {
  try {
    const { name, email, subject, message } = req.body;

    // Validate required fields
    if (!name || !email || !subject || !message) {
      return res.status(400).json({
        success: false,
        error: 'All fields are required: name, email, subject, and message'
      });
    }

    // Send contact notification to customer
    const customerEmail = await emailService.sendContactNotification({
      name,
      email,
      subject,
      message
    });

    // Send admin notification
    const adminEmail = await emailService.sendAdminNotification('contact', {
      name,
      email,
      subject,
      message
    });

    res.json({
      success: true,
      message: 'Contact notification sent successfully',
      messageIds: {
        customer: customerEmail.messageId,
        admin: adminEmail.messageId
      }
    });

  } catch (error) {
    console.error('Error sending contact notification:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to send contact notification: ' + error.message
    });
  }
});

/**
 * POST /api/email/schedule
 * Send schedule confirmation email
 *
 * Body:
 * {
 *   "name": "John Doe",
 *   "email": "john@example.com",
 *   "date": "2024-12-15",
 *   "time": "14:00",
 *   "service": "IT Support Consultation",
 *   "notes": "Discuss network infrastructure"
 * }
 */
router.post('/schedule', async (req, res) => {
  try {
    const { name, email, date, time, service, notes } = req.body;

    // Validate required fields
    if (!name || !email || !date || !time || !service) {
      return res.status(400).json({
        success: false,
        error: 'Required fields: name, email, date, time, and service'
      });
    }

    // Send schedule confirmation to customer
    const customerEmail = await emailService.sendScheduleConfirmation({
      name,
      email,
      date,
      time,
      service,
      notes: notes || ''
    });

    // Send admin notification
    const adminEmail = await emailService.sendAdminNotification('booking', {
      name,
      email,
      date,
      time,
      service,
      notes: notes || ''
    });

    res.json({
      success: true,
      message: 'Schedule confirmation sent successfully',
      messageIds: {
        customer: customerEmail.messageId,
        admin: adminEmail.messageId
      }
    });

  } catch (error) {
    console.error('Error sending schedule confirmation:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to send schedule confirmation: ' + error.message
    });
  }
});

/**
 * GET /api/email/status
 * Check email service status
 */
router.get('/status', async (req, res) => {
  try {
    const isConnected = await emailService.verifyConnection();

    res.json({
      success: true,
      status: isConnected ? 'connected' : 'disconnected',
      configured: !!(process.env.SMTP_HOST && process.env.SMTP_USER && process.env.SMTP_PASS),
      settings: {
        host: process.env.SMTP_HOST || 'not configured',
        port: process.env.SMTP_PORT || 'not configured',
        from: process.env.FROM_EMAIL || 'not configured',
        admin: process.env.ADMIN_EMAIL || 'not configured'
      }
    });
  } catch (error) {
    console.error('Error checking email status:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to check email service status'
    });
  }
});

export default router;
