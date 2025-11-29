# Rifat Erdem Sahin - Personal Website

This is the personal website for Rifat Erdem Sahin, an AI Solutions Architect based in Cambridge, UK.
https://hello.rifaterdemsahin.com

## 📁 Project Structure

```
web/
├── index.html                 # Main entry point (redirects to 5_Symbols/pages/index.html)
├── 5_Symbols/                 # Implementation & Code
│   ├── pages/                 # All HTML pages
│   │   ├── index.html         # Homepage
│   │   ├── cv.html            # CV/Resume page
│   │   ├── contact.html       # Contact form
│   │   ├── newsletter.html    # Newsletter signup
│   │   ├── courses.html       # Course showcase
│   │   ├── email-form.html    # Email form for coupons
│   │   ├── early-bird-registration.html  # Early bird registration
│   │   ├── blog.html          # Blog page
│   │   ├── delivery-pilot.html   # Delivery Pilot service page
│   │   └── post-email-page.html  # Post-email confirmation
│   └── assets/                # Static assets
│       ├── images/            # Images and photos
│       │   └── erdem_photo.jpeg  # Profile photo
│       ├── css/               # CSS files
│       └── js/                # JavaScript files
├── docs/                      # Documentation
│   ├── README.md              # This file
│   ├── courses.yaml           # Course data
│   ├── coupons.txt            # Coupon information
│   ├── todos.md               # Project todos
│   └── WORDPRESS_DEPLOYMENT_GUIDE.md  # Deployment guide
```

## 🚀 Features

### GitHub Repository Assessment
- **Location**: `5_Symbols/pages/delivery-pilot.html`
- **Functionality**: AI-powered code assessment with random grading (A-F)
- **Integration**: POST requests to `n8n.rifaterdemsahin.com`
- **Features**:
  - GitHub repository URL input
  - Agreement checkbox
  - Random grade generation with emojis
  - AI feedback display
  - Loading states and animations

### Pages Overview
- **Homepage**: Professional introduction and services overview
- **CV**: Detailed resume and experience
- **Contact**: Contact form and information
- **Newsletter**: Email subscription
- **Courses**: Course showcase and learning materials
- **Delivery Pilot**: AI-powered learning service
- **Early Bird**: Special registration offers
- **Blog**: Content and articles

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with CSS Variables
- **Fonts**: Inter (Google Fonts)
- **Icons**: Emoji-based icons
- **Integration**: N8N webhooks for data processing

## 📱 Responsive Design

All pages are fully responsive and optimized for:
- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (320px - 767px)

## 🎨 Design System

### Color Palette
- Primary: #2563eb (Blue)
- Secondary: #1e40af (Dark Blue)
- Accent: #3b82f6 (Light Blue)
- Success: #10b981 (Green)
- Warning: #f59e0b (Orange)
- Error: #ef4444 (Red)

### Typography
- Font Family: Inter
- Weights: 300, 400, 500, 600, 700

## 🔧 Development

### Local Development
1. Clone the repository
2. Open `index.html` in a web browser
3. Or serve using a local server:
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js
   npx serve .
   ```

### File Organization
- All HTML pages are in the `5_Symbols/pages/` directory
- Static assets (images, CSS, JS) are in the `5_Symbols/assets/` directory
- Documentation is in the `docs/` directory
- Main `index.html` redirects to `5_Symbols/pages/index.html`

## 📞 Contact

- **Website**: [rifaterdemsahin.com](https://rifaterdemsahin.com)
- **LinkedIn**: [linkedin.com/in/rifaterdemsahin](https://linkedin.com/in/rifaterdemsahin)
- **Email**: Available through contact form

## 📄 License

© 2024 Rifat Erdem Sahin. All rights reserved.
