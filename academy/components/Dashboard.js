/**
 * Dashboard Component
 * Main dashboard showing course progress, continue watching, and course list
 */

const Dashboard = ({ user, courses, progress, onCourseSelect, onLogout }) => {
    // Calculate overall stats
    const calculateOverallProgress = () => {
        if (!courses || !progress) return { completed: 0, total: 0, percent: 0 };

        let totalLessons = 0;
        let completedLessons = 0;

        courses.forEach(course => {
            course.modules?.forEach(module => {
                module.lessons?.forEach(lesson => {
                    totalLessons++;
                    if (progress[lesson.id]?.completed) {
                        completedLessons++;
                    }
                });
            });
        });

        return {
            completed: completedLessons,
            total: totalLessons,
            percent: totalLessons > 0 ? Math.round((completedLessons / totalLessons) * 100) : 0
        };
    };

    // Find continue watching lesson
    const getContinueWatching = () => {
        if (!courses || !progress) return null;

        let lastWatched = null;
        let lastTimestamp = 0;

        Object.entries(progress).forEach(([lessonId, lessonProgress]) => {
            if (lessonProgress.last_watched_at && !lessonProgress.completed) {
                const timestamp = new Date(lessonProgress.last_watched_at).getTime();
                if (timestamp > lastTimestamp) {
                    lastTimestamp = timestamp;
                    // Find the lesson details
                    for (const course of courses) {
                        for (const module of (course.modules || [])) {
                            for (const lesson of (module.lessons || [])) {
                                if (lesson.id === lessonId) {
                                    lastWatched = {
                                        ...lesson,
                                        courseName: course.title,
                                        moduleTitle: module.title,
                                        progress: lessonProgress
                                    };
                                }
                            }
                        }
                    }
                }
            }
        });

        return lastWatched;
    };

    // Get course progress
    const getCourseProgress = (course) => {
        if (!progress) return 0;
        let total = 0;
        let completed = 0;

        course.modules?.forEach(module => {
            module.lessons?.forEach(lesson => {
                total++;
                if (progress[lesson.id]?.completed) completed++;
            });
        });

        return total > 0 ? Math.round((completed / total) * 100) : 0;
    };

    const stats = calculateOverallProgress();
    const continueWatching = getContinueWatching();

    // Icons
    const LogoIcon = () => (
        <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 4L4 12V28L20 36L36 28V12L20 4Z" stroke="currentColor" strokeWidth="2" fill="none"/>
            <path d="M20 8L8 14V26L20 32L32 26V14L20 8Z" fill="currentColor" opacity="0.3"/>
            <path d="M14 18L20 14L26 18V24L20 28L14 24V18Z" fill="currentColor"/>
        </svg>
    );

    const BookIcon = () => (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
        </svg>
    );

    const CheckCircleIcon = () => (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" />
            <polyline points="22,4 12,14.01 9,11.01" />
        </svg>
    );

    const TrendingIcon = () => (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <polyline points="23,6 13.5,15.5 8.5,10.5 1,18" />
            <polyline points="17,6 23,6 23,12" />
        </svg>
    );

    const PlayIcon = () => (
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M8 5v14l11-7z" />
        </svg>
    );

    const ClockIcon = () => (
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <circle cx="12" cy="12" r="10" />
            <polyline points="12,6 12,12 16,14" />
        </svg>
    );

    const LogoutIcon = () => (
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4" />
            <polyline points="16,17 21,12 16,7" />
            <line x1="21" y1="12" x2="9" y2="12" />
        </svg>
    );

    const formatDuration = (seconds) => {
        if (!seconds) return '--:--';
        const mins = Math.floor(seconds / 60);
        return `${mins} min`;
    };

    const getInitials = (name) => {
        if (!name) return '?';
        return name.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2);
    };

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
                    <div className="academy-user-menu">
                        <span className="academy-user-name">{user?.name || 'Student'}</span>
                        <div className="academy-user-avatar">
                            {getInitials(user?.name)}
                        </div>
                        <button
                            className="btn btn-ghost btn-sm"
                            onClick={onLogout}
                            title="Sign out"
                        >
                            <LogoutIcon />
                        </button>
                    </div>
                </div>
            </header>

            {/* Main Content */}
            <main className="dashboard academy-container">
                {/* Dashboard Header */}
                <div className="dashboard-header">
                    <h1 className="dashboard-greeting">
                        Welcome back, {user?.name?.split(' ')[0] || 'Student'}!
                    </h1>
                    <p className="dashboard-subtitle">
                        Continue your AI implementation journey
                    </p>
                </div>

                {/* Stats Grid */}
                <div className="dashboard-stats">
                    <div className="stat-card">
                        <div className="stat-icon">
                            <BookIcon />
                        </div>
                        <div>
                            <div className="stat-value">{courses?.length || 0}</div>
                            <div className="stat-label">Courses</div>
                        </div>
                    </div>
                    <div className="stat-card">
                        <div className="stat-icon">
                            <CheckCircleIcon />
                        </div>
                        <div>
                            <div className="stat-value">{stats.completed}</div>
                            <div className="stat-label">Lessons Completed</div>
                        </div>
                    </div>
                    <div className="stat-card">
                        <div className="stat-icon">
                            <TrendingIcon />
                        </div>
                        <div>
                            <div className="stat-value">{stats.percent}%</div>
                            <div className="stat-label">Overall Progress</div>
                        </div>
                    </div>
                </div>

                {/* Continue Watching */}
                {continueWatching && (
                    <div className="dashboard-section">
                        <h2 className="section-title">
                            <PlayIcon /> Continue Watching
                        </h2>
                        <div
                            className="continue-card"
                            onClick={() => onCourseSelect(
                                courses.find(c => c.title === continueWatching.courseName),
                                continueWatching
                            )}
                        >
                            <div className="continue-thumbnail">
                                {continueWatching.thumbnail_url ? (
                                    <img src={continueWatching.thumbnail_url} alt={continueWatching.title} />
                                ) : (
                                    <div style={{
                                        width: '100%',
                                        height: '100%',
                                        display: 'flex',
                                        alignItems: 'center',
                                        justifyContent: 'center',
                                        background: 'linear-gradient(135deg, var(--academy-bg-dark) 0%, var(--academy-accent-muted) 100%)'
                                    }}>
                                        <PlayIcon />
                                    </div>
                                )}
                                <div className="continue-play-overlay">
                                    <div className="continue-play-btn">
                                        <PlayIcon />
                                    </div>
                                </div>
                            </div>
                            <div className="continue-content">
                                <div className="continue-module">
                                    {continueWatching.moduleTitle}
                                </div>
                                <h3 className="continue-title">{continueWatching.title}</h3>
                                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--academy-text-muted)', fontSize: '0.9rem', marginBottom: '12px' }}>
                                    <ClockIcon /> {formatDuration(continueWatching.duration_seconds)}
                                </div>
                                <div className="continue-progress">
                                    <ProgressBar
                                        progress={
                                            continueWatching.progress?.progress_seconds && continueWatching.duration_seconds
                                                ? (continueWatching.progress.progress_seconds / continueWatching.duration_seconds) * 100
                                                : 0
                                        }
                                        label="Lesson progress"
                                        size="sm"
                                    />
                                </div>
                            </div>
                        </div>
                    </div>
                )}

                {/* My Courses */}
                <div className="dashboard-section">
                    <h2 className="section-title">
                        <BookIcon /> My Courses
                    </h2>
                    <div className="courses-grid">
                        {courses?.map(course => {
                            const courseProgress = getCourseProgress(course);
                            const totalLessons = course.modules?.reduce((acc, m) => acc + (m.lessons?.length || 0), 0) || 0;

                            return (
                                <div
                                    key={course.id}
                                    className="course-card"
                                    onClick={() => onCourseSelect(course)}
                                >
                                    <div className="course-thumbnail">
                                        {course.thumbnail_url ? (
                                            <img src={course.thumbnail_url} alt={course.title} />
                                        ) : (
                                            <div style={{
                                                width: '100%',
                                                height: '100%',
                                                display: 'flex',
                                                alignItems: 'center',
                                                justifyContent: 'center'
                                            }}>
                                                <BookIcon />
                                            </div>
                                        )}
                                        {courseProgress === 100 && (
                                            <span className="course-badge" style={{ background: 'var(--academy-success)' }}>
                                                Completed
                                            </span>
                                        )}
                                        {courseProgress > 0 && courseProgress < 100 && (
                                            <span className="course-badge">
                                                {courseProgress}% Complete
                                            </span>
                                        )}
                                    </div>
                                    <div className="course-content">
                                        <h3 className="course-title">{course.title}</h3>
                                        <p className="course-description">{course.description}</p>
                                        <div className="course-meta">
                                            <span className="course-lessons">
                                                {totalLessons} lesson{totalLessons !== 1 ? 's' : ''}
                                            </span>
                                            <ProgressBarMini progress={courseProgress} />
                                        </div>
                                    </div>
                                </div>
                            );
                        })}

                        {(!courses || courses.length === 0) && (
                            <div style={{
                                gridColumn: '1 / -1',
                                textAlign: 'center',
                                padding: '60px 20px',
                                background: 'var(--academy-bg-card)',
                                borderRadius: '12px',
                                border: '1px solid var(--academy-border)'
                            }}>
                                <BookIcon />
                                <h3 style={{ marginTop: '16px', color: 'var(--academy-text-primary)' }}>
                                    No courses yet
                                </h3>
                                <p style={{ color: 'var(--academy-text-secondary)', marginTop: '8px' }}>
                                    Your enrolled courses will appear here.
                                </p>
                            </div>
                        )}
                    </div>
                </div>
            </main>
        </div>
    );
};

// Make component available globally
window.Dashboard = Dashboard;
