# Calendly Integration Guide - Support Forge

This guide provides complete instructions for integrating Calendly scheduling into the Support Forge website.

## Overview

The Calendly integration has been implemented with the following components:

1. **Backend API** - Express server with Calendly API integration
2. **API Routes** - RESTful endpoints for event types, availability, and booking
3. **Widget Example** - HTML page showing inline Calendly widget
4. **Client Examples** - JavaScript examples for custom integration

---

## Files Created

### Backend Server Files

```
server/
├── calendly.js                    # Calendly API integration module
├── routes/calendly.js             # API route handlers
└── server.js                      # Express server (with Calendly routes)
```

### Frontend Files

```
calendly-widget.html               # Demo page with multiple integration options
client-calendly-example.js         # Client-side JavaScript examples
.env                               # Environment variables (API key configured)
.env.example                       # Template for environment variables
```

### Documentation

```
CALENDLY_INTEGRATION_GUIDE.md      # This file
server/README.md                   # Server API documentation
```

---

## Quick Start

### 1. Install Dependencies

```bash
cd server
npm install
```

### 2. Start the Server

```bash
npm start
```

The server will start on `http://localhost:3000`

### 3. Test the Integration

Open in your browser:
- **Widget Demo**: `http://localhost:3000/calendly-widget.html`
- **API Health Check**: `http://localhost:3000/api/health`
- **Event Types**: `http://localhost:3000/api/calendly/event-types`

---

## Integration Options

### Option 1: Inline Widget (Recommended)

**Best for**: Seamless booking experience directly on your website

**Implementation**:

1. Add Calendly CSS to your `<head>`:
```html
<link href="https://assets.calendly.com/assets/external/widget.css" rel="stylesheet">
```

2. Add widget HTML where you want the calendar:
```html
<div class="calendly-inline-widget"
     data-url="https://calendly.com/perry-bailes?hide_gdpr_banner=1&primary_color=dc2626"
     style="min-width:320px;height:700px;">
</div>
```

3. Add Calendly JavaScript before closing `</body>`:
```html
<script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
```

**Customization**:
- `primary_color` - Brand color (hex without #)
- `text_color` - Text color
- `background_color` - Background color
- `hide_gdpr_banner` - Hide GDPR banner (set to 1)

**See**: `calendly-widget.html` for complete example

---

### Option 2: Popup Button

**Best for**: Keeping users on your page while booking

**Implementation**:

```html
<!-- Add to HTML -->
<button onclick="Calendly.initPopupWidget({url: 'https://calendly.com/perry-bailes?primary_color=dc2626'});return false;">
    Book a Meeting
</button>

<!-- Add to <head> -->
<link href="https://assets.calendly.com/assets/external/widget.css" rel="stylesheet">

<!-- Add before </body> -->
<script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
```

---

### Option 3: Direct Link

**Best for**: Simple implementation, opens in new tab

**Implementation**:

```html
<a href="https://calendly.com/perry-bailes" target="_blank">
    Schedule a Consultation
</a>
```

**Pre-fill form data**:
```javascript
function openCalendlyWithPrefill(name, email) {
    const url = new URL('https://calendly.com/perry-bailes');
    if (name) url.searchParams.set('name', name);
    if (email) url.searchParams.set('email', email);
    window.open(url.toString(), '_blank');
}
```

---

### Option 4: Custom API Integration

**Best for**: Full control over booking experience, custom UI

**Implementation**:

1. **Fetch Available Event Types**:
```javascript
const response = await fetch('http://localhost:3000/api/calendly/event-types');
const data = await response.json();
console.log(data.event_types);
```

2. **Get Available Time Slots**:
```javascript
const params = new URLSearchParams({
    event_type_uri: 'https://api.calendly.com/event_types/...',
    start_time: '2025-12-07T00:00:00Z',
    end_time: '2025-12-14T23:59:59Z'
});
const response = await fetch(`http://localhost:3000/api/calendly/availability?${params}`);
const data = await response.json();
console.log(data.available_slots);
```

3. **Create Booking**:
```javascript
const response = await fetch('http://localhost:3000/api/calendly/book', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        event_type_uri: 'https://api.calendly.com/event_types/...',
        start_time: '2025-12-07T14:00:00Z',
        invitee_email: 'client@example.com',
        invitee_name: 'John Doe',
        phone: '(555) 123-4567'
    })
});
const data = await response.json();
// Redirect to booking URL
window.location.href = data.booking_url;
```

**See**: `client-calendly-example.js` for complete examples

---

## Replacing the Current Schedule Form

### Current Implementation

The current `index.html` has a custom schedule form (lines 268-298) that doesn't actually book anything.

### Recommended Replacement Strategy

#### Strategy A: Replace with Inline Widget (Easiest)

1. Open `index.html`
2. Find the schedule section (around line 242)
3. Replace the schedule form HTML with:

```html
<section id="schedule" class="schedule-section">
    <div class="container">
        <div class="section-header">
            <span class="section-tag">Free Consultation</span>
            <h2>Schedule a Meeting</h2>
            <p class="section-description">Book a free 30-minute consultation to discuss your technology needs. No obligation, just expert advice.</p>
        </div>

        <div style="max-width: 900px; margin: 0 auto; background: #141419; border: 1px solid #2a2a35; border-radius: 12px; padding: 32px;">
            <!-- Calendly inline widget begins -->
            <div class="calendly-inline-widget"
                 data-url="https://calendly.com/perry-bailes?hide_gdpr_banner=1&primary_color=dc2626"
                 style="min-width:320px;height:700px;">
            </div>
            <!-- Calendly inline widget ends -->
        </div>
    </div>
</section>
```

4. Add before closing `</body>`:
```html
<script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
```

5. Add to `<head>`:
```html
<link href="https://assets.calendly.com/assets/external/widget.css" rel="stylesheet">
```

#### Strategy B: Keep Form, Add API Integration (More Work)

Keep the existing form design but wire it to the Calendly API:

1. Add event type selector
2. Load available time slots dynamically
3. Submit to API and redirect to Calendly booking URL

See `client-calendly-example.js` Example 6 for implementation.

---

## API Reference

### Base URL
```
http://localhost:3000/api/calendly
```

### Endpoints

#### GET /event-types
Returns all available event types

**Response**:
```json
{
  "success": true,
  "count": 2,
  "event_types": [
    {
      "uri": "https://api.calendly.com/event_types/...",
      "name": "30 Minute Meeting",
      "duration": 30,
      "scheduling_url": "https://calendly.com/perry-bailes/30min"
    }
  ]
}
```

#### GET /availability
Get available time slots

**Query Parameters**:
- `event_type_uri` (required)
- `start_time` (required) - ISO 8601 format
- `end_time` (required) - ISO 8601 format

**Example**:
```
GET /availability?event_type_uri=https://api.calendly.com/event_types/...&start_time=2025-12-07T00:00:00Z&end_time=2025-12-14T23:59:59Z
```

**Response**:
```json
{
  "success": true,
  "count": 24,
  "available_slots": [
    {
      "start_time": "2025-12-07T14:00:00Z",
      "status": "available",
      "invitees_remaining": 1
    }
  ]
}
```

#### POST /book
Create a booking (returns pre-filled Calendly link)

**Request Body**:
```json
{
  "event_type_uri": "https://api.calendly.com/event_types/...",
  "start_time": "2025-12-07T14:00:00Z",
  "invitee_email": "client@example.com",
  "invitee_name": "John Doe",
  "phone": "(555) 123-4567"
}
```

**Response**:
```json
{
  "success": true,
  "booking_url": "https://calendly.com/perry-bailes/30min?name=John+Doe&email=...",
  "message": "Please complete your booking using the provided link"
}
```

#### GET /user
Get Calendly user information

**Response**:
```json
{
  "success": true,
  "user": {
    "name": "Perry Bailes",
    "email": "perry.bailes@gmail.com",
    "scheduling_url": "https://calendly.com/perry-bailes"
  }
}
```

---

## Benefits of Calendly Integration

### Automatic Features You Get

1. **Real-time Calendar Sync** - No double bookings
2. **Time Zone Detection** - Automatically shows times in visitor's time zone
3. **Email Reminders** - Automatic confirmation and reminder emails
4. **Calendar Integration** - Syncs with Google Calendar, Outlook, etc.
5. **Mobile Responsive** - Works perfectly on all devices
6. **Rescheduling/Cancellation** - Clients can manage their bookings
7. **Video Conference Links** - Automatically generates Zoom/Meet links
8. **Customizable Questions** - Collect information you need before meetings

### Professional Appearance

- Branded booking experience
- Matches your website design (customizable colors)
- No "Powered by Calendly" branding on paid plans

---

## Environment Variables

The API key is already configured in `.env`:

```env
CALENDLY_API_KEY=eyJraWQi...
CALENDLY_USER_URI=https://api.calendly.com/users/5a82effc-8f25-4ed9-861b-0091854acd67
PORT=3000
NODE_ENV=development
```

**Important**: Never commit `.env` to version control. Use `.env.example` as a template.

---

## Testing the Integration

### 1. Test Server Health

```bash
curl http://localhost:3000/api/health
```

Expected response:
```json
{
  "status": "healthy",
  "calendly_api_key_set": true
}
```

### 2. Test Event Types

```bash
curl http://localhost:3000/api/calendly/event-types
```

### 3. Test Availability

```bash
curl "http://localhost:3000/api/calendly/availability?event_type_uri=YOUR_EVENT_URI&start_time=2025-12-07T00:00:00Z&end_time=2025-12-14T23:59:59Z"
```

### 4. Test Booking

```bash
curl -X POST http://localhost:3000/api/calendly/book \
  -H "Content-Type: application/json" \
  -d '{
    "event_type_uri": "YOUR_EVENT_URI",
    "start_time": "2025-12-07T14:00:00Z",
    "invitee_email": "test@example.com",
    "invitee_name": "Test User"
  }'
```

---

## Deployment Considerations

### Production Checklist

- [ ] Set `NODE_ENV=production` in environment
- [ ] Use HTTPS for all API calls
- [ ] Configure CORS for your domain only
- [ ] Add rate limiting to API endpoints
- [ ] Set up monitoring for API errors
- [ ] Configure proper error logging
- [ ] Test all booking flows end-to-end

### Security Notes

- API key is stored securely in environment variables
- All user input is validated server-side
- Email format validation prevents injection
- Date validation prevents booking in the past
- CORS should be configured for production domain

---

## Troubleshooting

### Issue: "CALENDLY_API_KEY environment variable is not set"
**Solution**: Make sure `.env` file exists in server directory with the API key

### Issue: "Failed to fetch event types"
**Solution**:
1. Check API key is valid
2. Verify server is running
3. Check network connectivity
4. Review server logs for detailed error

### Issue: Widget not showing
**Solution**:
1. Check Calendly JavaScript is loaded
2. Verify CSS is included
3. Check browser console for errors
4. Ensure minimum width/height are set

### Issue: "Cannot book events in the past"
**Solution**: Ensure time is in the future and in correct time zone (UTC)

---

## Support & Resources

### Calendly Documentation
- [API Documentation](https://developer.calendly.com/api-docs)
- [Widget Customization](https://help.calendly.com/hc/en-us/articles/223147027-Embed-options-overview)
- [URL Parameters](https://help.calendly.com/hc/en-us/articles/360020052833-Advanced-embed-options)

### Files to Review
- `server/calendly.js` - API integration functions
- `server/routes/calendly.js` - API endpoints
- `client-calendly-example.js` - Client-side examples
- `calendly-widget.html` - Widget demo page

---

## Next Steps

1. **Choose Your Integration Method** (Option 1 recommended for easiest implementation)
2. **Test Locally** - Visit `calendly-widget.html` to see all options
3. **Update index.html** - Replace current form with chosen integration
4. **Test Booking Flow** - Make a test booking to verify everything works
5. **Deploy** - Deploy server and updated frontend to production

---

## Contact

For questions or issues with this integration, contact the development team.

**Account**: Perry Bailes (perry.bailes@gmail.com)
**Scheduling URL**: https://calendly.com/perry-bailes
