# Strategy: Deployment Optimization & Quota Management

This document outlines the strategy for managing the deployment of the 1GB+ `rifaterdemsahin.com` site while staying within GitHub Actions limits.

## 1. Understanding the Limits
GitHub Actions pricing depends on your repository visibility:
- **Public Repositories**: Free and Unlimited (No minute limit).
- **Private Repositories**: 2,000 minutes/month (Free Plan).

### Usage Calculation (for Private Repos)
- **Average Deploy Time**: 15 minutes.
- **Monthly Quota**: 2,000 minutes.
- **Max Deploys**: ~133 per month (approx. 4 per day).

---

## 2. Optimization Strategies

### Strategy A: Manual Triggers (Recommended for heavy editing)
Instead of deploying on every single `git push`, you can trigger deployments only when you are finished with a batch of work.

**Action**: Add `workflow_dispatch` to your workflow (Done) and use the "Run workflow" button in the Actions tab.

### Strategy B: Development Branching
1.  Work and push all changes to a `development` branch.
2.  The `development` branch will **not** trigger a 15-minute deploy.
3.  When you are ready to go live, merge `development` into `main`.
4.  Result: 10 pushes = 1 deployment (Saves 135 minutes).

### Strategy C: Ignore Non-Web Files
Prevent deployments when you only update documentation or scratch files.

**Action**: Update `.github/workflows/deploy.yml` with path filters:
```yaml
on:
  push:
    branches: ["main"]
    paths-ignore:
      - 'README.md'
      - '4_Formula/**'
      - '6_Semblance/**'
      - '.gemini/**'
```

---

## 3. Action Plan: "The Batch-Push Rule"

To keep your GitHub Actions usage efficient, follow this protocol:
1.  **Work Locally**: Make all your changes, previews, and tests locally.
2.  **Commit Often**: Keep your commit history detailed.
3.  **Push Once**: Only push to `main` when you have a significant update or are finished for the day.
4.  **Monitor**: Keep an eye on the [Billing Dashboard](https://github.com/settings/billing) if your repo is private.

## 4. Conclusion
If your repository is **Public**, you don't need to worry about minutes—GitHub provides them for free to support open source. If it is **Private**, following the **Batch-Push Rule** will easily keep you within the 2,000-minute free tier.
