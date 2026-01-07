/**
 * Client-Side Calendly API Integration Example
 *
 * This file demonstrates how to use the Calendly API endpoints from your frontend.
 * You can integrate these examples into your existing script.js or create a new
 * dedicated file for scheduling functionality.
 */

// ===== CONFIGURATION =====
const API_BASE_URL = 'http://localhost:3000/api/calendly';

// ===== API HELPER FUNCTIONS =====

/**
 * Fetch all available event types
 * @returns {Promise<Array>} Array of event types
 */
async function fetchEventTypes() {
    try {
        const response = await fetch(`${API_BASE_URL}/event-types`);
        const data = await response.json();

        if (data.success) {
            console.log('Event Types:', data.event_types);
            return data.event_types;
        } else {
            throw new Error(data.error);
        }
    } catch (error) {
        console.error('Error fetching event types:', error);
        throw error;
    }
}

/**
 * Fetch available time slots for a specific event type
 * @param {string} eventTypeUri - URI of the event type
 * @param {Date} startDate - Start date for availability search
 * @param {Date} endDate - End date for availability search
 * @returns {Promise<Array>} Array of available time slots
 */
async function fetchAvailability(eventTypeUri, startDate, endDate) {
    try {
        const params = new URLSearchParams({
            event_type_uri: eventTypeUri,
            start_time: startDate.toISOString(),
            end_time: endDate.toISOString()
        });

        const response = await fetch(`${API_BASE_URL}/availability?${params}`);
        const data = await response.json();

        if (data.success) {
            console.log('Available Slots:', data.available_slots);
            return data.available_slots;
        } else {
            throw new Error(data.error);
        }
    } catch (error) {
        console.error('Error fetching availability:', error);
        throw error;
    }
}

/**
 * Book a meeting (returns pre-filled Calendly link)
 * @param {object} bookingData - Booking information
 * @returns {Promise<object>} Booking response with URL
 */
async function bookMeeting(bookingData) {
    try {
        const response = await fetch(`${API_BASE_URL}/book`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(bookingData)
        });

        const data = await response.json();

        if (data.success) {
            console.log('Booking created:', data);
            return data;
        } else {
            throw new Error(data.error);
        }
    } catch (error) {
        console.error('Error booking meeting:', error);
        throw error;
    }
}

/**
 * Get Calendly user information
 * @returns {Promise<object>} User information
 */
async function fetchUserInfo() {
    try {
        const response = await fetch(`${API_BASE_URL}/user`);
        const data = await response.json();

        if (data.success) {
            console.log('User Info:', data.user);
            return data.user;
        } else {
            throw new Error(data.error);
        }
    } catch (error) {
        console.error('Error fetching user info:', error);
        throw error;
    }
}

// ===== EXAMPLE USAGE =====

/**
 * Example 1: Load and display event types in a dropdown
 */
async function loadEventTypesDropdown() {
    const eventTypes = await fetchEventTypes();
    const selectElement = document.getElementById('event-type-select');

    if (selectElement) {
        selectElement.innerHTML = '<option value="">Select a meeting type</option>';
        eventTypes.forEach(eventType => {
            if (eventType.active) {
                const option = document.createElement('option');
                option.value = eventType.uri;
                option.textContent = `${eventType.name} (${eventType.duration} min)`;
                selectElement.appendChild(option);
            }
        });
    }
}

/**
 * Example 2: Load available time slots for the next week
 */
async function loadAvailableTimeSlots(eventTypeUri) {
    const now = new Date();
    const nextWeek = new Date(now.getTime() + 7 * 24 * 60 * 60 * 1000);

    const slots = await fetchAvailability(eventTypeUri, now, nextWeek);

    // Group slots by day
    const slotsByDay = {};
    slots.forEach(slot => {
        const date = new Date(slot.start_time);
        const dayKey = date.toLocaleDateString('en-US', {
            weekday: 'long',
            month: 'long',
            day: 'numeric'
        });

        if (!slotsByDay[dayKey]) {
            slotsByDay[dayKey] = [];
        }

        slotsByDay[dayKey].push({
            time: date.toLocaleTimeString('en-US', {
                hour: 'numeric',
                minute: '2-digit',
                hour12: true
            }),
            iso: slot.start_time
        });
    });

    console.log('Slots by day:', slotsByDay);
    return slotsByDay;
}

/**
 * Example 3: Display available time slots in the UI
 */
async function displayTimeSlotsInUI(eventTypeUri) {
    const container = document.getElementById('time-slots-container');
    if (!container) return;

    // Show loading state
    container.innerHTML = '<p>Loading available times...</p>';

    try {
        const slotsByDay = await loadAvailableTimeSlots(eventTypeUri);

        // Clear loading state
        container.innerHTML = '';

        // Create UI for each day
        Object.entries(slotsByDay).forEach(([day, slots]) => {
            const daySection = document.createElement('div');
            daySection.className = 'day-section';

            const dayTitle = document.createElement('h3');
            dayTitle.textContent = day;
            daySection.appendChild(dayTitle);

            const slotsContainer = document.createElement('div');
            slotsContainer.className = 'time-slots';

            slots.forEach(slot => {
                const button = document.createElement('button');
                button.className = 'time-slot-button';
                button.textContent = slot.time;
                button.dataset.isoTime = slot.iso;
                button.onclick = () => selectTimeSlot(slot.iso);
                slotsContainer.appendChild(button);
            });

            daySection.appendChild(slotsContainer);
            container.appendChild(daySection);
        });

    } catch (error) {
        container.innerHTML = '<p>Error loading time slots. Please try again.</p>';
    }
}

/**
 * Example 4: Handle time slot selection
 */
function selectTimeSlot(isoTime) {
    // Store selected time
    const selectedTimeInput = document.getElementById('selected-time');
    if (selectedTimeInput) {
        selectedTimeInput.value = isoTime;
    }

    // Update UI to show selection
    document.querySelectorAll('.time-slot-button').forEach(btn => {
        btn.classList.remove('selected');
    });
    event.target.classList.add('selected');

    console.log('Selected time:', isoTime);
}

/**
 * Example 5: Complete booking flow
 */
async function completeBooking(formData) {
    try {
        const bookingData = {
            event_type_uri: formData.eventTypeUri,
            start_time: formData.selectedTime, // ISO 8601 format
            invitee_email: formData.email,
            invitee_name: formData.name,
            phone: formData.phone || undefined,
            notes: formData.notes || undefined
        };

        const result = await bookMeeting(bookingData);

        // Redirect to Calendly to complete booking
        window.location.href = result.booking_url;

    } catch (error) {
        alert('Failed to create booking. Please try again.');
    }
}

/**
 * Example 6: Enhanced schedule form handler with Calendly API
 */
function setupEnhancedScheduleForm() {
    const scheduleForm = document.getElementById('schedule-form');
    if (!scheduleForm) return;

    // Load event types on page load
    loadEventTypesDropdown();

    // Listen for event type selection
    const eventTypeSelect = document.getElementById('event-type-select');
    if (eventTypeSelect) {
        eventTypeSelect.addEventListener('change', (e) => {
            if (e.target.value) {
                displayTimeSlotsInUI(e.target.value);
            }
        });
    }

    // Handle form submission
    scheduleForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(scheduleForm);

        const bookingInfo = {
            eventTypeUri: formData.get('event_type_uri'),
            selectedTime: formData.get('selected_time'),
            name: formData.get('name'),
            email: formData.get('email'),
            phone: formData.get('phone'),
            notes: formData.get('notes')
        };

        await completeBooking(bookingInfo);
    });
}

/**
 * Example 7: Simple direct link integration (easiest option)
 */
function setupSimpleCalendlyButton() {
    const bookButton = document.getElementById('book-calendly-btn');
    if (bookButton) {
        bookButton.addEventListener('click', async () => {
            try {
                // Get user info to get scheduling URL
                const userInfo = await fetchUserInfo();

                // Redirect to Calendly
                window.open(userInfo.scheduling_url, '_blank');

            } catch (error) {
                alert('Unable to open scheduling link. Please try again.');
            }
        });
    }
}

/**
 * Example 8: Pre-fill form with user data
 */
function openCalendlyWithPrefill(name, email) {
    const calendlyUrl = new URL('https://calendly.com/perry-bailes');

    if (name) calendlyUrl.searchParams.set('name', name);
    if (email) calendlyUrl.searchParams.set('email', email);

    // Open in new window
    window.open(calendlyUrl.toString(), '_blank');
}

// ===== INITIALIZE ON PAGE LOAD =====

document.addEventListener('DOMContentLoaded', () => {
    // Choose one of the following initialization methods:

    // Option A: Enhanced form with API integration
    // setupEnhancedScheduleForm();

    // Option B: Simple button that opens Calendly
    // setupSimpleCalendlyButton();

    // Option C: Inline Calendly widget (see calendly-widget.html)
    // No JavaScript needed - just embed the widget

    console.log('Calendly integration ready');
});

// ===== EXPORT FOR MODULE USAGE =====

// If using ES6 modules, export the functions
// export {
//     fetchEventTypes,
//     fetchAvailability,
//     bookMeeting,
//     fetchUserInfo,
//     loadEventTypesDropdown,
//     loadAvailableTimeSlots,
//     completeBooking
// };
