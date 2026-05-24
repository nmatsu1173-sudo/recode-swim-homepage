import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS for emotion-icon
icon_css = """
    .emotion-icon {
      font-size: 2.5rem;
      color: var(--color-accent);
      margin-bottom: 1rem;
      display: inline-block;
    }
"""
html = html.replace('/* Footer */', icon_css + '\n/* Footer */')

# 2. Add icons to the HTML cards
# 1: 一人練習で優先順位に迷う方 -> fa-compass
html = re.sub(
    r'(<h3 class="emotion-title">一人練習で優先順位に迷う方</h3>)', 
    r'<i class="fas fa-compass emotion-icon"></i>\n          \1', 
    html
)

# 2: 目標から逆算して設計したい方 -> fa-bullseye
html = re.sub(
    r'(<h3 class="emotion-title">目標から逆算して設計したい方</h3>)', 
    r'<i class="fas fa-bullseye emotion-icon"></i>\n          \1', 
    html
)

# 3: 身体と向き合い長く泳ぎたい方 -> fa-swimmer
html = re.sub(
    r'(<h3 class="emotion-title">身体と向き合い長く泳ぎたい方</h3>)', 
    r'<i class="fas fa-swimmer emotion-icon"></i>\n          \1', 
    html
)

# 4: 振り返りながら積み上げたい方 -> fa-chart-line
html = re.sub(
    r'(<h3 class="emotion-title">振り返りながら積み上げたい方</h3>)', 
    r'<i class="fas fa-chart-line emotion-icon"></i>\n          \1', 
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added pictograms to target audience section.")
