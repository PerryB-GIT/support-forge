/**
 * ProgressBar Component
 * Displays a visual progress indicator with percentage
 */

const ProgressBar = ({ progress = 0, showLabel = true, size = 'default', label = 'Progress' }) => {
    const percentage = Math.min(100, Math.max(0, progress));

    const sizeClass = {
        sm: 'progress-bar-sm',
        default: '',
        lg: 'progress-bar-lg'
    }[size] || '';

    return (
        <div className="progress-bar-wrapper">
            {showLabel && (
                <div className="progress-bar-label">
                    <span className="progress-bar-text">{label}</span>
                    <span className="progress-bar-percent">{Math.round(percentage)}%</span>
                </div>
            )}
            <div className={`progress-bar ${sizeClass}`}>
                <div
                    className="progress-bar-fill"
                    style={{ width: `${percentage}%` }}
                />
            </div>
        </div>
    );
};

// Mini progress bar for compact views
const ProgressBarMini = ({ progress = 0 }) => {
    const percentage = Math.min(100, Math.max(0, progress));

    return (
        <div className="progress-bar progress-bar-sm">
            <div
                className="progress-bar-fill"
                style={{ width: `${percentage}%` }}
            />
        </div>
    );
};

// Circular progress indicator
const CircularProgress = ({ progress = 0, size = 60, strokeWidth = 4 }) => {
    const percentage = Math.min(100, Math.max(0, progress));
    const radius = (size - strokeWidth) / 2;
    const circumference = radius * 2 * Math.PI;
    const offset = circumference - (percentage / 100) * circumference;

    return (
        <div className="circular-progress" style={{ width: size, height: size }}>
            <svg width={size} height={size}>
                <circle
                    className="circular-progress-bg"
                    stroke="var(--academy-bg-dark)"
                    fill="none"
                    strokeWidth={strokeWidth}
                    r={radius}
                    cx={size / 2}
                    cy={size / 2}
                />
                <circle
                    className="circular-progress-fill"
                    stroke="var(--academy-accent)"
                    fill="none"
                    strokeWidth={strokeWidth}
                    strokeLinecap="round"
                    r={radius}
                    cx={size / 2}
                    cy={size / 2}
                    style={{
                        strokeDasharray: circumference,
                        strokeDashoffset: offset,
                        transform: 'rotate(-90deg)',
                        transformOrigin: '50% 50%',
                        transition: 'stroke-dashoffset 0.5s ease'
                    }}
                />
            </svg>
            <div
                className="circular-progress-text"
                style={{
                    position: 'absolute',
                    top: '50%',
                    left: '50%',
                    transform: 'translate(-50%, -50%)',
                    fontSize: size * 0.22,
                    fontWeight: 600,
                    color: 'var(--academy-text-primary)'
                }}
            >
                {Math.round(percentage)}%
            </div>
        </div>
    );
};

// Make components available globally
window.ProgressBar = ProgressBar;
window.ProgressBarMini = ProgressBarMini;
window.CircularProgress = CircularProgress;
