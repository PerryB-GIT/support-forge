/**
 * CourseView Component
 * Displays a course with module accordion and lesson list
 */

const CourseView = ({ course, progress, onLessonSelect, onBack }) => {
    // Calculate course stats
    const getCourseStats = () => {
        let totalLessons = 0;
        let completedLessons = 0;
        let totalDuration = 0;

        course.modules?.forEach(module => {
            module.lessons?.forEach(lesson => {
                totalLessons++;
                totalDuration += lesson.duration_seconds || 0;
                if (progress?.[lesson.id]?.completed) {
                    completedLessons++;
                }
            });
        });

        return {
            totalLessons,
            completedLessons,
            totalDuration,
            percent: totalLessons > 0 ? Math.round((completedLessons / totalLessons) * 100) : 0
        };
    };

    const stats = getCourseStats();

    const formatTotalDuration = (seconds) => {
        if (!seconds) return '0h 0m';
        const hours = Math.floor(seconds / 3600);
        const mins = Math.floor((seconds % 3600) / 60);
        if (hours > 0) {
            return `${hours}h ${mins}m`;
        }
        return `${mins}m`;
    };

    // Icons
    const LogoIcon = () => (
        <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 4L4 12V28L20 36L36 28V12L20 4Z" stroke="currentColor" strokeWidth="2" fill="none"/>
            <path d="M20 8L8 14V26L20 32L32 26V14L20 8Z" fill="currentColor" opacity="0.3"/>
            <path d="M14 18L20 14L26 18V24L20 28L14 24V18Z" fill="currentColor"/>
        </svg>
    );

    const ArrowLeftIcon = () => (
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M19 12H5M12 19l-7-7 7-7" />
        </svg>
    );

    const ClockIcon = () => (
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <circle cx="12" cy="12" r="10" />
            <polyline points="12,6 12,12 16,14" />
        </svg>
    );

    const BookIcon = () => (
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
        </svg>
    );

    const LayersIcon = () => (
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <polygon points="12,2 2,7 12,12 22,7 12,2" />
            <polyline points="2,17 12,22 22,17" />
            <polyline points="2,12 12,17 22,12" />
        </svg>
    );

    const PlayIcon = () => (
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M8 5v14l11-7z" />
        </svg>
    );

    return (
        <div className="academy-app">
            {/* Header */}
            <header className="academy-header">
                <div className="academy-header-inner">
                    <a href="/" className="academy-logo">
                        <LogoIcon />
                        <span className="academy-logo-text">
                            AI Launchpad <span className="highlight">Academy</span>
                        </span>
                    </a>
                    <button className="btn btn-ghost" onClick={onBack}>
                        <ArrowLeftIcon />
                        Back to Dashboard
                    </button>
                </div>
            </header>

            {/* Main Content */}
            <main className="course-view academy-container">
                {/* Course Header */}
                <div className="course-view-header">
                    <div>
                        <h1 className="course-view-title">{course.title}</h1>
                        <p className="course-view-description">{course.description}</p>
                        <div className="course-view-stats">
                            <div className="course-stat">
                                <div className="course-stat-value" style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                    <LayersIcon /> {course.modules?.length || 0}
                                </div>
                                <div className="course-stat-label">Modules</div>
                            </div>
                            <div className="course-stat">
                                <div className="course-stat-value" style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                    <BookIcon /> {stats.totalLessons}
                                </div>
                                <div className="course-stat-label">Lessons</div>
                            </div>
                            <div className="course-stat">
                                <div className="course-stat-value" style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                    <ClockIcon /> {formatTotalDuration(stats.totalDuration)}
                                </div>
                                <div className="course-stat-label">Total Duration</div>
                            </div>
                        </div>
                    </div>

                    {/* Progress Card */}
                    <div className="course-progress-card">
                        <div className="course-progress-title">Your Progress</div>
                        <div className="course-progress-percent">{stats.percent}%</div>
                        <ProgressBar
                            progress={stats.percent}
                            showLabel={false}
                            size="lg"
                        />
                        <div style={{
                            marginTop: '16px',
                            display: 'flex',
                            justifyContent: 'space-between',
                            fontSize: '0.9rem',
                            color: 'var(--academy-text-secondary)'
                        }}>
                            <span>{stats.completedLessons} completed</span>
                            <span>{stats.totalLessons - stats.completedLessons} remaining</span>
                        </div>

                        {/* Find first incomplete lesson for Continue button */}
                        {stats.percent > 0 && stats.percent < 100 && (
                            <button
                                className="btn btn-primary btn-full"
                                style={{ marginTop: '20px' }}
                                onClick={() => {
                                    // Find first incomplete lesson
                                    for (const module of (course.modules || [])) {
                                        for (const lesson of (module.lessons || [])) {
                                            if (!progress?.[lesson.id]?.completed) {
                                                onLessonSelect(lesson);
                                                return;
                                            }
                                        }
                                    }
                                }}
                            >
                                <PlayIcon /> Continue Learning
                            </button>
                        )}

                        {stats.percent === 0 && (
                            <button
                                className="btn btn-primary btn-full"
                                style={{ marginTop: '20px' }}
                                onClick={() => {
                                    // Start from first lesson
                                    const firstLesson = course.modules?.[0]?.lessons?.[0];
                                    if (firstLesson) onLessonSelect(firstLesson);
                                }}
                            >
                                <PlayIcon /> Start Course
                            </button>
                        )}

                        {stats.percent === 100 && (
                            <div style={{
                                marginTop: '20px',
                                padding: '12px',
                                background: 'var(--academy-success)',
                                borderRadius: '8px',
                                textAlign: 'center',
                                color: 'white',
                                fontWeight: '500'
                            }}>
                                Course Completed!
                            </div>
                        )}
                    </div>
                </div>

                {/* Module Accordion */}
                <div className="course-modules">
                    <h2 className="section-title" style={{ marginBottom: '24px' }}>
                        <LayersIcon /> Course Content
                    </h2>
                    <ModuleAccordion
                        modules={course.modules || []}
                        progress={progress}
                        currentLessonId={null}
                        onLessonSelect={onLessonSelect}
                    />
                </div>
            </main>
        </div>
    );
};

// Make component available globally
window.CourseView = CourseView;
