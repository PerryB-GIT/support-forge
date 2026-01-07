FROM node:20-alpine

WORKDIR /app

# Install build dependencies for better-sqlite3
RUN apk add --no-cache python3 make g++

# Copy package files
COPY server/package*.json ./server/

# Install dependencies
WORKDIR /app/server
RUN npm install --production

# Copy server code
WORKDIR /app
COPY server/ ./server/

# Copy static frontend files
COPY *.html ./
COPY *.css ./
COPY *.js ./
COPY academy/ ./academy/
COPY assets/ ./assets/ 2>/dev/null || true
COPY images/ ./images/ 2>/dev/null || true

# Create data directory for SQLite
RUN mkdir -p /app/server/data

# Expose port
EXPOSE 3000

# Set working directory to server
WORKDIR /app/server

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/api/health || exit 1

# Start server
CMD ["node", "index.js"]
