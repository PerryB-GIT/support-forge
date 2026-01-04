import express from 'express';
import cors from 'cors';
import bodyParser from 'body-parser';
import dotenv from 'dotenv';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

// Route imports
import calendlyRoutes from './routes/calendly.js';
import emailRoutes from './routes/email.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;
const SUBMISSIONS_FILE = path.join(__dirname, 'data', 'submissions.json');

// Middleware
app.use(cors({
  origin: process.env.CORS_ORIGIN || '*',
  methods: ['GET', 'POST'],
  allowedHeaders: ['Content-Type']
}));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Ensure data directory and submissions file exist
async function initializeDataStore() {
  try {
    const dataDir = path.join(__dirname, 'data');
    await fs.mkdir(dataDir, { recursive: true });

    try {
      await fs.access(SUBMISSIONS_FILE);
    } catch {
      await fs.writeFile(SUBMISSIONS_FILE, JSON.stringify({ contacts: [], schedules: [] }, null, 2));
      console.log('Created submissions.json file');
    }
  } catch (error) {
    console.error('Error initializing data store:', error);
  }
}

// Validation helpers
function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function validatePhone(phone) {
  if (!phone) return true; // Phone is optional
  const phoneRegex = /^[\d\s\-\(\)]+$/;
  return phoneRegex.test(phone) && phone.replace(/\D/g, '').length >= 10;
}

function validateDate(dateString) {
  const date = new Date(dateString);
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  return date instanceof Date && !isNaN(date) && date >= today;
}

function sanitizeInput(input) {
  if (typeof input !== 'string') return input;
  return input.trim().replace(/[<>]/g, '');
}

// Read submissions from file
async function readSubmissions() {
  try {
    const data = await fs.readFile(SUBMISSIONS_FILE, 'utf-8');
    return JSON.parse(data);
  } catch (error) {
    console.error('Error reading submissions:', error);
    return { contacts: [], schedules: [] };
  }
}

// Write submissions to file
async function writeSubmissions(data) {
  try {
    await fs.writeFile(SUBMISSIONS_FILE, JSON.stringify(data, null, 2));
  } catch (error) {
    console.error('Error writing submissions:', error);
    throw error;
  }
}

// Routes
app.get('/', (req, res) => {
  res.json({
    message: 'Support Forge API',
    version: '1.0.0',
    endpoints: {
      contact: 'POST /api/contact',
      schedule: 'POST /api/schedule',
      calendly: '/api/calendly/*',
      email: '/api/email/*'
    }
  });
});

// Register route modules
app.use('/api/calendly', calendlyRoutes);
app.use('/api/email', emailRoutes);

// POST /api/contact - Handle contact form submissions
app.post('/api/contact', async (req, res) => {
  try {
    const { name, email, company, service, message } = req.body;

    // Validate required fields
    if (!name || !email || !message) {
      return res.status(400).json({
        success: false,
        error: 'Missing required fields: name, email, and message are required'
      });
    }

    // Validate email format
    if (!validateEmail(email)) {
      return res.status(400).json({
        success: false,
        error: 'Invalid email format'
      });
    }

    // Validate message length
    if (message.length < 10) {
      return res.status(400).json({
        success: false,
        error: 'Message must be at least 10 characters long'
      });
    }

    // Sanitize inputs
    const sanitizedData = {
      name: sanitizeInput(name),
      email: sanitizeInput(email),
      company: company ? sanitizeInput(company) : null,
      service: service || 'Not specified',
      message: sanitizeInput(message),
      timestamp: new Date().toISOString(),
      type: 'contact'
    };

    // Read current submissions
    const submissions = await readSubmissions();
    submissions.contacts.push(sanitizedData);

    // Write updated submissions
    await writeSubmissions(submissions);

    res.json({
      success: true,
      message: 'Contact form submitted successfully',
      data: {
        name: sanitizedData.name,
        email: sanitizedData.email,
        timestamp: sanitizedData.timestamp
      }
    });

  } catch (error) {
    console.error('Error processing contact form:', error);
    res.status(500).json({
      success: false,
      error: 'Internal server error. Please try again later.'
    });
  }
});

// POST /api/schedule - Handle consultation booking requests
app.post('/api/schedule', async (req, res) => {
  try {
    const { name, email, phone, date, time, topic } = req.body;

    // Validate required fields
    if (!name || !email || !date || !time) {
      return res.status(400).json({
        success: false,
        error: 'Missing required fields: name, email, date, and time are required'
      });
    }

    // Validate email format
    if (!validateEmail(email)) {
      return res.status(400).json({
        success: false,
        error: 'Invalid email format'
      });
    }

    // Validate phone format if provided
    if (phone && !validatePhone(phone)) {
      return res.status(400).json({
        success: false,
        error: 'Invalid phone number format'
      });
    }

    // Validate date
    if (!validateDate(date)) {
      return res.status(400).json({
        success: false,
        error: 'Invalid date or date is in the past'
      });
    }

    // Validate time format (should be HH:MM)
    const timeRegex = /^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/;
    if (!timeRegex.test(time)) {
      return res.status(400).json({
        success: false,
        error: 'Invalid time format. Use HH:MM format.'
      });
    }

    // Sanitize inputs
    const sanitizedData = {
      name: sanitizeInput(name),
      email: sanitizeInput(email),
      phone: phone ? sanitizeInput(phone) : null,
      date: date,
      time: time,
      topic: topic || 'General Consultation',
      timestamp: new Date().toISOString(),
      type: 'schedule'
    };

    // Read current submissions
    const submissions = await readSubmissions();
    submissions.schedules.push(sanitizedData);

    // Write updated submissions
    await writeSubmissions(submissions);

    res.json({
      success: true,
      message: 'Consultation scheduled successfully',
      data: {
        name: sanitizedData.name,
        email: sanitizedData.email,
        scheduledDate: sanitizedData.date,
        scheduledTime: sanitizedData.time,
        timestamp: sanitizedData.timestamp
      }
    });

  } catch (error) {
    console.error('Error processing schedule form:', error);
    res.status(500).json({
      success: false,
      error: 'Internal server error. Please try again later.'
    });
  }
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({
    success: false,
    error: 'Endpoint not found'
  });
});

// Error handler
app.use((err, req, res, next) => {
  console.error('Server error:', err);
  res.status(500).json({
    success: false,
    error: 'Internal server error'
  });
});

// Initialize and start server
async function startServer() {
  await initializeDataStore();

  app.listen(PORT, () => {
    console.log(`Support Forge API server running on port ${PORT}`);
    console.log(`Environment: ${process.env.NODE_ENV || 'development'}`);
    console.log(`CORS origin: ${process.env.CORS_ORIGIN || '*'}`);
  });
}

startServer();
