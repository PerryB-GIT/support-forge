/**
 * Calendly API Integration Module
 * Handles interactions with Calendly API for scheduling
 */

const CALENDLY_API_BASE = 'https://api.calendly.com';

/**
 * Get API headers with authorization
 */
function getHeaders() {
  const apiKey = process.env.CALENDLY_API_KEY;
  if (!apiKey) {
    throw new Error('CALENDLY_API_KEY environment variable is not set');
  }
  return {
    'Authorization': `Bearer ${apiKey}`,
    'Content-Type': 'application/json'
  };
}

/**
 * Get current user information
 */
export async function getCurrentUser() {
  const response = await fetch(`${CALENDLY_API_BASE}/users/me`, {
    headers: getHeaders()
  });

  if (!response.ok) {
    throw new Error(`Calendly API error: ${response.status}`);
  }

  const data = await response.json();
  return data.resource;
}

/**
 * List available event types for scheduling
 */
export async function getEventTypes(userUri = null) {
  const user = userUri || process.env.CALENDLY_USER_URI;
  if (!user) {
    throw new Error('User URI required - set CALENDLY_USER_URI or pass userUri');
  }

  const params = new URLSearchParams({ user, active: 'true' });
  const response = await fetch(`${CALENDLY_API_BASE}/event_types?${params}`, {
    headers: getHeaders()
  });

  if (!response.ok) {
    throw new Error(`Calendly API error: ${response.status}`);
  }

  const data = await response.json();
  return data.collection.map(event => ({
    uri: event.uri,
    name: event.name,
    slug: event.slug,
    duration: event.duration,
    description: event.description_plain,
    schedulingUrl: event.scheduling_url,
    active: event.active
  }));
}

/**
 * Get available time slots for an event type
 */
export async function getAvailability(eventTypeUri, startTime, endTime) {
  if (!eventTypeUri) {
    throw new Error('Event type URI is required');
  }

  const start = startTime || new Date().toISOString();
  const end = endTime || new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString();

  const params = new URLSearchParams({
    event_type: eventTypeUri,
    start_time: start,
    end_time: end
  });

  const response = await fetch(`${CALENDLY_API_BASE}/event_type_available_times?${params}`, {
    headers: getHeaders()
  });

  if (!response.ok) {
    throw new Error(`Calendly API error: ${response.status}`);
  }

  const data = await response.json();
  return data.collection.map(slot => ({
    startTime: slot.start_time,
    status: slot.status,
    inviteesRemaining: slot.invitees_remaining
  }));
}

/**
 * Generate a booking link for an event type
 */
export async function getBookingLink(eventTypeUri, prefill = {}) {
  const response = await fetch(eventTypeUri, {
    headers: getHeaders()
  });

  if (!response.ok) {
    throw new Error(`Calendly API error: ${response.status}`);
  }

  const data = await response.json();
  const baseUrl = data.resource.scheduling_url;

  const params = new URLSearchParams();
  if (prefill.name) params.append('name', prefill.name);
  if (prefill.email) params.append('email', prefill.email);

  const queryString = params.toString();
  return queryString ? `${baseUrl}?${queryString}` : baseUrl;
}

export default {
  getCurrentUser,
  getEventTypes,
  getAvailability,
  getBookingLink
};
