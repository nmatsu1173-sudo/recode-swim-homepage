import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the entire <style> block with our new sincere, light, clean CSS.
new_css = """  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    :root {
      /* Color Palette (Sincere Light Theme) */
      --color-heading: #1E293B; /* Deep Navy */
      --color-text-main: #334155; /* Slate 700 */
      --color-secondary: #475569; /* Slate 600 */
      --color-accent: #0284C7; /* Sincere Swimming Blue */
      --color-accent-light: #E0F2FE; /* Sky 100 for light backgrounds */
      --color-primary: #FFFFFF;
      --color-bg-base: #FFFFFF;
      --color-bg-alt: #F8FAFC; /* Slate 50 */
      --color-border: #E2E8F0; /* Slate 200 */

      /* Typography */
      --font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Segoe UI", "Hiragino Kaku Gothic ProN", "Hiragino Sans", "Meiryo", sans-serif;
      --line-height-base: 1.85;
      --letter-spacing-base: 0.05em;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: var(--font-family);
      font-size: 1.05rem;
      color: var(--color-text-main);
      background-color: var(--color-bg-base);
      line-height: var(--line-height-base);
      letter-spacing: var(--letter-spacing-base);
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }

    img { max-width: 100%; height: auto; display: block; }

    .highlight {
      font-weight: 700;
      color: var(--color-heading);
      background: linear-gradient(transparent 65%, var(--color-accent-light) 65%);
      padding: 0 0.2em;
    }

    .highlight-white {
      font-weight: 700;
      color: var(--color-heading);
      background: linear-gradient(transparent 65%, var(--color-accent-light) 65%);
      padding: 0 0.2em;
    }

    @media (min-width: 768px) { .sp-only { display: none; } }
    .ib { display: inline-block; }
    .nowrap { display: inline-block; white-space: nowrap; }

    h1, h2, h3, h4 {
      line-height: 1.4;
      font-weight: 700;
      color: var(--color-heading);
    }

    h2 {
      font-size: 2rem;
      margin-bottom: 3.5rem;
      text-align: center;
      position: relative;
      letter-spacing: 0.08em;
    }

    h2::after {
      content: "";
      position: absolute;
      bottom: -15px;
      left: 50%;
      transform: translateX(-50%);
      width: 40px;
      height: 3px;
      background-color: var(--color-accent);
      border-radius: 2px;
    }

    h3 { font-size: 1.35rem; margin-bottom: 1rem; }
    p { margin-bottom: 1.5rem; color: var(--color-secondary); }

    .container { width: 100%; max-width: 800px; margin: 0 auto; padding: 0 1.5rem; position: relative; z-index: 2; }
    section { padding: 5rem 0; position: relative; }

    /* Clean Background Sections */
    .bg-carbon, .bg-alt-light, .bg-alt {
      background-color: var(--color-bg-alt);
      color: var(--color-text-main);
      padding: 5rem 0;
      margin: 0;
      z-index: 1;
      clip-path: none;
    }
    
    .bg-carbon h2, .bg-alt h2, .bg-alt-light h2 { color: var(--color-heading); }
    .bg-carbon p, .bg-alt p, .bg-alt-light p { color: var(--color-secondary); }

    .text-center { text-align: center; }

    /* Buttons */
    .btn {
      display: inline-block;
      width: 100%;
      max-width: 320px;
      text-align: center;
      background: var(--color-accent);
      color: #FFFFFF;
      text-decoration: none;
      padding: 1.25rem 2rem;
      border-radius: 8px; /* Sincere rounded corners */
      font-weight: 600;
      font-size: 1.1rem;
      letter-spacing: 0.05em;
      transition: all 0.3s ease;
      border: none;
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.2);
    }

    .btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(2, 132, 199, 0.3);
      background: #0369A1; /* Slightly darker blue on hover */
      color: #FFFFFF;
    }

    /* Hero */
    .hero {
      min-height: 80vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding-top: 4rem;
      clip-path: none;
      background-color: var(--color-bg-base);
    }

    .hero-slideshow, .hero-slide, .hero-overlay {
      position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    }

    .hero-slideshow { z-index: 1; }
    .hero-slide {
      background-size: cover; background-position: center; opacity: 0;
      animation: heroSlideshowAnim 15s infinite; filter: brightness(0.85);
    }
    .hero-slide:nth-child(1) { background-image: url('assets/images/hero_swim_3.png'); animation-delay: 0s; }
    .hero-slide:nth-child(2) { background-image: url('assets/images/recode_hero_bg2.jpg'); animation-delay: 5s; }
    .hero-slide:nth-child(3) { background-image: url('assets/images/recode_hero_bg1.jpg'); animation-delay: 10s; }

    .hero-overlay {
      background: linear-gradient(90deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.85) 50%, rgba(255,255,255,0.4) 100%);
      z-index: 2;
    }

    @keyframes heroSlideshowAnim {
      0% { opacity: 0; transform: scale(1.02); }
      8%, 33% { opacity: 1; }
      41%, 100% { opacity: 0; transform: scale(1.06); }
    }

    .hero-logo {
      display: inline-flex; align-items: center; gap: 0.7rem;
      font-size: 1.4rem; font-weight: 700; letter-spacing: 0.1em;
      margin-bottom: 2.5rem; color: var(--color-heading);
      position: relative;
    }
    .hero-logo-img { width: 32px; height: 32px; object-fit: contain; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1)); }

    .hero-catch {
      font-size: 2.8rem; margin-bottom: 1.5rem; line-height: 1.3; color: var(--color-heading);
    }
    .hero-catch span { color: var(--color-accent); }

    .hero-sub {
      font-size: 1.15rem; margin-bottom: 2.5rem; color: var(--color-text-main); font-weight: 500;
      line-height: 1.8;
    }

    /* Cards */
    .grid-cards {
      display: grid; grid-template-columns: 1fr; gap: 1.5rem; margin-top: 2rem;
    }
    @media (min-width: 768px) { .grid-cards { grid-template-columns: repeat(2, 1fr); gap: 2rem; } }

    .sport-card {
      background: #FFFFFF;
      border: 1px solid var(--color-border);
      padding: 2.5rem 2rem;
      border-radius: 12px; /* Soft rounded corners */
      box-shadow: 0 4px 12px rgba(0,0,0,0.03);
      position: relative;
      transition: all 0.3s ease;
      z-index: 1;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }
    .sport-card::before {
      content: none;
    }
    .sport-card:hover { transform: translateY(-3px); box-shadow: 0 10px 24px rgba(0,0,0,0.06); border-color: var(--color-accent-light); }

    .sport-card h3 { color: var(--color-heading); font-size: 1.25rem; margin-bottom: 1rem; }
    .sport-card p { margin: 0; color: var(--color-secondary); }

    /* Features / Flow */
    .flow-list { display: flex; flex-direction: column; gap: 1rem; max-width: 600px; margin: 0 auto; }
    .flow-card {
      background: #FFFFFF; padding: 1.75rem 2rem;
      border: 1px solid var(--color-border);
      border-left: 4px solid var(--color-border);
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.02);
      display: flex; flex-direction: column;
      transition: all 0.3s ease;
    }
    .flow-card.flow-active { border-left-color: var(--color-accent); }
    .flow-step { font-weight: 600; color: var(--color-accent); letter-spacing: 0.1em; margin-bottom: 0.5rem; font-size: 0.9rem; }
    .flow-title { font-size: 1.2rem; margin-bottom: 0.5rem; color: var(--color-heading); }
    
    /* Pricing */
    .pricing-card {
      background: #FFFFFF;
      padding: 2.5rem;
      border: 1px solid var(--color-border);
      border-radius: 12px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.04);
      text-align: center;
      position: relative;
      border-top: 4px solid var(--color-accent);
    }
    .pricing-card:hover { box-shadow: 0 10px 30px rgba(0,0,0,0.08); }
    .pricing-price { font-size: 2.2rem; font-weight: 700; color: var(--color-accent); margin: 1.5rem 0; }
    .pricing-price span { font-size: 1rem; color: var(--color-secondary); font-weight: 500; }
    
    /* Remove Carbon Theme variants */
    .bg-carbon .sport-card, .bg-carbon .pricing-card, .bg-carbon .flow-card {
      background: #FFFFFF; color: var(--color-text-main); box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }
    .bg-carbon .sport-card h3, .bg-carbon .flow-title, .bg-carbon .pricing-card h3 { color: var(--color-heading); }
    .bg-carbon .pricing-price { color: var(--color-accent); }
    .bg-carbon .sport-card p, .bg-carbon .flow-desc { color: var(--color-secondary); }

    /* Cinema / Image Grid */
    .cinema-slider-container {
      max-width: 600px;
      margin: 2.5rem auto 0;
      position: relative;
    }

    .cinema-card-wrapper {
      width: 100%;
      aspect-ratio: 1672 / 941;
      position: relative;
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid var(--color-border);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
    }

    .cinema-slide {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-size: cover;
      background-position: center;
      opacity: 0;
      transition: opacity 0.8s ease-in-out;
      z-index: 1;
    }

    .cinema-slide.active { opacity: 1; z-index: 2; }
    
    .cinema-nav {
      display: flex; justify-content: center; align-items: center; margin-top: 1.5rem; gap: 0.5rem;
    }

    .cinema-nav-btn {
      background: none; border: none; color: var(--color-secondary); cursor: pointer; padding: 0.5rem;
      border-radius: 4px; display: flex; flex-direction: column; align-items: center; transition: color 0.3s ease;
    }
    .cinema-nav-btn.active { color: var(--color-accent); font-weight: 600; }
    .nav-num { font-size: 0.8rem; opacity: 0.8; }
    .nav-text { font-size: 0.95rem; }

    /* Footer */
    footer {
      background: var(--color-bg-base); color: var(--color-secondary); text-align: center; padding: 3rem 0;
      border-top: 1px solid var(--color-border);
      clip-path: none; margin-top: 0;
    }

    @media (min-width: 768px) {
      h2 { font-size: 2.4rem; }
      .hero-catch { font-size: 3.5rem; }
      .btn { max-width: 280px; }
    }
  </style>"""

html = re.sub(r'<style>.*?</style>', new_css, html, flags=re.DOTALL)

# Revert specific text colors to inherit from body
html = html.replace('style="color: #FFFFFF;"', '')
html = html.replace('class="hero-catch" >\n        目標までの', 'class="hero-catch">\n        目標までの')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html to Sincere Light Theme.")
