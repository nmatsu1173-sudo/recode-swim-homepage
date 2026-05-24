import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace text
old_text = "一人で練習するマスターズスイマーのための<br>"
new_text = "目標に向けて積み上げたいスイマーのための<br>"
content = content.replace(old_text, new_text)

# Replace image and background position
old_css = """    .hero-slide:nth-child(3) {
      background-image: url('assets/images/recode_hero_bg3.jpg');
      background-position: center top;
      animation-delay: 10s;
    }"""
new_css = """    .hero-slide:nth-child(3) {
      background-image: url('assets/images/recode_hero_bg3_tri_real.png');
      background-position: center center;
      animation-delay: 10s;
    }"""
content = content.replace(old_css, new_css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
