# Formula: GitHub Actions Automated Deployment

This formula outlines how to transition from manual GitHub Pages publishing to automated CI/CD using GitHub Actions.

## 1. Objective
Automate the deployment of `rifaterdemsahin.com` every time a change is pushed to the `main` branch. This ensures the site is always in sync without manual "unpublish/publish" cycles.

## 2. Prerequisites
- Repository: `rifaterdemsahin/web`
- Branch: `main`
- Custom Domain: `www.rifaterdemsahin.com` (configured in `CNAME` file)

## 3. Implementation Steps

### Step 1: Create the Workflow File
Create a new file at `.github/workflows/deploy.yml`.

### Step 2: Define the Workflow Logic
The workflow should use the official `actions/deploy-pages` action.

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Setup Pages
        uses: actions/configure-pages@v4
      
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: '.' # Deploy the root directory
      
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### Step 3: Enable Actions Deployment in GitHub UI
1.  Go to **Settings** -> **Pages**.
2.  Under **Build and deployment** -> **Source**, change from "Deploy from a branch" to **"GitHub Actions"**.

## 4. Key Advantages
- **Consistency**: The `CNAME` file and site content are deployed atomically.
- **Speed**: Deployment happens within seconds of a `git push`.
- **Logs**: If a deployment fails, you get detailed error logs in the **Actions** tab.
- **Environment Tracking**: GitHub will show a "Deployment" status on the repo homepage.

## 5. Verification
- [ ] Push a small change to `README.md`.
- [ ] Monitor the **Actions** tab for a green checkmark.
- [ ] Verify the live site reflects the change immediately.
