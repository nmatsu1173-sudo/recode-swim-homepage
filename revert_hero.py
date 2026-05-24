import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_css = """    .hero-slide:nth-child(1) {
      background-image: url('assets/images/recode_hero_bg_origin.jpg');
      background-position: center center;
      animation-delay: 0s;
    }

    .hero-slide:nth-child(2) {
      background-image: url('assets/images/recode_hero_bg_origin.jpg');
      background-position: center center;
      animation-delay: 5s;
    }

    .hero-slide:nth-child(3) {
      background-image: url('assets/images/recode_hero_bg_origin.jpg');
      background-position: center center;
      animation-delay: 10s;
    }"""

new_css = """    .hero-slide:nth-child(1) {
      background-image: url('assets/images/recode_hero_bg1.jpg');
      animation-delay: 0s;
    }

    .hero-slide:nth-child(2) {
      background-image: url('assets/images/recode_hero_bg2.jpg');
      background-position: center top;
      animation-delay: 5s;
    }

    .hero-slide:nth-child(3) {
      background-image: url('assets/images/recode_hero_bg3.jpg');
      background-position: center top;
      animation-delay: 10s;
    }"""

content = content.replace(old_css, new_css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
