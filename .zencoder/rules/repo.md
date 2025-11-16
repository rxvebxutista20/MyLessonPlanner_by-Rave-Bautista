---
description: Repository Information Overview
alwaysApply: true
---

# RAVE BAUTISTA LESSON PLANNER Information

## Summary
A modern web-based lesson planning application designed for educators to generate comprehensive lesson plans, daily lesson logs (DLLs), and table of specifications (TOS) using AI-powered assistance. The application integrates Google's Gemini API through a secure serverless backend, featuring multiple curriculum formats (MATATAG, K-12, SHS, Multigrade, DLP) with export capabilities to PDF and DOCX formats. Built with a glassmorphism UI design using Tailwind CSS and vanilla JavaScript.

## Structure
- **index.html** (64 KB): Main application file containing complete HTML markup, embedded JavaScript logic, and UI structure
- **styles.css** (5 KB): Styling with Tailwind CSS, glassmorphism effects, animations, and dark theme design
- **Netlify/** - Serverless backend directory
  - **functions/generate.js** (2.2 KB): Node.js Netlify function serving as secure API middleware for Google Gemini requests
- **.vscode/** - Editor configuration
  - **settings.json**: VS Code workspace settings including Python testing configuration

## Language & Runtime
**Primary Language**: JavaScript (Vanilla JS + HTML5 + CSS3)
**Backend Runtime**: Node.js (Netlify Functions)
**Build System**: None required (static site)
**Package Manager**: None (all dependencies loaded via CDN)
**Deployment Platform**: Netlify

## Dependencies

**Frontend Libraries (via CDN)**:
- **Tailwind CSS**: Utility-first CSS framework (loaded from cdn.tailwindcss.com)
- **Google Fonts**: M PLUS Rounded 1c font family for typography
- **Marked.js**: Markdown parser library for content rendering
- **jsPDF** (v2.5.1): PDF generation from HTML
- **html2canvas** (v1.4.1): HTML to canvas conversion for PDF rendering
- **html-docx-js-typescript** (v1.5.0): DOCX document generation

**Backend Dependencies**:
- **Node.js Runtime**: Netlify Functions environment
- **fetch API**: Built-in for HTTP requests to Google Gemini API

**Environment Variables**:
- `GEMINI_API_KEY`: Google Gemini API authentication key (set in Netlify dashboard)

## Build & Installation

**Development**:
```bash
# No build process required
# Open index.html in a web browser or serve via local HTTP server
# For local testing with Netlify Functions, use:
netlify dev
```

**Deployment to Netlify**:
```bash
# Deploy the entire directory structure
netlify deploy --prod

# Or connect GitHub repository for automatic deployments
```

**Configuration Required**:
1. Set `GEMINI_API_KEY` environment variable in Netlify dashboard
2. Ensure `Netlify/` directory is included in deployment

## Main Files & Application Structure

**Entry Points**:
- **index.html**: Single-page application entry point with all UI views and client-side logic
  - Login modal for owner authentication
  - Owner Dashboard with hub cards (Lesson Planner, DLL Generator, TOS Generator, Profile)
  - Multiple generator views for each tool type
  - Output display and export functionality

**API Endpoint**:
- **Netlify/functions/generate.js**: POST endpoint at `/.netlify/functions/generate`
  - Accepts: `{ systemPrompt, userQuery }`
  - Returns: Google Gemini API response with generated content

**Key Features**:
- 15+ lesson plan templates (MATATAG Weekly, K-12 Weekly/Daily, SHS, Multigrade, DLP formats)
- DLL (Daily Lesson Log) generator
- TOS (Table of Specifications) generator
- Real-time Markdown rendering
- PDF export with Times New Roman 12pt formatting
- DOCX export with document styling
- Login authentication with hardcoded credentials
- Copy to clipboard functionality

## Design & Styling

**Color Scheme**: Dark gradient background with glassmorphism elements
**UI Framework**: Tailwind CSS with custom utilities
**Responsive Design**: Mobile-first approach with breakpoints for sm, md, lg
**Animations**: Gradient background animation, card hover effects, loading spinner
**Accessibility**: High contrast white text on dark backgrounds

## Security Considerations

**API Key Protection**:
- API key stored only in Netlify environment variables (not exposed to frontend)
- Netlify Function acts as secure middleware between frontend and Google Gemini API

**Authentication**:
- Simple login modal with username/password validation
- Credentials hardcoded in JavaScript (suitable for single-owner application)

## Testing & Validation
**Configuration**: .vscode/settings.json indicates Python unittest setup for potential backend testing
**Current Status**: No active test files in repository
**Recommended Testing**: Add unit tests for Netlify function and integration tests for API calls
