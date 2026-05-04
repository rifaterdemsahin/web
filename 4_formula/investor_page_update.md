# Implementation Plan: Investor Page Refinement

The goal is to modernize the `investor.html` page to reflect an AI-first business model instead of a managed service provider (MSP) approach, while improving overall readability and visual appeal.

## 1. Content Changes

### 1.1 Remove Old Business Model
- Remove the "💼 Business Model" section (lines 397-419) which lists daily rates (£500, £800, £1,200).
- This model is too labor-intensive and doesn't scale as well as an AI-first approach.

### 1.2 Replace with "AI-First Transformation" Model
- Introduce a new section focused on platform-led growth:
    - **Platform Licensing:** Subscription-based access to AI-powered skills gap analysis.
    - **Agentic Framework Implementation:** Enterprise solutions for deploying AI agents in developer workflows.
    - **Strategic Advisory:** High-level transformation consulting for building "Always Learning" organizations.
    - **Strategic Partnerships:** Revenue sharing with AI and Cloud providers.

### 1.3 Update "Why Delivery Pilot?" Section
- Update the "Scalable Model" card (line 355) to remove mentions of daily rates.
- Update the "Recurring Revenue" card (line 370) to focus on platform subscriptions and long-term enterprise integration.

### 1.4 Update Top Section (Hero & Opportunity)
- Refine the Hero section to be more "reading friendly" and professional.
- Enhance the "💡 The Opportunity" section with better visual hierarchy.

## 2. Design Improvements

- **Typography:** Increase line heights and letter spacing for better readability.
- **Glassmorphism:** Apply subtle backdrop filters and gradients to content cards.
- **Animations:** Add subtle entry animations for cards.
- **Color Palette:** Ensure a premium look using deep blues, purples, and clean whites.

## 3. Implementation Steps

1.  **Backup:** (Handled by version control).
2.  **Modify `investor.html`:**
    - Update the CSS to include modern design tokens.
    - Update the Hero HTML.
    - Update the "Why Delivery Pilot?" section content.
    - Replace the "Business Model" section.
3.  **Verification:**
    - Check mobile responsiveness.
    - Validate semantic HTML and SEO tags.
