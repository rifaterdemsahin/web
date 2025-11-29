**Integration Steps:**

1.  **Place `common-styles.css`:**
    *   Save the `common-styles.css` file in your project's `assets/css/` directory.
    *   Link this CSS file in the `<head>` section of *all* your HTML pages. Ensure it's placed after any existing reset or base styles (like `main.css`) but before any page-specific styles, allowing for proper cascading and overrides.
    *   Example for files inside the `pages/` directory (like `pages/index.html`, `pages/about.html`, etc.):
        ```html
        <head>
            <!-- ... other meta and link tags ... -->
            <link rel="stylesheet" href="../assets/css/main.css"> <!-- Existing CSS -->
            <link rel="stylesheet" href="../assets/css/common-styles.css"> <!-- New common styles -->
            <!-- ... page-specific styles if any ... -->
        </head>
        ```

2.  **Integrate `common-nav.html`:**
    *   Copy the entire content of `common-nav.html` (including the `<nav>` element and the `<script>` tag).
    *   In *each* of your HTML pages where you want this navigation menu to appear, replace your existing navigation structure (typically within a `<nav>` tag near the top of your `<body>`) with the `<nav>` element from `common-nav.html`.
    *   Place the `<script>` tag from `common-nav.html` at the end of your `<body>` tag, just before the closing `</body>` tag. This ensures the DOM is fully loaded before the script tries to access elements.

    *Example for a page inside the `pages/` directory:*
    ```html
    <body>
        <!-- Common Navigation Bar -->
        <nav class="navbar">
            <div class="navbar-container container">
                <a href="index.html" class="navbar-brand">Rifat Erdem Sahin</a>
                <button class="hamburger" aria-label="Toggle navigation">&#9776;</button>
                <ul class="nav-links">
                    <li><a href="index.html">🏠 Home</a></li>
                    <li><a href="delivery-pilot.html">🚀 Delivery Pilot</a></li>
                    <li><a href="courses.html">🎓 Courses</a></li>
                    <li><a href="early-bird-registration.html">🐦 Early Bird</a></li>
                    <li><a href="ebook.html">📚 Ebook</a></li>
                    <li><a href="newsletter.html">📧 Newsletter</a></li>
                    <li><a href="investor.html">💼 Investors</a></li>
                    <li><a href="about.html">👤 About</a></li>
                    <li><a href="contact.html">📞 Contact</a></li>
                </ul>
            </div>
        </nav>

        <!-- Your main page content -->
        <main>
            <!-- ... content here ... -->
        </main>

        <!-- Footer -->
        <footer>
            <!-- ... footer content ... -->
        </footer>

        <!-- Common Navigation Script (place at the end of body) -->
        <script>
            document.addEventListener('DOMContentLoaded', () => {
                const hamburger = document.querySelector('.hamburger');
                const navLinks = document.querySelector('.nav-links');

                if (hamburger && navLinks) {
                    hamburger.addEventListener('click', () => {
                        navLinks.classList.toggle('active');
                    });
                }
            });
        </script>
        <!-- Your other scripts -->
        <script src="assets/js/main.js"></script>
    </body>
    ```

**Important Notes on Paths:**

*   **Current Setup:** The links provided in `common-nav.html` (e.g., `index.html`, `delivery-pilot.html`) are designed to work when the HTML file integrating them is located within the `pages/` directory (e.g., `pages/index.html`, `pages/about.html`). In this context, `index.html` refers to `pages/index.html`, and `delivery-pilot.html` refers to `pages/delivery-pilot.html`.
*   **Root `index.html`:** Your project's root `index.html` currently redirects to `pages/index.html`. If you were to use this common menu in the root `index.html` *without* redirection, you would need to adjust the paths within the `<nav>` snippet to `pages/index.html`, `pages/delivery-pilot.html`, etc. (e.g., `<a href="pages/index.html">🏠 Home</a>`). Given your redirection, this is not strictly necessary for the root `index.html`.

This setup will provide a consistent navigation and styling across your specified HTML pages.