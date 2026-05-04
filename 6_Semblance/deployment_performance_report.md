# Performance Report: GitHub Pages Deployment Analysis

## 📊 Deployment Metadata
- **Artifact Size**: 1.03 GB (Full) / ~10MB (Fast)
- **File Count**: ~22,560 (Full) / ~500 (Fast)
- **Full Deploy Duration**: ~15 minutes
- **Fast Deploy Duration**: ~45 seconds

---

## ⚡ Dual-Workflow Solution (APPLIED)
To prevent waiting 15 minutes for every update, I have implemented two workflows:

1.  **Fast Deploy (`deploy.yml`)**: 
    - **Trigger**: Automatic on `git push`.
    - **Logic**: Automatically **excludes** the heavy `20*` folders.
    - **Speed**: Very fast (~45s).
    - **Side Effect**: Blog posts will 404 until you run the full deploy.
2.  **Full Deploy (`deploy_full.yml`)**:
    - **Trigger**: Manual only (via Actions tab).
    - **Logic**: Includes the entire 1GB archive.
    - **Timeout**: **1 Hour** (to ensure completion).

---

## 🛠️ Optimization Recommendations

### 1. Optimize Media (Images/Videos)
- **Action**: Compress images in `2023` and `2024`. Use external hosting for videos.

### 2. Core-Then-Blog Protocol
- Use the **Fast Deploy** for your daily work on the homepage, UI, and documentation.
- Use the **Full Deploy** once a week or whenever you add new blog posts.

### 3. Workflow "Dispatch" Control
- You can manually trigger the Full Deploy from the **Actions** tab on GitHub.

---

## 📈 Long-term Strategy
If the site continues to grow, we should consider splitting historical years into sub-repositories.

**Status**: Dual-workflow implemented. Fast deploys for core updates; manual 1-hour timeout deploys for the full 1GB archive.
