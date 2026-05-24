import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add FontAwesome to head if not present
if 'font-awesome' not in html:
    html = html.replace('</head>', '  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n</head>')

# 2. Add CSS for .line-cta-btn
line_css = """
    .line-cta-btn {
      background: #06C755 !important; /* LINE Green */
      color: #FFFFFF !important;
      box-shadow: 0 4px 12px rgba(6, 199, 85, 0.3) !important;
      display: inline-flex !important;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
    }
    .line-cta-btn:hover {
      background: #05B34C !important;
      box-shadow: 0 6px 16px rgba(6, 199, 85, 0.4) !important;
      transform: translateY(-2px);
    }
    .line-cta-btn i {
      font-size: 1.4rem;
    }
"""

# inject CSS
html = html.replace('</style>', line_css + '\n  </style>')

# 3. Add the icon to the text
html = re.sub(r'>LINEで現在地を相談する</a>', '><i class="fab fa-line"></i> LINEで現在地を相談する</a>', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated LINE buttons.")
