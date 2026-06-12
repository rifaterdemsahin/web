# CV 404 Fix — Semblance Plan

## Problem
Old WordPress CV links are broken (404) after site migration to GitHub Pages:
- `rifaterdemsahin.com/wp-content/uploads/2025/05/erdem-sahin-cv_summary_2025_may.pdf`
- `rifaterdemsahin.com/wp-content/uploads/2025/05/erdem-sahin-cv_summary_2025_may.docx`

These URLs were embedded in emails, LinkedIn, and recruiter correspondence.

## Root Cause
Site migrated from WordPress to GitHub Pages static site. WordPress upload paths no longer exist. GitHub Pages serves `404.html` for any missing path, but the 404 page had no redirect for CV-related URLs.

## Fix Applied

### 1. CV PDFs uploaded to repo
92 role-specific CVs committed to `5_Symbols/cv/cv_*.pdf` and served directly from GitHub Pages.

### 2. Recruiter CV selector page
New page at `5_Symbols/pages/cv.html`:
- Lists all 92 CVs grouped by category (AI/ML, Cloud, DevOps, Security, Data, Engineering, Business)
- Live search filter
- Category tab filter
- One-click Download + View buttons for each PDF

### 3. 404 redirect
`404.html` updated: any request to `/wp-content/uploads/` paths containing "cv" or "resume" auto-redirects (JS) to `/5_Symbols/pages/cv.html`.

### 4. Nav link
"CV" added to `common-nav.html` so all pages link to the recruiter selector.

### 5. CI/CD verification
`.github/workflows/post-deploy-cv-test.yml` triggers after every deploy and checks:
- CV selector page returns HTTP 200
- Sample CV PDFs (5 roles) return HTTP 200
- Old WordPress 404 URL responses contain the redirect script

## New canonical URL for recruiters
`https://www.rifaterdemsahin.com/5_Symbols/pages/cv.html`
