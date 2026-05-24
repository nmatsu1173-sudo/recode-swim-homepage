import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Hero CSS (justify-content and padding)
html = re.sub(r'(\.hero\s*\{[^}]*?justify-content:\s*)center;', r'\1flex-end;\n      align-items: flex-start;\n      padding-bottom: 6rem;', html)

# 2. Update LINE Button CSS (border-radius and white-space)
html = re.sub(r'(\.line-cta-btn\s*\{[^}]*?gap:\s*0\.5rem;)', r'\1\n      border-radius: 50px !important;\n      white-space: nowrap !important;\n      width: max-content !important;\n      padding: 1rem 2rem !important;', html)

# 3. Update Hero Text Content
old_hero_text = r'<h1 class="hero-catch"[^>]*>\s*あなただけのパフォーマンス設計をサポート\s*</h1>'
new_hero_text = """<h1 class="hero-catch" style="color: #FFFFFF; font-size: 2.5rem; line-height: 1.5; margin-bottom: 2rem; text-align: left;">
        あなただけの<br>
        パフォーマンス設計を<br>
        アドバイザーと作る。
      </h1>"""
html = re.sub(old_hero_text, new_hero_text, html, flags=re.DOTALL)

# Make sure the container text alignment inside hero is left
html = re.sub(r'(<section class="hero"[^>]*>\s*<div class="container")', r'\1 style="text-align: left;"', html)

# Also align the sub text to left explicitly if it had text-center
html = re.sub(r'(<p class="hero-sub".*?)style="([^"]*)"', r'\1style="\2 text-align: left;"', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated Hero text, layout, and LINE buttons.")
