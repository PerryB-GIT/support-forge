import nodemailer from 'nodemailer';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';
import dotenv from 'dotenv';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

dotenv.config();

/**
 * Email Service Module
 * Handles all email notifications for the Support Forge website
 */

class EmailService {
  constructor() {
    this.transporter = null;
    this.initialize();
  }

  /**
   * Initialize the email transporter with SMTP configuration
   */
  initialize() {
    try {
      this.transporter = nodemailer.createTransport({
        host: process.env.SMTP_HOST,
        port: parseInt(process.env.SMTP_PORT || '587'),
        secure: process.env.SMTP_PORT === '465', // true for 465, false for other ports
        auth: {
          user: process.env.SMTP_USER,
          pass: process.env.SMTP_PASS,
        },
      });

      console.log('✓ Email service initialized successfully');
    } catch (error) {
      console.error('✗ Failed to initialize email service:', error.message);
      throw error;
    }
  }

  /**
   * Verify the email connection
   * @returns {Promise<boolean>} True if connection is successful
   */
  async verifyConnection() {
    try {
      await this.transporter.verify();
      console.log('✓ SMTP connection verified');
      return true;
    } catch (error) {
      console.error('✗ SMTP connection failed:', error.message);
      return false;
    }
  }

  /**
   * Load and populate an email template
   * @param {string} templateName - Name of the template file
   * @param {Object} data - Data to populate the template
   * @returns {Promise<string>} Populated HTML template
   */
  async loadTemplate(templateName, data) {
    try {
      const templatePath = path.join(__dirname, 'templates', templateName);
      let template = await fs.readFile(templatePath, 'utf-8');

      // Replace all placeholders in the template
      Object.keys(data).forEach(key => {
        const placeholder = new RegExp(`{{${key}}}`, 'g');
        template = template.replace(placeholder, data[key] || '');
      });

      return template;
    } catch (error) {
      console.error(`✗ Failed to load template ${templateName}:`, error.message);
      throw error;
    }
  }

  /**
   * Send email when contact form is submitted
   * @param {Object} formData - Contact form data
   * @param {string} formData.name - Contact name
   * @param {string} formData.email - Contact email
   * @param {string} formData.subject - Email subject
   * @param {string} formData.message - Email message
   * @returns {Promise<Object>} Email send result
   */
  async sendContactNotification(formData) {
    try {
      const { name, email, subject, message } = formData;

      // Load and populate template
      const html = await this.loadTemplate('contact-notification.html', {
        name,
        email,
        subject,
        message,
        date: new Date().toLocaleDateString('en-US', {
          weekday: 'long',
          year: 'numeric',
          month: 'long',
          day: 'numeric',
        }),
      });

      // Plain text version
      const text = `
New Contact Form Submission

From: ${name} <${email}>
Subject: ${subject}
Date: ${new Date().toLocaleString()}

Message:
${message}
      `.trim();

      // Send email
      const info = await this.transporter.sendMail({
        from: `"Support Forge" <${process.env.FROM_EMAIL}>`,
        to: email,
        subject: `Thank you for contacting Support Forge - ${subject}`,
        text,
        html,
      });

      console.log('✓ Contact notification sent:', info.messageId);
      return { success: true, messageId: info.messageId };
    } catch (error) {
      console.error('✗ Failed to send contact notification:', error.message);
      throw error;
    }
  }

  /**
   * Send confirmation email when consultation is booked
   * @param {Object} bookingData - Booking information
   * @param {string} bookingData.name - Client name
   * @param {string} bookingData.email - Client email
   * @param {string} bookingData.date - Consultation date
   * @param {string} bookingData.time - Consultation time
   * @param {string} bookingData.service - Service type
   * @param {string} bookingData.notes - Additional notes
   * @returns {Promise<Object>} Email send result
   */
  async sendScheduleConfirmation(bookingData) {
    try {
      const { name, email, date, time, service, notes } = bookingData;

      // Load and populate template
      const html = await this.loadTemplate('schedule-confirmation.html', {
        name,
        date,
        time,
        service,
        notes: notes || 'No additional notes',
        confirmationNumber: `SF-${Date.now().toString(36).toUpperCase()}`,
      });

      // Plain text version
      const text = `
Consultation Booking Confirmation - Support Forge

Hello ${name},

Thank you for scheduling a consultation with Support Forge!

Booking Details:
- Date: ${date}
- Time: ${time}
- Service: ${service}
- Notes: ${notes || 'No additional notes'}
- Confirmation #: SF-${Date.now().toString(36).toUpperCase()}

We look forward to meeting with you!

If you need to reschedule or have any questions, please contact us at ${process.env.ADMIN_EMAIL}

Best regards,
Support Forge Team
      `.trim();

      // Send email
      const info = await this.transporter.sendMail({
        from: `"Support Forge" <${process.env.FROM_EMAIL}>`,
        to: email,
        subject: 'Consultation Booking Confirmed - Support Forge',
        text,
        html,
      });

      console.log('✓ Schedule confirmation sent:', info.messageId);
      return { success: true, messageId: info.messageId };
    } catch (error) {
      console.error('✗ Failed to send schedule confirmation:', error.message);
      throw error;
    }
  }

  /**
   * Send notification to admin about new submissions
   * @param {string} type - Type of notification (contact, booking)
   * @param {Object} data - Submission data
   * @returns {Promise<Object>} Email send result
   */
  async sendAdminNotification(type, data) {
    try {
      let templateData = {
        type: type.toUpperCase(),
        timestamp: new Date().toLocaleString(),
      };

      // Prepare data based on type
      if (type === 'contact') {
        templateData = {
          ...templateData,
          title: 'New Contact Form Submission',
          details: `
            <p><strong>Name:</strong> ${data.name}</p>
            <p><strong>Email:</strong> ${data.email}</p>
            <p><strong>Subject:</strong> ${data.subject}</p>
            <p><strong>Message:</strong></p>
            <p style="padding: 15px; background: #f5f5f5; border-left: 3px solid #b87333; margin: 10px 0;">${data.message}</p>
          `,
        };
      } else if (type === 'booking') {
        templateData = {
          ...templateData,
          title: 'New Consultation Booking',
          details: `
            <p><strong>Name:</strong> ${data.name}</p>
            <p><strong>Email:</strong> ${data.email}</p>
            <p><strong>Date:</strong> ${data.date}</p>
            <p><strong>Time:</strong> ${data.time}</p>
            <p><strong>Service:</strong> ${data.service}</p>
            <p><strong>Notes:</strong> ${data.notes || 'No additional notes'}</p>
          `,
        };
      }

      // Load and populate template
      const html = await this.loadTemplate('admin-notification.html', templateData);

      // Plain text version
      const text = `
${templateData.title}
${new Date().toLocaleString()}

${type === 'contact' ? `
Name: ${data.name}
Email: ${data.email}
Subject: ${data.subject}
Message: ${data.message}
` : `
Name: ${data.name}
Email: ${data.email}
Date: ${data.date}
Time: ${data.time}
Service: ${data.service}
Notes: ${data.notes || 'No additional notes'}
`}
      `.trim();

      // Send email
      const info = await this.transporter.sendMail({
        from: `"Support Forge Notifications" <${process.env.FROM_EMAIL}>`,
        to: process.env.ADMIN_EMAIL,
        subject: `[Support Forge] ${templateData.title}`,
        text,
        html,
      });

      console.log('✓ Admin notification sent:', info.messageId);
      return { success: true, messageId: info.messageId };
    } catch (error) {
      console.error('✗ Failed to send admin notification:', error.message);
      throw error;
    }
  }

  /**
   * Send a test email to verify configuration
   * @param {string} recipient - Email address to send test to
   * @returns {Promise<Object>} Email send result
   */
  async sendTestEmail(recipient) {
    try {
      const info = await this.transporter.sendMail({
        from: `"Support Forge" <${process.env.FROM_EMAIL}>`,
        to: recipient,
        subject: 'Test Email - Support Forge Email Service',
        text: 'This is a test email from the Support Forge email service. If you received this, your email configuration is working correctly!',
        html: `
          <div style="font-family: 'Georgia', serif; max-width: 600px; margin: 0 auto; padding: 20px; background: #1a1a1a; color: #e0e0e0;">
            <h2 style="color: #b87333; border-bottom: 2px solid #b87333; padding-bottom: 10px;">Test Email</h2>
            <p>This is a test email from the Support Forge email service.</p>
            <p style="padding: 15px; background: #2a2a2a; border-left: 3px solid #b87333; margin: 20px 0;">
              <strong style="color: #b87333;">Success!</strong> If you received this email, your email configuration is working correctly.
            </p>
            <p style="color: #999; font-size: 12px; margin-top: 30px; padding-top: 20px; border-top: 1px solid #333;">
              Sent from Support Forge Email Service<br>
              ${new Date().toLocaleString()}
            </p>
          </div>
        `,
      });

      console.log('✓ Test email sent:', info.messageId);
      return { success: true, messageId: info.messageId };
    } catch (error) {
      console.error('✗ Failed to send test email:', error.message);
      throw error;
    }
  }
}

// Create and export a singleton instance
const emailService = new EmailService();

export default emailService;
