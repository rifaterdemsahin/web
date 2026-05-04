# Plan: Blog Index Link Fix & Readability Enhancement

## 1. Objectives
- Replace placeholder links in `blog/index.html` with real, recent blog posts.
- Improve visual aesthetics for a "premium" feel (glassmorphism, modern typography).
- Add a "Test Mode" to make it easier to verify links.
- Ensure SEO best practices (Title, Meta, Semantics).

## 2. Implementation Steps

### Phase 1: Content Update
- Extract titles and slugs from the latest 10 posts identified via `find`.
- Update `blog/index.html` with these real links.
- Update the "Categories" sidebar with real links or meaningful tags.

### Phase 2: Visual Enhancement
- Update `blog/index.html` CSS (or internal styles) to:
    - Use Inter font.
    - Implement a glassmorphic card design for blog posts.
    - Add hover effects and micro-animations.
    - Use a deep blue/dark theme consistent with the lead magnet hero.

### Phase 3: Link Testing Feature
- Add a small "Link Inspector" utility (hidden by default or toggled via a button).
- When active, it will:
    - Highlight all outbound links.
    - Show the full URL in a tooltip or small badge.
    - Allow for a quick "Test All" visual check.

### Phase 4: Validation & Sync
- Run a quick link check script in `scratch/`.
- Commit and push changes.

## 3. Post Data (Latest 5)
1. `/2027/02/17/contractors-and-passports/` - Contractors and Passports
2. `/2026/12/03/how-to-build-a-high-income-career-without-a-degree/` - How to Build a High-Income Career Without a Degree
3. `/2026/11/14/📡-testing-a-4g-router-to-move-data-to-nas-a-wireless-marvel-🚀/` - Testing a 4G Router
4. `/2026/09/11/ai-based-graph-generation/` - AI Based Graph Generation
5. `/2026/09/06/why-is-it-hard-to-diagnose-high-functioning-autism-in-adults/` - Diagnosing High-Functioning Autism

## 4. Testing Plan
- Manually click through the first 5 links.
- Use the new "Test Mode" to verify path correctness.
