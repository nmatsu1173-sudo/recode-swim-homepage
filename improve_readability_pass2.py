import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Body & Base line height
content = content.replace('--line-height-base: 1.85;', '--line-height-base: 1.9;')
content = content.replace('font-size: 1rem;\n      color: var(--color-text-main);', 'font-size: 1.05rem;\n      color: var(--color-text-main);\n      line-break: strict; /* 日本語の不自然な改行を防ぐ */')

# 2. Add text-wrap: balance to Headings
content = content.replace('      line-height: 1.4;\n      font-weight: 600;', '      line-height: 1.4;\n      font-weight: 600;\n      text-wrap: balance;')

# 3. Update Highlight CSS
old_highlight = """    .highlight {
      font-weight: 700;
      color: #FFFFFF;
      background: linear-gradient(transparent 70%, rgba(14, 165, 233, 0.45) 70%);
      padding: 0 0.15em;
    }"""
new_highlight = """    .highlight {
      font-weight: 700;
      color: #F8FAFC;
      background: linear-gradient(transparent 62%, rgba(56, 189, 248, 0.4) 62%);
      padding: 0 0.08em;
    }
    .nowrap {
      display: inline-block;
      white-space: nowrap;
    }"""
content = content.replace(old_highlight, new_highlight)

# 4. Small font bumps
content = content.replace('font-size: 0.85rem;', 'font-size: 0.95rem;')
content = content.replace('font-size: 0.8rem;', 'font-size: 0.95rem;')
content = content.replace('font-size: 0.9rem;', 'font-size: 1rem;')
content = content.replace('font-size: 0.93rem;', 'font-size: 1rem;')
content = content.replace('font-size: 0.95rem;', 'font-size: 1.02rem;')
content = content.replace('font-size: 0.88rem;', 'font-size: 1rem;')

# Buttons note
content = content.replace('font-size: 0.75rem;', 'font-size: 0.95rem;')

# Add .nowrap to highlights in HTML
content = content.replace('class="highlight"', 'class="highlight nowrap"')

# Ensure no horizontal overflow caused by nowrap on mobile by allowing some flexibility
# Well, inline-block nowrap is safe if it's just short phrases. 

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
