# GitHub Usage

This document outlines the configuration and usage of GitHub for this project, including workflows, branching strategies, and environment settings.

## Repository Overview

This repository hosts the web project and utilizes GitHub Actions for continuous deployment.

## Workflows

The project uses GitHub Actions to automate deployment tasks.

### Static Content Deployment (`static.yml`)

This workflow handles the deployment of static content to GitHub Pages.

- **File**: `.github/workflows/static.yml`
- **Triggers**:
  - Push to the `main` branch.
  - Manual trigger via `workflow_dispatch`.
- **Permissions**:
  - `contents: read`
  - `pages: write`
  - `id-token: write`
- **Concurrency**: Ensures only one deployment runs at a time, but does not cancel in-progress runs to allow production deployments to complete.
- **Jobs**:
  - **Deploy**:
    - **Environment**: `github-pages`
    - **Runner**: `ubuntu-latest`
    - **Steps**:
      1. Checkout code (`actions/checkout@v4`).
      2. Setup Pages (`actions/configure-pages@v5`).
      3. Upload artifact (`actions/upload-pages-artifact@v3`) - Uploads the entire repository (`.`).
      4. Deploy to GitHub Pages (`actions/deploy-pages@v4`).

## Branching Strategy

- **Main Branch (`main`)**: The default branch. Pushes to this branch trigger the deployment workflow.

## Environment

- **GitHub Pages**: The project is deployed to GitHub Pages. The URL is provided by the deployment job output.

## Related Documentation

- [Codespaces Usage](./codespaces.md): Details on using GitHub Codespaces for development.
