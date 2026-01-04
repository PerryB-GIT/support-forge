/**
 * Calendly API Routes
 * Express router for Calendly integration endpoints
 */

import express from 'express';
import { getEventTypes, getAvailability, getBookingLink, getCurrentUser } from '../calendly.js';

const router = express.Router();

/**
 * GET /api/calendly/user
 * Get current Calendly user info
 */
router.get('/user', async (req, res) => {
  try {
    const user = await getCurrentUser();
    res.json({
      success: true,
      data: user
    });
  } catch (error) {
    console.error('Error fetching Calendly user:', error.message);
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

/**
 * GET /api/calendly/event-types
 * List available event types for scheduling
 */
router.get('/event-types', async (req, res) => {
  try {
    const eventTypes = await getEventTypes();
    res.json({
      success: true,
      data: eventTypes
    });
  } catch (error) {
    console.error('Error fetching event types:', error.message);
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

/**
 * GET /api/calendly/availability
 * Get available time slots for an event type
 * Query params: eventType, startTime, endTime
 */
router.get('/availability', async (req, res) => {
  try {
    const { eventType, startTime, endTime } = req.query;

    if (!eventType) {
      return res.status(400).json({
        success: false,
        error: 'eventType query parameter is required'
      });
    }

    const slots = await getAvailability(eventType, startTime, endTime);
    res.json({
      success: true,
      data: slots
    });
  } catch (error) {
    console.error('Error fetching availability:', error.message);
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

/**
 * POST /api/calendly/book
 * Generate a booking link (direct booking requires paid Calendly plan)
 * Body: { eventType, name, email }
 */
router.post('/book', async (req, res) => {
  try {
    const { eventType, name, email } = req.body;

    if (!eventType) {
      return res.status(400).json({
        success: false,
        error: 'eventType is required'
      });
    }

    const bookingUrl = await getBookingLink(eventType, { name, email });

    res.json({
      success: true,
      data: {
        bookingUrl,
        message: 'Use this URL to complete your booking'
      }
    });
  } catch (error) {
    console.error('Error generating booking link:', error.message);
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

export default router;
