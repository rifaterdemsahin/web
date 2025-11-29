# Project Folder Structure and Contents

This document provides an overview of the project's folder structure and the purpose of each key file and directory.

## High-Level Overview

The project is a personal portfolio and business website for Rifat Erdem Sahin, an AI Solutions Architect. It is a static website built with HTML, CSS, and JavaScript.

## Folder Structure

```
.
├── 1_real
│   └── okr.md
├── 2_environment
│   ├── codespaces-macos.md
│   ├── macos-local.md
│   └── windows.md
├── 3_ui
│   ├── about.svg
│   ├── assesment.svg
│   ├── blog.svg
│   ├── contact.svg
│   ├── courses.svg
│   ├── delivery-pilot.svg
│   ├── delivery_pilot_screenshot.txt
│   ├── early-bird-registration.svg
│   ├── ebook.svg
│   ├── email-form.svg
│   ├── index_screenshot.txt
│   ├── investor.svg
│   ├── newsletter.svg
│   └── post-email-page.svg
├── 4_formula
│   └── folder_structure_contents.md
├── assets
│   ├── css
│   │   ├── common-styles.css
│   │   └── main.css
│   ├── ebook
│   │   ├── rag.pdf
│   │   └── readme.txt
│   ├── images
│   │   ├── delivery_pilot.png
│   │   └── erdem_photo.jpeg
│   ├── js
│   │   └── main.js
│   └── pdf
│       ├── delivery_pilot_november_27.pdf
│       ├── delivery_pilot_november_27_turkish.pdf
│       └── readme.md
├── common-nav.html
├── docs
│   ├── coupons.txt
│   ├── courses.yaml
│   ├── github-pages-setup.md
│   ├── readme.md
│   └── todos.md
├── index.html
├── MASTER_PROMPT.md
├── pages
│   ├── about.html
│   ├── assesment.html
│   ├── blog.html
│   ├── contact.html
│   ├── courses.html
│   ├── delivery-pilot.html
│   ├── early-bird-registration.html
│   ├── ebook.html
│   ├── email-form.html
│   ├── index.html
│   ├── investor.html
│   ├── newsletter.html
│   └── post-email-page.html
└── README.md
```

## Folder and File Descriptions

### `1_real/`
- **Purpose:** Contains files related to the real-world application and goals of the project.
- **`okr.md`:** Defines the Objectives and Key Results (OKRs) for the website, outlining the strategic goals and measurable outcomes.

### `2_environment/`
- **Purpose:** Holds documentation on how to set up and run the project in different environments.
- **`codespaces-macos.md`:** Instructions for running the project in a GitHub Codespace on macOS.
- **`macos-local.md`:** Instructions for running the project locally on a macOS machine.
- **`windows.md`:** Instructions for running the project on a Windows machine.

### `3_ui/`
- **Purpose:** Contains UI-related assets, such as SVG icons and placeholder images for screenshots.
- **`*.svg`:** A collection of SVG icons representing the main pages of the website.
- **`*_screenshot.txt`:** Placeholder files describing the content of screenshots for the main pages.

### `4_formula/`
- **Purpose:** This folder contains meta-documentation about the project structure and prompts.
- **`folder_structure_contents.md`:** This file, providing a map of the project.

### `assets/`
- **Purpose:** Stores all static assets for the website.
- **`css/`:** Contains the CSS files.
  - **`common-styles.css`:** The main stylesheet with the new, modern design.
  - **`main.css`:** An older stylesheet, which is being phased out.
- **`ebook/`:** Contains an ebook in PDF format and a related readme.
- **`images/`:** Stores images used on the website.
- **`js/`:** Contains the main JavaScript file.
- **`pdf/`:** Contains PDF documents for download.

### `docs/`
- **Purpose:** Contains various documentation files related to the project.
- **`courses.yaml`:** A YAML file with data about the courses offered.
- **Other files:** Various markdown and text files with notes, todos, and setup guides.

### `pages/`
- **Purpose:** Contains the main HTML pages of the website.
- **`index.html`:** The main landing page.
- **Other HTML files:** Each file corresponds to a specific page on the website (e.g., about, contact, courses).

### Root Directory Files
- **`index.html`:** The main entry point of the website, which redirects to `pages/index.html`.
- **`common-nav.html`:** A reusable HTML snippet for the common navigation bar.
- **`MASTER_PROMPT.md`:** A detailed prompt containing all the information needed to recreate the website.
- **`README.md`:** The main README file for the project.
- **`sitemap.xml`, `robots.txt`:** Standard files for SEO and web crawlers.
