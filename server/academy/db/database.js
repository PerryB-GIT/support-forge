import Database from 'better-sqlite3';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Database file location
const DB_PATH = process.env.ACADEMY_DB_PATH || path.join(__dirname, '..', '..', 'data', 'academy.db');

// Ensure data directory exists
const dataDir = path.dirname(DB_PATH);
if (!fs.existsSync(dataDir)) {
  fs.mkdirSync(dataDir, { recursive: true });
}

// Initialize database connection
const db = new Database(DB_PATH, {
  verbose: process.env.NODE_ENV === 'development' ? console.log : null
});

// Enable foreign keys and WAL mode for better performance
db.pragma('journal_mode = WAL');
db.pragma('foreign_keys = ON');

/**
 * Run all pending migrations
 */
export function runMigrations() {
  const migrationsDir = path.join(__dirname, 'migrations');

  // Create migrations tracking table if it doesn't exist
  db.exec(`
    CREATE TABLE IF NOT EXISTS _migrations (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT UNIQUE NOT NULL,
      applied_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
  `);

  // Get list of applied migrations
  const appliedMigrations = db.prepare('SELECT name FROM _migrations').all().map(m => m.name);

  // Get all migration files
  const migrationFiles = fs.readdirSync(migrationsDir)
    .filter(f => f.endsWith('.sql'))
    .sort();

  // Run pending migrations
  for (const file of migrationFiles) {
    if (!appliedMigrations.includes(file)) {
      console.log(`Running migration: ${file}`);
      const sql = fs.readFileSync(path.join(migrationsDir, file), 'utf-8');

      db.transaction(() => {
        db.exec(sql);
        db.prepare('INSERT INTO _migrations (name) VALUES (?)').run(file);
      })();

      console.log(`Migration applied: ${file}`);
    }
  }
}

/**
 * Initialize the database (run migrations)
 */
export function initializeDatabase() {
  try {
    runMigrations();
    console.log('Academy database initialized successfully');
  } catch (error) {
    console.error('Failed to initialize academy database:', error);
    throw error;
  }
}

/**
 * Close database connection (for graceful shutdown)
 */
export function closeDatabase() {
  db.close();
}

// Export the database instance
export default db;
