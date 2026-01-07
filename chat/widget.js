// Support Forge AI Chat Widget
(function() {
  'use strict';

  // Configuration
  const CONFIG = {
    apiEndpoint: '/api/chat',
    botName: 'Support Forge AI',
    placeholder: 'Ask me anything about IT & AI...',
    welcomeMessage: "Hi! I'm the Support Forge AI assistant. How can I help you today?",
  };

  // State
  let isOpen = false;
  let isLoading = false;
  let messages = [];

  // Create widget HTML
  function createWidget() {
    const widget = document.createElement('div');
    widget.id = 'sf-chat-widget';
    widget.innerHTML = `
      <style>
        #sf-chat-widget {
          --sf-copper: #c97c4b;
          --sf-copper-light: #e8a87c;
          --sf-dark: #0a0a0f;
          --sf-surface: #141419;
          --sf-border: #2a2a35;
          --sf-text: #f9fafb;
          --sf-text-muted: #9ca3af;
          font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        #sf-chat-button {
          position: fixed;
          bottom: 24px;
          right: 24px;
          width: 60px;
          height: 60px;
          border-radius: 50%;
          background: linear-gradient(135deg, var(--sf-copper), var(--sf-copper-light));
          border: none;
          cursor: pointer;
          box-shadow: 0 4px 20px rgba(201, 124, 75, 0.4);
          z-index: 9998;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: transform 0.2s, box-shadow 0.2s;
        }

        #sf-chat-button:hover {
          transform: scale(1.05);
          box-shadow: 0 6px 24px rgba(201, 124, 75, 0.5);
        }

        #sf-chat-button svg {
          width: 28px;
          height: 28px;
          fill: white;
        }

        #sf-chat-button .close-icon {
          display: none;
        }

        #sf-chat-button.open .chat-icon {
          display: none;
        }

        #sf-chat-button.open .close-icon {
          display: block;
        }

        #sf-chat-container {
          position: fixed;
          bottom: 100px;
          right: 24px;
          width: 380px;
          height: 520px;
          background: var(--sf-dark);
          border: 1px solid var(--sf-border);
          border-radius: 16px;
          box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
          z-index: 9999;
          display: none;
          flex-direction: column;
          overflow: hidden;
        }

        #sf-chat-container.open {
          display: flex;
          animation: slideUp 0.3s ease;
        }

        @keyframes slideUp {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        #sf-chat-header {
          padding: 16px 20px;
          background: var(--sf-surface);
          border-bottom: 1px solid var(--sf-border);
          display: flex;
          align-items: center;
          gap: 12px;
        }

        #sf-chat-header-icon {
          width: 40px;
          height: 40px;
          border-radius: 10px;
          background: linear-gradient(135deg, var(--sf-copper), var(--sf-copper-light));
          display: flex;
          align-items: center;
          justify-content: center;
        }

        #sf-chat-header-icon svg {
          width: 20px;
          height: 20px;
          fill: white;
        }

        #sf-chat-header-info h3 {
          margin: 0;
          font-size: 15px;
          font-weight: 600;
          color: var(--sf-text);
        }

        #sf-chat-header-info p {
          margin: 2px 0 0;
          font-size: 12px;
          color: var(--sf-text-muted);
        }

        #sf-chat-messages {
          flex: 1;
          overflow-y: auto;
          padding: 16px;
          display: flex;
          flex-direction: column;
          gap: 12px;
        }

        #sf-chat-messages::-webkit-scrollbar {
          width: 6px;
        }

        #sf-chat-messages::-webkit-scrollbar-thumb {
          background: var(--sf-border);
          border-radius: 3px;
        }

        .sf-message {
          max-width: 85%;
          padding: 12px 16px;
          border-radius: 16px;
          font-size: 14px;
          line-height: 1.5;
          word-wrap: break-word;
        }

        .sf-message.user {
          align-self: flex-end;
          background: var(--sf-copper);
          color: white;
          border-bottom-right-radius: 4px;
        }

        .sf-message.assistant {
          align-self: flex-start;
          background: var(--sf-surface);
          color: var(--sf-text);
          border: 1px solid var(--sf-border);
          border-bottom-left-radius: 4px;
        }

        .sf-message.assistant p {
          margin: 0 0 8px 0;
        }

        .sf-message.assistant p:last-child {
          margin-bottom: 0;
        }

        .sf-typing {
          display: flex;
          gap: 4px;
          padding: 12px 16px;
          background: var(--sf-surface);
          border: 1px solid var(--sf-border);
          border-radius: 16px;
          border-bottom-left-radius: 4px;
          align-self: flex-start;
        }

        .sf-typing span {
          width: 8px;
          height: 8px;
          background: var(--sf-text-muted);
          border-radius: 50%;
          animation: bounce 1.4s infinite;
        }

        .sf-typing span:nth-child(2) {
          animation-delay: 0.2s;
        }

        .sf-typing span:nth-child(3) {
          animation-delay: 0.4s;
        }

        @keyframes bounce {
          0%, 60%, 100% {
            transform: translateY(0);
          }
          30% {
            transform: translateY(-4px);
          }
        }

        #sf-chat-input-container {
          padding: 12px 16px;
          background: var(--sf-surface);
          border-top: 1px solid var(--sf-border);
        }

        #sf-chat-input-wrapper {
          display: flex;
          gap: 8px;
          align-items: flex-end;
        }

        #sf-chat-input {
          flex: 1;
          background: var(--sf-dark);
          border: 1px solid var(--sf-border);
          border-radius: 12px;
          padding: 12px 16px;
          color: var(--sf-text);
          font-size: 14px;
          resize: none;
          min-height: 44px;
          max-height: 120px;
          line-height: 1.4;
        }

        #sf-chat-input::placeholder {
          color: var(--sf-text-muted);
        }

        #sf-chat-input:focus {
          outline: none;
          border-color: var(--sf-copper);
        }

        #sf-chat-send {
          width: 44px;
          height: 44px;
          border-radius: 12px;
          background: var(--sf-copper);
          border: none;
          cursor: pointer;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: background 0.2s;
          flex-shrink: 0;
        }

        #sf-chat-send:hover {
          background: var(--sf-copper-light);
        }

        #sf-chat-send:disabled {
          opacity: 0.5;
          cursor: not-allowed;
        }

        #sf-chat-send svg {
          width: 20px;
          height: 20px;
          fill: white;
        }

        @media (max-width: 480px) {
          #sf-chat-container {
            width: calc(100% - 32px);
            height: calc(100% - 140px);
            right: 16px;
            bottom: 90px;
            border-radius: 12px;
          }

          #sf-chat-button {
            right: 16px;
            bottom: 16px;
          }
        }
      </style>

      <button id="sf-chat-button" aria-label="Open chat">
        <svg class="chat-icon" viewBox="0 0 24 24">
          <path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H6l-2 2V4h16v12z"/>
        </svg>
        <svg class="close-icon" viewBox="0 0 24 24">
          <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
        </svg>
      </button>

      <div id="sf-chat-container">
        <div id="sf-chat-header">
          <div id="sf-chat-header-icon">
            <svg viewBox="0 0 24 24">
              <path d="M12 2L2 7v10l10 5 10-5V7L12 2zm0 2.5L19 8l-7 3.5L5 8l7-3.5zM4 9.5l7 3.5v6.5l-7-3.5V9.5zm9 10v-6.5l7-3.5v6.5l-7 3.5z"/>
            </svg>
          </div>
          <div id="sf-chat-header-info">
            <h3>${CONFIG.botName}</h3>
            <p>Powered by Claude AI</p>
          </div>
        </div>
        <div id="sf-chat-messages"></div>
        <div id="sf-chat-input-container">
          <div id="sf-chat-input-wrapper">
            <textarea id="sf-chat-input" placeholder="${CONFIG.placeholder}" rows="1"></textarea>
            <button id="sf-chat-send" aria-label="Send message">
              <svg viewBox="0 0 24 24">
                <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
              </svg>
            </button>
          </div>
        </div>
      </div>
    `;

    document.body.appendChild(widget);
    initializeWidget();
  }

  function initializeWidget() {
    const button = document.getElementById('sf-chat-button');
    const container = document.getElementById('sf-chat-container');
    const messagesContainer = document.getElementById('sf-chat-messages');
    const input = document.getElementById('sf-chat-input');
    const sendButton = document.getElementById('sf-chat-send');

    // Toggle chat
    button.addEventListener('click', () => {
      isOpen = !isOpen;
      button.classList.toggle('open', isOpen);
      container.classList.toggle('open', isOpen);

      if (isOpen && messages.length === 0) {
        addMessage('assistant', CONFIG.welcomeMessage);
      }

      if (isOpen) {
        setTimeout(() => input.focus(), 100);
      }
    });

    // Auto-resize textarea
    input.addEventListener('input', () => {
      input.style.height = 'auto';
      input.style.height = Math.min(input.scrollHeight, 120) + 'px';
    });

    // Send on Enter (Shift+Enter for new line)
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
      }
    });

    // Send button click
    sendButton.addEventListener('click', sendMessage);
  }

  function addMessage(role, content) {
    messages.push({ role, content });
    renderMessages();
  }

  function renderMessages() {
    const container = document.getElementById('sf-chat-messages');
    container.innerHTML = messages.map(msg => `
      <div class="sf-message ${msg.role}">
        ${msg.role === 'assistant' ? formatMessage(msg.content) : escapeHtml(msg.content)}
      </div>
    `).join('');

    if (isLoading) {
      container.innerHTML += `
        <div class="sf-typing">
          <span></span>
          <span></span>
          <span></span>
        </div>
      `;
    }

    container.scrollTop = container.scrollHeight;
  }

  function formatMessage(content) {
    return content.split('\n').map(line =>
      line.trim() ? `<p>${escapeHtml(line)}</p>` : ''
    ).join('');
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  async function sendMessage() {
    const input = document.getElementById('sf-chat-input');
    const sendButton = document.getElementById('sf-chat-send');
    const content = input.value.trim();

    if (!content || isLoading) return;

    // Add user message
    addMessage('user', content);
    input.value = '';
    input.style.height = 'auto';

    // Show loading
    isLoading = true;
    sendButton.disabled = true;
    renderMessages();

    try {
      const response = await fetch(CONFIG.apiEndpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          messages: messages.filter(m => m.role !== 'system').map(m => ({
            role: m.role,
            content: m.content
          }))
        })
      });

      if (!response.ok) throw new Error('Failed to get response');

      // Handle streaming response
      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let assistantMessage = '';

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        const lines = chunk.split('\n');

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = line.slice(6);
            if (data === '[DONE]') continue;

            try {
              const parsed = JSON.parse(data);
              if (parsed.content) {
                assistantMessage += parsed.content;
                // Update the last message or add new one
                if (messages[messages.length - 1]?.role === 'assistant') {
                  messages[messages.length - 1].content = assistantMessage;
                } else {
                  messages.push({ role: 'assistant', content: assistantMessage });
                }
                isLoading = false;
                renderMessages();
              }
            } catch (e) {
              // Ignore parse errors
            }
          }
        }
      }

    } catch (error) {
      console.error('Chat error:', error);
      addMessage('assistant', "I apologize, but I'm having trouble connecting right now. Please try again or contact us directly at support@support-forge.com");
    } finally {
      isLoading = false;
      sendButton.disabled = false;
      renderMessages();
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createWidget);
  } else {
    createWidget();
  }
})();
