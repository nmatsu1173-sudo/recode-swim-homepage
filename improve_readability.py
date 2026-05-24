import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS Variables
content = content.replace('--line-height-base: 1.7;', '--line-height-base: 1.85;')

# body
content = content.replace('font-size: 0.95rem;\n      color: var(--color-text-main);', 'font-size: 1rem;\n      color: var(--color-text-main);')

# Headings
content = content.replace('font-size: 1.5rem;\n      margin-bottom: 3rem;', 'font-size: 1.6rem;\n      margin-bottom: 3rem;')
content = content.replace('font-size: 1.25rem;\n      margin-bottom: 1rem;', 'font-size: 1.35rem;\n      margin-bottom: 1.25rem;')

# Add highlight class to CSS
highlight_css = """    .highlight {
      font-weight: 700;
      color: #FFFFFF;
      background: linear-gradient(transparent 70%, rgba(14, 165, 233, 0.45) 70%);
      padding: 0 0.15em;
    }
"""
if '.highlight {' not in content:
    content = content.replace('/*==================================================\n      Typography & Layout\n    ==================================================*/', '/*==================================================\n      Typography & Layout\n    ==================================================*/\n' + highlight_css)

# Card descriptions
content = content.replace('font-size: 0.88rem;\n      color: #E2E8F0;', 'font-size: 0.95rem;\n      color: #E2E8F0;')
content = content.replace('font-size: 0.95rem;\n      font-weight: 700;\n      color: #FFFFFF;', 'font-size: 1.05rem;\n      font-weight: 700;\n      color: #FFFFFF;')

# Buttons
content = content.replace('font-size: 1.05rem;\n      font-weight: 600;\n      letter-spacing: 0.05em;', 'font-size: 1.15rem;\n      font-weight: 700;\n      letter-spacing: 0.05em;\n      padding: 1.1rem 1rem;')
content = content.replace('padding: 1rem 1rem;', 'padding: 1.15rem 1rem;')

# Hero
content = content.replace('font-size: 1.8rem;\n      /* Mobile font size */', 'font-size: 1.9rem;\n      /* Mobile font size */')
content = content.replace('font-size: 1.1rem;\n      margin-bottom: 1.5rem;', 'font-size: 1.15rem;\n      margin-bottom: 1.5rem;')
content = content.replace('font-size: 0.95rem;\n      color: #CBD5E1;', 'font-size: 1.05rem;\n      color: #CBD5E1;')
content = content.replace('font-size: 0.85rem;\n      color: #CBD5E1;', 'font-size: 0.95rem;\n      color: #CBD5E1;')

# Emotion cards
content = content.replace('font-size: 1.1rem;\n      color: #FFFFFF;', 'font-size: 1.15rem;\n      color: #FFFFFF;')
content = content.replace('font-size: 0.95rem;\n      color: #F8FAFC; /* 視認性向上のため明るいグレーに変更 */', 'font-size: 1rem;\n      color: #FFFFFF; /* 視認性向上のため明るく */')

# Features
content = content.replace('font-size: 0.9rem; /* 0.92rem から 0.9rem へ微調整して上品さを向上 */\n      line-height: 1.7;', 'font-size: 0.98rem;\n      line-height: 1.85;')

# FAQ Accordion CSS padding update for mobile tap
content = content.replace('padding: 1.25rem 0;', 'padding: 1.5rem 0;')
content = content.replace('padding: 0 0 1.5rem 2rem;', 'padding: 0 0 1.75rem 2.25rem;')
content = content.replace('top: 1.25rem;', 'top: 1.5rem;')

# HTML content modifications (highlighting)
# 1. 相談前に、3つの質問で現在地を整理する -> 現在地を整理する
content = content.replace('3つの質問で現在地を整理する', '3つの質問で<span class="highlight">現在地を整理</span>する')

# 2. 一人練習で優先順位に迷う方
content = content.replace('一人で練習していて、何を優先すればいいか迷っている方。', '一人で練習していて、<span class="highlight">何を優先すればいいか</span>迷っている方。')
content = content.replace('大会や記録に向けて、目標から逆算して練習したい方。', '大会や記録に向けて、<span class="highlight">目標から逆算</span>して練習したい方。')
content = content.replace('40代以降も、身体と向き合いながら泳ぎ続けたい方。', '40代以降も、<span class="highlight">身体と向き合い</span>ながら泳ぎ続けたい方。')
content = content.replace('練習量を増やすだけでなく、振り返りながら積み上げたい方。', '練習量を増やすだけでなく、<span class="highlight">振り返りながら積み上げたい</span>方。')

# 3. RECODEとは
content = content.replace('現在地・課題・練習環境を整理し、限られた時間の中で何を優先して積み上げるかを一緒に整えていきます。', '現在地・課題・練習環境を整理し、限られた時間の中で<span class="highlight">何を優先して積み上げるか</span>を一緒に整えていきます。')

# 4. お客様の声
content = content.replace('練習量を増やすことより、何を意識して積み上げるか。', '練習量を増やすことより、<span class="highlight">何を意識して積み上げるか</span>。')

# 5. Flow
content = content.replace('<h3 class="flow-title">現在地を整理</h3>', '<h3 class="flow-title"><span class="highlight">現在地を整理</span></h3>')

# Mobile specific paddings (already 3.5rem, we can make card padding larger)
content = content.replace('padding: 2.25rem 1.75rem;', 'padding: 2.5rem 2rem;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
