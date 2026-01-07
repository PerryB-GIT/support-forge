/**
 * Quick Database Seed Script for AI Launchpad Academy
 * Seeds essential course content without external files
 */

import Database from 'better-sqlite3';
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const DB_PATH = process.env.ACADEMY_DB_PATH || path.join(__dirname, '..', '..', 'data', 'academy.db');

// Ensure data directory exists
const dataDir = path.dirname(DB_PATH);
if (!fs.existsSync(dataDir)) {
  fs.mkdirSync(dataDir, { recursive: true });
}

const db = new Database(DB_PATH);
db.pragma('journal_mode = WAL');
db.pragma('foreign_keys = ON');

// Course configuration
const COURSE = {
  slug: 'ai-launchpad-academy',
  title: 'AI Launchpad Academy',
  description: 'Master AI automation with Claude Code, MCP servers, and enterprise deployment strategies. Transform your workflow with cutting-edge AI tools.',
  price_cents: 99700
};

// Module definitions with lessons
const CONTENT = [
  {
    number: 0,
    title: 'Welcome & Setup',
    description: 'Get started with the course',
    lessons: [
      { id: '0.1-welcome', title: 'Welcome to AI Launchpad Academy', duration: 180 }
    ]
  },
  {
    number: 7,
    title: 'Security & Best Practices',
    description: 'Secure your automations and follow responsible AI principles',
    lessons: [
      { id: '7.1-credential-security', title: 'Credential Security Fundamentals', duration: 720, videos: [
        { part: 1, filename: '7.1-credential-security-part1.mp4', s3Key: 'videos/module-7/7.1-credential-security-part1.mp4' },
        { part: 2, filename: '7.1-credential-security-part2.mp4', s3Key: 'videos/module-7/7.1-credential-security-part2.mp4' },
        { part: 3, filename: '7.1-credential-security-part3.mp4', s3Key: 'videos/module-7/7.1-credential-security-part3.mp4' },
        { part: 4, filename: '7.1-credential-security-part4.mp4', s3Key: 'videos/module-7/7.1-credential-security-part4.mp4' }
      ]}
    ]
  },
  {
    number: 8,
    title: 'Capstone Projects',
    description: 'Build complete agent workflows from start to finish',
    lessons: [
      { id: '8.1-capstone-project-overview', title: 'Capstone Project Overview', duration: 480, videos: [
        { part: 1, filename: '8.1-capstone-overview.mp4', s3Key: 'videos/module-8/8.1-capstone-overview.mp4' }
      ]},
      { id: '8.2-building-client-onboarding-agent', title: 'Building a Client Onboarding Agent', duration: 720, videos: [
        { part: 1, filename: '8.2-onboarding-part1.mp4', s3Key: 'videos/module-8/8.2-onboarding-part1.mp4' },
        { part: 2, filename: '8.2-onboarding-part2.mp4', s3Key: 'videos/module-8/8.2-onboarding-part2.mp4' }
      ]}
    ]
  }
];

function runMigrations() {
  const migrationsDir = path.join(__dirname, 'migrations');

  db.exec(`
    CREATE TABLE IF NOT EXISTS _migrations (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT UNIQUE NOT NULL,
      applied_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
  `);

  const applied = db.prepare('SELECT name FROM _migrations').all().map(m => m.name);
  const files = fs.readdirSync(migrationsDir).filter(f => f.endsWith('.sql')).sort();

  for (const file of files) {
    if (!applied.includes(file)) {
      console.log(`Running migration: ${file}`);
      const sql = fs.readFileSync(path.join(migrationsDir, file), 'utf-8');
      db.transaction(() => {
        db.exec(sql);
        db.prepare('INSERT INTO _migrations (name) VALUES (?)').run(file);
      })();
    }
  }
}

function seedDatabase() {
  console.log('=== Quick Seed for AI Launchpad Academy ===\n');

  runMigrations();

  db.transaction(() => {
    // Clear existing data
    db.exec('DELETE FROM user_progress');
    db.exec('DELETE FROM video_parts');
    db.exec('DELETE FROM lessons');
    db.exec('DELETE FROM modules');
    db.exec('DELETE FROM enrollments');
    db.exec('DELETE FROM courses');

    // Insert course
    const courseResult = db.prepare(`
      INSERT INTO courses (slug, title, description, price_cents, is_published)
      VALUES (?, ?, ?, ?, 1)
    `).run(COURSE.slug, COURSE.title, COURSE.description, COURSE.price_cents);

    const courseId = courseResult.lastInsertRowid;
    console.log(`Course created: ${COURSE.title} (ID: ${courseId})`);

    // Insert modules and lessons
    for (const mod of CONTENT) {
      const modResult = db.prepare(`
        INSERT INTO modules (course_id, module_number, title, description, sort_order)
        VALUES (?, ?, ?, ?, ?)
      `).run(courseId, mod.number, mod.title, mod.description, mod.number);

      const moduleId = modResult.lastInsertRowid;
      console.log(`  Module ${mod.number}: ${mod.title}`);

      for (let i = 0; i < mod.lessons.length; i++) {
        const lesson = mod.lessons[i];
        const lessonResult = db.prepare(`
          INSERT INTO lessons (module_id, script_id, lesson_number, title, duration_seconds, sort_order, is_preview)
          VALUES (?, ?, ?, ?, ?, ?, ?)
        `).run(moduleId, lesson.id, i + 1, lesson.title, lesson.duration, i + 1, mod.number === 0 ? 1 : 0);

        const lessonId = lessonResult.lastInsertRowid;
        console.log(`    Lesson: ${lesson.title}`);

        // Insert videos if present
        if (lesson.videos) {
          for (const video of lesson.videos) {
            db.prepare(`
              INSERT INTO video_parts (lesson_id, part_number, s3_key, status)
              VALUES (?, ?, ?, 'ready')
            `).run(lessonId, video.part, video.s3Key);
            console.log(`      Video: ${video.filename}`);
          }
        }
      }
    }
  })();

  // Print summary
  const stats = {
    courses: db.prepare('SELECT COUNT(*) as c FROM courses').get().c,
    modules: db.prepare('SELECT COUNT(*) as c FROM modules').get().c,
    lessons: db.prepare('SELECT COUNT(*) as c FROM lessons').get().c,
    videos: db.prepare("SELECT COUNT(*) as c FROM video_parts WHERE status = 'ready'").get().c
  };

  console.log('\n=== Seed Complete ===');
  console.log(`Courses: ${stats.courses}`);
  console.log(`Modules: ${stats.modules}`);
  console.log(`Lessons: ${stats.lessons}`);
  console.log(`Ready Videos: ${stats.videos}`);
}

try {
  seedDatabase();
  db.close();
} catch (error) {
  console.error('Seed failed:', error);
  db.close();
  process.exit(1);
}
