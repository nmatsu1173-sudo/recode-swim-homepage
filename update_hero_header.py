import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# --- 1. CSS UPDATES ---
css_additions = """
    /* Header & Menu */
    .header {
      position: fixed; top: 0; left: 0; width: 100%; height: 70px;
      display: flex; justify-content: center; align-items: center;
      background: rgba(15, 23, 42, 0.9);
      backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
      z-index: 1000;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding: 0 1.5rem;
    }
    .header-logo {
      display: inline-flex; align-items: center; gap: 0.5rem;
      font-size: 1.25rem; font-weight: 700; letter-spacing: 0.1em;
      color: #FFFFFF; text-decoration: none;
    }
    .header-logo-img { width: 24px; height: 24px; object-fit: contain; }
    
    .hamburger {
      position: absolute; right: 1.5rem; top: 50%; transform: translateY(-50%);
      background: none; border: none; cursor: pointer;
      width: 28px; height: 20px; display: flex; flex-direction: column; justify-content: space-between;
      z-index: 1001;
    }
    .hamburger span {
      display: block; width: 100%; height: 2px; background: #FFFFFF;
      transition: all 0.3s ease; border-radius: 2px;
    }
    .hamburger.open span:nth-child(1) { transform: translateY(9px) rotate(45deg); }
    .hamburger.open span:nth-child(2) { opacity: 0; }
    .hamburger.open span:nth-child(3) { transform: translateY(-9px) rotate(-45deg); }

    .fullscreen-menu {
      position: fixed; top: 0; left: 0; width: 100%; height: 100vh;
      background: rgba(15, 23, 42, 0.98);
      display: flex; flex-direction: column; justify-content: center; align-items: center;
      z-index: 999;
      opacity: 0; visibility: hidden; transition: all 0.4s ease;
    }
    .fullscreen-menu.open { opacity: 1; visibility: visible; }
    .menu-list { list-style: none; text-align: center; }
    .menu-item { margin-bottom: 2.5rem; }
    .menu-link {
      font-size: 1.3rem; font-weight: 600; color: #FFFFFF; text-decoration: none;
      letter-spacing: 0.05em; transition: color 0.3s ease;
    }
    .menu-link:hover { color: var(--color-accent); }

    @media (min-width: 768px) {
      .header { justify-content: flex-start; }
      .header-logo { margin-left: 1rem; }
    }
"""
html = html.replace('/* Hero */', css_additions + '\n    /* Hero */')

# Update Hero CSS to gradient and remove slideshow CSS
html = re.sub(r'\.hero\s*\{[^}]*?background-color:[^}]*?\}', 
              '.hero {\n      min-height: 80vh;\n      display: flex;\n      flex-direction: column;\n      justify-content: center;\n      padding-top: 70px;\n      background: linear-gradient(135deg, #0F172A 0%, #0284C7 100%);\n      clip-path: none;\n    }', 
              html)
html = re.sub(r'\.hero-slideshow, \.hero-slide, \.hero-overlay.*?@keyframes heroSlideshowAnim.*?\n    }', '', html, flags=re.DOTALL)

# Hero catch color is now explicitly white because background is dark blue
html = re.sub(r'(\.hero-catch\s*\{[^}]*?)color:\s*var\(--color-heading\);([^}]*?\})', r'\1color: #FFFFFF;\2', html)
html = re.sub(r'(\.hero-sub\s*\{[^}]*?)color:\s*var\(--color-text-main\);([^}]*?\})', r'\1color: #E2E8F0;\2', html)
html = re.sub(r'(\.hero-desc\s*\{[^}]*?\}|\.hero-desc.*?color:.*?\}|\.hero-sub-highlight.*?color:.*?\})', '', html, flags=re.DOTALL)

# --- 2. HTML UPDATES ---
header_html = """
  <!-- Header -->
  <header class="header">
    <a href="#" class="header-logo">
      <img src="assets/images/recode_logo_mark_white_transparent.png" alt="RECODE" class="header-logo-img">
      <span>RECODE</span>
    </a>
    <button class="hamburger" id="hamburger-btn">
      <span></span><span></span><span></span>
    </button>
  </header>

  <!-- Fullscreen Menu -->
  <nav class="fullscreen-menu" id="fs-menu">
    <ul class="menu-list">
      <li class="menu-item"><a href="#about" class="menu-link">RECODEとは</a></li>
      <li class="menu-item"><a href="#features" class="menu-link">サービスの特徴</a></li>
      <li class="menu-item"><a href="#pricing" class="menu-link">料金プラン</a></li>
      <li class="menu-item"><a href="#flow" class="menu-link">ご相談からの流れ</a></li>
      <li class="menu-item"><a href="#faq" class="menu-link">よくあるご質問</a></li>
    </ul>
  </nav>
"""
html = html.replace('<body>', '<body>\n' + header_html)

# Remove old hero slideshow and overlay
html = re.sub(r'<div class="hero-slideshow">.*?</div>\n\s*<div class="hero-overlay"></div>', '', html, flags=re.DOTALL)

# Remove old hero logo div
html = re.sub(r'<div class="hero-logo">.*?</div>', '', html, flags=re.DOTALL)

# Update Hero Catch and Sub
old_hero_content_pattern = r'<h1 class="hero-catch".*?</h1>\s*<p class="hero-sub".*?</p>.*?<p class="hero-desc".*?</p>'
new_hero_content = """<h1 class="hero-catch" style="color: #FFFFFF; font-size: 2.5rem; line-height: 1.4; margin-bottom: 2rem;">
        あなただけのパフォーマンス設計をサポート
      </h1>

      <p class="hero-sub" style="color: #E2E8F0; font-weight: 500; line-height: 1.8; font-size: 1.15rem; border-left: none; padding-left: 0;">
        現在地から目標までの練習設計図をアドバイザーと共につくるサービス。<br>
        限られた時間の中で、今やるべき積み上げ方を整えます。
      </p>"""
html = re.sub(old_hero_content_pattern, new_hero_content, html, flags=re.DOTALL)
# It's possible the old HTML was missing hero-desc because my previous script removed it. Let's do a fallback replace if needed.
if 'あなただけのパフォーマンス設計' not in html:
    # Let's target by finding <h1 class="hero-catch">
    html = re.sub(r'<h1 class="hero-catch".*?</p>', new_hero_content, html, flags=re.DOTALL)

# Add IDs to sections
html = html.replace('<section class="about-section">', '<section class="about-section" id="about">')
html = re.sub(r'(<section[^>]*>)\s*<div class="container">\s*<h2>サービスの特徴</h2>', r'<section class="bg-alt" id="features">\n    <div class="container">\n      <h2>サービスの特徴</h2>', html)
html = re.sub(r'(<section[^>]*>)\s*<div class="container">\s*<h2>サポート内容と料金の目安</h2>', r'<section class="bg-alt" id="pricing">\n    <div class="container">\n      <h2>サポート内容と料金の目安</h2>', html)
html = re.sub(r'(<section[^>]*>)\s*<div class="container">\s*<h2>ご相談からの流れ</h2>', r'<section class="bg-alt" id="flow">\n    <div class="container">\n      <h2>ご相談からの流れ</h2>', html)
html = re.sub(r'(<section>)\s*<div class="container">\s*<h2>よくあるご質問</h2>', r'<section id="faq">\n    <div class="container">\n      <h2>よくあるご質問</h2>', html)

# Add Menu JS
js_additions = """
  <!-- Hamburger Menu Script -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const hamburgerBtn = document.getElementById('hamburger-btn');
      const fsMenu = document.getElementById('fs-menu');
      const menuLinks = document.querySelectorAll('.menu-link');

      function toggleMenu() {
        hamburgerBtn.classList.toggle('open');
        fsMenu.classList.toggle('open');
      }

      hamburgerBtn.addEventListener('click', toggleMenu);

      menuLinks.forEach(link => {
        link.addEventListener('click', function() {
          hamburgerBtn.classList.remove('open');
          fsMenu.classList.remove('open');
        });
      });
    });
  </script>
"""
html = html.replace('</body>', js_additions + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html with Header, Menu, and Gradient Hero.")
