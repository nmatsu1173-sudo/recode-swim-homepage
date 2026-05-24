import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS
hero_css_pattern = r'(\.hero\s*\{[^}]*?background:\s*)linear-gradient\([^)]+\),\s*url\([^)]+\)[^;]+;'
new_hero_css = r'\1transparent;\n      overflow: hidden;\n      position: relative;'

html = re.sub(hero_css_pattern, new_hero_css, html)

slideshow_css = """
    .hero-slideshow, .hero-slide, .hero-overlay {
      position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    }
    .hero-slideshow { z-index: 0; }
    .hero-slide {
      background-size: cover; background-position: center; opacity: 0;
      animation: heroZoomFade 18s infinite linear; 
    }
    /* 3 images, 18s total. Each is visible for 6s. 
       Fade in over 1.5s, hold for 4.5s, fade out over 1.5s */
    .hero-slide:nth-child(1) { background-image: url('assets/images/hero_swim_3.png'); animation-delay: 0s; }
    .hero-slide:nth-child(2) { background-image: url('assets/images/recode_hero_bg2.jpg'); animation-delay: 6s; }
    .hero-slide:nth-child(3) { background-image: url('assets/images/recode_hero_bg1.jpg'); animation-delay: 12s; }

    .hero-overlay {
      background: linear-gradient(135deg, rgba(15,23,42,0.85) 0%, rgba(2,132,199,0.75) 100%);
      z-index: 1;
      pointer-events: none; /* so it doesn't block clicks if any */
    }

    @keyframes heroZoomFade {
      0% { opacity: 0; transform: scale(1.0); }
      8% { opacity: 1; }
      33% { opacity: 1; }
      41% { opacity: 0; transform: scale(1.1); }
      100% { opacity: 0; transform: scale(1.1); }
    }
"""
html = html.replace('/* Hero */', '/* Hero */\n' + slideshow_css)

# 2. Update HTML
# Find <section class="hero"...> and insert the div right after the opening tag
section_match = re.search(r'<section class="hero"[^>]*>', html)
if section_match:
    section_tag = section_match.group(0)
    slideshow_html = """
    <div class="hero-slideshow">
      <div class="hero-slide"></div>
      <div class="hero-slide"></div>
      <div class="hero-slide"></div>
    </div>
    <div class="hero-overlay"></div>
"""
    html = html.replace(section_tag, section_tag + slideshow_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added zooming slideshow to Hero.")
