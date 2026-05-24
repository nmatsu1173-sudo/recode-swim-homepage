import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Voice card padding for mobile
content = content.replace('      padding: 2.5rem 2rem;\n      border-radius: 8px;', '      padding: 1.75rem 1.5rem;\n      border-radius: 8px;')

# Mid CTA card padding for mobile
content = content.replace('      padding: 2.25rem 1.5rem;\n      text-align: center;', '      padding: 1.75rem 1.25rem;\n      text-align: center;')

# Pricing card padding for mobile
content = content.replace('padding: 1.25rem 1rem; /* スマホ向けに余白を小さくし重さを軽減 */', 'padding: 1.25rem 1.15rem;')

# Emotion card padding
content = content.replace('padding: 1.75rem 1.5rem;', 'padding: 1.5rem 1.25rem;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
