import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Hero Microcopy
microcopy_old = r'<div >\s*まずは現在地の整理から。<br>いきなり申し込みでなくても大丈夫です。\s*</div>'
microcopy_new = r"""<div style="font-size: 12px; color: #FFFFFF; line-height: 1.4; margin-top: 0.8rem; letter-spacing: 0.05em; opacity: 0.9;">
          まずは現在地の整理から。<br>いきなり申し込みでなくても大丈夫です。
        </div>"""
html = re.sub(microcopy_old, microcopy_new, html)

# 2. Add Post-it Voice Card CSS
voice_css = """
    .bg-wall { background: #334155; } /* Dark slate background to make post-its pop */
    .bg-wall h2 { color: #FFFFFF; }
    .bg-wall p { color: #CBD5E1; }

    .voice-card {
      background: #FFFBEB; /* soft post-it yellow */
      color: #334155;
      padding: 2.5rem 2rem;
      border-radius: 2px;
      box-shadow: 2px 8px 20px rgba(0,0,0,0.15);
      position: relative;
      margin-top: 1rem;
      transition: all 0.3s ease;
      display: flex; flex-direction: column;
    }
    .voice-card::before {
      content: '';
      position: absolute;
      top: -10px;
      left: 50%;
      transform: translateX(-50%) rotate(-2deg);
      width: 70px;
      height: 25px;
      background: rgba(255, 255, 255, 0.4);
      border: 1px solid rgba(0,0,0,0.05);
      box-shadow: 0 1px 2px rgba(0,0,0,0.05);
      backdrop-filter: blur(2px);
      z-index: 2;
    }
    .voice-card:nth-child(odd) {
      transform: rotate(-2deg);
    }
    .voice-card:nth-child(even) {
      transform: rotate(1.5deg);
    }
    .voice-card:hover {
      transform: translateY(-5px) rotate(0deg);
      box-shadow: 4px 12px 24px rgba(0,0,0,0.2);
    }
    .voice-card-title {
      font-size: 1.15rem; font-weight: 700; margin-bottom: 1rem; line-height: 1.5; color: #0F172A;
    }
    .voice-text {
      line-height: 1.8; font-size: 0.95rem; margin-bottom: 1.5rem; color: #334155; flex-grow: 1;
    }
    .voice-meta {
      font-size: 0.85rem; font-weight: 600; color: #64748B; text-align: right; margin-top: auto;
    }
"""
html = html.replace('/* Footer */', voice_css + '\n/* Footer */')

# 3. Update HTML for Voice Cards
# Replace the section class
html = re.sub(r'<!-- お客様の声 -->\s*<section class="bg-carbon">', r'<!-- お客様の声 -->\n  <section class="bg-wall">', html)

# Replace sport-card inside the voice section with voice-card
voice_section_pattern = r'(<!-- お客様の声 -->.*?)</section>'
match = re.search(voice_section_pattern, html, re.DOTALL)
if match:
    voice_content = match.group(1)
    voice_content = voice_content.replace('sport-card"', 'voice-card"')
    voice_content = voice_content.replace('sport-card-title', 'voice-card-title')
    html = html.replace(match.group(1), voice_content)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated Hero microcopy and implemented Voice post-it cards.")
