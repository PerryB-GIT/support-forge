import express from 'express';
import db from '../db/database.js';
import { requireAuth } from '../middleware/auth.js';

const router = express.Router();

/**
 * GET /api/progress
 * Get all progress for the authenticated user
 */
router.get('/', requireAuth, (req, res) => {
  try {
    const userId = req.user.id;

    // Get progress grouped by course
    const courseProgress = db.prepare(`
      SELECT
        c.id as course_id,
        c.slug,
        c.title as course_title,
        e.enrolled_at,
        COUNT(DISTINCT vp.id) as total_videos,
        COUNT(DISTINCT CASE WHEN up.completed = 1 THEN vp.id END) as completed_videos,
        COALESCE(SUM(vp.duration_seconds), 0) as total_duration,
        COALESCE(SUM(CASE WHEN up.completed = 1 THEN vp.duration_seconds ELSE COALESCE(up.progress_seconds, 0) END), 0) as watched_duration,
        MAX(up.last_watched_at) as last_activity
      FROM enrollments e
      JOIN courses c ON c.id = e.course_id
      LEFT JOIN modules m ON m.course_id = c.id
      LEFT JOIN lessons l ON l.module_id = m.id
      LEFT JOIN video_parts vp ON vp.lesson_id = l.id AND vp.status = 'ready'
      LEFT JOIN user_progress up ON up.video_part_id = vp.id AND up.user_id = e.user_id
      WHERE e.user_id = ? AND e.payment_status IN ('completed', 'free')
      GROUP BY c.id
      ORDER BY last_activity DESC NULLS LAST
    `).all(userId);

    // Get recent activity (last 10 videos watched)
    const recentActivity = db.prepare(`
      SELECT
        up.id,
        up.progress_seconds,
        up.completed,
        up.last_watched_at,
        vp.id as video_part_id,
        vp.part_number,
        vp.title as video_title,
        vp.duration_seconds,
        l.id as lesson_id,
        l.title as lesson_title,
        l.lesson_number,
        m.id as module_id,
        m.title as module_title,
        m.module_number,
        c.id as course_id,
        c.slug as course_slug,
        c.title as course_title
      FROM user_progress up
      JOIN video_parts vp ON vp.id = up.video_part_id
      JOIN lessons l ON l.id = vp.lesson_id
      JOIN modules m ON m.id = l.module_id
      JOIN courses c ON c.id = m.course_id
      WHERE up.user_id = ?
      ORDER BY up.last_watched_at DESC
      LIMIT 10
    `).all(userId);

    // Calculate overall stats
    const overallStats = db.prepare(`
      SELECT
        COUNT(DISTINCT c.id) as enrolled_courses,
        COUNT(DISTINCT CASE WHEN up.completed = 1 THEN vp.id END) as total_completed_videos,
        COALESCE(SUM(CASE WHEN up.completed = 1 THEN vp.duration_seconds ELSE COALESCE(up.progress_seconds, 0) END), 0) as total_watch_time
      FROM enrollments e
      JOIN courses c ON c.id = e.course_id
      LEFT JOIN modules m ON m.course_id = c.id
      LEFT JOIN lessons l ON l.module_id = m.id
      LEFT JOIN video_parts vp ON vp.lesson_id = l.id AND vp.status = 'ready'
      LEFT JOIN user_progress up ON up.video_part_id = vp.id AND up.user_id = e.user_id
      WHERE e.user_id = ? AND e.payment_status IN ('completed', 'free')
    `).get(userId);

    res.json({
      success: true,
      data: {
        overall: {
          enrolledCourses: overallStats.enrolled_courses || 0,
          completedVideos: overallStats.total_completed_videos || 0,
          totalWatchTimeSeconds: overallStats.total_watch_time || 0,
          totalWatchTimeFormatted: formatDuration(overallStats.total_watch_time || 0)
        },
        courses: courseProgress.map(course => ({
          courseId: course.course_id,
          slug: course.slug,
          title: course.course_title,
          enrolledAt: course.enrolled_at,
          lastActivity: course.last_activity,
          progress: {
            totalVideos: course.total_videos,
            completedVideos: course.completed_videos,
            totalDurationSeconds: course.total_duration,
            watchedDurationSeconds: course.watched_duration,
            percentComplete: course.total_duration > 0
              ? Math.round((course.watched_duration / course.total_duration) * 100)
              : 0
          }
        })),
        recentActivity: recentActivity.map(activity => ({
          id: activity.id,
          videoPartId: activity.video_part_id,
          progressSeconds: activity.progress_seconds,
          completed: !!activity.completed,
          lastWatchedAt: activity.last_watched_at,
          video: {
            partNumber: activity.part_number,
            title: activity.video_title,
            durationSeconds: activity.duration_seconds
          },
          lesson: {
            id: activity.lesson_id,
            number: activity.lesson_number,
            title: activity.lesson_title
          },
          module: {
            id: activity.module_id,
            number: activity.module_number,
            title: activity.module_title
          },
          course: {
            id: activity.course_id,
            slug: activity.course_slug,
            title: activity.course_title
          }
        }))
      }
    });
  } catch (error) {
    console.error('Get progress error:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to fetch progress'
    });
  }
});

/**
 * GET /api/progress/course/:courseId
 * Get detailed progress for a specific course
 */
router.get('/course/:courseId', requireAuth, (req, res) => {
  try {
    const userId = req.user.id;
    const { courseId } = req.params;

    // Verify enrollment
    const enrollment = db.prepare(`
      SELECT id, enrolled_at
      FROM enrollments
      WHERE user_id = ? AND course_id = ? AND payment_status IN ('completed', 'free')
    `).get(userId, courseId);

    if (!enrollment) {
      return res.status(403).json({
        success: false,
        error: 'Not enrolled in this course'
      });
    }

    // Get progress by module
    const moduleProgress = db.prepare(`
      SELECT
        m.id as module_id,
        m.module_number,
        m.title as module_title,
        COUNT(DISTINCT vp.id) as total_videos,
        COUNT(DISTINCT CASE WHEN up.completed = 1 THEN vp.id END) as completed_videos,
        COALESCE(SUM(vp.duration_seconds), 0) as total_duration,
        COALESCE(SUM(CASE WHEN up.completed = 1 THEN vp.duration_seconds ELSE COALESCE(up.progress_seconds, 0) END), 0) as watched_duration
      FROM modules m
      LEFT JOIN lessons l ON l.module_id = m.id
      LEFT JOIN video_parts vp ON vp.lesson_id = l.id AND vp.status = 'ready'
      LEFT JOIN user_progress up ON up.video_part_id = vp.id AND up.user_id = ?
      WHERE m.course_id = ?
      GROUP BY m.id
      ORDER BY m.sort_order ASC, m.module_number ASC
    `).all(userId, courseId);

    // Get individual video progress
    const videoProgress = db.prepare(`
      SELECT
        up.id,
        up.progress_seconds,
        up.completed,
        up.completed_at,
        up.last_watched_at,
        vp.id as video_part_id,
        vp.part_number,
        vp.title as video_title,
        vp.duration_seconds,
        l.id as lesson_id,
        l.lesson_number,
        l.title as lesson_title,
        m.id as module_id,
        m.module_number
      FROM user_progress up
      JOIN video_parts vp ON vp.id = up.video_part_id
      JOIN lessons l ON l.id = vp.lesson_id
      JOIN modules m ON m.id = l.module_id
      WHERE up.user_id = ? AND m.course_id = ?
      ORDER BY m.sort_order, l.sort_order, vp.part_number
    `).all(userId, courseId);

    // Find next unwatched video
    const nextVideo = db.prepare(`
      SELECT
        vp.id as video_part_id,
        vp.part_number,
        vp.title as video_title,
        l.id as lesson_id,
        l.lesson_number,
        l.title as lesson_title,
        m.id as module_id,
        m.module_number,
        m.title as module_title,
        COALESCE(up.progress_seconds, 0) as progress_seconds
      FROM modules m
      JOIN lessons l ON l.module_id = m.id
      JOIN video_parts vp ON vp.lesson_id = l.id AND vp.status = 'ready'
      LEFT JOIN user_progress up ON up.video_part_id = vp.id AND up.user_id = ?
      WHERE m.course_id = ? AND (up.completed IS NULL OR up.completed = 0)
      ORDER BY m.sort_order, l.sort_order, vp.part_number
      LIMIT 1
    `).get(userId, courseId);

    res.json({
      success: true,
      data: {
        enrolledAt: enrollment.enrolled_at,
        modules: moduleProgress.map(m => ({
          moduleId: m.module_id,
          moduleNumber: m.module_number,
          title: m.module_title,
          progress: {
            totalVideos: m.total_videos,
            completedVideos: m.completed_videos,
            totalDurationSeconds: m.total_duration,
            watchedDurationSeconds: m.watched_duration,
            percentComplete: m.total_duration > 0
              ? Math.round((m.watched_duration / m.total_duration) * 100)
              : 0,
            isComplete: m.total_videos > 0 && m.total_videos === m.completed_videos
          }
        })),
        videos: videoProgress.map(v => ({
          progressId: v.id,
          videoPartId: v.video_part_id,
          partNumber: v.part_number,
          title: v.video_title,
          durationSeconds: v.duration_seconds,
          progressSeconds: v.progress_seconds,
          completed: !!v.completed,
          completedAt: v.completed_at,
          lastWatchedAt: v.last_watched_at,
          lessonId: v.lesson_id,
          lessonNumber: v.lesson_number,
          lessonTitle: v.lesson_title,
          moduleId: v.module_id,
          moduleNumber: v.module_number
        })),
        nextVideo: nextVideo ? {
          videoPartId: nextVideo.video_part_id,
          partNumber: nextVideo.part_number,
          title: nextVideo.video_title,
          lessonId: nextVideo.lesson_id,
          lessonNumber: nextVideo.lesson_number,
          lessonTitle: nextVideo.lesson_title,
          moduleId: nextVideo.module_id,
          moduleNumber: nextVideo.module_number,
          moduleTitle: nextVideo.module_title,
          resumeAt: nextVideo.progress_seconds
        } : null
      }
    });
  } catch (error) {
    console.error('Get course progress error:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to fetch course progress'
    });
  }
});

/**
 * POST /api/progress/:videoPartId
 * Update progress for a video part
 */
router.post('/:videoPartId', requireAuth, (req, res) => {
  try {
    const userId = req.user.id;
    const { videoPartId } = req.params;
    const { progressSeconds } = req.body;

    // Validate progress
    if (typeof progressSeconds !== 'number' || progressSeconds < 0) {
      return res.status(400).json({
        success: false,
        error: 'progressSeconds must be a non-negative number'
      });
    }

    // Verify user has access to this video
    const videoPart = db.prepare(`
      SELECT vp.id, vp.duration_seconds, c.id as course_id
      FROM video_parts vp
      JOIN lessons l ON l.id = vp.lesson_id
      JOIN modules m ON m.id = l.module_id
      JOIN courses c ON c.id = m.course_id
      JOIN enrollments e ON e.course_id = c.id AND e.user_id = ? AND e.payment_status IN ('completed', 'free')
      WHERE vp.id = ?
    `).get(userId, videoPartId);

    if (!videoPart) {
      return res.status(403).json({
        success: false,
        error: 'Not enrolled in this course or video not found'
      });
    }

    // Cap progress at video duration
    const cappedProgress = Math.min(progressSeconds, videoPart.duration_seconds);

    // Upsert progress
    const existingProgress = db.prepare(`
      SELECT id, completed FROM user_progress
      WHERE user_id = ? AND video_part_id = ?
    `).get(userId, videoPartId);

    if (existingProgress) {
      // Don't update if already completed (prevent resetting completion)
      if (!existingProgress.completed) {
        db.prepare(`
          UPDATE user_progress
          SET progress_seconds = ?,
              last_watched_at = datetime('now'),
              updated_at = datetime('now')
          WHERE id = ?
        `).run(cappedProgress, existingProgress.id);
      }
    } else {
      db.prepare(`
        INSERT INTO user_progress (user_id, video_part_id, progress_seconds, last_watched_at)
        VALUES (?, ?, ?, datetime('now'))
      `).run(userId, videoPartId, cappedProgress);
    }

    res.json({
      success: true,
      data: {
        videoPartId: parseInt(videoPartId),
        progressSeconds: cappedProgress,
        durationSeconds: videoPart.duration_seconds,
        percentComplete: Math.round((cappedProgress / videoPart.duration_seconds) * 100)
      }
    });
  } catch (error) {
    console.error('Update progress error:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to update progress'
    });
  }
});

/**
 * POST /api/progress/:videoPartId/complete
 * Mark a video part as complete
 */
router.post('/:videoPartId/complete', requireAuth, (req, res) => {
  try {
    const userId = req.user.id;
    const { videoPartId } = req.params;

    // Verify user has access to this video
    const videoPart = db.prepare(`
      SELECT vp.id, vp.duration_seconds, c.id as course_id
      FROM video_parts vp
      JOIN lessons l ON l.id = vp.lesson_id
      JOIN modules m ON m.id = l.module_id
      JOIN courses c ON c.id = m.course_id
      JOIN enrollments e ON e.course_id = c.id AND e.user_id = ? AND e.payment_status IN ('completed', 'free')
      WHERE vp.id = ?
    `).get(userId, videoPartId);

    if (!videoPart) {
      return res.status(403).json({
        success: false,
        error: 'Not enrolled in this course or video not found'
      });
    }

    // Upsert completion
    const existingProgress = db.prepare(`
      SELECT id FROM user_progress
      WHERE user_id = ? AND video_part_id = ?
    `).get(userId, videoPartId);

    if (existingProgress) {
      db.prepare(`
        UPDATE user_progress
        SET completed = 1,
            completed_at = datetime('now'),
            progress_seconds = ?,
            last_watched_at = datetime('now'),
            updated_at = datetime('now')
        WHERE id = ?
      `).run(videoPart.duration_seconds, existingProgress.id);
    } else {
      db.prepare(`
        INSERT INTO user_progress (user_id, video_part_id, progress_seconds, completed, completed_at, last_watched_at)
        VALUES (?, ?, ?, 1, datetime('now'), datetime('now'))
      `).run(userId, videoPartId, videoPart.duration_seconds);
    }

    // Check if this completes the lesson
    const lessonComplete = db.prepare(`
      SELECT
        COUNT(*) as total_parts,
        SUM(CASE WHEN up.completed = 1 THEN 1 ELSE 0 END) as completed_parts
      FROM video_parts vp
      JOIN lessons l ON l.id = vp.lesson_id
      JOIN (SELECT lesson_id FROM video_parts WHERE id = ?) target ON target.lesson_id = l.id
      LEFT JOIN user_progress up ON up.video_part_id = vp.id AND up.user_id = ?
      WHERE vp.status = 'ready'
    `).get(videoPartId, userId);

    // Check if this completes the course
    const courseComplete = db.prepare(`
      SELECT
        COUNT(*) as total_videos,
        SUM(CASE WHEN up.completed = 1 THEN 1 ELSE 0 END) as completed_videos
      FROM video_parts vp
      JOIN lessons l ON l.id = vp.lesson_id
      JOIN modules m ON m.id = l.module_id
      LEFT JOIN user_progress up ON up.video_part_id = vp.id AND up.user_id = ?
      WHERE m.course_id = ? AND vp.status = 'ready'
    `).get(userId, videoPart.course_id);

    res.json({
      success: true,
      data: {
        videoPartId: parseInt(videoPartId),
        completed: true,
        completedAt: new Date().toISOString(),
        lessonComplete: lessonComplete.total_parts === lessonComplete.completed_parts,
        courseComplete: courseComplete.total_videos === courseComplete.completed_videos
      }
    });
  } catch (error) {
    console.error('Mark complete error:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to mark as complete'
    });
  }
});

/**
 * DELETE /api/progress/:videoPartId
 * Reset progress for a video part (for rewatching)
 */
router.delete('/:videoPartId', requireAuth, (req, res) => {
  try {
    const userId = req.user.id;
    const { videoPartId } = req.params;

    // Verify user has access
    const progress = db.prepare(`
      SELECT up.id
      FROM user_progress up
      JOIN video_parts vp ON vp.id = up.video_part_id
      JOIN lessons l ON l.id = vp.lesson_id
      JOIN modules m ON m.id = l.module_id
      JOIN courses c ON c.id = m.course_id
      JOIN enrollments e ON e.course_id = c.id AND e.user_id = ? AND e.payment_status IN ('completed', 'free')
      WHERE up.user_id = ? AND up.video_part_id = ?
    `).get(userId, userId, videoPartId);

    if (!progress) {
      return res.status(404).json({
        success: false,
        error: 'Progress record not found'
      });
    }

    // Reset progress (don't delete, just reset values)
    db.prepare(`
      UPDATE user_progress
      SET progress_seconds = 0,
          completed = 0,
          completed_at = NULL,
          updated_at = datetime('now')
      WHERE id = ?
    `).run(progress.id);

    res.json({
      success: true,
      message: 'Progress reset successfully'
    });
  } catch (error) {
    console.error('Reset progress error:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to reset progress'
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
