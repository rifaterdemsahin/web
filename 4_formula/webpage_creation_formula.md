# 🧪 Formula: Webpage Creation

This formula provides a standardized process for creating high-quality, premium webpages. It consists of two phases: **Discovery** (gathering requirements) and **The Prompt** (instructing the AI).

---

##  Phase 1: Discovery (The Questions)

Before writing any code, answer the following questions to define the page's purpose and scope.

### 1. Core Identity
- **What is the primary goal of this page?** (e.g., Sell a course, capture emails, inform about a service)
- **Who is the target audience?** (e.g., Developers, executives, students)
- **What is the single most important "Call to Action" (CTA)?** (e.g., "Buy Now", "Subscribe", "Contact Us")

### 2. Content & Structure
- **What are the key sections required?** (e.g., Hero, Features, Testimonials, FAQ, Footer)
- **Do you have specific copy/text ready, or should the AI generate placeholders?**
- **Are there any specific images or assets that must be included?**

### 3. Design & Aesthetics
- **What is the desired "vibe"?** (e.g., Professional & Corporate, Playful & Vibrant, Dark & Futuristic)
- **Are there specific color preferences or brand guidelines?**
- **Should it match the existing site style or have a unique look?**

### 4. Technical Specifics
- **Are there any specific interactive elements?** (e.g., Forms, calculators, sliders)
- **Does it need to integrate with any external tools?** (e.g., n8n, Mailchimp, Google Sheets)

---

## Phase 2: The Prompt (The Directives)

Once the discovery phase is complete, use the following prompt to instruct the AI. Fill in the bracketed sections `[ ]` with your specific details.

```markdown
# Role
You are an expert Web Developer and UI/UX Designer known for creating "premium," high-converting, and visually stunning web experiences.

# Task
Create a single-file HTML webpage (or a set of files if necessary) for: **[INSERT PAGE NAME/PURPOSE HERE]**

# Context & Requirements
[PASTE ANSWERS FROM DISCOVERY PHASE HERE]

# Technology Stack
- **Structure**: HTML5 (Semantic, Accessible)
- **Styling**: Vanilla CSS (No frameworks like Tailwind/Bootstrap unless explicitly requested).
- **Interactivity**: Vanilla JavaScript.
- **Icons**: FontAwesome (CDN) or SVG.
- **Fonts**: Google Fonts (Inter, Roboto, or Outfit).

# Design Directives (Non-Negotiable)
1.  **Premium Aesthetics**: The design MUST look professional and expensive. Use generous whitespace, subtle shadows, and glassmorphism where appropriate.
2.  **Typography**: Use a modern type scale. Headings should be bold and impactful. Body text should be legible with good line height.
3.  **Color Palette**: Use a harmonious color palette. Avoid default HTML colors (red, blue). Use HSL or Hex codes for specific, curated shades.
4.  **Responsiveness**: The page must be fully responsive and look perfect on Mobile, Tablet, and Desktop.
5.  **Micro-Animations**: Add subtle hover effects to buttons and cards. Elements should fade in or slide up upon scrolling into view.

# SEO Best Practices
- Include a descriptive `<title>` tag.
- Include a compelling `<meta name="description">`.
- Use proper heading hierarchy (`h1` -> `h2` -> `h3`).
- Ensure all interactive elements have `aria-labels` if text is not visible.

# Implementation Process
1.  **Plan**: Briefly outline the structure based on the requirements.
2.  **Foundation**: Set up the HTML skeleton and core CSS variables (colors, typography).
3.  **Components**: Build the sections (Hero, Features, etc.) one by one.
4.  **Polish**: Add the "wow" factor with animations and final CSS tweaks.

# Output
Provide the complete, copy-pasteable code for:
1.  `index.html` (containing HTML, CSS in `<style>`, and JS in `<script>` for a single-file solution, or separate files if requested).
```
