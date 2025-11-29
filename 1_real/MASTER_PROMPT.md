# Master Prompt for Website Recreation

This prompt contains all the necessary information to recreate the website.

## File Structure

```
.
├── 2025
│   ├── 08
│   │   └── 27
│   │       └── 🚀-how-to-apply-yaml-configurations-using-kubectl-in-terminal
│   │           └── index.html
│   └── 09
│       └── 14
│           └── how_to_talk_to_Computers
│               └── index.html
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
├── copilot.md
├── cursor.md
├── delivery-guide.md
├── docs
│   ├── coupons.txt
│   ├── courses.yaml
│   ├── github-pages-setup.md
│   ├── readme.md
│   └── todos.md
├── formula
├── gemini.md
├── index.html
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
├── README.md
├── robots.txt
└── sitemap.xml
```

## HTML File Descriptions

### `./index.html`
- **Purpose:** The main entry point of the website. It immediately redirects to `pages/index.html`.
- **Key Elements:** Contains a meta refresh tag for redirection.

### `./5_Symbols/pages/index.html`
- **Purpose:** The main landing page of the website.
- **Key Elements:**
    - Hero section with a greeting, title, subtitle, and description.
    - Profile card with an image, name, title, and location.
    - "My AI Transformation Journey" section with a timeline.
    - "Bridging Two Worlds" section with skill cards.
    - Call-to-action section.
    - Footer with social media links.

### `./5_Symbols/pages/about.html`
- **Purpose:** Provides detailed information about Rifat Erdem Sahin.
- **Key Elements:**
    - "Why Work With Me in AI Transformation" section.
    - CV preview with sections on "Why AI Transformation Matters", "Why Work With Rifat Erdem Sahin", "AI Transformation Services", and "Credentials & Trust".
    - "Start Your AI Transformation" section with options to schedule a consultation or download a CV.
    - Contact information and social media links.

### `./5_Symbols/pages/assesment.html`
- **Purpose:** An AI-powered DevOps maturity assessment tool.
- **Key Elements:**
    - A React-based questionnaire with 24 questions across 6 categories.
    - A form to schedule a free assessment call.
    - Displays a maturity report with scores and recommendations.

### `./5_Symbols/pages/blog.html`
- **Purpose:** A blog page that showcases recent articles and directs users to the main WordPress blog.
- **Key Elements:**
    - A header with a title and subtitle.
    - A prominent link to the WordPress blog.
    - A grid of featured blog posts.
    - A sidebar with "About the Blog", "Categories", "Newsletter Signup", and "Connect With Me" widgets.

### `./5_Symbols/pages/contact.html`
- **Purpose:** A page for users to get in touch.
- **Key Elements:**
    - "Get In Touch" header.
    - Availability status indicator.
    - Contact information section with email, phone, WhatsApp, address, etc.
    - A contact form for sending a message.

### `./5_Symbols/pages/courses.html`
- **Purpose:** Showcases the AI courses offered.
- **Key Elements:**
    - "Delivery Pilot Showcase" header.
    - A grid of course cards, each with an image, category, title, description, duration, level, and links to enroll.
    - "Coming Soon" section with a newsletter signup form.

### `./5_Symbols/pages/delivery-pilot.html`
- **Purpose:** Describes the "Delivery Pilot" service for AI-powered learning.
- **Key Elements:**
    - Hero section with a description of the service and a call-to-action.
    - "The 3 Stages of Transformation" section (Assessment, Training, Implementation).
    - "Top 10 AI Courses" section.
    - "Support Plans" (pricing) section.
    - A section to schedule a free assessment call.

### `./5_Symbols/pages/early-bird-registration.html`
- **Purpose:** A form for users to register for early access to AI courses.
- **Key Elements:**
    - "Bridge the AI Skills Gap Early!" header.
    - A registration form with fields for email and course interests.
    - "Why Join Our Early Bird List?" section with benefits.

### `./5_Symbols/pages/ebook.html`
- **Purpose:** A landing page for users to download an ebook.
- **Key Elements:**
    - A form to enter an email address to receive the ebook.
    - A success message with a download link after submission.
    - The page content is dynamically updated based on a URL parameter (`type`).

### `./pages/email-form.html`
- **Purpose:** A form for users to get a free Udemy coupon.
- **Key Elements:**
    - "Bridge the AI Skills Gap!" header.
    - A form to enter an email address to receive a coupon code.
    - The page dynamically fetches course data from a YAML file.

### `./5_Symbols/pages/investor.html`
- **Purpose:** Provides information for potential investors.
- **Key Elements:**
    - "Investment Opportunity" hero section.
    - "The Opportunity" section with market statistics.
    - "Why Delivery Pilot?" section with key advantages.
    - "Business Model" and "Use of Funds" sections.
    - A call-to-action to contact for investment inquiries.

### `./5_Symbols/pages/newsletter.html`
- **Purpose:** A page for users to subscribe to the newsletter.
- **Key Elements:**
    - "Join the AI Skills Revolution!" header.
    - A newsletter subscription form.
    - "What You'll Get", "Newsletter Stats", and "Why Subscribe?" sections.
    - A section with recent blog posts.

### `./5_Symbols/pages/post-email-page.html`
- **Purpose:** A "thank you" page displayed after a user submits the email form for a coupon.
- **Key Elements:**
    - "Welcome to the AI Learning Revolution!" header.
    - Displays the course information and a referral code.
    - A button to access the course.
    - The page dynamically fetches course data and email from local storage or URL parameters.

### `./5_Symbols/common-nav.html`
- **Purpose:** A reusable HTML snippet for the common navigation bar.
- **Key Elements:**
    - A responsive navigation bar with a logo, links to all major pages, and a hamburger menu for mobile.
    - A script to handle the hamburger menu functionality.

### `./2025/08/27/🚀-how-to-apply-yaml-configurations-using-kubectl-in-terminal/index.html`
- **Purpose:** A blog post explaining how to apply YAML configurations using kubectl.
- **Key Elements:**
    - A step-by-step guide with code blocks.
    - Key tips and an explanation of the `cat <<EOF` command.

### `./2025/09/14/how_to_talk_to_Computers/index.html`
- **Purpose:** A placeholder file.
- **Key Elements:** Contains only the text "start > End".
---

## File Content

### `./2025/09/14/how_to_talk_to_Computers/index.html`

```
start > End```
