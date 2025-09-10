# GitHub Pages Setup Guide

This guide explains how to set up your website to work without `.html` extensions on GitHub Pages.

## Overview

GitHub Pages automatically serves `index.html` files when accessing a directory without specifying a filename. This allows for clean URLs without the `.html` extension.

## Directory Structure for Blog Posts

For blog posts, use the following structure:

```
/2025/08/27/🚀-how-to-apply-yaml-configurations-using-kubectl-in-terminal/
├── index.html  (main blog post content)
```

## How It Works

### Without index.html (❌ Not Working)
```
URL: https://yourusername.github.io/2025/08/27/🚀-how-to-apply-yaml-configurations-using-kubectl-in-terminal.html
File: /2025/08/27/🚀-how-to-apply-yaml-configurations-using-kubectl-in-terminal.html
```

### With index.html (✅ Working)
```
URL: https://yourusername.github.io/2025/08/27/🚀-how-to-apply-yaml-configurations-using-kubectl-in-terminal/
File: /2025/08/27/🚀-how-to-apply-yaml-configurations-using-kubectl-in-terminal/index.html
```

## Step-by-Step Setup

### 1. Create Directory Structure
```bash
mkdir -p /2025/08/27/🚀-how-to-apply-yaml-configurations-using-kubectl-in-terminal/
```

### 2. Move HTML Content
Instead of creating a single HTML file, create a directory and place an `index.html` file inside:

```bash
# Instead of this:
touch /2025/08/27/🚀-how-to-apply-yaml-configurations-using-kubectl-in-terminal.html

# Do this:
mkdir -p /2025/08/27/🚀-how-to-apply-yaml-configurations-using-kubectl-in-terminal/
touch /2025/08/27/🚀-how-to-apply-yaml-configurations-using-kubectl-in-terminal/index.html
```

### 3. Update Navigation Links
Update all navigation links to point to the directory (without `.html`):

```html
<!-- Instead of -->
<a href="/2025/08/27/🚀-how-to-apply-yaml-configurations-using-kubectl-in-terminal.html">

<!-- Use -->
<a href="/2025/08/27/🚀-how-to-apply-yaml-configurations-using-kubectl-in-terminal/">
```

## Benefits

1. **Clean URLs**: No `.html` extension in the URL
2. **SEO Friendly**: Better for search engines
3. **User Friendly**: Easier to remember and share
4. **Professional**: Looks more like a proper website

## GitHub Pages Configuration

### Repository Settings
1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under **Source**, select:
   - **Deploy from a branch**: `main` (or your default branch)
   - **Folder**: `/ (root)`

### Custom Domain (Optional)
If you have a custom domain:
1. Add a `CNAME` file in the root directory
2. Add your domain in the Pages settings
3. Configure DNS records with your domain provider

## File Naming Conventions

### Blog Posts
- Use descriptive, URL-friendly names
- Include emojis for visual appeal
- Use hyphens instead of spaces
- Keep names lowercase for consistency

Example:
```
/2025/08/27/🚀-how-to-apply-yaml-configurations-using-kubectl-in-terminal/
```

### Static Pages
For main site pages, you can use either approach:
- `pages/index.html` → accessible as `/pages/`
- `pages/about.html` → accessible as `/pages/about.html`

## Troubleshooting

### Common Issues

1. **404 Error**: Make sure the directory contains an `index.html` file
2. **Styling Issues**: Check relative paths in CSS and image references
3. **Navigation Broken**: Update all internal links to use the new structure

### Testing Locally
Before pushing to GitHub, test locally:
```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve .

# Using PHP
php -S localhost:8000
```

## Best Practices

1. **Consistent Structure**: Use the same pattern for all blog posts
2. **SEO Optimization**: Include proper meta tags and structured data
3. **Mobile Responsive**: Ensure all pages work on mobile devices
4. **Fast Loading**: Optimize images and minimize CSS/JS
5. **Accessibility**: Use semantic HTML and proper alt tags

## Example Implementation

Here's how a complete blog post structure should look:

```
/2025/08/27/🚀-how-to-apply-yaml-configurations-using-kubectl-in-terminal/
├── index.html          # Main blog post content
└── assets/             # Optional: post-specific assets
    ├── images/
    └── css/
```

The `index.html` file contains the complete blog post with:
- Proper HTML structure
- SEO meta tags
- Responsive CSS
- Navigation links
- Footer

## Deployment

1. Commit your changes:
```bash
git add .
git commit -m "Add blog post: kubectl YAML tutorial"
git push origin main
```

2. GitHub Pages will automatically deploy your changes
3. Your blog post will be available at:
   `https://yourusername.github.io/2025/08/27/🚀-how-to-apply-yaml-configurations-using-kubectl-in-terminal/`

## Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Jekyll Documentation](https://jekyllrb.com/docs/) (if using Jekyll)
- [Custom Domains on GitHub Pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
