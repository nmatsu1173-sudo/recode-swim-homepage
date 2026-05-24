import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the entire <style> block with our new bold, angled, sports aesthetic CSS.
new_css = """  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,400;0,600;0,800;0,900;1,800;1,900&display=swap');

    :root {
      /* Color Palette (Dynamic Sports Theme) */
      --color-heading: #111111;
      --color-text-main: #333333;
      --color-secondary: #555555;
      --color-accent: #00E5FF; /* Vivid Swimming Blue */
      --color-accent-dark: #00B8CC;
      --color-primary: #FFFFFF;
      --color-bg-base: #FFFFFF;
      --color-bg-alt: #F4F6F8;
      --color-carbon: #141414; /* Carbon Black */
      --color-border: #E5E7EB;

      /* Typography */
      --font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Segoe UI", "Hiragino Kaku Gothic ProN", "Hiragino Sans", sans-serif;
      --line-height-base: 1.7;
      --letter-spacing-base: 0.02em;
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
      font-weight: 900;
      font-style: italic;
      color: var(--color-carbon);
      background: linear-gradient(transparent 60%, var(--color-accent) 60%);
      padding: 0 0.1em;
      text-transform: uppercase;
    }

    .highlight-white {
      font-weight: 900;
      font-style: italic;
      color: #FFFFFF;
      background: linear-gradient(transparent 60%, var(--color-accent) 60%);
      padding: 0 0.1em;
      text-transform: uppercase;
    }

    @media (min-width: 768px) { .sp-only { display: none; } }
    .ib { display: inline-block; }
    .nowrap { display: inline-block; white-space: nowrap; }

    h1, h2, h3, h4 {
      line-height: 1.2;
      font-weight: 900;
      font-style: italic;
      text-transform: uppercase;
      color: var(--color-heading);
      letter-spacing: 0.05em;
    }

    h2 {
      font-size: 2.5rem;
      margin-bottom: 3rem;
      text-align: center;
      position: relative;
    }

    h2::after {
      content: "";
      position: absolute;
      bottom: -15px;
      left: 50%;
      transform: translateX(-50%) skewX(-20deg);
      width: 60px;
      height: 6px;
      background-color: var(--color-accent);
    }

    h3 { font-size: 1.6rem; margin-bottom: 1rem; }
    p { margin-bottom: 1.5rem; color: var(--color-secondary); }

    .container { width: 100%; max-width: 800px; margin: 0 auto; padding: 0 1.5rem; position: relative; z-index: 2; }
    section { padding: 5rem 0; position: relative; }

    /* Dynamic Angled Sections */
    .bg-carbon {
      background-color: var(--color-carbon);
      color: #FFFFFF;
      clip-path: polygon(0 4vw, 100% 0, 100% calc(100% - 4vw), 0 100%);
      padding: 8rem 0;
      margin: -2vw 0;
      z-index: 1;
    }
    
    .bg-carbon h2 { color: #FFFFFF; }
    .bg-carbon p { color: #A0AEC0; }

    .bg-alt-light {
      background-color: var(--color-bg-alt);
    }

    .text-center { text-align: center; }

    /* Buttons */
    .btn {
      display: inline-block;
      width: 100%;
      max-width: 320px;
      text-align: center;
      background: var(--color-accent);
      color: var(--color-carbon);
      text-decoration: none;
      padding: 1.25rem 2rem;
      border-radius: 50px;
      font-weight: 900;
      font-style: italic;
      font-size: 1.15rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
      border: 2px solid transparent;
      box-shadow: 0 10px 20px rgba(0, 229, 255, 0.3);
    }

    .btn:hover {
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 15px 25px rgba(0, 229, 255, 0.4);
      background: var(--color-carbon);
      color: var(--color-accent);
      border-color: var(--color-accent);
    }

    /* Hero */
    .hero {
      min-height: 90vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding-top: 4rem;
      clip-path: polygon(0 0, 100% 0, 100% calc(100% - 6vw), 0 100%);
      background-color: var(--color-carbon);
    }

    .hero-slideshow, .hero-slide, .hero-overlay {
      position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    }

    .hero-slideshow { z-index: 1; }
    .hero-slide {
      background-size: cover; background-position: center; opacity: 0;
      animation: heroSlideshowAnim 15s infinite; filter: brightness(0.6) contrast(1.1);
    }
    .hero-slide:nth-child(1) { background-image: url('assets/images/hero_swim_3.png'); animation-delay: 0s; }
    .hero-slide:nth-child(2) { background-image: url('assets/images/recode_hero_bg2.jpg'); animation-delay: 5s; }
    .hero-slide:nth-child(3) { background-image: url('assets/images/recode_hero_bg1.jpg'); animation-delay: 10s; }

    .hero-overlay {
      background: linear-gradient(135deg, rgba(20,20,20,0.9) 0%, rgba(20,20,20,0.4) 100%);
      z-index: 2;
    }

    @keyframes heroSlideshowAnim {
      0% { opacity: 0; transform: scale(1.02); }
      8%, 33% { opacity: 1; }
      41%, 100% { opacity: 0; transform: scale(1.06); }
    }

    .hero-logo {
      display: inline-flex; align-items: center; gap: 0.7rem;
      font-size: 1.5rem; font-weight: 900; font-style: italic; letter-spacing: 0.15em;
      margin-bottom: 3rem; color: #FFFFFF;
      position: relative;
    }
    .hero-logo::after {
      content: ''; position: absolute; bottom: -8px; left: 0; width: 40px; height: 4px; background: var(--color-accent); transform: skewX(-20deg);
    }
    .hero-logo-img { width: 28px; height: 28px; object-fit: contain; }

    .hero-catch {
      font-size: 3rem; margin-bottom: 1.5rem; line-height: 1.1; color: #FFFFFF;
    }
    .hero-catch span { color: var(--color-accent); }

    .hero-sub {
      font-size: 1.25rem; margin-bottom: 2.5rem; color: #E2E8F0; font-weight: 600;
      border-left: 4px solid var(--color-accent); padding-left: 1rem;
    }

    /* Cards */
    .grid-cards {
      display: grid; grid-template-columns: 1fr; gap: 1.5rem; margin-top: 3rem;
    }
    @media (min-width: 768px) { .grid-cards { grid-template-columns: repeat(2, 1fr); } }

    .sport-card {
      background: #FFFFFF;
      border: none;
      padding: 2.5rem;
      border-radius: 0; /* Sharp corners for sports feel */
      box-shadow: 0 10px 30px rgba(0,0,0,0.08);
      position: relative;
      transition: all 0.3s ease;
      z-index: 1;
      overflow: hidden;
    }
    .sport-card::before {
      content: ''; position: absolute; top: 0; left: 0; width: 6px; height: 100%;
      background: var(--color-accent); transform: skewX(-15deg) translateX(-10px);
      transition: all 0.3s ease;
    }
    .sport-card:hover { transform: translateY(-5px); box-shadow: 0 15px 40px rgba(0,0,0,0.12); }
    .sport-card:hover::before { transform: skewX(-15deg) translateX(0); width: 100%; opacity: 0.05; }

    .sport-card h3 { color: var(--color-carbon); font-size: 1.4rem; margin-bottom: 1rem; }
    .sport-card p { margin: 0; color: var(--color-secondary); }

    /* Features / Flow */
    .flow-list { display: flex; flex-direction: column; gap: 1rem; max-width: 600px; margin: 0 auto; }
    .flow-card {
      background: #FFFFFF; padding: 1.5rem 2rem;
      border-left: 6px solid var(--color-carbon);
      box-shadow: 0 5px 15px rgba(0,0,0,0.05);
      display: flex; flex-direction: column;
    }
    .flow-card.flow-active { border-left-color: var(--color-accent); }
    .flow-step { font-weight: 900; font-style: italic; color: var(--color-accent); letter-spacing: 0.1em; margin-bottom: 0.5rem; font-size: 0.9rem; }
    .flow-title { font-size: 1.3rem; margin-bottom: 0.5rem; }
    
    /* Pricing */
    .pricing-card {
      background: #FFFFFF;
      padding: 2.5rem;
      box-shadow: 0 10px 30px rgba(0,0,0,0.08);
      text-align: center;
      position: relative;
      border-top: 6px solid var(--color-carbon);
    }
    .pricing-card:hover { border-top-color: var(--color-accent); }
    .pricing-price { font-size: 2.5rem; font-weight: 900; font-style: italic; color: var(--color-carbon); margin: 1.5rem 0; }
    .pricing-price span { font-size: 1rem; color: var(--color-secondary); font-weight: 600; }
    
    /* Carbon Theme variants for cards inside bg-carbon */
    .bg-carbon .sport-card, .bg-carbon .pricing-card, .bg-carbon .flow-card {
      background: #1A1A1A; color: #FFFFFF;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .bg-carbon .sport-card h3, .bg-carbon .flow-title, .bg-carbon .pricing-card h3 { color: #FFFFFF; }
    .bg-carbon .pricing-price { color: var(--color-accent); }
    .bg-carbon .sport-card p, .bg-carbon .flow-desc { color: #A0AEC0; }

    /* Cinema / Image Grid (Simplified for sports look) */
    .img-grid {
      display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-top: 2rem;
    }
    .img-grid-item {
      aspect-ratio: 16/9; background-size: cover; background-position: center;
      clip-path: polygon(5% 0, 100% 0, 95% 100%, 0 100%);
      transition: all 0.4s ease;
      filter: grayscale(80%) contrast(1.2);
    }
    .img-grid-item:hover { filter: grayscale(0%) contrast(1.1); transform: scale(1.05); }

    /* Footer */
    footer {
      background: var(--color-carbon); color: #888; text-align: center; padding: 4rem 0 2rem;
      clip-path: polygon(0 4vw, 100% 0, 100% 100%, 0 100%);
      margin-top: -2vw;
    }

    @media (min-width: 768px) {
      h2 { font-size: 3rem; }
      .hero-catch { font-size: 4.5rem; }
      .btn { max-width: 280px; }
    }
  </style>"""

# Find the <style> block and replace it
html = re.sub(r'<style>.*?</style>', new_css, html, flags=re.DOTALL)

# Now, we need to adjust the HTML structure to use the new classes.
# 1. Update Highlight spans
html = html.replace('class="highlight"', 'class="highlight"') # keep as is
# if inside carbon section, we might need highlight-white, but the CSS handles gradient fine.

# 2. Update Hero Catch
html = html.replace('目標までの練習に、<br>\n        自分専用の設計図を。', '目標までの練習に、<br>\n        自分専用の<span>設計図</span>を。')

# 3. Update sections to use bg-carbon or bg-alt-light
# Section 1.6: Flow diagram (Let's make this bg-alt-light)
html = html.replace('<section style="padding: 2.5rem 0 3.5rem;">', '<section class="bg-alt-light">')

# Voices: Carbon
html = html.replace('<section class="bg-alt-2">', '<section class="bg-carbon">', 1)
# Features: bg-alt-light
html = html.replace('<section class="bg-alt-2">', '<section class="bg-alt-light">')

# Emotion cards (こんな方へ): bg-carbon
html = html.replace('<section class="bg-alt">', '<section class="bg-carbon">', 1)

# About (RECODEとは): Keep white
# Pricing: bg-carbon
html = html.replace('<section class="bg-alt">', '<section class="bg-carbon">', 1)

# Flow (ご相談からの流れ): bg-alt-light
# (already handled above if class was bg-alt-2)

# Operator Profile: bg-carbon
html = html.replace('<section class="bg-alt operator-profile-section">', '<section class="bg-carbon">')

# Mid CTA: Let's remove inline styles and use sport-card
html = html.replace('mid-cta-card', 'sport-card text-center')

# Update Grid Classes
html = html.replace('emotion-cards-grid', 'grid-cards')
html = html.replace('emotion-card', 'sport-card')

html = html.replace('features-wrapper', 'grid-cards')
html = html.replace('feature-box', 'sport-card')

html = html.replace('voices-grid', 'grid-cards')
html = html.replace('voice-card', 'sport-card')

html = html.replace('flow-card--start', 'flow-active')

# Fix inline styles that override our new CSS
html = re.sub(r'style="[^"]*background[^"]*"', '', html)
html = re.sub(r'style="[^"]*color[^"]*"', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html to Dynamic Swimming Blue Theme.")
