import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS for about-section-dark
dark_css = """
    .about-section-dark {
      position: relative;
      background: #0F172A;
      color: #FFFFFF;
      padding: 6rem 0;
      overflow: hidden;
    }
    .about-section-dark::before {
      content: '';
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: linear-gradient(to right, rgba(15,23,42,0.95) 0%, rgba(15,23,42,0.4) 100%), url('assets/images/recode_watch_bg.png') center/cover no-repeat;
      z-index: 0;
      opacity: 0.8;
      filter: grayscale(30%);
    }
    .about-section-dark .container {
      position: relative; z-index: 1;
    }
    .about-section-dark h2 {
      color: #FFFFFF;
      text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
    .about-section-dark p {
      color: #E2E8F0;
      text-shadow: 0 1px 3px rgba(0,0,0,0.8);
      font-weight: 500;
      font-size: 1.15rem !important; /* Slightly larger for readability */
    }
    .about-section-dark .highlight {
      background: transparent;
      color: #38BDF8; /* bright neon blue for dark mode */
      font-weight: 700;
    }
"""
html = html.replace('/* Footer */', dark_css + '\n/* Footer */')

# 2. Update HTML class
html = html.replace('<section class="about-section" id="about">', '<section class="about-section-dark" id="about">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated RECODE section to dark mode with watch background.")
