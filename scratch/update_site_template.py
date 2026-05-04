import os
import re

# Master Nav and Footer from 5_Symbols/pages/index.html
NAV_HTML_TEMPLATE = """
    <nav class="navbar">
        <div class="nav-container container">
            <a href="{prefix}5_Symbols/pages/index.html" class="navbar-brand">Rifat Erdem Sahin</a>
            <button class="hamburger" aria-label="Toggle navigation">&#9776;</button>
            
            <ul class="nav-links">
                <li class="has-dropdown">
                    <a href="{prefix}5_Symbols/pages/about.html">👤 About</a>
                    <ul class="dropdown-menu">
                        <li><a href="{prefix}5_Symbols/pages/about.html#who">Who I Am</a></li>
                        <li><a href="{prefix}5_Symbols/pages/about.html#track-record">Track Record</a></li>
                        <li><a href="{prefix}5_Symbols/pages/about.html#credentials">Philosophy</a></li>
                    </ul>
                </li>
                <li class="has-dropdown">
                    <a href="/blog/">📝 Blog</a>
                    <ul class="dropdown-menu">
                        <li><a href="/blog/">Latest Posts</a></li>
                        <li><a href="{prefix}5_Symbols/pages/archive.html">Archive</a></li>
                        <li><a href="{prefix}5_Symbols/pages/newsletter.html">Newsletter</a></li>
                    </ul>
                </li>
                <li class="has-dropdown">
                    <a href="{prefix}5_Symbols/pages/latest.html">✨ Content</a>
                    <ul class="dropdown-menu">
                        <li><a href="https://www.youtube.com/@RifatErdemSahin" target="_blank">YouTube</a></li>
                        <li><a href="{prefix}5_Symbols/pages/latest.html">Latest Updates</a></li>
                        <li><a href="{prefix}5_Symbols/pages/tags.html">Topics</a></li>
                    </ul>
                </li>
                <li class="has-dropdown">
                    <a href="{prefix}5_Symbols/pages/courses.html">🎓 Courses</a>
                    <ul class="dropdown-menu">
                        <li><a href="https://www.coursera.org/instructor/~184662540" target="_blank">Coursera</a></li>
                        <li><a href="https://www.udemy.com/user/rifat-erdem-sahin-2/" target="_blank">Udemy</a></li>
                        <li><a href="{prefix}5_Symbols/pages/ebook.html">Free Ebook</a></li>
                    </ul>
                </li>
                <li class="has-dropdown">
                    <a href="{prefix}5_Symbols/pages/delivery-pilot.html">🚀 Services</a>
                    <ul class="dropdown-menu">
                        <li><a href="{prefix}5_Symbols/pages/delivery-pilot.html">Delivery Pilot</a></li>
                        <li><a href="{prefix}5_Symbols/pages/enterprise-ai-maturity.html">Enterprise AI</a></li>
                        <li><a href="{prefix}5_Symbols/pages/workshops.html">Workshops</a></li>
                    </ul>
                </li>
                <li><a href="https://github.com/rifaterdemsahin" target="_blank">🛠️ Tools</a></li>
                <li><a href="{prefix}5_Symbols/pages/contact.html">📞 Contact</a></li>
            </ul>

            <div class="nav-utility">
                <a href="https://www.linkedin.com/in/rifaterdemsahin/" target="_blank" class="social-icon" style="color: var(--text-secondary); font-size: 1.2rem; margin-right: 1rem;"><i class="fab fa-linkedin"></i></a>
                <a href="{prefix}5_Symbols/pages/contact.html" class="btn btn-primary btn-sm btn-cta">Book a Call</a>
            </div>
        </div>
    </nav>
"""

FOOTER_HTML_TEMPLATE = """
    <footer class="footer">
        <div class="footer-content">
            <div class="footer-links">
                <a href="{prefix}5_Symbols/pages/about.html">About</a>
                <a href="/blog/">Blog</a>
                <a href="{prefix}5_Symbols/pages/latest.html">Content</a>
                <a href="{prefix}5_Symbols/pages/courses.html">Courses</a>
                <a href="{prefix}5_Symbols/pages/delivery-pilot.html">Services</a>
                <a href="{prefix}5_Symbols/pages/workshops.html">Workshops</a>
                <a href="https://github.com/rifaterdemsahin" target="_blank">Tools</a>
                <a href="{prefix}5_Symbols/pages/contact.html">Contact</a>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Rifat Erdem Sahin. All rights reserved.</p>
                <p style="color: #00ff88; margin-top: 1rem;">🚀 Bridging the AI Skills Gap | SC Cleared | NATO Security Clearance</p>
                <p style="font-size: 0.8rem; opacity: 0.7; margin-top: 0.5rem;">Cambridge, UK | Dual British/Turkish Citizen</p>
            </div>
        </div>
    </footer>
"""

HAMBURGER_SCRIPT = """
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
"""

def update_file(file_path, root_dir):
    relative_path = os.path.relpath(file_path, root_dir)
    # Special case for 5_Symbols/pages - prefix should be ../
    if "5_Symbols/pages" in relative_path:
        prefix = "../"
    else:
        depth = relative_path.count(os.sep)
        prefix = "../" * depth
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip the master file itself to avoid recursive templates
    if file_path.endswith("5_Symbols/pages/index.html"):
        return

    # 1. Update Navigation
    nav_pattern = re.compile(r'<nav class="navbar">.*?</nav>', re.DOTALL)
    new_nav = NAV_HTML_TEMPLATE.format(prefix=prefix)
    content = nav_pattern.sub(new_nav, content)
    
    # 2. Update Footer
    footer_pattern = re.compile(r'<footer class="footer">.*?</footer>', re.DOTALL)
    new_footer = FOOTER_HTML_TEMPLATE.format(prefix=prefix)
    content = footer_pattern.sub(new_footer, content)
    
    # 3. Ensure main.css is present
    if 'main.css' not in content:
        main_css_link = f'<link rel="stylesheet" href="{prefix}5_Symbols/assets/css/main.css">'
        # Look for common-styles.css with any prefix
        css_pattern = re.compile(r'<link rel="stylesheet" href=".*?common-styles\.css">')
        match = css_pattern.search(content)
        if match:
            content = content.replace(match.group(0), main_css_link + "\n    " + match.group(0))
        else:
            # Fallback: insert before </head>
            content = content.replace('</head>', f'    {main_css_link}\n</head>')

    # 4. Ensure Inter font is present
    inter_font = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">'
    if 'family=Inter' not in content:
        content = content.replace('</head>', f'    {inter_font}\n</head>')

    # 5. Ensure Hamburger script is present
    if 'hamburger' not in content or '.classList.toggle(\'active\')' not in content:
        content = content.replace('</body>', HAMBURGER_SCRIPT + "\n</body>")
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    root_dir = "/Users/rifaterdemsahin/projects/web"
    
    # 1. Year directories
    for year in range(2020, 2028):
        year_dir = os.path.join(root_dir, str(year))
        if os.path.exists(year_dir):
            for root, dirs, files in os.walk(year_dir):
                for file in files:
                    if file == "index.html":
                        file_path = os.path.join(root, file)
                        update_file(file_path, root_dir)
    
    # 2. blog directory
    blog_dir = os.path.join(root_dir, "blog")
    if os.path.exists(blog_dir):
        for root, dirs, files in os.walk(blog_dir):
            for file in files:
                if file.endswith(".html"):
                    update_file(os.path.join(root, file), root_dir)
                    
    # 3. 5_Symbols/pages directory
    pages_dir = os.path.join(root_dir, "5_Symbols/pages")
    if os.path.exists(pages_dir):
        for file in os.listdir(pages_dir):
            if file.endswith(".html"):
                update_file(os.path.join(pages_dir, file), root_dir)

if __name__ == "__main__":
    main()
