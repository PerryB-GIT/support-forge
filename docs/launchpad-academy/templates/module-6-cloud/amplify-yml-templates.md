# AWS Amplify Build Configuration Templates

Ready-to-use `amplify.yml` configurations for common project types.

---

## What is amplify.yml?

The `amplify.yml` file controls how AWS Amplify builds and deploys your application. Place it in your project root directory.

---

## Next.js (App Router)

```yaml
# amplify.yml - Next.js with App Router
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm ci --cache .npm --prefer-offline
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: .next
    files:
      - '**/*'
  cache:
    paths:
      - .npm/**/*
      - .next/cache/**/*
      - node_modules/**/*
```

---

## Next.js (Static Export)

```yaml
# amplify.yml - Next.js Static Export
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm ci --cache .npm --prefer-offline
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: out
    files:
      - '**/*'
  cache:
    paths:
      - .npm/**/*
      - node_modules/**/*
```

---

## React (Create React App)

```yaml
# amplify.yml - Create React App
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm ci --cache .npm --prefer-offline
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: build
    files:
      - '**/*'
  cache:
    paths:
      - .npm/**/*
      - node_modules/**/*
```

---

## React + Vite

```yaml
# amplify.yml - React with Vite
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm ci --cache .npm --prefer-offline
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: dist
    files:
      - '**/*'
  cache:
    paths:
      - .npm/**/*
      - node_modules/**/*
```

---

## Vue.js

```yaml
# amplify.yml - Vue.js
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm ci --cache .npm --prefer-offline
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: dist
    files:
      - '**/*'
  cache:
    paths:
      - .npm/**/*
      - node_modules/**/*
```

---

## Static HTML/CSS/JS

```yaml
# amplify.yml - Static Site
version: 1
frontend:
  phases:
    build:
      commands:
        - echo "No build required for static site"
  artifacts:
    baseDirectory: /
    files:
      - '**/*'
```

---

## Static with Subdirectory

```yaml
# amplify.yml - Static Site in /public folder
version: 1
frontend:
  phases:
    build:
      commands:
        - echo "Serving from public directory"
  artifacts:
    baseDirectory: public
    files:
      - '**/*'
```

---

## Monorepo (Single App)

```yaml
# amplify.yml - Monorepo with apps/web
version: 1
applications:
  - frontend:
      phases:
        preBuild:
          commands:
            - cd apps/web && npm ci
        build:
          commands:
            - cd apps/web && npm run build
      artifacts:
        baseDirectory: apps/web/dist
        files:
          - '**/*'
      cache:
        paths:
          - apps/web/node_modules/**/*
    appRoot: apps/web
```

---

## With Environment Variables

```yaml
# amplify.yml - Using Environment Variables
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm ci --cache .npm --prefer-offline
        # Environment variables set in Amplify Console
        - echo "API_URL=$API_URL"
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: .next
    files:
      - '**/*'
  cache:
    paths:
      - .npm/**/*
      - node_modules/**/*
```

---

## With Custom Build Image (Node 18)

```yaml
# amplify.yml - Specific Node Version
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - nvm install 18
        - nvm use 18
        - npm ci --cache .npm --prefer-offline
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: .next
    files:
      - '**/*'
  cache:
    paths:
      - .npm/**/*
      - node_modules/**/*
```

---

## With Pre/Post Build Hooks

```yaml
# amplify.yml - With Hooks
version: 1
frontend:
  phases:
    preBuild:
      commands:
        # Install dependencies
        - npm ci --cache .npm --prefer-offline
        # Run linting
        - npm run lint
        # Run tests
        - npm run test:ci
    build:
      commands:
        - npm run build
    postBuild:
      commands:
        # Generate sitemap
        - npm run generate-sitemap
        # Notify build success (optional)
        - echo "Build completed successfully"
  artifacts:
    baseDirectory: .next
    files:
      - '**/*'
  cache:
    paths:
      - .npm/**/*
      - node_modules/**/*
```

---

## With Backend (Amplify Gen 2)

```yaml
# amplify.yml - Full Stack with Backend
version: 1
backend:
  phases:
    build:
      commands:
        - npm ci --cache .npm --prefer-offline
        - npx ampx pipeline-deploy --branch $AWS_BRANCH --app-id $AWS_APP_ID
frontend:
  phases:
    preBuild:
      commands:
        - npm ci --cache .npm --prefer-offline
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: .next
    files:
      - '**/*'
  cache:
    paths:
      - .npm/**/*
      - node_modules/**/*
```

---

## Troubleshooting Configurations

### Build Fails - Check Node Version

```yaml
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - node --version
        - npm --version
        - nvm install 18
        - nvm use 18
        - npm ci
```

### Out of Memory

```yaml
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm ci
    build:
      commands:
        # Increase Node memory limit
        - export NODE_OPTIONS="--max-old-space-size=4096"
        - npm run build
```

### Caching Issues

```yaml
version: 1
frontend:
  phases:
    preBuild:
      commands:
        # Clear cache if issues
        - rm -rf node_modules
        - rm -rf .next/cache
        - npm ci
```

---

## Best Practices

### 1. Always Use `npm ci`
```yaml
- npm ci --cache .npm --prefer-offline
```
Faster and more reliable than `npm install`.

### 2. Cache Effectively
```yaml
cache:
  paths:
    - .npm/**/*           # npm cache
    - node_modules/**/*   # dependencies
    - .next/cache/**/*    # Next.js cache
```

### 3. Set Node Version Explicitly
```yaml
- nvm use 18
```
Ensures consistent builds.

### 4. Use Environment Variables
Set in Amplify Console, not in amplify.yml:
- `API_URL`
- `NEXT_PUBLIC_*` variables
- Build-specific configs

---

## Quick Reference

| Framework | baseDirectory | Key Command |
|-----------|---------------|-------------|
| Next.js (SSR) | `.next` | `npm run build` |
| Next.js (Static) | `out` | `npm run build` |
| Create React App | `build` | `npm run build` |
| Vite | `dist` | `npm run build` |
| Vue | `dist` | `npm run build` |
| Static HTML | `/` | - |

---

*AI Launchpad Academy - Support Forge*
