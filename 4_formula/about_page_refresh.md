# About Page Refresh Plan

The goal is to remove the interactive 3D tilt animation from the About page and improve its overall professionalism and readability.

## Objectives
1. **Remove Animation**: Strip out the `mousemove` event listener that causes cards to tilt.
2. **Improve Readability**:
    - Enhance typography contrast.
    - Standardize spacing between sections.
    - Simplify the layout of the CV-style content.
3. **Professionalism**:
    - Replace the "floating" card effect with a more stable, grounded design.
    - Refine the color palette for better professional appeal.
    - Clean up the header and footer integration.

## Proposed Changes

### 1. `about.html`
- **Script Removal**: Delete the `document.addEventListener('mousemove', ...)` block.
- **Content Structure**:
    - Ensure clear section headers.
    - Use bullet points for easier scanning of track record and skills.
    - Refine the "Download CV" section to look like a professional sidebar or footer call-to-action.

### 2. Styling (CSS)
- **Card Design**: Remove `perspective` and `transform` logic from hover states.
- **Typography**:
    - Increase base font size slightly if needed.
    - Use a clearer hierarchy for `h1`, `h2`, and `h3`.
- **White Space**: Add more padding between major content blocks to prevent visual clutter.

## Implementation Steps
1. Create a backup (implicit in agent workflow).
2. Edit `about.html` to remove the JS animation code.
3. Apply CSS updates to `about.html` (either inline or via `main.css` if global, but I'll stick to specific improvements for about page).
4. Verify the look and feel.

## Verification
- Confirm that moving the mouse does not cause cards to tilt.
- Verify that the text is easy to read on both desktop and mobile.
- Ensure all links and buttons are clearly visible and professional.
