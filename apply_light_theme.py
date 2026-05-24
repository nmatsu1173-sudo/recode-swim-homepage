import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update :root CSS variables
root_css = """    :root {
      /* Color Palette (Light Theme) */
      --color-heading: #1E293B;
      --color-text-main: #334155;
      --color-secondary: #475569;
      --color-accent: #0284C7;
      --color-primary: #FFFFFF;
      --color-bg-base: #FFFFFF;
      --color-bg-alt: #F1F5F9;
      --color-border: #E2E8F0;

      /* Typography */
      --font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Segoe UI", "Hiragino Kaku Gothic ProN", "Hiragino Sans", "Meiryo", sans-serif;
      --line-height-base: 1.85;
      --letter-spacing-base: 0.05em;
    }"""
html = re.sub(r':root\s*\{[^}]+\}', root_css, html)

# 2. Typography updates
# h2 size
html = re.sub(r'(h2\s*\{[^}]*font-size:\s*)1\.6rem;', r'\g<1>1.9rem;', html)
# h3 size
html = re.sub(r'(h3\s*\{[^}]*font-size:\s*)1\.35rem;', r'\g<1>1.5rem;', html)
# line-height base and letter spacing
html = re.sub(r'(--line-height-base:\s*)1\.9;', r'\g<1>1.85;', html)
html = re.sub(r'(--letter-spacing-base:\s*)0\.04em;', r'\g<1>0.06em;', html)

# 3. Component Color Replacements
replacements = [
    # General text colors in cards
    (r'color:\s*#FFFFFF;', r'color: var(--color-heading);'),
    (r'color:\s*#F8FAFC;', r'color: var(--color-text-main);'),
    (r'color:\s*#E2E8F0;', r'color: var(--color-secondary);'),
    (r'color:\s*#CBD5E1;', r'color: #64748B;'),
    
    # Specific Card Backgrounds
    (r'background:\s*#253346;', r'background: #FFFFFF;'),
    (r'background:\s*#1e293b;', r'background: #FFFFFF;'),
    (r'background-color:\s*#2F3E56\s*!important;', r'background-color: #F8FAFC !important;'),
    (r'background:\s*#3A4961;', r'background: #FFFFFF;'),
    (r'background:\s*rgba\(255,\s*255,\s*255,\s*0\.03\);', r'background: #FFFFFF;'),
    (r'background:\s*rgba\(255,\s*255,\s*255,\s*0\.02\);', r'background: #F8FAFC;'),
    (r'background:\s*rgba\(30,\s*41,\s*59,\s*0\.35\);', r'background: #F1F5F9;'),

    # Borders
    (r'border:\s*1px\s*solid\s*rgba\(255,\s*255,\s*255,\s*0\.05\);', r'border: 1px solid #E2E8F0;'),
    (r'border:\s*1px\s*solid\s*rgba\(255,\s*255,\s*255,\s*0\.06\);', r'border: 1px solid #E2E8F0;'),
    (r'border:\s*1px\s*solid\s*rgba\(255,\s*255,\s*255,\s*0\.08\);', r'border: 1px solid #E2E8F0;'),
    (r'border:\s*1px\s*solid\s*rgba\(255,\s*255,\s*255,\s*0\.10\);', r'border: 1px solid #E2E8F0;'),
    (r'border:\s*1px\s*solid\s*rgba\(255,\s*255,\s*255,\s*0\.1\);', r'border: 1px solid #E2E8F0;'),
    (r'border-top:\s*1px\s*solid\s*rgba\(255,\s*255,\s*255,\s*0\.05\);', r'border-top: 1px solid #E2E8F0;'),
    (r'border-top:\s*1px\s*solid\s*rgba\(255,\s*255,\s*255,\s*0\.08\);', r'border-top: 1px solid #E2E8F0;'),
    (r'border-top:\s*1px\s*solid\s*rgba\(255,\s*255,\s*255,\s*0\.1\);', r'border-top: 1px solid #E2E8F0;'),
    (r'border-top:\s*1px\s*solid\s*rgba\(255,\s*255,\s*255,\s*0\.06\);', r'border-top: 1px solid #E2E8F0;'),
    (r'border-top:\s*1px\s*solid\s*rgba\(255,\s*255,\s*255,\s*0\.15\);', r'border-top: 1px solid #E2E8F0;'),
    (r'border-bottom:\s*1px\s*solid\s*rgba\(255,\s*255,\s*255,\s*0\.05\);', r'border-bottom: 1px solid #E2E8F0;'),
    (r'border-bottom:\s*1px\s*solid\s*rgba\(255,\s*255,\s*255,\s*0\.15\);', r'border-bottom: 1px solid #E2E8F0;'),
    
    # Specific elements
    (r'\.bg-alt-2\s*\{[\s\S]*?\}', r'.bg-alt-2 {\n      background-color: var(--color-bg-base);\n    }'),
    (r'color:\s*#808F9F;', r'color: #94A3B8;'),
    (r'color:\s*#F1F5F9;', r'color: var(--color-text-main);'),
    (r'color:\s*rgba\(255,\s*255,\s*255,\s*0\.7\);', r'color: var(--color-secondary);'),
    
    # Hero section overrides (Hero should remain white text)
    (r'\.hero-catch\s*\{([^}]*?)color:\s*var\(--color-heading\);([^}]*?)\}', r'.hero-catch {\1color: #FFFFFF;\2}'),
    (r'\.hero-sub\s*\{([^}]*?)color:\s*var\(--color-secondary\);([^}]*?)\}', r'.hero-sub {\1color: #E2E8F0;\2}'),
    (r'\.hero-desc\s*\{([^}]*?)color:\s*#64748B;([^}]*?)\}', r'.hero-desc {\1color: #CBD5E1;\2}'),
    (r'\.hero-sub-highlight\s*\{([^}]*?)color:\s*var\(--color-heading\);([^}]*?)\}', r'.hero-sub-highlight {\1color: #FFFFFF;\2}'),
    (r'\.hero-sub-cta\s*\{([^}]*?)color:\s*#64748B;([^}]*?)\}', r'.hero-sub-cta {\1color: #CBD5E1;\2}'),
    (r'class="hero-catch"\s*>\s*目標までの', r'class="hero-catch" style="color: #FFFFFF;">\n        目標までの'),
    
    # Pricing Details
    (r'color:\s*#B0BFD0;', r'color: var(--color-secondary);'),
    (r'color:\s*#8BA8C5;', r'color: var(--color-accent);'),
    
    # Shadows
    (r'box-shadow:\s*0\s*4px\s*12px\s*rgba\(15,\s*23,\s*42,\s*0\.15\);', r'box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);'),
    (r'box-shadow:\s*0\s*10px\s*20px\s*rgba\(15,\s*23,\s*42,\s*0\.2\);', r'box-shadow: 0 10px 20px rgba(0, 0, 0, 0.08);'),
    (r'box-shadow:\s*0\s*4px\s*20px\s*rgba\(0,\s*0,\s*0,\s*0\.15\);', r'box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);'),
    (r'box-shadow:\s*0\s*10px\s*30px\s*rgba\(15,\s*23,\s*42,\s*0\.2\);', r'box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);'),

    # Hover Backgrounds for light mode cards
    (r'background:\s*rgba\(37,\s*51,\s*70,\s*0\.9\);', r'background: #F8FAFC;'),
    (r'background:\s*rgba\(37,\s*51,\s*70,\s*0\.4\);', r'background: #F8FAFC;'),
]

for old, new in replacements:
    html = re.sub(old, new, html)

# Explicitly ensure .bg-alt-2 is set to var(--color-bg-alt) or base
if '.bg-alt-2 {' not in html:
    html = html.replace('.bg-alt {', '.bg-alt {\n      background-color: var(--color-bg-alt);\n    }\n    .bg-alt-2 {')

# Fix highlight style for light theme
html = re.sub(
    r'\.highlight\s*\{\s*font-weight:\s*700;\s*color:\s*var\(--color-text-main\);\s*background:\s*linear-gradient\(transparent\s*62%,\s*rgba\(56,\s*189,\s*248,\s*0\.4\)\s*62%\);\s*padding:\s*0\s*0\.08em;\s*\}',
    r'.highlight {\n      font-weight: 700;\n      color: var(--color-heading);\n      background: linear-gradient(transparent 62%, rgba(2, 132, 199, 0.2) 62%);\n      padding: 0 0.08em;\n    }',
    html
)
html = re.sub(
    r'\.highlight\s*\{\s*font-weight:\s*700;\s*color:\s*#F8FAFC;\s*background:\s*linear-gradient\(transparent\s*62%,\s*rgba\(56,\s*189,\s*248,\s*0\.4\)\s*62%\);\s*padding:\s*0\s*0\.08em;\s*\}',
    r'.highlight {\n      font-weight: 700;\n      color: var(--color-heading);\n      background: linear-gradient(transparent 62%, rgba(2, 132, 199, 0.2) 62%);\n      padding: 0 0.08em;\n    }',
    html
)

# Replace inline <span style="color: #FFFFFF; font-weight: 600;">
html = html.replace('color: #FFFFFF; font-weight: 600;', 'color: var(--color-heading); font-weight: 600;')
html = html.replace('color: var(--color-heading); font-weight: 600;', 'color: var(--color-heading); font-weight: 700;')

# Cinema slide adjustments
# Text in cinema slide should probably remain white because images are dark
html = html.replace('.cinema-step-title {\n      font-size: 1.75rem;\n      font-weight: 700;\n      color: var(--color-heading);', '.cinema-step-title {\n      font-size: 1.75rem;\n      font-weight: 700;\n      color: #FFFFFF;')
html = html.replace('.cinema-step-desc {\n      font-size: 1rem;\n      line-height: 1.6;\n      color: var(--color-secondary);', '.cinema-step-desc {\n      font-size: 1rem;\n      line-height: 1.6;\n      color: #F8FAFC;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html to Light Theme.")
