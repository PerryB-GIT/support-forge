/**
 * RegisterForm Component
 * User registration form for new academy accounts
 */

const RegisterForm = ({ onRegister, onSwitchToLogin }) => {
    const [formData, setFormData] = React.useState({
        name: '',
        email: '',
        password: '',
        confirmPassword: ''
    });
    const [error, setError] = React.useState('');
    const [loading, setLoading] = React.useState(false);
    const [showPassword, setShowPassword] = React.useState(false);
    const [passwordStrength, setPasswordStrength] = React.useState(0);

    // Update form field
    const updateField = (field, value) => {
        setFormData(prev => ({ ...prev, [field]: value }));
        if (field === 'password') {
            setPasswordStrength(calculatePasswordStrength(value));
        }
    };

    // Calculate password strength (0-4)
    const calculatePasswordStrength = (password) => {
        let strength = 0;
        if (password.length >= 8) strength++;
        if (password.match(/[a-z]/) && password.match(/[A-Z]/)) strength++;
        if (password.match(/\d/)) strength++;
        if (password.match(/[^a-zA-Z\d]/)) strength++;
        return strength;
    };

    const getStrengthLabel = () => {
        const labels = ['Very Weak', 'Weak', 'Fair', 'Good', 'Strong'];
        return labels[passwordStrength];
    };

    const getStrengthColor = () => {
        const colors = ['#EF4444', '#F59E0B', '#EAB308', '#84CC16', '#10B981'];
        return colors[passwordStrength];
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');

        // Validation
        if (formData.password !== formData.confirmPassword) {
            setError('Passwords do not match');
            return;
        }

        if (formData.password.length < 8) {
            setError('Password must be at least 8 characters');
            return;
        }

        setLoading(true);

        try {
            const response = await fetch('/api/academy/auth/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    name: formData.name,
                    email: formData.email,
                    password: formData.password
                })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Registration failed');
            }

            // Store tokens
            localStorage.setItem('academy_token', data.token);
            localStorage.setItem('academy_refresh_token', data.refreshToken);
            localStorage.setItem('academy_user', JSON.stringify(data.user));

            // Notify parent
            onRegister(data.user, data.token);
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

    const CheckIcon = () => (
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M20 6L9 17l-5-5" />
        </svg>
    );

    return (
        <div className="auth-container">
            <div className="auth-card">
                <a href="/" className="auth-logo">
                    <LogoIcon />
                    <span className="auth-logo-text">AI Launchpad Academy</span>
                </a>

                <h1 className="auth-title">Create Account</h1>
                <p className="auth-subtitle">Start your AI implementation journey today</p>

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
                        <label className="form-label" htmlFor="name">Full Name</label>
                        <input
                            id="name"
                            type="text"
                            className="form-input"
                            placeholder="John Doe"
                            value={formData.name}
                            onChange={(e) => updateField('name', e.target.value)}
                            required
                            autoComplete="name"
                        />
                    </div>

                    <div className="form-group">
                        <label className="form-label" htmlFor="email">Email Address</label>
                        <input
                            id="email"
                            type="email"
                            className="form-input"
                            placeholder="you@example.com"
                            value={formData.email}
                            onChange={(e) => updateField('email', e.target.value)}
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
                                placeholder="Create a strong password"
                                value={formData.password}
                                onChange={(e) => updateField('password', e.target.value)}
                                required
                                autoComplete="new-password"
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
                        {formData.password && (
                            <div style={{ marginTop: '8px' }}>
                                <div style={{
                                    display: 'flex',
                                    gap: '4px',
                                    marginBottom: '4px'
                                }}>
                                    {[0, 1, 2, 3].map(i => (
                                        <div
                                            key={i}
                                            style={{
                                                flex: 1,
                                                height: '4px',
                                                borderRadius: '2px',
                                                background: i < passwordStrength
                                                    ? getStrengthColor()
                                                    : 'var(--academy-bg-dark)'
                                            }}
                                        />
                                    ))}
                                </div>
                                <span style={{
                                    fontSize: '0.8rem',
                                    color: getStrengthColor()
                                }}>
                                    {getStrengthLabel()}
                                </span>
                            </div>
                        )}
                    </div>

                    <div className="form-group">
                        <label className="form-label" htmlFor="confirmPassword">Confirm Password</label>
                        <input
                            id="confirmPassword"
                            type={showPassword ? 'text' : 'password'}
                            className="form-input"
                            placeholder="Re-enter your password"
                            value={formData.confirmPassword}
                            onChange={(e) => updateField('confirmPassword', e.target.value)}
                            required
                            autoComplete="new-password"
                        />
                        {formData.confirmPassword && formData.password === formData.confirmPassword && (
                            <div className="form-success" style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                                <CheckIcon /> Passwords match
                            </div>
                        )}
                    </div>

                    <div style={{
                        marginBottom: '20px',
                        fontSize: '0.85rem',
                        color: 'var(--academy-text-muted)'
                    }}>
                        By creating an account, you agree to our{' '}
                        <a href="/terms.html" style={{ color: 'var(--academy-accent)' }}>Terms of Service</a>
                        {' '}and{' '}
                        <a href="/privacy.html" style={{ color: 'var(--academy-accent)' }}>Privacy Policy</a>.
                    </div>

                    <button
                        type="submit"
                        className="btn btn-primary btn-full btn-lg"
                        disabled={loading}
                    >
                        {loading ? (
                            <span style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                <span className="loading-spinner" style={{ width: '20px', height: '20px' }}></span>
                                Creating account...
                            </span>
                        ) : (
                            'Create Account'
                        )}
                    </button>
                </form>

                <p className="auth-footer">
                    Already have an account?{' '}
                    <a href="#" onClick={(e) => { e.preventDefault(); onSwitchToLogin(); }}>
                        Sign in
                    </a>
                </p>
            </div>
        </div>
    );
};

// Make component available globally
window.RegisterForm = RegisterForm;
