import express from 'express';
import { initializeDatabase } from './db/database.js';

// Route imports
import authRoutes from './routes/auth.js';
import courseRoutes from './routes/courses.js';
import progressRoutes from './routes/progress.js';

const router = express.Router();

/**
 * Initialize the Academy module
 * - Sets up database and runs migrations
 * - Mounts all routes
 */
export function initializeAcademy(app) {
  // Initialize database
  initializeDatabase();

  // Mount academy routes under /api
  app.use('/api/auth', authRoutes);
  app.use('/api/courses', courseRoutes);
  app.use('/api/progress', progressRoutes);

  console.log('Academy module initialized');
  console.log('  Routes mounted:');
  console.log('    - /api/auth (register, login, me, refresh, logout, password)');
  console.log('    - /api/courses (list, detail, modules, lessons, enroll)');
  console.log('    - /api/progress (get, update, complete)');
}

// Also export a router for alternative mounting
router.use('/auth', authRoutes);
router.use('/courses', courseRoutes);
router.use('/progress', progressRoutes);

export { router as academyRouter };
export default { initializeAcademy, academyRouter: router };
