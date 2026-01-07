/**
 * LessonView Component
 * Video player page with progress tracking, multi-part tabs, and navigation
 */

const LessonView = ({
    course,
    lesson,
    modules,
    progress,
    onLessonSelect,
    onBack,
    onProgressUpdate,
    onMarkComplete
}) => {
    const [currentPartIndex, setCurrentPartIndex] = React.useState(0);
    const [player, setPlayer] = React.useState(null);
    const [isPlaying, setIsPlaying] = React.useState(false);
    const [currentTime, setCurrentTime] = React.useState(0);
    const videoRef = React.useRef(null);
    const progressIntervalRef = React.useRef(null);

    // Get video parts - if no parts, create single part from lesson
    const videoParts = lesson.video_parts && lesson.video_parts.length > 0
        ? lesson.video_parts
        : [{
            title: lesson.title,
            video_url: lesson.video_url,
            duration_seconds: lesson.duration_seconds
          }];

    const currentPart = videoParts[currentPartIndex];

    // Initialize Plyr player
    React.useEffect(() => {
        if (videoRef.current && window.Plyr) {
            const plyrInstance = new Plyr(videoRef.current, {
                controls: [
                    'play-large', 'rewind', 'play', 'fast-forward',
                    'progress', 'current-time', 'duration', 'mute',
                    'volume', 'settings', 'pip', 'fullscreen'
                ],
                settings: ['quality', 'speed'],
                speed: { selected: 1, options: [0.5, 0.75, 1, 1.25, 1.5, 2] },
                keyboard: { focused: true, global: true }
            });

            setPlayer(plyrInstance);

            // Event listeners
            plyrInstance.on('play', () => setIsPlaying(true));
            plyrInstance.on('pause', () => setIsPlaying(false));
            plyrInstance.on('timeupdate', () => {
                setCurrentTime(plyrInstance.currentTime);
            });

            // Restore progress if available
            const lessonProgress = progress?.[lesson.id];
            if (lessonProgress?.progress_seconds && !lessonProgress.completed) {
                plyrInstance.once('loadeddata', () => {
                    plyrInstance.currentTime = lessonProgress.progress_seconds;
                });
            }

            return () => {
                plyrInstance.destroy();
            };
        }
    }, [lesson.id, currentPartIndex]);

    // Progress tracking - send update every 30 seconds
    React.useEffect(() => {
        if (isPlaying) {
            progressIntervalRef.current = setInterval(() => {
                if (onProgressUpdate && currentTime > 0) {
                    onProgressUpdate(lesson.id, {
                        progress_seconds: Math.floor(currentTime),
                        part_index: currentPartIndex,
                        total_parts: videoParts.length
                    });
                }
            }, 30000); // 30 seconds
        }

        return () => {
            if (progressIntervalRef.current) {
                clearInterval(progressIntervalRef.current);
            }
        };
    }, [isPlaying, currentTime, lesson.id, currentPartIndex]);

    // Save progress on unmount or lesson change
    React.useEffect(() => {
        return () => {
            if (onProgressUpdate && currentTime > 0) {
                onProgressUpdate(lesson.id, {
                    progress_seconds: Math.floor(currentTime),
                    part_index: currentPartIndex,
                    total_parts: videoParts.length
                });
            }
        };
    }, [lesson.id]);

    // Find previous/next lesson
    const getAdjacentLessons = () => {
        const allLessons = [];
        modules.forEach(module => {
            module.lessons?.forEach(l => allLessons.push(l));
        });

        const currentIndex = allLessons.findIndex(l => l.id === lesson.id);
        return {
            prev: currentIndex > 0 ? allLessons[currentIndex - 1] : null,
            next: currentIndex < allLessons.length - 1 ? allLessons[currentIndex + 1] : null
        };
    };

    const { prev: prevLesson, next: nextLesson } = getAdjacentLessons();

    const isCompleted = progress?.[lesson.id]?.completed;

    // Handle mark complete
    const handleMarkComplete = () => {
        if (onMarkComplete) {
            onMarkComplete(lesson.id, !isCompleted);
        }
    };

    // Get current module for breadcrumb
    const getCurrentModule = () => {
        for (const module of modules) {
            if (module.lessons?.some(l => l.id === lesson.id)) {
                return module;
            }
        }
        return null;
    };

    const currentModule = getCurrentModule();

    // Icons
    const LogoIcon = () => (
        <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 4L4 12V28L20 36L36 28V12L20 4Z" stroke="currentColor" strokeWidth="2" fill="none"/>
            <path d="M20 8L8 14V26L20 32L32 26V14L20 8Z" fill="currentColor" opacity="0.3"/>
            <path d="M14 18L20 14L26 18V24L20 28L14 24V18Z" fill="currentColor"/>
        </svg>
    );

    const ArrowLeftIcon = () => (
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M19 12H5M12 19l-7-7 7-7" />
        </svg>
    );

    const ArrowRightIcon = () => (
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M5 12h14M12 5l7 7-7 7" />
        </svg>
    );

    const CheckIcon = () => (
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M20 6L9 17l-5-5" />
        </svg>
    );

    const GridIcon = () => (
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <rect x="3" y="3" width="7" height="7" />
            <rect x="14" y="3" width="7" height="7" />
            <rect x="14" y="14" width="7" height="7" />
            <rect x="3" y="14" width="7" height="7" />
        </svg>
    );

    const formatDuration = (seconds) => {
        if (!seconds) return '--:--';
        const mins = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${mins}:${secs.toString().padStart(2, '0')}`;
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
                    <button className="btn btn-ghost" onClick={onBack}>
                        <GridIcon />
                        Course Overview
                    </button>
                </div>
            </header>

            {/* Lesson View Layout */}
            <div className="lesson-view">
                {/* Main Video Area */}
                <div className="lesson-main">
                    {/* Video Parts Tabs (if multiple parts) */}
                    {videoParts.length > 1 && (
                        <div className="video-parts-tabs">
                            {videoParts.map((part, index) => {
                                const partCompleted = progress?.[lesson.id]?.completed_parts?.includes(index);
                                return (
                                    <button
                                        key={index}
                                        className={`video-part-tab ${currentPartIndex === index ? 'active' : ''} ${partCompleted ? 'completed' : ''}`}
                                        onClick={() => setCurrentPartIndex(index)}
                                    >
                                        Part {index + 1}: {part.title || `Section ${index + 1}`}
                                    </button>
                                );
                            })}
                        </div>
                    )}

                    {/* Video Container */}
                    <div className="video-container">
                        <video
                            ref={videoRef}
                            key={`${lesson.id}-${currentPartIndex}`}
                            playsInline
                        >
                            <source src={currentPart.video_url} type="video/mp4" />
                            Your browser does not support the video tag.
                        </video>
                    </div>

                    {/* Controls Bar */}
                    <div className="lesson-controls">
                        <div className="lesson-info-bar">
                            <div className="lesson-breadcrumb">
                                {course.title} / {currentModule?.title}
                            </div>
                            <h1 className="lesson-current-title">
                                {lesson.title}
                                {videoParts.length > 1 && ` - Part ${currentPartIndex + 1}`}
                            </h1>
                        </div>

                        <div className="lesson-nav-buttons">
                            {/* Mark Complete Button */}
                            <button
                                className={`mark-complete-btn ${isCompleted ? 'completed' : ''}`}
                                onClick={handleMarkComplete}
                            >
                                <CheckIcon />
                                {isCompleted ? 'Completed' : 'Mark Complete'}
                            </button>

                            {/* Previous Lesson */}
                            <button
                                className="btn btn-secondary"
                                onClick={() => prevLesson && onLessonSelect(prevLesson)}
                                disabled={!prevLesson}
                            >
                                <ArrowLeftIcon /> Previous
                            </button>

                            {/* Next Lesson */}
                            <button
                                className="btn btn-primary"
                                onClick={() => nextLesson && onLessonSelect(nextLesson)}
                                disabled={!nextLesson}
                            >
                                Next <ArrowRightIcon />
                            </button>
                        </div>
                    </div>
                </div>

                {/* Sidebar - Lesson List */}
                <LessonSidebar
                    modules={modules}
                    progress={progress}
                    currentLessonId={lesson.id}
                    onLessonSelect={onLessonSelect}
                />
            </div>
        </div>
    );
};

// Make component available globally
window.LessonView = LessonView;
