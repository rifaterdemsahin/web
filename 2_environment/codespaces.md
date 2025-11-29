# GitHub Codespaces Usage

This project uses GitHub Codespaces as a cloud-based development environment. It allows you to write, run, and debug the code directly in your browser or in VS Code.

## Development Environment

Since this is a static website project, the Codespace environment is straightforward. It uses a standard Linux image and relies on Python's built-in HTTP server for local preview.

*   **Local Preview**: We use `python3 -m http.server 8080` to serve the files locally within the Codespace.
*   **Detailed Guide**: For step-by-step instructions on running the project in a Codespace, please refer to [codespaces-macos.md](codespaces-macos.md).

## Deployment

There is a build and deployment process for GitHub Pages, configured in the `.github/workflows` folder (specifically `static.yml`).

*   **Automatic Deployment**: After every commit to the main branch, a GitHub Action triggers to deploy the latest changes to the live site.
