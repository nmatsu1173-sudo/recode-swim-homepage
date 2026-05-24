import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update .hero padding-bottom to stick closer to bottom
html = re.sub(r'(padding-bottom:\s*)6rem;', r'\g<1>3rem;', html)

# 2. Update inline style of .hero-catch
html = html.replace(
    'style="color: #FFFFFF; font-size: 2.5rem; line-height: 1.5; margin-bottom: 2rem; text-align: left;"',
    'style="color: #FFFFFF; font-size: 2.5rem; line-height: 1.3; margin-bottom: 1rem; text-align: left;"'
)

# 3. Update inline style of .hero-sub
html = html.replace(
    'style="color: #E2E8F0; font-weight: 500; line-height: 1.8; font-size: 1.15rem; border-left: none; padding-left: 0; text-align: left;"',
    'style="color: #E2E8F0; font-weight: 500; line-height: 1.5; font-size: 0.95rem; border-left: none; padding-left: 0; text-align: left;"'
)

# 4. Update margin-top of the button wrapper
html = html.replace(
    '<div style="margin-top: 2.5rem;">',
    '<div style="margin-top: 1rem;">'
)

# 5. Check if there are other media query padding-bottoms for .hero
# Line 629: .hero { min-height: 100vh; padding-bottom: 4rem; ... } inside media query
html = re.sub(r'(\.hero\s*\{[^}]*padding-bottom:\s*)4rem;', r'\g<1>2.5rem;', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated hero to be more compact and pinned to the bottom left.")
