# Support Forge API Server

Backend API server for the Support Forge website, handling contact form submissions and consultation scheduling requests.

## Features

- RESTful API endpoints for contact and scheduling forms
- Input validation and sanitization
- CORS support for frontend integration
- Local JSON file-based storage
- Proper error handling and responses

## Prerequisites

- Node.js (v14 or higher)
- npm or yarn

## Installation

1. Navigate to the server directory:
```bash
cd server
```

2. Install dependencies:
```bash
npm install
```

3. Create environment file:
```bash
cp .env.example .env
```

4. (Optional) Edit `.env` to customize configuration:
```bash
# Default values work for local development
PORT=3000
NODE_ENV=development
CORS_ORIGIN=*
```

## Running the Server

### Development Mode
```bash
npm run dev
```
This uses Node's `--watch` flag to auto-restart on file changes.

### Production Mode
```bash
npm start
```

The server will start on `http://localhost:3000` (or the port specified in your `.env` file).

## API Endpoints

### GET /
Health check endpoint that returns API information.

**Response:**
```json
{
  "message": "Support Forge API",
  "version": "1.0.0",
  "endpoints": {
    "contact": "POST /api/contact",
    "schedule": "POST /api/schedule"
  }
}
```

### POST /api/contact
Handle contact form submissions.

**Request Body:**
```json
{
  "name": "John Smith",
  "email": "john@company.com",
  "company": "Acme Corp",
  "service": "AI Solutions",
  "message": "I'm interested in your AI consulting services."
}
```

**Required Fields:** `name`, `email`, `message`

**Validation Rules:**
- Valid email format
- Message must be at least 10 characters
- Inputs are sanitized to prevent XSS

**Success Response (200):**
```json
{
  "success": true,
  "message": "Contact form submitted successfully",
  "data": {
    "name": "John Smith",
    "email": "john@company.com",
    "timestamp": "2025-12-06T12:00:00.000Z"
  }
}
```

**Error Response (400):**
```json
{
  "success": false,
  "error": "Missing required fields: name, email, and message are required"
}
```

### POST /api/schedule
Handle consultation scheduling requests.

**Request Body:**
```json
{
  "name": "John Smith",
  "email": "john@company.com",
  "phone": "(555) 123-4567",
  "date": "2025-12-15",
  "time": "14:00",
  "topic": "AI Strategy Consultation"
}
```

**Required Fields:** `name`, `email`, `date`, `time`

**Validation Rules:**
- Valid email format
- Valid phone format (if provided)
- Date must be today or in the future
- Time must be in HH:MM format
- Inputs are sanitized to prevent XSS

**Success Response (200):**
```json
{
  "success": true,
  "message": "Consultation scheduled successfully",
  "data": {
    "name": "John Smith",
    "email": "john@company.com",
    "scheduledDate": "2025-12-15",
    "scheduledTime": "14:00",
    "timestamp": "2025-12-06T12:00:00.000Z"
  }
}
```

**Error Response (400):**
```json
{
  "success": false,
  "error": "Invalid date or date is in the past"
}
```

## Data Storage

Submissions are stored locally in `server/data/submissions.json`:

```json
{
  "contacts": [
    {
      "name": "John Smith",
      "email": "john@company.com",
      "company": "Acme Corp",
      "service": "AI Solutions",
      "message": "I'm interested in your AI consulting services.",
      "timestamp": "2025-12-06T12:00:00.000Z",
      "type": "contact"
    }
  ],
  "schedules": [
    {
      "name": "Jane Doe",
      "email": "jane@example.com",
      "phone": "(555) 987-6543",
      "date": "2025-12-15",
      "time": "14:00",
      "topic": "AI Strategy Consultation",
      "timestamp": "2025-12-06T12:00:00.000Z",
      "type": "schedule"
    }
  ]
}
```

## Security Features

1. **Input Validation:** All inputs are validated before processing
2. **Input Sanitization:** HTML tags are removed to prevent XSS attacks
3. **CORS Protection:** Configurable CORS origin for production security
4. **Email Validation:** RFC-compliant email validation
5. **Date Validation:** Prevents scheduling in the past

## CORS Configuration

For development, CORS is open to all origins (`*`). In production, set `CORS_ORIGIN` in your `.env` file:

```env
CORS_ORIGIN=https://your-frontend-domain.com
```

## Project Structure

```
server/
├── index.js              # Main Express server
├── package.json          # Dependencies and scripts
├── .env.example          # Environment variables template
├── .env                  # Your local environment (not in git)
├── README.md             # This file
└── data/
    └── submissions.json  # Local storage for form submissions
```

## Future Enhancements

This basic server can be extended with:

- Database integration (PostgreSQL, MongoDB)
- Email notifications (nodemailer)
- Authentication/authorization
- Rate limiting
- Webhook integrations
- Admin dashboard for viewing submissions

## Troubleshooting

**Port already in use:**
```bash
# Change PORT in .env file or kill the process using the port
PORT=3001 npm start
```

**CORS errors:**
```bash
# Make sure CORS_ORIGIN is set correctly in .env
# For development, use CORS_ORIGIN=*
```

**Module not found errors:**
```bash
# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

## License

MIT
