// Support Forge Chat API Server
const express = require('express');
const Anthropic = require('@anthropic-ai/sdk').default;
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.CHAT_PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());

// Rate limiting (simple in-memory)
const rateLimit = new Map();
const RATE_LIMIT_WINDOW = 60000; // 1 minute
const RATE_LIMIT_MAX = 10; // max requests per window

function checkRateLimit(ip) {
  const now = Date.now();
  const record = rateLimit.get(ip);

  if (!record || now - record.timestamp > RATE_LIMIT_WINDOW) {
    rateLimit.set(ip, { timestamp: now, count: 1 });
    return true;
  }

  if (record.count >= RATE_LIMIT_MAX) {
    return false;
  }

  record.count++;
  return true;
}

// System prompt
const SYSTEM_PROMPT = `You are the Support Forge AI Assistant, a helpful and knowledgeable technical support agent for Support Forge, an AI & IT consulting company based in your area.

Your role is to:
- Answer technical questions about IT infrastructure, software, and technology
- Help troubleshoot common technical issues
- Provide guidance on best practices for IT and software development
- Assist with questions about Support Forge services
- Encourage visitors to book a consultation for complex needs

Guidelines:
- Be professional, friendly, and concise
- Provide accurate technical information
- Keep responses focused and under 200 words when possible
- If asked about pricing or specific project quotes, encourage them to book a free consultation
- For complex issues, suggest scheduling a consultation
- Don't make up information about Support Forge that isn't listed below

Support Forge Services:
- AI Integration & Automation: Implement AI solutions to streamline business processes
- IT Infrastructure Management: Network setup, cloud migration, security audits
- Software Development & Consulting: Custom applications, API development, system integration
- Technical Support & Training: Ongoing support, staff training, documentation
- Cloud Solutions: AWS, Azure, Google Cloud setup and optimization

To book a consultation, visitors can use the scheduling form on the website or email support@support-forge.com.

Remember: You're representing Support Forge, so maintain a helpful and professional tone that builds trust.`;

// Initialize Anthropic client
const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

// Chat endpoint
app.post('/api/chat', async (req, res) => {
  const clientIP = req.ip || req.connection.remoteAddress;

  // Check rate limit
  if (!checkRateLimit(clientIP)) {
    return res.status(429).json({
      error: 'Too many requests. Please wait a moment before trying again.'
    });
  }

  const { messages } = req.body;

  if (!messages || !Array.isArray(messages) || messages.length === 0) {
    return res.status(400).json({ error: 'Messages are required' });
  }

  // Validate messages
  const validMessages = messages.filter(m =>
    m.role && ['user', 'assistant'].includes(m.role) && m.content
  ).map(m => ({
    role: m.role,
    content: String(m.content).slice(0, 2000) // Limit message length
  }));

  if (validMessages.length === 0) {
    return res.status(400).json({ error: 'No valid messages provided' });
  }

  // Set up streaming response
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');

  try {
    const stream = await anthropic.messages.stream({
      model: 'claude-3-haiku-20240307', // Using Haiku for faster responses
      max_tokens: 1024,
      system: SYSTEM_PROMPT,
      messages: validMessages,
    });

    for await (const event of stream) {
      if (event.type === 'content_block_delta' && event.delta.type === 'text_delta') {
        res.write(`data: ${JSON.stringify({ content: event.delta.text })}\n\n`);
      }
    }

    res.write('data: [DONE]\n\n');
    res.end();

  } catch (error) {
    console.error('Chat error:', error);

    // If headers not sent yet, send error response
    if (!res.headersSent) {
      res.status(500).json({ error: 'Failed to process chat request' });
    } else {
      res.write(`data: ${JSON.stringify({ error: 'An error occurred' })}\n\n`);
      res.end();
    }
  }
});

// Health check
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', service: 'support-forge-chat' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Support Forge Chat API running on port ${PORT}`);
});
