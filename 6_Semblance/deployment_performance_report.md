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

### 2. Deployment Frequency Management
- **The Culprit**: Small changes trigger a full 1GB redeploy.
- **Action**: Batch your changes. Instead of pushing every single file edit, commit locally and push in larger batches to minimize the number of 10-minute waits.

### 3. Workflow "Dispatch" Control
- **Action**: If you are doing heavy editing, you can temporarily disable the "on push" trigger in `.github/workflows/deploy.yml` and use the "Run workflow" button manually when you are ready to go live.

---

## 📈 Long-term Strategy
If the site continues to grow (e.g., reaching 5GB+), the standard GitHub Actions runner may hit timeout limits (typically 360 minutes, so you have plenty of time, but the wait will become frustrating). 

At that point, we should consider:
- **Sub-repositories**: Splitting historical years into their own repositories/subdomains.
- **SSG Migration**: Moving to a Static Site Generator that optimizes the build/output, though this is a major refactor.

**Status**: Currently acceptable for a "free" hosting solution of this scale, but requires patience for each deployment.
