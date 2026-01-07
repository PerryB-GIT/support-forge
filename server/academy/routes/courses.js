import express from 'express';
import db from '../db/database.js';
import { requireAuth, optionalAuth, requireEnrollment } from '../middleware/auth.js';
import { generateSignedUrl } from '../services/videoService.js';

const router = express.Router();

/**
 * GET /api/courses
 * List all published courses
 * Optional auth - shows enrollment status if logged in
 */
router.get('/', optionalAuth, (req, res) => {
  try {
    const courses = db.prepare(`
      SELECT
        c.id,
        c.slug,
        c.title,
        c.description,
        c.price_cents,
        c.thumbnail_url,
        c.created_at,
        COUNT(DISTINCT m.id) as module_count,
        COUNT(DISTINCT l.id) as lesson_count,
        COALESCE(SUM(l.duration_seconds), 0) as total_duration_seconds
      FROM courses c
      LEFT JOIN modules m ON m.course_id = c.id
      LEFT JOIN lessons l ON l.module_id = m.id
      WHERE c.is_published = 1
      GROUP BY c.id
      ORDER BY c.created_at DESC
    `).all();

    // If user is logged in, add enrollment status
    let enrolledCourseIds = [];
    if (req.user) {
      const enrollments = db.prepare(`
        SELECT course_id FROM enrollments
        WHERE user_id = ? AND payment_status IN ('completed', 'free')
      `).all(req.user.id);
      enrolledCourseIds = enrollments.map(e => e.course_id);
    }

    const coursesWithEnrollment = courses.map(course => ({
      ...course,
      price: {
        cents: course.price_cents,
        formatted: course.price_cents === 0 ? 'Free' : `$${(course.price_cents / 100).toFixed(2)}`
      },
      isEnrolled: enrolledCourseIds.includes(course.id),
      moduleCount: course.module_count,
      lessonCount: course.lesson_count,
      totalDuration: formatDuration(course.total_duration_seconds)
    }));

    res.json({
      success: true,
      data: coursesWithEnrollment
    });
  } catch (error) {
    console.error('List courses error:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to fetch courses'
    });
  }
});

/**
 * GET /api/courses/:slug
 * Get single course with modules
 * Optional auth - shows enrollment status and progress if logged in
 */
router.get('/:slug', optionalAuth, (req, res) => {
  try {
    const { slug } = req.params;

    // Get course details
    const course = db.prepare(`
      SELECT
        id, slug, title, description, price_cents, thumbnail_url, created_at, is_published
      FROM courses
      WHERE slug = ?
    `).get(slug);

    if (!course) {
      return res.status(404).json({
        success: false,
        error: 'Course not found'
      });
    }

    // Only show unpublished courses to enrolled users
    if (!course.is_published) {
      if (!req.user) {
        return res.status(404).json({
          success: false,
          error: 'Course not found'
        });
      }

      const enrollment = db.prepare(`
        SELECT id FROM enrollments
        WHERE user_id = ? AND course_id = ? AND payment_status IN ('completed', 'free')
      `).get(req.user.id, course.id);

      if (!enrollment) {
        return res.status(404).json({
          success: false,
          error: 'Course not found'
        });
      }
    }

    // Get modules with lesson counts
    const modules = db.prepare(`
      SELECT
        m.id,
        m.module_number,
        m.title,
        m.description,
        m.sort_order,
        COUNT(l.id) as lesson_count,
        COALESCE(SUM(l.duration_seconds), 0) as total_duration_seconds
      FROM modules m
      LEFT JOIN lessons l ON l.module_id = m.id
      WHERE m.course_id = ?
      GROUP BY m.id
      ORDER BY m.sort_order ASC, m.module_number ASC
    `).all(course.id);

    // Check enrollment status
    let enrollment = null;
    let progress = null;

    if (req.user) {
      enrollment = db.prepare(`
        SELECT id, enrolled_at, expires_at, payment_status
        FROM enrollments
        WHERE user_id = ? AND course_id = ? AND payment_status IN ('completed', 'free')
      `).get(req.user.id, course.id);

      if (enrollment) {
        // Get progress for this course
        const progressData = db.prepare(`
          SELECT
            COUNT(DISTINCT vp.id) as total_videos,
            COUNT(DISTINCT CASE WHEN up.completed = 1 THEN vp.id END) as completed_videos,
            COALESCE(SUM(vp.duration_seconds), 0) as total_duration,
            COALESCE(SUM(CASE WHEN up.completed = 1 THEN vp.duration_seconds ELSE COALESCE(up.progress_seconds, 0) END), 0) as watched_duration
          FROM modules m
          JOIN lessons l ON l.module_id = m.id
          JOIN video_parts vp ON vp.lesson_id = l.id
          LEFT JOIN user_progress up ON up.video_part_id = vp.id AND up.user_id = ?
          WHERE m.course_id = ?
        `).get(req.user.id, course.id);

        progress = {
          totalVideos: progressData.total_videos,
          completedVideos: progressData.completed_videos,
          totalDurationSeconds: progressData.total_duration,
          watchedDurationSeconds: progressData.watched_duration,
          percentComplete: progressData.total_duration > 0
            ? Math.round((progressData.watched_duration / progressData.total_duration) * 100)
            : 0
        };
      }
    }

    res.json({
      success: true,
      data: {
        course: {
          ...course,
          price: {
            cents: course.price_cents,
            formatted: course.price_cents === 0 ? 'Free' : `$${(course.price_cents / 100).toFixed(2)}`
          }
        },
        modules: modules.map(m => ({
          ...m,
          lessonCount: m.lesson_count,
          totalDuration: formatDuration(m.total_duration_seconds)
        })),
        isEnrolled: !!enrollment,
        enrollment: enrollment ? {
          enrolledAt: enrollment.enrolled_at,
          expiresAt: enrollment.expires_at
        } : null,
        progress
      }
    });
  } catch (error) {
    console.error('Get course error:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to fetch course'
    });
  }
});

/**
 * GET /api/courses/:slug/modules/:moduleId/lessons
 * Get lessons for a specific module
 * Requires authentication and enrollment
 */
router.get('/:slug/modules/:moduleId/lessons', requireAuth, requireEnrollment, (req, res) => {
  try {
    const { moduleId } = req.params;
    const courseId = req.course.id;
    const userId = req.user.id;

    // Verify module belongs to this course
    const module = db.prepare(`
      SELECT id, module_number, title, description, sort_order
      FROM modules
      WHERE id = ? AND course_id = ?
    `).get(moduleId, courseId);

    if (!module) {
      return res.status(404).json({
        success: false,
        error: 'Module not found'
      });
    }

    // Get lessons with video parts and progress
    const lessons = db.prepare(`
      SELECT
        l.id,
        l.lesson_number,
        l.title,
        l.description,
        l.duration_seconds,
        l.sort_order,
        l.is_preview
      FROM lessons l
      WHERE l.module_id = ?
      ORDER BY l.sort_order ASC, l.lesson_number ASC
    `).all(moduleId);

    // Get video parts for each lesson with progress
    const lessonsWithVideos = lessons.map(lesson => {
      const videoParts = db.prepare(`
        SELECT
          vp.id,
          vp.part_number,
          vp.title,
          vp.duration_seconds,
          vp.status,
          up.progress_seconds,
          up.completed,
          up.last_watched_at
        FROM video_parts vp
        LEFT JOIN user_progress up ON up.video_part_id = vp.id AND up.user_id = ?
        WHERE vp.lesson_id = ? AND vp.status = 'ready'
        ORDER BY vp.part_number ASC
      `).all(userId, lesson.id);

      const totalProgress = videoParts.reduce((acc, vp) => {
        if (vp.completed) return acc + vp.duration_seconds;
        return acc + (vp.progress_seconds || 0);
      }, 0);

      const totalDuration = videoParts.reduce((acc, vp) => acc + vp.duration_seconds, 0);
      const isCompleted = videoParts.length > 0 && videoParts.every(vp => vp.completed);

      return {
        ...lesson,
        duration: formatDuration(lesson.duration_seconds),
        videoParts: videoParts.map(vp => ({
          id: vp.id,
          partNumber: vp.part_number,
          title: vp.title,
          duration: formatDuration(vp.duration_seconds),
          durationSeconds: vp.duration_seconds,
          progressSeconds: vp.progress_seconds || 0,
          completed: !!vp.completed,
          lastWatchedAt: vp.last_watched_at
        })),
        progress: {
          watchedSeconds: totalProgress,
          totalSeconds: totalDuration,
          percentComplete: totalDuration > 0 ? Math.round((totalProgress / totalDuration) * 100) : 0,
          isCompleted
        }
      };
    });

    res.json({
      success: true,
      data: {
        module: {
          id: module.id,
          moduleNumber: module.module_number,
          title: module.title,
          description: module.description
        },
        lessons: lessonsWithVideos
      }
    });
  } catch (error) {
    console.error('Get lessons error:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to fetch lessons'
    });
  }
});

/**
 * GET /api/courses/:slug/video/:videoPartId
 * Get signed URL for video playback
 * Requires authentication and enrollment
 */
router.get('/:slug/video/:videoPartId', requireAuth, requireEnrollment, async (req, res) => {
  try {
    const { videoPartId } = req.params;
    const courseId = req.course.id;

    // Verify video part belongs to this course
    const videoPart = db.prepare(`
      SELECT vp.id, vp.s3_key, vp.cloudfront_url, vp.duration_seconds, vp.status
      FROM video_parts vp
      JOIN lessons l ON l.id = vp.lesson_id
      JOIN modules m ON m.id = l.module_id
      WHERE vp.id = ? AND m.course_id = ? AND vp.status = 'ready'
    `).get(videoPartId, courseId);

    if (!videoPart) {
      return res.status(404).json({
        success: false,
        error: 'Video not found or not ready'
      });
    }

    // Generate signed URL
    const signedUrl = await generateSignedUrl(videoPart.s3_key, videoPart.cloudfront_url);

    res.json({
      success: true,
      data: {
        videoId: videoPart.id,
        url: signedUrl,
        durationSeconds: videoPart.duration_seconds,
        expiresIn: '4 hours'
      }
    });
  } catch (error) {
    console.error('Get video URL error:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to generate video URL'
    });
  }
});

/**
 * POST /api/courses/:slug/enroll
 * Enroll user in a free course
 * Requires authentication
 */
router.post('/:slug/enroll', requireAuth, (req, res) => {
  try {
    const { slug } = req.params;
    const userId = req.user.id;

    // Get course
    const course = db.prepare(`
      SELECT id, title, price_cents, is_published
      FROM courses
      WHERE slug = ? AND is_published = 1
    `).get(slug);

    if (!course) {
      return res.status(404).json({
        success: false,
        error: 'Course not found'
      });
    }

    // Check if already enrolled
    const existingEnrollment = db.prepare(`
      SELECT id FROM enrollments WHERE user_id = ? AND course_id = ?
    `).get(userId, course.id);

    if (existingEnrollment) {
      return res.status(400).json({
        success: false,
        error: 'Already enrolled in this course'
      });
    }

    // Only allow direct enrollment for free courses
    if (course.price_cents > 0) {
      return res.status(400).json({
        success: false,
        error: 'This course requires payment. Please use the checkout process.'
      });
    }

    // Create enrollment
    const result = db.prepare(`
      INSERT INTO enrollments (user_id, course_id, enrolled_at, payment_status)
      VALUES (?, ?, datetime('now'), 'free')
    `).run(userId, course.id);

    res.status(201).json({
      success: true,
      message: 'Successfully enrolled in course',
      data: {
        enrollmentId: result.lastInsertRowid,
        course: {
          id: course.id,
          title: course.title
        }
      }
    });
  } catch (error) {
    console.error('Enrollment error:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to enroll in course'
    });
  }
});

/**
 * Format seconds into human-readable duration
 */
function formatDuration(seconds) {
  if (!seconds || seconds === 0) return '0m';

  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);

  if (hours > 0) {
    return `${hours}h ${minutes}m`;
  }
  return `${minutes}m`;
}

export default router;
