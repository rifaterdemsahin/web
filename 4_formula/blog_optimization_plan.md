# Blog SEO and Inter-linking Plan

## Objective
Enhance discoverability and search engine optimization for blog posts under the `2026` directory and beyond.

## Steps Taken
1.  **Robots.txt Optimization**:
    *   Added explicit `Allow` rules for all blog year directories (`2020`, `2023`, `2024`, `2025`, `2026`, `2027`).
    *   Confirmed `Sitemap` location for search engine guidance.

2.  **Automated Post Relationships**:
    *   Developed a Python script to scan the blog directories for `2020`, `2023`, `2024`, `2025`, and `2026`.
    *   Programmatically injected "Related Reading" sections into over 4,600 blog posts.
    *   Each post now links to the 3 most recent posts from the same year, improving user engagement and internal link density across the entire archive.

3.  **Comprehensive Sitemap Generation**:
    *   Updated the site's `sitemap.xml` to include all historical blog posts across all years.
    *   The sitemap now contains over 4,600 URLs, providing a clear roadmap for search engine crawlers.

4.  **Deployment**:
    *   All changes were committed and pushed to the `main` branch on GitHub.

## Future Recommendations
*   Run the linking script periodically as new posts are added.
*   Consider cross-year relationships for even better topical clustering.
