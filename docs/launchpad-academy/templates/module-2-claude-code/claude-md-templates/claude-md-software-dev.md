# CLAUDE.md Template: Software Development

Copy this template to your project root and customize for your team.

---

```markdown
# Software Development Claude Configuration

## About This Project

- **Project Name**: [Your Project Name]
- **Description**: [One-line description of what it does]
- **Repository**: [GitHub/GitLab URL]
- **Documentation**: [Link to docs]
- **Production URL**: [Live site/app URL]

## About Me

- **Name**: [Your Name]
- **Role**: [Developer / Lead / Architect / Founder]
- **Focus Areas**: [Frontend / Backend / Full-stack / DevOps]

---

## Tech Stack

### Frontend
- **Framework**: [Next.js / React / Vue / Angular / Svelte]
- **Language**: [TypeScript / JavaScript]
- **Styling**: [Tailwind CSS / CSS Modules / Styled Components / Sass]
- **State Management**: [Zustand / Redux / Jotai / Context API]
- **Testing**: [Jest / Vitest / Playwright / Cypress]

### Backend
- **Runtime**: [Node.js / Python / Go / Rust]
- **Framework**: [Express / Fastify / FastAPI / Gin]
- **API Style**: [REST / GraphQL / tRPC]
- **Authentication**: [NextAuth / Auth0 / Clerk / Custom JWT]

### Database
- **Primary**: [PostgreSQL / MySQL / MongoDB]
- **ORM/Client**: [Prisma / Drizzle / TypeORM / Mongoose]
- **Cache**: [Redis / Memcached]
- **Search**: [Elasticsearch / Algolia / Meilisearch]

### Infrastructure
- **Hosting**: [Vercel / AWS / GCP / Azure / DigitalOcean]
- **CI/CD**: [GitHub Actions / GitLab CI / CircleCI]
- **Containers**: [Docker / Kubernetes]
- **CDN**: [CloudFlare / CloudFront / Vercel Edge]

---

## Code Style & Conventions

### General Principles
- Write TypeScript with strict mode enabled
- Prefer functional and declarative patterns
- Use meaningful variable/function names (no abbreviations)
- Keep functions small and single-purpose
- Write self-documenting code; add comments for "why" not "what"

### File Naming
- Components: `PascalCase.tsx` (e.g., `UserProfile.tsx`)
- Utilities: `camelCase.ts` (e.g., `formatDate.ts`)
- Constants: `SCREAMING_SNAKE_CASE` (e.g., `API_ENDPOINTS.ts`)
- Test files: `*.test.ts` or `*.spec.ts`
- Types: `*.types.ts` or inline in component

### React/Next.js Specific
- Use functional components with hooks
- Prefer named exports over default exports
- Keep components in dedicated folders with index.ts
- Co-locate tests, styles, and types with components
- Use Server Components by default, Client Components when needed

### Code Organization
```
/src
  /app                 # Next.js App Router pages
  /components
    /ui                # Reusable UI primitives
    /features          # Feature-specific components
    /layouts           # Layout components
  /lib
    /api               # API client and utilities
    /db                # Database connection and queries
    /utils             # Helper functions
    /hooks             # Custom React hooks
    /types             # Shared TypeScript types
  /config              # Configuration files
  /styles              # Global styles
```

### Git Conventions
- Use conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`
- Keep commits atomic and focused
- Write descriptive commit messages
- Squash WIP commits before merging
- Always include Claude Code co-author line

---

## Common Tasks

### Starting Development
```bash
# Install dependencies
npm install

# Set up environment
cp .env.example .env.local
# Edit .env.local with your values

# Start development server
npm run dev
```

### Database Operations
```bash
# Generate Prisma client after schema changes
npx prisma generate

# Run migrations
npx prisma migrate dev

# Open Prisma Studio
npx prisma studio

# Seed database
npx prisma db seed
```

### Testing
```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run e2e tests
npm run test:e2e

# Check coverage
npm run test:coverage
```

### Deployment
```bash
# Build for production
npm run build

# Deploy to staging
npm run deploy:staging

# Deploy to production
npm run deploy:prod
```

---

## Key Files Reference

| File | Purpose |
|------|---------|
| `/src/lib/db.ts` | Database connection and Prisma client |
| `/src/lib/auth.ts` | Authentication configuration |
| `/src/lib/api/client.ts` | API client for external services |
| `/src/config/constants.ts` | App-wide constants |
| `/src/types/index.ts` | Shared TypeScript types |
| `/.env.example` | Environment variable template |
| `/prisma/schema.prisma` | Database schema |

---

## API Structure

### Internal API Routes
```
/api
  /auth
    /[...nextauth]      # NextAuth handlers
  /users
    /route.ts           # GET (list), POST (create)
    /[id]/route.ts      # GET, PUT, DELETE by ID
  /[resource]
    /route.ts           # Collection endpoints
    /[id]/route.ts      # Item endpoints
```

### External APIs Used
- **[Service Name]**: [Purpose, rate limits, docs link]
- **[Service Name]**: [Purpose, rate limits, docs link]

---

## Environment Variables

### Required
```env
DATABASE_URL=           # PostgreSQL connection string
NEXTAUTH_SECRET=        # Auth encryption key
NEXTAUTH_URL=           # Base URL for auth
```

### Optional / Feature Flags
```env
STRIPE_SECRET_KEY=      # Payments (if enabled)
SENDGRID_API_KEY=       # Email service
ANALYTICS_ID=           # Analytics tracking
FEATURE_NEW_UI=         # Feature flag
```

---

## Common Patterns

### API Route Handler
```typescript
// Standard pattern for API routes
export async function GET(request: Request) {
  try {
    const data = await db.resource.findMany();
    return Response.json(data);
  } catch (error) {
    console.error('Failed to fetch:', error);
    return Response.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
```

### Server Component Data Fetching
```typescript
// Fetch data directly in Server Components
async function Page() {
  const data = await db.resource.findMany();
  return <Component data={data} />;
}
```

### Error Handling
```typescript
// Wrap async operations
try {
  const result = await riskyOperation();
  return { success: true, data: result };
} catch (error) {
  if (error instanceof KnownError) {
    return { success: false, error: error.message };
  }
  throw error; // Re-throw unknown errors
}
```

---

## Claude Instructions

### When Writing Code
- Follow the code style conventions above
- Include proper TypeScript types (no `any`)
- Add error handling for all async operations
- Write tests for new functionality
- Update relevant documentation

### When Reviewing Code
- Check for TypeScript errors
- Verify error handling exists
- Look for security issues (injection, XSS, etc.)
- Check for performance concerns
- Ensure consistent naming

### When Debugging
- Start with error message analysis
- Check relevant logs
- Verify environment variables
- Test with minimal reproduction
- Document findings

### Do NOT
- Use `any` type without explicit permission
- Skip error handling
- Commit console.log statements
- Hardcode secrets or credentials
- Modify production directly

---

## Deployment Information

### Environments
| Environment | URL | Branch | Auto-deploy |
|------------|-----|--------|-------------|
| Development | localhost:3000 | - | - |
| Staging | staging.example.com | `develop` | Yes |
| Production | example.com | `main` | Manual |

### Deployment Checklist
1. [ ] All tests passing
2. [ ] No TypeScript errors
3. [ ] Environment variables set
4. [ ] Database migrations run
5. [ ] Monitoring configured
6. [ ] Rollback plan ready

---

## Troubleshooting

### Common Issues

**Build fails with type errors**
- Run `npm run typecheck` to see all errors
- Check for missing type definitions
- Ensure `tsconfig.json` is correct

**Database connection issues**
- Verify `DATABASE_URL` format
- Check network/firewall rules
- Ensure database is running

**Auth not working**
- Check `NEXTAUTH_URL` matches your domain
- Verify `NEXTAUTH_SECRET` is set
- Check provider configuration

---

## Quick Commands for Claude

```
"Review the code in [file] for bugs and improvements"
"Write tests for [component/function]"
"Refactor [file] to improve readability"
"Create a new API endpoint for [resource]"
"Add error handling to [file]"
"Update the types in [file] to match the new schema"
"Help me debug this error: [paste error]"
```
```

---

## How to Use This Template

1. **Copy the content** between the markdown code fences
2. **Create** `CLAUDE.md` in your project root
3. **Customize** the tech stack section for your project
4. **Fill in** your actual file structure and patterns
5. **Update** as your codebase evolves

## Tips for Development Teams

- Keep the file in version control
- Update when tech stack changes
- Add project-specific patterns as they emerge
- Include onboarding information for new team members
- Reference from PR templates
