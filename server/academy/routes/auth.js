import express from 'express';
import bcrypt from 'bcryptjs';
import db from '../db/database.js';
import { requireAuth, generateToken, generateRefreshToken } from '../middleware/auth.js';

const router = express.Router();

// Validation constants
const MIN_PASSWORD_LENGTH = 8;
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const BCRYPT_ROUNDS = 12;

/**
 * Validate email format
 */
function isValidEmail(email) {
  return EMAIL_REGEX.test(email);
}

/**
 * Validate password strength
 */
function isValidPassword(password) {
  if (password.length < MIN_PASSWORD_LENGTH) {
    return { valid: false, message: `Password must be at least ${MIN_PASSWORD_LENGTH} characters long` };
  }
  if (!/[A-Z]/.test(password)) {
    return { valid: false, message: 'Password must contain at least one uppercase letter' };
  }
  if (!/[a-z]/.test(password)) {
    return { valid: false, message: 'Password must contain at least one lowercase letter' };
  }
  if (!/[0-9]/.test(password)) {
    return { valid: false, message: 'Password must contain at least one number' };
  }
  return { valid: true };
}

/**
 * POST /api/auth/register
 * Create a new user account
 */
router.post('/register', async (req, res) => {
  try {
    const { email, password, name } = req.body;

    // Validate required fields
    if (!email || !password || !name) {
      return res.status(400).json({
        success: false,
        error: 'Email, password, and name are required'
      });
    }

    // Validate email format
    if (!isValidEmail(email)) {
      return res.status(400).json({
        success: false,
        error: 'Invalid email format'
      });
    }

    // Validate password strength
    const passwordValidation = isValidPassword(password);
    if (!passwordValidation.valid) {
      return res.status(400).json({
        success: false,
        error: passwordValidation.message
      });
    }

    // Validate name
    const trimmedName = name.trim();
    if (trimmedName.length < 2) {
      return res.status(400).json({
        success: false,
        error: 'Name must be at least 2 characters long'
      });
    }

    // Check if email already exists
    const existingUser = db.prepare('SELECT id FROM users WHERE email = ?').get(email.toLowerCase());
    if (existingUser) {
      return res.status(409).json({
        success: false,
        error: 'An account with this email already exists'
      });
    }

    // Hash password
    const passwordHash = await bcrypt.hash(password, BCRYPT_ROUNDS);

    // Create user
    const result = db.prepare(`
      INSERT INTO users (email, password_hash, name, created_at)
      VALUES (?, ?, ?, datetime('now'))
    `).run(email.toLowerCase(), passwordHash, trimmedName);

    const userId = result.lastInsertRowid;

    // Generate tokens
    const accessToken = generateToken(userId);
    const refreshToken = generateRefreshToken(userId);

    // Store refresh token hash
    const refreshTokenHash = await bcrypt.hash(refreshToken, 10);
    db.prepare(`
      INSERT INTO refresh_tokens (user_id, token_hash, expires_at)
      VALUES (?, ?, datetime('now', '+30 days'))
    `).run(userId, refreshTokenHash);

    res.status(201).json({
      success: true,
      message: 'Account created successfully',
      data: {
        user: {
          id: userId,
          email: email.toLowerCase(),
          name: trimmedName
        },
        accessToken,
        refreshToken
      }
    });
  } catch (error) {
    console.error('Registration error:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to create account. Please try again.'
    });
  }
});

/**
 * POST /api/auth/login
 * Authenticate user and return JWT token
 */
router.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;

    // Validate required fields
    if (!email || !password) {
      return res.status(400).json({
        success: false,
        error: 'Email and password are required'
      });
    }

    // Find user by email
    const user = db.prepare(`
      SELECT id, email, password_hash, name, is_active
      FROM users
      WHERE email = ?
    `).get(email.toLowerCase());

    if (!user) {
      return res.status(401).json({
        success: false,
        error: 'Invalid email or password'
      });
    }

    // Check if account is active
    if (!user.is_active) {
      return res.status(403).json({
        success: false,
        error: 'Account is deactivated. Please contact support.'
      });
    }

    // Verify password
    const passwordMatch = await bcrypt.compare(password, user.password_hash);
    if (!passwordMatch) {
      return res.status(401).json({
        success: false,
        error: 'Invalid email or password'
      });
    }

    // Update last login timestamp
    db.prepare(`
      UPDATE users SET last_login_at = datetime('now') WHERE id = ?
    `).run(user.id);

    // Generate tokens
    const accessToken = generateToken(user.id);
    const refreshToken = generateRefreshToken(user.id);

    // Store refresh token hash (revoke old ones first)
    db.prepare('UPDATE refresh_tokens SET revoked = 1 WHERE user_id = ?').run(user.id);

    const refreshTokenHash = await bcrypt.hash(refreshToken, 10);
    db.prepare(`
      INSERT INTO refresh_tokens (user_id, token_hash, expires_at)
      VALUES (?, ?, datetime('now', '+30 days'))
    `).run(user.id, refreshTokenHash);

    res.json({
      success: true,
      message: 'Login successful',
      data: {
        user: {
          id: user.id,
          email: user.email,
          name: user.name
        },
        accessToken,
        refreshToken
      }
    });
  } catch (error) {
    console.error('Login error:', error);
    res.status(500).json({
      success: false,
      error: 'Login failed. Please try again.'
    });
  }
});

/**
 * GET /api/auth/me
 * Get current authenticated user's profile
 */
router.get('/me', requireAuth, (req, res) => {
  try {
    // Get user's enrollments
    const enrollments = db.prepare(`
      SELECT
        e.id as enrollment_id,
        e.enrolled_at,
        e.expires_at,
        c.id as course_id,
        c.slug,
        c.title,
        c.description
      FROM enrollments e
      JOIN courses c ON e.course_id = c.id
      WHERE e.user_id = ? AND e.payment_status IN ('completed', 'free')
    `).all(req.user.id);

    // Get overall progress summary
    const progressSummary = db.prepare(`
      SELECT
        COUNT(DISTINCT vp.id) as total_videos,
        COUNT(DISTINCT CASE WHEN up.completed = 1 THEN vp.id END) as completed_videos,
        SUM(vp.duration_seconds) as total_duration,
        SUM(CASE WHEN up.completed = 1 THEN vp.duration_seconds ELSE up.progress_seconds END) as watched_duration
      FROM enrollments e
      JOIN courses c ON e.course_id = c.id
      JOIN modules m ON m.course_id = c.id
      JOIN lessons l ON l.module_id = m.id
      JOIN video_parts vp ON vp.lesson_id = l.id
      LEFT JOIN user_progress up ON up.video_part_id = vp.id AND up.user_id = e.user_id
      WHERE e.user_id = ? AND e.payment_status IN ('completed', 'free')
    `).get(req.user.id);

    res.json({
      success: true,
      data: {
        user: {
          id: req.user.id,
          email: req.user.email,
          name: req.user.name,
          created_at: req.user.created_at
        },
        enrollments,
        progress: {
          totalVideos: progressSummary?.total_videos || 0,
          completedVideos: progressSummary?.completed_videos || 0,
          totalDurationSeconds: progressSummary?.total_duration || 0,
          watchedDurationSeconds: progressSummary?.watched_duration || 0
        }
      }
    });
  } catch (error) {
    console.error('Get user profile error:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to fetch user profile'
    });
  }
});

/**
 * POST /api/auth/refresh
 * Refresh access token using refresh token
 */
router.post('/refresh', async (req, res) => {
  try {
    const { refreshToken } = req.body;

    if (!refreshToken) {
      return res.status(400).json({
        success: false,
        error: 'Refresh token is required'
      });
    }

    // Find valid refresh tokens for comparison
    const tokens = db.prepare(`
      SELECT id, user_id, token_hash, expires_at
      FROM refresh_tokens
      WHERE revoked = 0 AND datetime(expires_at) > datetime('now')
    `).all();

    let validToken = null;
    for (const token of tokens) {
      const match = await bcrypt.compare(refreshToken, token.token_hash);
      if (match) {
        validToken = token;
        break;
      }
    }

    if (!validToken) {
      return res.status(401).json({
        success: false,
        error: 'Invalid or expired refresh token'
      });
    }

    // Get user
    const user = db.prepare(`
      SELECT id, email, name, is_active
      FROM users
      WHERE id = ? AND is_active = 1
    `).get(validToken.user_id);

    if (!user) {
      return res.status(401).json({
        success: false,
        error: 'User not found or inactive'
      });
    }

    // Generate new access token
    const accessToken = generateToken(user.id);

    res.json({
      success: true,
      data: {
        accessToken
      }
    });
  } catch (error) {
    console.error('Token refresh error:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to refresh token'
    });
  }
});

/**
 * POST /api/auth/logout
 * Revoke refresh token (logout)
 */
router.post('/logout', requireAuth, async (req, res) => {
  try {
    // Revoke all refresh tokens for this user
    db.prepare('UPDATE refresh_tokens SET revoked = 1 WHERE user_id = ?').run(req.user.id);

    res.json({
      success: true,
      message: 'Logged out successfully'
    });
  } catch (error) {
    console.error('Logout error:', error);
    res.status(500).json({
      success: false,
      error: 'Logout failed'
    });
  }
});

/**
 * PUT /api/auth/password
 * Change password for authenticated user
 */
router.put('/password', requireAuth, async (req, res) => {
  try {
    const { currentPassword, newPassword } = req.body;

    if (!currentPassword || !newPassword) {
      return res.status(400).json({
        success: false,
        error: 'Current password and new password are required'
      });
    }

    // Validate new password strength
    const passwordValidation = isValidPassword(newPassword);
    if (!passwordValidation.valid) {
      return res.status(400).json({
        success: false,
        error: passwordValidation.message
      });
    }

    // Get current password hash
    const user = db.prepare('SELECT password_hash FROM users WHERE id = ?').get(req.user.id);

    // Verify current password
    const passwordMatch = await bcrypt.compare(currentPassword, user.password_hash);
    if (!passwordMatch) {
      return res.status(401).json({
        success: false,
        error: 'Current password is incorrect'
      });
    }

    // Hash new password
    const newPasswordHash = await bcrypt.hash(newPassword, BCRYPT_ROUNDS);

    // Update password
    db.prepare(`
      UPDATE users SET password_hash = ?, updated_at = datetime('now') WHERE id = ?
    `).run(newPasswordHash, req.user.id);

    // Revoke all refresh tokens (force re-login)
    db.prepare('UPDATE refresh_tokens SET revoked = 1 WHERE user_id = ?').run(req.user.id);

    res.json({
      success: true,
      message: 'Password changed successfully. Please log in again.'
    });
  } catch (error) {
    console.error('Password change error:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to change password'
    });
  }
});

export default router;
