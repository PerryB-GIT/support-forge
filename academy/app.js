/**
 * AI Launchpad Academy - Main Application
 * React-based course portal with JWT authentication
 */

const API_BASE = '/api/academy';

// API Helper with auth
const api = {
    getToken: () => localStorage.getItem('academy_token'),

    async request(endpoint, options = {}) {
        const token = this.getToken();
        const headers = {
            'Content-Type': 'application/json',
            ...(token && { 'Authorization': `Bearer ${token}` }),
            ...options.headers
        };

        try {
            const response = await fetch(`${API_BASE}${endpoint}`, {
                ...options,
                headers
            });

            if (response.status === 401) {
                // Token expired - try refresh
                const refreshed = await this.refreshToken();
                if (refreshed) {
                    // Retry with new token
                    headers['Authorization'] = `Bearer ${this.getToken()}`;
                    return fetch(`${API_BASE}${endpoint}`, { ...options, headers });
                }
                // Refresh failed - logout
                localStorage.removeItem('academy_token');
                localStorage.removeItem('academy_refresh_token');
                localStorage.removeItem('academy_user');
                window.location.reload();
            }

            return response;
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    },

    async refreshToken() {
        const refreshToken = localStorage.getItem('academy_refresh_token');
        if (!refreshToken) return false;

        try {
            const response = await fetch(`${API_BASE}/auth/refresh`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ refreshToken })
            });

            if (response.ok) {
                const data = await response.json();
                localStorage.setItem('academy_token', data.token);
                return true;
            }
        } catch (error) {
            console.error('Token refresh failed:', error);
        }
        return false;
    },

    async get(endpoint) {
        return this.request(endpoint);
    },

    async post(endpoint, data) {
        return this.request(endpoint, {
            method: 'POST',
            body: JSON.stringify(data)
        });
    },

    async put(endpoint, data) {
        return this.request(endpoint, {
            method: 'PUT',
            body: JSON.stringify(data)
        });
    }
};

// Toast notification system
const Toast = {
    container: null,

    init() {
        if (!this.container) {
            this.container = document.createElement('div');
            this.container.className = 'toast-container';
            document.body.appendChild(this.container);
        }
    },

    show(message, type = 'info', duration = 4000) {
        this.init();

        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        toast.textContent = message;

        this.container.appendChild(toast);

        setTimeout(() => {
            toast.style.animation = 'slideIn 0.3s ease reverse';
            setTimeout(() => toast.remove(), 300);
        }, duration);
    },

    success(message) {
        this.show(message, 'success');
    },

    error(message) {
        this.show(message, 'error');
    }
};

// Main App Component
const AcademyApp = () => {
    // App state
    const [view, setView] = React.useState('loading'); // loading, login, register, dashboard, course, lesson
    const [user, setUser] = React.useState(null);
    const [courses, setCourses] = React.useState([]);
    const [progress, setProgress] = React.useState({});
    const [currentCourse, setCurrentCourse] = React.useState(null);
    const [currentLesson, setCurrentLesson] = React.useState(null);
    const [loading, setLoading] = React.useState(true);

    // Check authentication on mount
    React.useEffect(() => {
        checkAuth();
    }, []);

    const checkAuth = async () => {
        const token = localStorage.getItem('academy_token');
        const savedUser = localStorage.getItem('academy_user');

        if (token && savedUser) {
            try {
                setUser(JSON.parse(savedUser));
                await loadUserData();
                setView('dashboard');
            } catch (error) {
                console.error('Auth check failed:', error);
                setView('login');
            }
        } else {
            setView('login');
        }
        setLoading(false);
    };

    const loadUserData = async () => {
        try {
            // Load courses
            const coursesRes = await api.get('/courses');
            if (coursesRes.ok) {
                const coursesData = await coursesRes.json();
                setCourses(coursesData.courses || []);
            }

            // Load progress
            const progressRes = await api.get('/progress');
            if (progressRes.ok) {
                const progressData = await progressRes.json();
                setProgress(progressData.progress || {});
            }
        } catch (error) {
            console.error('Failed to load user data:', error);
            Toast.error('Failed to load course data');
        }
    };

    // Auth handlers
    const handleLogin = async (userData, token) => {
        setUser(userData);
        await loadUserData();
        setView('dashboard');
        Toast.success(`Welcome back, ${userData.name}!`);
    };

    const handleRegister = async (userData, token) => {
        setUser(userData);
        await loadUserData();
        setView('dashboard');
        Toast.success(`Welcome to the Academy, ${userData.name}!`);
    };

    const handleLogout = () => {
        localStorage.removeItem('academy_token');
        localStorage.removeItem('academy_refresh_token');
        localStorage.removeItem('academy_user');
        setUser(null);
        setCourses([]);
        setProgress({});
        setCurrentCourse(null);
        setCurrentLesson(null);
        setView('login');
        Toast.success('Signed out successfully');
    };

    // Navigation handlers
    const handleCourseSelect = (course, resumeLesson = null) => {
        setCurrentCourse(course);
        if (resumeLesson) {
            setCurrentLesson(resumeLesson);
            setView('lesson');
        } else {
            setCurrentLesson(null);
            setView('course');
        }
    };

    const handleLessonSelect = (lesson) => {
        setCurrentLesson(lesson);
        setView('lesson');
    };

    const handleBackToDashboard = () => {
        setCurrentCourse(null);
        setCurrentLesson(null);
        setView('dashboard');
    };

    const handleBackToCourse = () => {
        setCurrentLesson(null);
        setView('course');
    };

    // Progress handlers
    const handleProgressUpdate = async (lessonId, progressData) => {
        try {
            const response = await api.post(`/progress/${lessonId}`, progressData);
            if (response.ok) {
                // Update local progress
                setProgress(prev => ({
                    ...prev,
                    [lessonId]: {
                        ...prev[lessonId],
                        ...progressData,
                        last_watched_at: new Date().toISOString()
                    }
                }));
            }
        } catch (error) {
            console.error('Failed to save progress:', error);
        }
    };

    const handleMarkComplete = async (lessonId, completed) => {
        try {
            const response = await api.post(`/progress/${lessonId}/complete`, { completed });
            if (response.ok) {
                setProgress(prev => ({
                    ...prev,
                    [lessonId]: {
                        ...prev[lessonId],
                        completed,
                        completed_at: completed ? new Date().toISOString() : null
                    }
                }));
                Toast.success(completed ? 'Lesson marked as complete!' : 'Lesson marked as incomplete');
            }
        } catch (error) {
            console.error('Failed to mark complete:', error);
            Toast.error('Failed to update lesson status');
        }
    };

    // Render loading state
    if (loading || view === 'loading') {
        return (
            <div className="academy-loading">
                <div className="loading-spinner"></div>
                <p>Loading Academy...</p>
            </div>
        );
    }

    // Render based on current view
    switch (view) {
        case 'login':
            return (
                <LoginForm
                    onLogin={handleLogin}
                    onSwitchToRegister={() => setView('register')}
                />
            );

        case 'register':
            return (
                <RegisterForm
                    onRegister={handleRegister}
                    onSwitchToLogin={() => setView('login')}
                />
            );

        case 'dashboard':
            return (
                <Dashboard
                    user={user}
                    courses={courses}
                    progress={progress}
                    onCourseSelect={handleCourseSelect}
                    onLogout={handleLogout}
                />
            );

        case 'course':
            return (
                <CourseView
                    course={currentCourse}
                    progress={progress}
                    onLessonSelect={handleLessonSelect}
                    onBack={handleBackToDashboard}
                />
            );

        case 'lesson':
            return (
                <LessonView
                    course={currentCourse}
                    lesson={currentLesson}
                    modules={currentCourse?.modules || []}
                    progress={progress}
                    onLessonSelect={handleLessonSelect}
                    onBack={handleBackToCourse}
                    onProgressUpdate={handleProgressUpdate}
                    onMarkComplete={handleMarkComplete}
                />
            );

        default:
            return (
                <div className="academy-loading">
                    <p>Something went wrong. Please refresh the page.</p>
                </div>
            );
    }
};

// Initialize App
const initAcademy = () => {
    const root = ReactDOM.createRoot(document.getElementById('academy-root'));
    root.render(<AcademyApp />);
};

// Start when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAcademy);
} else {
    initAcademy();
}
