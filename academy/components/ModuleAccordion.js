/**
 * ModuleAccordion Component
 * Expandable module list showing lessons within each module
 */

const ModuleAccordion = ({ modules, progress, currentLessonId, onLessonSelect }) => {
    const [expandedModules, setExpandedModules] = React.useState([]);

    // Auto-expand module containing current lesson
    React.useEffect(() => {
        if (currentLessonId) {
            const moduleWithCurrentLesson = modules.find(m =>
                m.lessons.some(l => l.id === currentLessonId)
            );
            if (moduleWithCurrentLesson && !expandedModules.includes(moduleWithCurrentLesson.id)) {
                setExpandedModules(prev => [...prev, moduleWithCurrentLesson.id]);
            }
        }
    }, [currentLessonId, modules]);

    const toggleModule = (moduleId) => {
        setExpandedModules(prev =>
            prev.includes(moduleId)
                ? prev.filter(id => id !== moduleId)
                : [...prev, moduleId]
        );
    };

    const getModuleProgress = (module) => {
        if (!progress || !module.lessons.length) return 0;
        const completedLessons = module.lessons.filter(lesson =>
            progress[lesson.id]?.completed
        ).length;
        return (completedLessons / module.lessons.length) * 100;
    };

    const getLessonStatus = (lessonId) => {
        if (!progress || !progress[lessonId]) return 'pending';
        if (progress[lessonId].completed) return 'completed';
        if (progress[lessonId].progress_seconds > 0) return 'in-progress';
        return 'pending';
    };

    const isModuleCompleted = (module) => {
        return module.lessons.every(lesson => progress?.[lesson.id]?.completed);
    };

    const formatDuration = (seconds) => {
        if (!seconds) return '--:--';
        const mins = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${mins}:${secs.toString().padStart(2, '0')}`;
    };

    // Icons
    const ChevronIcon = () => (
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M6 9l6 6 6-6" />
        </svg>
    );

    const CheckIcon = () => (
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3">
            <path d="M20 6L9 17l-5-5" />
        </svg>
    );

    const PlayIcon = () => (
        <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor">
            <path d="M8 5v14l11-7z" />
        </svg>
    );

    return (
        <div className="module-list">
            {modules.map((module, moduleIndex) => {
                const isExpanded = expandedModules.includes(module.id);
                const moduleProgress = getModuleProgress(module);
                const moduleCompleted = isModuleCompleted(module);

                return (
                    <div
                        key={module.id}
                        className={`module-item ${isExpanded ? 'active' : ''}`}
                    >
                        <div
                            className="module-header"
                            onClick={() => toggleModule(module.id)}
                        >
                            <div className="module-header-left">
                                <div className={`module-number ${moduleCompleted ? 'completed' : ''}`}>
                                    {moduleCompleted ? <CheckIcon /> : moduleIndex + 1}
                                </div>
                                <div>
                                    <div className="module-title">{module.title}</div>
                                    <div className="module-meta">
                                        {module.lessons.length} lesson{module.lessons.length !== 1 ? 's' : ''}
                                        {module.description && ` - ${module.description}`}
                                    </div>
                                </div>
                            </div>
                            <div className="module-header-right">
                                <div className="module-progress-mini">
                                    <ProgressBarMini progress={moduleProgress} />
                                </div>
                                <div className="module-chevron">
                                    <ChevronIcon />
                                </div>
                            </div>
                        </div>

                        <div className="module-content">
                            <div className="lesson-list">
                                {module.lessons.map((lesson, lessonIndex) => {
                                    const status = getLessonStatus(lesson.id);
                                    const isActive = lesson.id === currentLessonId;
                                    const hasMultipleParts = lesson.video_parts && lesson.video_parts.length > 1;

                                    return (
                                        <div
                                            key={lesson.id}
                                            className={`lesson-item ${isActive ? 'active' : ''}`}
                                            onClick={() => onLessonSelect(lesson)}
                                        >
                                            <div className={`lesson-status ${status}`}>
                                                {status === 'completed' && <CheckIcon />}
                                                {status === 'in-progress' && <PlayIcon />}
                                            </div>
                                            <div className="lesson-info">
                                                <div className="lesson-title">
                                                    {moduleIndex + 1}.{lessonIndex + 1} {lesson.title}
                                                </div>
                                                <div className="lesson-duration">
                                                    {formatDuration(lesson.duration_seconds)}
                                                </div>
                                            </div>
                                            {hasMultipleParts && (
                                                <div className="lesson-parts-badge">
                                                    {lesson.video_parts.length} parts
                                                </div>
                                            )}
                                        </div>
                                    );
                                })}
                            </div>
                        </div>
                    </div>
                );
            })}
        </div>
    );
};

// Sidebar version for lesson view
const LessonSidebar = ({ modules, progress, currentLessonId, onLessonSelect }) => {
    const CheckIcon = () => (
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3">
            <path d="M20 6L9 17l-5-5" />
        </svg>
    );

    const formatDuration = (seconds) => {
        if (!seconds) return '--:--';
        const mins = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${mins}:${secs.toString().padStart(2, '0')}`;
    };

    // Flatten all lessons with their module context
    const allLessons = modules.flatMap((module, moduleIndex) =>
        module.lessons.map((lesson, lessonIndex) => ({
            ...lesson,
            moduleTitle: module.title,
            moduleIndex,
            lessonIndex,
            fullNumber: `${moduleIndex + 1}.${lessonIndex + 1}`
        }))
    );

    return (
        <div className="lesson-sidebar">
            <div className="lesson-sidebar-header">
                <div className="lesson-sidebar-title">Course Content</div>
                <ProgressBarMini
                    progress={
                        allLessons.length > 0
                            ? (allLessons.filter(l => progress?.[l.id]?.completed).length / allLessons.length) * 100
                            : 0
                    }
                />
            </div>
            <div className="sidebar-lesson-list">
                {allLessons.map((lesson) => {
                    const isCompleted = progress?.[lesson.id]?.completed;
                    const isActive = lesson.id === currentLessonId;

                    return (
                        <div
                            key={lesson.id}
                            className={`sidebar-lesson-item ${isActive ? 'active' : ''}`}
                            onClick={() => onLessonSelect(lesson)}
                        >
                            <div className={`sidebar-lesson-number ${isCompleted ? 'completed' : ''}`}>
                                {isCompleted ? <CheckIcon /> : lesson.fullNumber}
                            </div>
                            <div className="sidebar-lesson-title">{lesson.title}</div>
                            <div className="sidebar-lesson-duration">
                                {formatDuration(lesson.duration_seconds)}
                            </div>
                        </div>
                    );
                })}
            </div>
        </div>
    );
};

// Make components available globally
window.ModuleAccordion = ModuleAccordion;
window.LessonSidebar = LessonSidebar;
