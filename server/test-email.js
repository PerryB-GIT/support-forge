import dotenv from 'dotenv';
import emailService from './email.js';

dotenv.config();

/**
 * Email Service Test Script
 * Tests all email functionality to ensure proper configuration
 */

async function runTests() {
  console.log('\n=================================');
  console.log('  Email Service Test Suite');
  console.log('=================================\n');

  try {
    // Test 1: Verify SMTP configuration
    console.log('Test 1: Verifying SMTP Configuration...');
    console.log('----------------------------------');
    console.log(`SMTP Host: ${process.env.SMTP_HOST || 'NOT SET'}`);
    console.log(`SMTP Port: ${process.env.SMTP_PORT || 'NOT SET'}`);
    console.log(`SMTP User: ${process.env.SMTP_USER || 'NOT SET'}`);
    console.log(`SMTP Pass: ${process.env.SMTP_PASS ? '***' : 'NOT SET'}`);
    console.log(`From Email: ${process.env.FROM_EMAIL || 'NOT SET'}`);
    console.log(`Admin Email: ${process.env.ADMIN_EMAIL || 'NOT SET'}\n`);

    if (!process.env.SMTP_HOST || !process.env.SMTP_USER || !process.env.SMTP_PASS) {
      console.error('❌ SMTP configuration incomplete!');
      console.error('Please configure your .env file with SMTP settings.\n');
      process.exit(1);
    }

    // Test 2: Verify SMTP connection
    console.log('Test 2: Verifying SMTP Connection...');
    console.log('----------------------------------');
    const isConnected = await emailService.verifyConnection();

    if (!isConnected) {
      console.error('❌ Could not connect to SMTP server!\n');
      process.exit(1);
    }

    console.log('');

    // Test 3: Send test email
    console.log('Test 3: Sending Test Email...');
    console.log('----------------------------------');
    const testRecipient = process.env.SMTP_USER; // Send to yourself
    console.log(`Recipient: ${testRecipient}`);

    const testResult = await emailService.sendTestEmail(testRecipient);
    console.log(`Message ID: ${testResult.messageId}\n`);

    // Test 4: Test contact notification template
    console.log('Test 4: Testing Contact Notification...');
    console.log('----------------------------------');
    const contactResult = await emailService.sendContactNotification({
      name: 'Test User',
      email: testRecipient,
      subject: 'Test Contact Form Submission',
      message: 'This is a test message from the email service test script.'
    });
    console.log(`Message ID: ${contactResult.messageId}\n`);

    // Test 5: Test schedule confirmation template
    console.log('Test 5: Testing Schedule Confirmation...');
    console.log('----------------------------------');
    const scheduleResult = await emailService.sendScheduleConfirmation({
      name: 'Test User',
      email: testRecipient,
      date: '2024-12-15',
      time: '14:00',
      service: 'IT Support Consultation',
      notes: 'This is a test booking from the email service test script.'
    });
    console.log(`Message ID: ${scheduleResult.messageId}\n`);

    // Test 6: Test admin notification - contact
    console.log('Test 6: Testing Admin Notification (Contact)...');
    console.log('----------------------------------');
    const adminContactResult = await emailService.sendAdminNotification('contact', {
      name: 'Test User',
      email: testRecipient,
      subject: 'Test Contact Submission',
      message: 'This is a test admin notification for contact form.'
    });
    console.log(`Message ID: ${adminContactResult.messageId}\n`);

    // Test 7: Test admin notification - booking
    console.log('Test 7: Testing Admin Notification (Booking)...');
    console.log('----------------------------------');
    const adminBookingResult = await emailService.sendAdminNotification('booking', {
      name: 'Test User',
      email: testRecipient,
      date: '2024-12-15',
      time: '14:00',
      service: 'IT Support Consultation',
      notes: 'This is a test admin notification for booking.'
    });
    console.log(`Message ID: ${adminBookingResult.messageId}\n`);

    // All tests passed
    console.log('=================================');
    console.log('  ✅ All tests passed!');
    console.log('=================================\n');
    console.log('Email service is working correctly.');
    console.log(`Check your inbox at ${testRecipient} for the test emails.\n`);

  } catch (error) {
    console.error('\n❌ Test failed with error:');
    console.error('----------------------------------');
    console.error(`Error: ${error.message}`);
    console.error(`Code: ${error.code || 'N/A'}`);

    if (error.code === 'EAUTH') {
      console.error('\nAuthentication failed. Please check:');
      console.error('- Your SMTP username and password are correct');
      console.error('- If using Gmail, you need an "App Password" (not your regular password)');
      console.error('- Visit: https://support.google.com/accounts/answer/185833');
    } else if (error.code === 'ESOCKET') {
      console.error('\nConnection failed. Please check:');
      console.error('- Your SMTP host and port are correct');
      console.error('- Your firewall is not blocking the connection');
      console.error('- You have internet connectivity');
    }

    console.error('\n');
    process.exit(1);
  }
}

// Run tests
runTests();
