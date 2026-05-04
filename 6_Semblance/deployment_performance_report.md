# Performance Report: GitHub Pages Deployment Analysis

## 📊 Deployment Metadata
- **Artifact Size**: 1.03 GB
- **File Count**: ~22,560 files
- **Observed Duration**: 10m 40s (In Progress)
- **Bottleneck**: Artifact Upload (`upload-pages-artifact`)

---

## ❓ Will it take this long every time?
**Yes.** GitHub Actions' current architecture for GitHub Pages involves creating a fresh artifact for every deployment. Unlike tools that use "incremental sync" (uploading only changed files), GitHub Actions must:
1.  Zip all 22,000+ files into a single 1GB package.
2.  Upload that 1GB package to GitHub's internal storage.
3.  Notify the Pages server to extract and serve the new content.

Because of this, every push to `main` will trigger a ~10-15 minute deployment cycle.

---

## 🛠️ Optimization Recommendations

### 1. Optimize Media (Images/Videos)
- **The Culprit**: Folders `2023` and `2024` contain over 1GB of data.
- **Action**: Identify and compress images. Move large video files to external hosting (YouTube, Loom, Google Drive) and embed them instead of storing them in the repository.

### 2. Batch Your Pushes
- **The Culprit**: Small changes trigger a full 1GB redeploy.
- **Action**: Batch your changes. Instead of pushing every single file edit, commit locally and push in larger batches to minimize the number of 10-minute waits.

### 3. Workflow "Dispatch" Control
- **Action**: If you are doing heavy editing, you can temporarily disable the "on push" trigger and use the "Run workflow" button manually.

### 4. Increase Deployment Timeout (APPLIED)
- **The Problem**: GitHub's default deployment timeout is 10 minutes. For a 1GB site, the extraction process can exceed this limit, leading to `Error: Timeout reached`.
- **Action**: I have updated `.github/workflows/deploy.yml` to set the timeout to **30 minutes** (`timeout: 1800000`).

---

## 📈 Long-term Strategy
If the site continues to grow, we should consider splitting historical years into sub-repositories or using incremental deployment tools.

**Status**: The 10-minute wait is normal for a 1GB static archive on GitHub Pages. I have increased the timeout to 30 minutes to prevent premature failures.
