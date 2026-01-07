/**
 * Database Seed Script for AI Launchpad Academy
 *
 * Imports course content from parsed script JSON files and seeds the database
 *
 * Run with: node server/academy/db/seed.js
 */

import Database from 'better-sqlite3';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Paths
const DB_PATH = process.env.ACADEMY_DB_PATH || path.join(__dirname, '..', '..', 'data', 'academy.db');
const SCRIPTS_DIR = path.join(__dirname, '..', '..', 'scripts', 'output', 'parsed-scripts');
const SUMMARY_FILE = path.join(SCRIPTS_DIR, '_summary.json');

// Ensure data directory exists
const dataDir = path.dirname(DB_PATH);
if (!fs.existsSync(dataDir)) {
  fs.mkdirSync(dataDir, { recursive: true });
}

// Initialize database
const db = new Database(DB_PATH);
db.pragma('journal_mode = WAL');
db.pragma('foreign_keys = ON');

// Course configuration
const COURSE_CONFIG = {
  slug: 'ai-launchpad-academy',
  title: 'AI Launchpad Academy',
  description: 'Master AI automation with Claude Code, MCP servers, and enterprise deployment strategies.',
  price_cents: 99700, // $997.00
  is_published: 1
};

// Module definitions
const MODULES = [
  { number: 0, title: 'Welcome & Setup', description: 'Get started with the course and prepare your learning environment.' },
  { number: 1, title: 'Foundations', description: 'Build your AI readiness and set up essential accounts.' },
  { number: 2, title: 'Claude Code Mastery', description: 'Master Claude Code from installation to advanced features.' },
  { number: 3, title: 'MCP Deep Dive', description: 'Connect Claude to external services with MCP servers.' },
  { number: 4, title: 'Skills & Plugins', description: 'Extend Claude with skills and plugins for specialized tasks.' },
  { number: 5, title: 'Automation Engines', description: 'Build powerful automations with n8n and Zapier.' },
  { number: 6, title: 'Cloud Deployment', description: 'Deploy AI workloads to AWS and Google Cloud.' },
  { number: 7, title: 'Security & Best Practices', description: 'Secure your automations and follow responsible AI principles.' },
  { number: 8, title: 'Capstone Projects', description: 'Build complete agent workflows from start to finish.' }
];

// Completed videos with their S3 locations
const COMPLETED_VIDEOS = [
  { lessonId: '7.1-credential-security', part: 1, filename: '7.1-credential-security-part1.mp4' },
  { lessonId: '7.1-credential-security', part: 2, filename: '7.1-credential-security-part2.mp4' },
  { lessonId: '7.1-credential-security', part: 3, filename: '7.1-credential-security-part3.mp4' },
  { lessonId: '7.1-credential-security', part: 4, filename: '7.1-credential-security-part4.mp4' },
  { lessonId: '8.1-capstone-project-overview', part: 1, filename: '8.1-capstone-overview.mp4' },
  { lessonId: '8.2-building-client-onboarding-agent', part: 1, filename: '8.2-onboarding-part1.mp4' },
  { lessonId: '8.2-building-client-onboarding-agent', part: 2, filename: '8.2-onboarding-part2.mp4' }
];

/**
 * Parse module number from script_id
 * Examples:
 *   "5.1-automation-strategy" -> 5
 *   "script-0.1-welcome" -> 0
 *   "script-2.3-prompting-business-tasks" -> 2
 */
function parseModuleNumber(scriptId) {
  // Handle "script-X.Y-name" format
  const scriptMatch = scriptId.match(/^script-(\d+)\.\d+-/);
  if (scriptMatch) {
    return parseInt(scriptMatch[1], 10);
  }

  // Handle "X.Y-name" format
  const directMatch = scriptId.match(/^(\d+)\.\d+-/);
  if (directMatch) {
    return parseInt(directMatch[1], 10);
  }

  console.warn(`Could not parse module number from script_id: ${scriptId}`);
  return null;
}

/**
 * Parse lesson number from script_id for sort order
 */
function parseLessonNumber(scriptId) {
  const scriptMatch = scriptId.match(/script-\d+\.(\d+)-/);
  if (scriptMatch) {
    return parseInt(scriptMatch[1], 10);
  }

  const directMatch = scriptId.match(/^\d+\.(\d+)-/);
  if (directMatch) {
    return parseInt(directMatch[1], 10);
  }

  return 1;
}

/**
 * Run migrations from the migrations folder
 */
function runMigrations() {
  const migrationsDir = path.join(__dirname, 'migrations');

  // Create migrations tracking table
  db.exec(`
    CREATE TABLE IF NOT EXISTS _migrations (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT UNIQUE NOT NULL,
      applied_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
  `);

  const appliedMigrations = db.prepare('SELECT name FROM _migrations').all().map(m => m.name);

  const migrationFiles = fs.readdirSync(migrationsDir)
    .filter(f => f.endsWith('.sql'))
    .sort();

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
 * Seed the database with course content
 */
function seedDatabase() {
  console.log('\n=== AI Launchpad Academy Database Seeder ===\n');

  // Run migrations first
  console.log('Running migrations...');
  runMigrations();
  console.log('Migrations complete.\n');

  // Read summary file
  if (!fs.existsSync(SUMMARY_FILE)) {
    console.error(`Summary file not found: ${SUMMARY_FILE}`);
    process.exit(1);
  }

  const summary = JSON.parse(fs.readFileSync(SUMMARY_FILE, 'utf-8'));
  console.log(`Found ${summary.total_scripts} scripts totaling ${Math.round(summary.total_duration_minutes)} minutes\n`);

  // Begin transaction for seeding
  const seedTransaction = db.transaction(() => {
    // Clear existing data (in reverse dependency order)
    console.log('Clearing existing data...');
    db.exec('DELETE FROM lesson_progress');
    db.exec('DELETE FROM video_parts');
    db.exec('DELETE FROM lessons');
    db.exec('DELETE FROM modules');
    db.exec('DELETE FROM enrollments');
    db.exec('DELETE FROM courses');

    // Insert course
    console.log('Creating course...');
    const insertCourse = db.prepare(`
      INSERT INTO courses (slug, title, description, price_cents, is_published)
      VALUES (@slug, @title, @description, @price_cents, @is_published)
    `);
    const courseResult = insertCourse.run(COURSE_CONFIG);
    const courseId = courseResult.lastInsertRowid;
    console.log(`Created course: ${COURSE_CONFIG.title} (ID: ${courseId})`);

    // Insert modules
    console.log('\nCreating modules...');
    const insertModule = db.prepare(`
      INSERT INTO modules (course_id, module_number, title, description, sort_order)
      VALUES (@course_id, @module_number, @title, @description, @sort_order)
    `);

    const moduleIds = {};
    for (const mod of MODULES) {
      const result = insertModule.run({
        course_id: courseId,
        module_number: mod.number,
        title: mod.title,
        description: mod.description,
        sort_order: mod.number
      });
      moduleIds[mod.number] = result.lastInsertRowid;
      console.log(`  Module ${mod.number}: ${mod.title} (ID: ${result.lastInsertRowid})`);
    }

    // Insert lessons from scripts
    console.log('\nCreating lessons...');
    const insertLesson = db.prepare(`
      INSERT INTO lessons (module_id, script_id, title, description, duration_seconds, segment_count, sort_order, is_free_preview)
      VALUES (@module_id, @script_id, @title, @description, @duration_seconds, @segment_count, @sort_order, @is_free_preview)
    `);

    const lessonIds = {};
    let lessonCount = 0;

    for (const scriptInfo of summary.scripts) {
      const moduleNumber = parseModuleNumber(scriptInfo.script_id);

      if (moduleNumber === null || moduleIds[moduleNumber] === undefined) {
        console.warn(`  Skipping ${scriptInfo.script_id}: cannot determine module`);
        continue;
      }

      const lessonNumber = parseLessonNumber(scriptInfo.script_id);

      // First lesson of module 0 is free preview
      const isFreePreview = moduleNumber === 0 && lessonNumber === 1 ? 1 : 0;

      const result = insertLesson.run({
        module_id: moduleIds[moduleNumber],
        script_id: scriptInfo.script_id,
        title: scriptInfo.title,
        description: null, // Could extract from first segment later
        duration_seconds: scriptInfo.duration_seconds,
        segment_count: scriptInfo.segments,
        sort_order: lessonNumber,
        is_free_preview: isFreePreview
      });

      lessonIds[scriptInfo.script_id] = result.lastInsertRowid;
      lessonCount++;
      console.log(`  Lesson ${moduleNumber}.${lessonNumber}: ${scriptInfo.title} (${Math.round(scriptInfo.duration_seconds)}s)`);
    }

    console.log(`\nCreated ${lessonCount} lessons total`);

    // Insert video parts for completed videos
    console.log('\nCreating video parts...');
    const insertVideoPart = db.prepare(`
      INSERT INTO video_parts (lesson_id, part_number, s3_key, filename, duration_seconds, status)
      VALUES (@lesson_id, @part_number, @s3_key, @filename, @duration_seconds, @status)
    `);

    let videoCount = 0;
    for (const video of COMPLETED_VIDEOS) {
      const lessonId = lessonIds[video.lessonId];

      if (!lessonId) {
        console.warn(`  Skipping ${video.filename}: lesson ${video.lessonId} not found`);
        continue;
      }

      // Extract module number for S3 path
      const moduleNumber = parseModuleNumber(video.lessonId);
      const s3Key = `videos/module-${moduleNumber}/${video.filename}`;

      insertVideoPart.run({
        lesson_id: lessonId,
        part_number: video.part,
        s3_key: s3Key,
        filename: video.filename,
        duration_seconds: null, // Would need to extract from video metadata
        status: 'ready'
      });

      videoCount++;
      console.log(`  Video: ${video.filename} -> ${s3Key}`);
    }

    console.log(`\nCreated ${videoCount} video parts (status: ready)`);

    // Create pending video parts for lessons without videos
    console.log('\nCreating pending video placeholders...');
    let pendingCount = 0;

    for (const [scriptId, lessonId] of Object.entries(lessonIds)) {
      // Check if this lesson already has videos
      const existingParts = db.prepare('SELECT COUNT(*) as count FROM video_parts WHERE lesson_id = ?').get(lessonId);

      if (existingParts.count === 0) {
        // Create a pending placeholder
        const moduleNumber = parseModuleNumber(scriptId);
        const lessonNumber = parseLessonNumber(scriptId);
        const filename = `${moduleNumber}.${lessonNumber}-${scriptId.replace(/^(script-)?\d+\.\d+-/, '')}.mp4`;
        const s3Key = `videos/module-${moduleNumber}/${filename}`;

        insertVideoPart.run({
          lesson_id: lessonId,
          part_number: 1,
          s3_key: s3Key,
          filename: filename,
          duration_seconds: null,
          status: 'pending'
        });

        pendingCount++;
      }
    }

    console.log(`Created ${pendingCount} pending video placeholders`);
  });

  // Execute the transaction
  seedTransaction();

  // Print summary
  console.log('\n=== Seed Complete ===');

  const stats = {
    courses: db.prepare('SELECT COUNT(*) as count FROM courses').get().count,
    modules: db.prepare('SELECT COUNT(*) as count FROM modules').get().count,
    lessons: db.prepare('SELECT COUNT(*) as count FROM lessons').get().count,
    videoParts: db.prepare('SELECT COUNT(*) as count FROM video_parts').get().count,
    readyVideos: db.prepare("SELECT COUNT(*) as count FROM video_parts WHERE status = 'ready'").get().count,
    pendingVideos: db.prepare("SELECT COUNT(*) as count FROM video_parts WHERE status = 'pending'").get().count
  };

  console.log('\nDatabase Statistics:');
  console.log(`  Courses: ${stats.courses}`);
  console.log(`  Modules: ${stats.modules}`);
  console.log(`  Lessons: ${stats.lessons}`);
  console.log(`  Video Parts: ${stats.videoParts}`);
  console.log(`    - Ready: ${stats.readyVideos}`);
  console.log(`    - Pending: ${stats.pendingVideos}`);

  console.log(`\nDatabase saved to: ${DB_PATH}`);
}

// Run the seeder
try {
  seedDatabase();
  db.close();
  process.exit(0);
} catch (error) {
  console.error('Seed failed:', error);
  db.close();
  process.exit(1);
}
