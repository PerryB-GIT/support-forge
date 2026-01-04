/**
 * Calendly API Test Script
 *
 * This script tests the Calendly API integration to verify everything is working correctly.
 * Run: node test-calendly.js
 */

require('dotenv').config();
const calendly = require('./calendly');

async function testCalendlyIntegration() {
    console.log('\n=================================');
    console.log('Calendly API Integration Test');
    console.log('=================================\n');

    // Check API key
    if (!process.env.CALENDLY_API_KEY) {
        console.error('❌ CALENDLY_API_KEY not set in .env file');
        process.exit(1);
    }
    console.log('✓ API Key configured');

    try {
        // Test 1: Get User Info
        console.log('\n--- Test 1: Get User Info ---');
        const userInfo = await calendly.getUserInfo();
        console.log('✓ User Info Retrieved:');
        console.log(`  Name: ${userInfo.name}`);
        console.log(`  Email: ${userInfo.email}`);
        console.log(`  Scheduling URL: ${userInfo.scheduling_url}`);
        console.log(`  Time Zone: ${userInfo.timezone}`);

        // Test 2: Get Event Types
        console.log('\n--- Test 2: Get Event Types ---');
        const eventTypes = await calendly.getEventTypes();
        console.log(`✓ Found ${eventTypes.length} event type(s):`);
        eventTypes.forEach((et, index) => {
            console.log(`\n  Event ${index + 1}:`);
            console.log(`    Name: ${et.name}`);
            console.log(`    Duration: ${et.duration} minutes`);
            console.log(`    Slug: ${et.slug}`);
            console.log(`    Active: ${et.active}`);
            console.log(`    Scheduling URL: ${et.scheduling_url}`);
            console.log(`    URI: ${et.uri}`);
        });

        // Test 3: Get Availability (if event types exist)
        if (eventTypes.length > 0) {
            const firstEventType = eventTypes[0];
            console.log(`\n--- Test 3: Get Availability for "${firstEventType.name}" ---`);

            const now = new Date();
            const twoWeeksLater = new Date(now.getTime() + 14 * 24 * 60 * 60 * 1000);

            try {
                const availability = await calendly.getAvailability(
                    firstEventType.uri,
                    now.toISOString(),
                    twoWeeksLater.toISOString()
                );

                console.log(`✓ Found ${availability.length} available slot(s) in next 2 weeks`);

                if (availability.length > 0) {
                    console.log('\n  Sample slots:');
                    availability.slice(0, 5).forEach((slot, index) => {
                        const date = new Date(slot.start_time);
                        console.log(`    ${index + 1}. ${date.toLocaleString('en-US', {
                            weekday: 'short',
                            month: 'short',
                            day: 'numeric',
                            hour: 'numeric',
                            minute: '2-digit',
                            hour12: true
                        })}`);
                    });

                    if (availability.length > 5) {
                        console.log(`    ... and ${availability.length - 5} more`);
                    }
                }
            } catch (error) {
                console.log(`⚠ Availability check failed: ${error.message}`);
                console.log('  (This might be normal if no slots are available)');
            }
        }

        // Test 4: Create Booking Link
        if (eventTypes.length > 0) {
            console.log('\n--- Test 4: Create Booking Link ---');
            const testBooking = await calendly.createScheduledEvent(
                eventTypes[0].uri,
                new Date().toISOString(),
                'test@example.com',
                'Test User',
                { phone: '(555) 123-4567' }
            );

            console.log('✓ Booking link generated:');
            console.log(`  URL: ${testBooking.booking_url}`);
            console.log(`  Event: ${testBooking.event_type}`);
            console.log(`  Invitee: ${testBooking.invitee_name} (${testBooking.invitee_email})`);
        }

        // Test 5: List Scheduled Events
        console.log('\n--- Test 5: List Scheduled Events ---');
        try {
            const now = new Date();
            const futureEvents = await calendly.listScheduledEvents({
                min_start_time: now.toISOString(),
                status: 'active',
                count: 10
            });

            console.log(`✓ Found ${futureEvents.length} upcoming event(s)`);

            if (futureEvents.length > 0) {
                console.log('\n  Upcoming events:');
                futureEvents.forEach((event, index) => {
                    const date = new Date(event.start_time);
                    console.log(`    ${index + 1}. ${event.name} - ${date.toLocaleString('en-US', {
                        weekday: 'short',
                        month: 'short',
                        day: 'numeric',
                        hour: 'numeric',
                        minute: '2-digit',
                        hour12: true
                    })}`);
                });
            }
        } catch (error) {
            console.log(`⚠ Could not list scheduled events: ${error.message}`);
        }

        console.log('\n=================================');
        console.log('✓ All tests completed successfully!');
        console.log('=================================\n');

        console.log('Next Steps:');
        console.log('1. Start the server: npm start');
        console.log('2. Test API endpoints: curl http://localhost:3000/api/health');
        console.log('3. View widget demo: http://localhost:3000/calendly-widget.html');
        console.log('4. Integrate into your website using the guide\n');

    } catch (error) {
        console.error('\n❌ Test failed:', error.message);
        console.error('\nError details:', error);
        process.exit(1);
    }
}

// Run tests
testCalendlyIntegration();
