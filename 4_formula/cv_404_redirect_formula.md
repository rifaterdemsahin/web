# Formula: Fixing Broken Legacy URLs (404 → Smart Redirect)

**Problem class:** Old platform URLs embedded in the wild (emails, LinkedIn, CVs) that break when a site migrates.

---

## The One-Line Formula

```
Dead URL  →  404.html (JS detect)  →  Best-match live page
```

---

## Why This Works on GitHub Pages

GitHub Pages has no server-side routing (no `.htaccess`, no redirects config).
Every missing URL hits **404.html** — that is the only interception point.
JavaScript runs there, reads `window.location.pathname`, and redirects before the user sees anything.

---

## The 3-Part Fix

### Part 1 — Move the files to the right place

| Before (WordPress)                                   | After (GitHub Pages)                          |
|------------------------------------------------------|-----------------------------------------------|
| `/wp-content/uploads/2025/05/cv_summary_may.pdf`     | `/5_Symbols/cv/cv_devops_engineer.pdf`        |

- Commit the real files into the repo under a logical path.
- GitHub Pages serves them instantly at that path.

### Part 2 — Intercept in 404.html

```js
(function() {
  var path = window.location.pathname;

  // Old WordPress CV/resume uploads → new CV selector
  if (path.indexOf('/wp-content/uploads/') !== -1 &&
      (path.indexOf('cv') !== -1 || path.indexOf('resume') !== -1)) {
    window.location.replace('/5_Symbols/pages/cv.html');
    return;
  }
})();
```

**Key:** `window.location.replace()` (not `href`) so the 404 URL doesn't land in browser history.

### Part 3 — Build the landing page the redirect points to

The old URL was for one specific file. The redirect lands on a **selector page** where recruiters can find the exact CV they need — better UX than a direct file link.

---

## Decision Tree

```
Incoming 404
│
├── Does the path match a known old pattern?
│   ├── YES → window.location.replace(best_match_live_url)
│   └── NO  → Show the 404 page normally
│
└── Is there a unique live equivalent?
    ├── YES → redirect to that exact page
    └── NO  → redirect to the closest parent/category page
```

---

## Post-Deploy Verification (CI/CD)

Add a GitHub Actions workflow triggered on `workflow_run` (after deploy) that:

1. `curl -I <new_page>` → assert HTTP 200
2. `curl -s <old_404_url>` → assert response body contains redirect script
3. `curl -I <sample_asset>` → assert HTTP 200 for a representative file

```yaml
- name: Verify CV page is live
  run: |
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" "https://example.com/5_Symbols/pages/cv.html")
    [ "$STATUS" = "200" ] || exit 1
```

---

## Reuse This Pattern For

| Scenario                        | Old path pattern           | Redirect target               |
|---------------------------------|----------------------------|-------------------------------|
| Blog post URL structure changed | `/p/slug` → `/blog/slug`   | Exact new post or `/blog.html`|
| Product page renamed            | `/products/old-name`       | `/products/new-name`          |
| Removed WordPress pages         | `/wp-content/...`          | Closest live page             |
| Migrated course platform        | `/courses/id/lessons/id`   | `/courses.html`               |

---

## Files Changed in This Fix

| File                                              | Change                                  |
|---------------------------------------------------|-----------------------------------------|
| `404.html`                                        | Added CV path detection + JS redirect   |
| `5_Symbols/pages/cv.html`                         | New recruiter CV selector (92 roles)    |
| `5_Symbols/common-nav.html`                       | Added CV nav link                       |
| `.github/workflows/post-deploy-cv-test.yml`       | Post-deploy URL verification CI         |
| `6_Semblance/cv_404_fix_plan.md`                  | Fix documentation                       |
