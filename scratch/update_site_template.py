import os
import re

files = [
    "about.html", "blog.html", "contact.html", "courses.html", 
    "delivery-pilot.html", "enterprise-ai-maturity.html", "index.html"
]
base_path = "/Users/rifaterdemsahin/projects/web/5_Symbols/pages/"

navbar_html = """    <nav class="navbar">
        <div class="nav-container container">
            <a href="index.html" class="navbar-brand">Rifat Erdem Sahin</a>
            <button class="hamburger" aria-label="Toggle navigation">&#9776;</button>
            
            <ul class="nav-links">
                <li class="has-dropdown">
                    <a href="about.html">👤 About</a>
                    <ul class="dropdown-menu">
                        <li><a href="about.html#who">Who I Am</a></li>
                        <li><a href="about.html#track-record">Track Record</a></li>
                        <li><a href="about.html#credentials">Philosophy</a></li>
                    </ul>
                </li>
                <li class="has-dropdown">
                    <a href="/blog/">📝 Blog</a>
                    <ul class="dropdown-menu">
                        <li><a href="/blog/">Latest Posts</a></li>
                        <li><a href="archive.html">Archive</a></li>
                        <li><a href="newsletter.html">Newsletter</a></li>
                    </ul>
                </li>
                <li class="has-dropdown">
                    <a href="latest.html">✨ Content</a>
                    <ul class="dropdown-menu">
                        <li><a href="https://www.youtube.com/@RifatErdemSahin" target="_blank">YouTube</a></li>
                        <li><a href="latest.html">Latest Updates</a></li>
                        <li><a href="tags.html">Topics</a></li>
                    </ul>
                </li>
                <li class="has-dropdown">
                    <a href="courses.html">🎓 Courses</a>
                    <ul class="dropdown-menu">
                        <li><a href="https://www.coursera.org/instructor/~184662540" target="_blank">Coursera</a></li>
                        <li><a href="https://www.udemy.com/user/rifat-exclusive-sahin-2/" target="_blank">Udemy</a></li>
                        <li><a href="ebook.html">Free Ebook</a></li>
                    </ul>
                </li>
                <li class="has-dropdown">
                    <a href="delivery-pilot.html">🚀 Services</a>
                    <ul class="dropdown-menu">
                        <li><a href="delivery-pilot.html">Delivery Pilot</a></li>
                        <li><a href="enterprise-ai-maturity.html">Enterprise AI</a></li>
                        <li><a href="workshops.html">Workshops</a></li>
                    </ul>
                </li>
                <li><a href="https://github.com/rifaterdemsahin" target="_blank">🛠️ Tools</a></li>
                <li><a href="contact.html">📞 Contact</a></li>
            </ul>

            <div class="nav-utility">
                <a href="https://www.linkedin.com/in/rifaterdemsahin/" target="_blank" class="social-icon" style="color: var(--text-secondary); font-size: 1.2rem; margin-right: 1rem;"><i class="fab fa-linkedin"></i></a>
                <a href="contact.html" class="btn btn-primary btn-sm btn-cta">Book a Call</a>
            </div>
        </div>
    </nav>"""

footer_html = """    <footer class="footer">
        <div class="footer-content">
            <div class="footer-links">
                <a href="about.html">About</a>
                <a href="/blog/">Blog</a>
                <a href="latest.html">Content</a>
                <a href="courses.html">Courses</a>
                <a href="delivery-pilot.html">Services</a>
                <a href="https://github.com/rifaterdemsahin" target="_blank">Tools</a>
                <a href="contact.html">Contact</a>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Rifat Erdem Sahin. All rights reserved.</p>
                <p style="color: #00ff88; margin-top: 1rem;">🚀 Bridging the AI Skills Gap | SC Cleared | NATO Security Clearance</p>
                <p style="font-size: 0.8rem; opacity: 0.7; margin-top: 0.5rem;">Cambridge, UK | Dual British/Turkish Citizen</p>
            </div>
        </div>
    </footer>"""

for filename in files:
    file_path = os.path.join(base_path, filename)
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.read()
        
        # Replace Navbar
        content = re.sub(r'<nav class="navbar">.*?</nav>', navbar_html, content, flags=re.DOTALL)
        
        # Replace Footer
        content = re.sub(r'<footer class="footer">.*?</footer>', footer_html, content, flags=re.DOTALL)
        
        with open(file_path, "w") as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"File not found: {filename}")
