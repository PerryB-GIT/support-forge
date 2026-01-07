# Developer CLAUDE.md Template
# Save this file as CLAUDE.md in your project root directory

## About Me
- **Name**: [Your Name]
- **Role**: [Full-Stack Developer / Frontend / Backend / DevOps]
- **Experience Level**: [Junior / Mid / Senior / Lead]
- **Primary Languages**: [JavaScript, Python, Go, etc.]

## Tech Stack Preferences

### Frontend
- **Framework**: [React / Vue / Angular / Svelte]
- **Styling**: [Tailwind CSS / CSS Modules / Styled Components]
- **State Management**: [Redux / Zustand / Jotai / Context]
- **Build Tool**: [Vite / Webpack / Next.js]

### Backend
- **Runtime**: [Node.js / Python / Go / Rust]
- **Framework**: [Express / FastAPI / Gin / Actix]
- **API Style**: [REST / GraphQL / tRPC]
- **Database**: [PostgreSQL / MongoDB / MySQL / DynamoDB]

### Infrastructure
- **Cloud Provider**: [AWS / GCP / Azure / Vercel]
- **Container**: [Docker / Podman]
- **Orchestration**: [Kubernetes / ECS / Cloud Run]
- **CI/CD**: [GitHub Actions / GitLab CI / Jenkins]

## Code Style Preferences

### General
- Use TypeScript over JavaScript when possible
- Prefer functional programming patterns
- Write self-documenting code with meaningful names
- Add comments only for complex business logic
- Maximum line length: [80 / 100 / 120] characters

### Naming Conventions
- **Variables**: camelCase
- **Constants**: SCREAMING_SNAKE_CASE
- **Functions**: camelCase (verb + noun)
- **Classes/Types**: PascalCase
- **Files**: kebab-case.ts or PascalCase.tsx for components

### Code Organization
- Group imports: external, internal, relative
- Keep functions under [50] lines
- One component per file for React
- Colocate tests with source files

### Error Handling
- Always use try-catch for async operations
- Create custom error classes for domain errors
- Log errors with context (user ID, request ID)
- Never swallow errors silently

## Git Workflow

### Branch Naming
- `feature/[ticket-id]-short-description`
- `fix/[ticket-id]-bug-description`
- `hotfix/critical-issue`
- `refactor/area-of-refactor`

### Commit Messages
Use conventional commits:
- `feat: add user authentication flow`
- `fix: resolve null pointer in payment processing`
- `docs: update API documentation`
- `refactor: extract validation logic`
- `test: add unit tests for user service`
- `chore: update dependencies`

### PR Guidelines
- Keep PRs under 400 lines when possible
- Include description of changes
- Link related issues
- Add screenshots for UI changes

## Testing Standards

### Unit Tests
- Use [Jest / Vitest / pytest] for unit tests
- Aim for [80%] code coverage
- Test edge cases and error paths
- Mock external dependencies

### Integration Tests
- Test API endpoints end-to-end
- Use test database for data operations
- Clean up test data after runs

### E2E Tests
- Use [Playwright / Cypress] for critical paths
- Test happy path and key error scenarios
- Run in CI before merge

## Project Structure
```
src/
├── components/     # UI components
├── hooks/          # Custom React hooks
├── services/       # API and external service calls
├── utils/          # Helper functions
├── types/          # TypeScript type definitions
├── constants/      # App constants
├── config/         # Configuration files
└── __tests__/      # Test files
```

## Environment Setup

### Required Tools
- Node.js v[20]+
- [pnpm / npm / yarn] as package manager
- Docker Desktop
- [VS Code / WebStorm / Neovim]

### VS Code Extensions
- ESLint
- Prettier
- GitLens
- Error Lens
- Thunder Client

## Common Commands
```bash
# Development
[npm/pnpm] run dev          # Start dev server
[npm/pnpm] run build        # Production build
[npm/pnpm] run test         # Run tests
[npm/pnpm] run lint         # Lint code
[npm/pnpm] run type-check   # TypeScript check

# Database
[npm/pnpm] run db:migrate   # Run migrations
[npm/pnpm] run db:seed      # Seed database
[npm/pnpm] run db:reset     # Reset database

# Docker
docker-compose up -d        # Start services
docker-compose logs -f      # View logs
```

## API Design Guidelines

### REST Endpoints
- Use plural nouns: `/users`, `/orders`
- Use HTTP methods correctly: GET, POST, PUT, PATCH, DELETE
- Version APIs: `/api/v1/users`
- Return appropriate status codes

### Response Format
```json
{
  "success": true,
  "data": {},
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 100
  }
}
```

### Error Response
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "details": []
  }
}
```

## Security Practices
- Never commit secrets or API keys
- Use environment variables for configuration
- Validate and sanitize all user input
- Use parameterized queries for database
- Implement rate limiting on public APIs
- Keep dependencies updated

## Performance Guidelines
- Lazy load components and routes
- Optimize images (WebP, proper sizing)
- Implement caching strategies
- Use database indexes appropriately
- Monitor and optimize N+1 queries

## Documentation Requirements
- README.md for project setup
- API documentation (OpenAPI/Swagger)
- Architecture decision records (ADRs)
- Inline JSDoc for public functions
