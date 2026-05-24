import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# .cta-note adjustment
content = content.replace('font-size: 0.75rem;\n      color: #94A3B8;\n      margin-top: 1rem;', 'font-size: 0.9rem;\n      color: #CBD5E1;\n      margin-top: 1.25rem;')

# Flow notes text adjustments (if explicit sizes exist, or I can just append CSS for them)
flow_notes_css = """    .flow-note-main {
      font-size: 1rem;
      font-weight: 700;
      color: #FFFFFF;
    }
    .flow-note-sub {
      font-size: 0.95rem;
      color: #CBD5E1;
    }
    /* 1.5 運営者メッセージの調整などももしあれば */
"""
content = content.replace('    /* 1.5 運営者メッセージ */', flow_notes_css + '    /* 1.5 運営者メッセージ */')

if '.flow-note-main' not in content:
    # insert before '/* 7. 運営者プロフィール */' or just append inside Flow Section CSS
    content = content.replace('    /* 「ご相談からの流れ」安心文 */', '    /* 「ご相談からの流れ」安心文 */\n' + flow_notes_css)

# Update some flow card title sizes for better readability
content = content.replace('font-size: 1.05rem; /* 少し落として上品に */', 'font-size: 1.15rem;')
content = content.replace('font-size: 0.93rem;\n      color: #E2E8F0;', 'font-size: 1rem;\n      color: #E2E8F0;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
