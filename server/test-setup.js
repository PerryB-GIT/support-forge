#!/usr/bin/env node

/**
 * Quick setup test script
 * Run this after npm install to verify everything is working
 */

import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

async function testSetup() {
  console.log('Testing Support Forge API setup...\n');

  const checks = [
    {
      name: 'Dependencies installed',
      test: async () => {
        const packageJson = JSON.parse(await fs.readFile(path.join(__dirname, 'package.json'), 'utf-8'));
        const deps = Object.keys(packageJson.dependencies);
        for (const dep of deps) {
          try {
            await import(dep);
          } catch (e) {
            throw new Error(`Missing dependency: ${dep}`);
          }
        }
      }
    },
    {
      name: 'Data directory exists',
      test: async () => {
        await fs.access(path.join(__dirname, 'data'));
      }
    },
    {
      name: 'Submissions file exists',
      test: async () => {
        const submissionsPath = path.join(__dirname, 'data', 'submissions.json');
        await fs.access(submissionsPath);
        const data = JSON.parse(await fs.readFile(submissionsPath, 'utf-8'));
        if (!data.contacts || !data.schedules) {
          throw new Error('Invalid submissions.json structure');
        }
      }
    },
    {
      name: '.env.example exists',
      test: async () => {
        await fs.access(path.join(__dirname, '.env.example'));
      }
    },
    {
      name: 'Main server file exists',
      test: async () => {
        await fs.access(path.join(__dirname, 'index.js'));
      }
    }
  ];

  let passed = 0;
  let failed = 0;

  for (const check of checks) {
    try {
      await check.test();
      console.log(`✓ ${check.name}`);
      passed++;
    } catch (error) {
      console.log(`✗ ${check.name}: ${error.message}`);
      failed++;
    }
  }

  console.log(`\n${passed} passed, ${failed} failed\n`);

  if (failed === 0) {
    console.log('Setup is complete! Run "npm start" to start the server.');
  } else {
    console.log('Please fix the issues above before starting the server.');
    process.exit(1);
  }
}

testSetup().catch(console.error);
