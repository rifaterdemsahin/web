# Copilot Instructions for Web Project

## Project Overview
This is a personal website with AI engineering content, including blog posts, courses, and ebooks.

## Domain Information
- Primary Domain: https://hello.rifaterdemsahin.com
- Repository: rifaterdemsahin/web

## Project Structure
```
/pages/ - Main website pages (HTML)
/assets/ - Static assets (CSS, JS, images, ebooks)
/docs/ - Documentation and guides
/2025/ - Blog posts organized by date
```

## eBook System

### Dynamic Content Loading
The ebook.html page supports URL parameters to display different content:
- `?type=rag` - Displays RAG (Retrieval-Augmented Generation) guide
- `?type=default` - Displays default AI Engineering guide
- No parameter defaults to the RAG guide

### Content Configuration
eBook content is managed through an internal JSON structure in the HTML file. Each content type includes:
- Title
- Icon
- Description
- PDF link
- Custom styling/messaging

### Adding New eBook Types
1. Add entry to the `ebookContent` JSON object in ebook.html
2. Include: title, icon, subtitle, pdfUrl, pdfName
3. Test with URL parameter: `?type=your-new-type`

## Development Guidelines
- Keep HTML files in `/pages/`
- Store assets in appropriate `/assets/` subdirectories
- Use domain `https://hello.rifaterdemsahin.com` for all external links
- Follow existing styling patterns (gradient backgrounds, rounded corners)

## Git Workflow
- Main branch: `main`
- Pull before making changes
- Commit messages should be descriptive

## Notes
- Static site hosted on GitHub Pages
- Email collection integrated with n8n webhooks
- Focus on AI engineering education content
