/**
 * LoginForm Component
 * Email/password login form with JWT authentication
 */

const LoginForm = ({ onLogin, onSwitchToRegister }) => {
    const [email, setEmail] = React.useState('');
    const [password, setPassword] = React.useState('');
    const [error, setError] = React.useState('');
    const [loading, setLoading] = React.useState(false);
    const [showPassword, setShowPassword] = React.useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        try {
            const response = await fetch('/api/academy/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, password })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Login failed');
            }

            // Store tokens
            localStorage.setItem('academy_token', data.token);
            localStorage.setItem('academy_refresh_token', data.refreshToken);
            localStorage.setItem('academy_user', JSON.stringify(data.user));

            // Notify parent
            onLogin(data.user, data.token);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    // Icons
    const LogoIcon = () => (
        <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M20 4L4 12V28L20 36L36 28V12L20 4Z" stroke="currentColor" strokeWidth="2" fill="none"/>
            <path d="M20 8L8 14V26L20 32L32 26V14L20 8Z" fill="currentColor" opacity="0.3"/>
            <path d="M14 18L20 14L26 18V24L20 28L14 24V18Z" fill="currentColor"/>
        </svg>
    );

    const EyeIcon = () => (
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
            <circle cx="12" cy="12" r="3" />
        </svg>
    );

    const EyeOffIcon = () => (
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M17.94 17.94A10.07 10.07 0 0112 20c-7 0-11-8-11-8a18.45 18.45 0 015.06-5.94M9.9 4.24A9.12 9.12 0 0112 4c7 0 11 8 11 8a18.5 18.5 0 01-2.16 3.19m-6.72-1.07a3 3 0 11-4.24-4.24" />
            <line x1="1" y1="1" x2="23" y2="23" />
        </svg>
    );

    return (
        <div className="auth-container">
            <div className="auth-card">
                <a href="/" className="auth-logo">
                    <LogoIcon />
                    <span className="auth-logo-text">AI Launchpad Academy</span>
                </a>

                <h1 className="auth-title">Welcome Back</h1>
                <p className="auth-subtitle">Sign in to continue your learning journey</p>

                <form onSubmit={handleSubmit}>
                    {error && (
                        <div className="form-error mb-4" style={{
                            padding: '12px',
                            background: 'rgba(239, 68, 68, 0.1)',
                            borderRadius: '8px',
                            textAlign: 'center'
                        }}>
                            {error}
                        </div>
                    )}

                    <div className="form-group">
                        <label className="form-label" htmlFor="email">Email Address</label>
                        <input
                            id="email"
                            type="email"
                            className="form-input"
                            placeholder="you@example.com"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                            autoComplete="email"
                        />
                    </div>

                    <div className="form-group">
                        <label className="form-label" htmlFor="password">Password</label>
                        <div style={{ position: 'relative' }}>
                            <input
                                id="password"
                                type={showPassword ? 'text' : 'password'}
                                className="form-input"
                                placeholder="Enter your password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                                autoComplete="current-password"
                                style={{ paddingRight: '48px' }}
                            />
                            <button
                                type="button"
                                onClick={() => setShowPassword(!showPassword)}
                                style={{
                                    position: 'absolute',
                                    right: '12px',
                                    top: '50%',
                                    transform: 'translateY(-50%)',
                                    background: 'none',
                                    border: 'none',
                                    cursor: 'pointer',
                                    color: 'var(--academy-text-muted)',
                                    padding: '4px'
                                }}
                            >
                                {showPassword ? <EyeOffIcon /> : <EyeIcon />}
                            </button>
                        </div>
                    </div>

                    <div style={{ textAlign: 'right', marginBottom: '20px' }}>
                        <a
                            href="#"
                            style={{
                                color: 'var(--academy-accent)',
                                textDecoration: 'none',
                                fontSize: '0.9rem'
                            }}
                        >
                            Forgot password?
                        </a>
                    </div>

                    <button
                        type="submit"
                        className="btn btn-primary btn-full btn-lg"
                        disabled={loading}
                    >
                        {loading ? (
                            <span style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                <span className="loading-spinner" style={{ width: '20px', height: '20px' }}></span>
                                Signing in...
                            </span>
                        ) : (
                            'Sign In'
                        )}
                    </button>
                </form>

                <p className="auth-footer">
                    Don't have an account?{' '}
                    <a href="#" onClick={(e) => { e.preventDefault(); onSwitchToRegister(); }}>
                        Create one
                    </a>
                </p>

                <div className="auth-divider">
                    <span>Need help?</span>
                </div>

                <p style={{ textAlign: 'center', fontSize: '0.85rem', color: 'var(--academy-text-muted)' }}>
                    Contact <a href="mailto:support@support-forge.com" style={{ color: 'var(--academy-accent)' }}>
                        support@support-forge.com
                    </a>
                </p>
            </div>
        </div>
    );
};

// Make component available globally
window.LoginForm = LoginForm;
