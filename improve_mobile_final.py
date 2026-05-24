import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Cinema Nav HTML
old_nav = """        <div class="cinema-nav">
          <button class="cinema-nav-btn active" data-index="0">01 目標</button>
          <span class="cinema-nav-divider">｜</span>
          <button class="cinema-nav-btn" data-index="1">02 現在地</button>
          <span class="cinema-nav-divider">｜</span>
          <button class="cinema-nav-btn" data-index="2">03 設計図</button>
          <span class="cinema-nav-divider">｜</span>
          <button class="cinema-nav-btn" data-index="3">04 実施</button>
          <span class="cinema-nav-divider">｜</span>
          <button class="cinema-nav-btn" data-index="4">05 調整</button>
        </div>"""
new_nav = """        <div class="cinema-nav">
          <button class="cinema-nav-btn active" data-index="0"><span class="nav-num">01</span><span class="nav-text">目標</span></button>
          <span class="cinema-nav-divider"></span>
          <button class="cinema-nav-btn" data-index="1"><span class="nav-num">02</span><span class="nav-text">現在地</span></button>
          <span class="cinema-nav-divider"></span>
          <button class="cinema-nav-btn" data-index="2"><span class="nav-num">03</span><span class="nav-text">設計図</span></button>
          <span class="cinema-nav-divider"></span>
          <button class="cinema-nav-btn" data-index="3"><span class="nav-num">04</span><span class="nav-text">実施</span></button>
          <span class="cinema-nav-divider"></span>
          <button class="cinema-nav-btn" data-index="4"><span class="nav-num">05</span><span class="nav-text">調整</span></button>
        </div>"""
content = content.replace(old_nav, new_nav)

# 2. Update Cinema Nav CSS
# Find the CSS block for cinema-nav
old_cinema_nav_css = """    .cinema-nav {
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: 1.75rem;
      gap: 0.15rem;
    }

    .cinema-nav-btn {
      background: none;
      border: none;
      color: #64748B; /* 控えめなグレー */
      font-size: 1.02rem;
      font-weight: 600;
      cursor: pointer;
      padding: 0.75rem 0.85rem; /* タップしやすいサイズ */
      transition: color 0.3s ease, text-shadow 0.3s ease;
      letter-spacing: 0.05em;
      border-radius: 4px;
    }"""
new_cinema_nav_css = """    .cinema-nav {
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: 1.75rem;
      gap: 0.2rem;
    }

    .cinema-nav-btn {
      background: none;
      border: none;
      color: #64748B;
      cursor: pointer;
      padding: 0.5rem;
      transition: color 0.3s ease, text-shadow 0.3s ease;
      border-radius: 4px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.2rem;
    }
    
    .nav-num {
      font-size: 0.85rem;
      font-family: 'Inter', sans-serif;
      letter-spacing: 0.1em;
      opacity: 0.8;
    }
    
    .nav-text {
      font-size: 0.95rem;
      font-weight: 600;
      letter-spacing: 0.05em;
    }"""
content = content.replace(old_cinema_nav_css, new_cinema_nav_css)

# Update mobile media query for cinema-nav
old_cinema_nav_mobile = """      .cinema-nav {
        gap: 0;
      }

      .cinema-nav-btn {
        font-size: 1.02rem;
        padding: 0.75rem 0.5rem; /* スマホでも押しやすいサイズ（タップターゲット44px以上を維持） */
      }

      .cinema-nav-divider {
        font-size: 0.95rem;
      }"""
new_cinema_nav_mobile = """      .cinema-nav {
        gap: 0;
        justify-content: space-between;
        width: 100%;
        padding: 0 0.5rem;
      }

      .cinema-nav-btn {
        padding: 0.5rem 0.25rem;
      }
      
      .nav-num { font-size: 0.8rem; }
      .nav-text { font-size: 0.9rem; }

      .cinema-nav-divider {
        display: none;
      }"""
content = content.replace(old_cinema_nav_mobile, new_cinema_nav_mobile)

# 3. Add .ib class to CSS
ib_css = """
    .ib {
      display: inline-block;
    }
"""
content = content.replace('.nowrap {', ib_css + '    .nowrap {')

# 4. Fix specific text line breaks using .ib and .nowrap

# "何を優先して積み上げるかを一緒に整えていきます。"
old_recode_desc = "を一緒に整えていきます。"
new_recode_desc = "<span class=\"nowrap\">を一緒に整えていきます。</span>"
content = content.replace(old_recode_desc, new_recode_desc)

# Pricing section text
old_pricing_1 = "どのプランが合うか分からない方は、まずLINEでご相談ください。<br>\n          目標・現在地・練習環境を確認したうえで、無理のない進め方をご提案します。"
new_pricing_1 = "<span class=\"ib\">どのプランが合うか分からない方は、</span><span class=\"ib\">まずLINEでご相談ください。</span><br>\n          <span class=\"ib\">目標・現在地・練習環境を確認したうえで、</span><span class=\"ib\">無理のない進め方を</span><span class=\"ib\">ご提案します。</span>"
content = content.replace(old_pricing_1, new_pricing_1)

# Flow section intro
old_flow_intro_1 = "はじめから申し込みを前提にする必要はありません。<br>\n        まずは、今の目標と練習の迷いを整理するところから始めます。"
new_flow_intro_1 = "<span class=\"ib\">はじめから申し込みを</span><span class=\"ib\">前提にする必要はありません。</span><br>\n        <span class=\"ib\">まずは今の目標と練習の迷いを</span><span class=\"ib\">整理するところから始めます。</span>"
content = content.replace(old_flow_intro_1, new_flow_intro_1)

old_flow_intro_2 = "相談 → 整理 → 提案 → 積み上げ。<br>\n        この流れで進みます。"
new_flow_intro_2 = "<span class=\"ib\">相談 → 整理 → 提案 → 積み上げ。</span><br>\n        <span class=\"ib\">この流れで進みます。</span>"
content = content.replace(old_flow_intro_2, new_flow_intro_2)

# Final CTA
old_final_cta = "今の現在地と、次に整えるべきことを一緒に整理します。"
new_final_cta = "<span class=\"ib\">今の現在地と、次に整えるべきことを</span><span class=\"ib\">一緒に整理します。</span>"
content = content.replace(old_final_cta, new_final_cta)

# 5. Improve CTA button styling to make it "more clickable" but not e-commerce
old_btn_css = """      background: linear-gradient(135deg, rgba(14, 165, 233, 0.15) 0%, rgba(14, 165, 233, 0.05) 100%);
      border: 1px solid rgba(14, 165, 233, 0.4);
      color: var(--color-heading);
      text-decoration: none;
      padding: 1.15rem 1rem;
      border-radius: 6px;
      font-weight: 600;
      font-size: 1.05rem;
      transition: transform 0.2s, background 0.2s, border-color 0.2s, box-shadow 0.2s;
      letter-spacing: 0.05em;
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.3);"""
new_btn_css = """      background: linear-gradient(135deg, rgba(14, 165, 233, 0.25) 0%, rgba(14, 165, 233, 0.1) 100%);
      border: 1px solid rgba(14, 165, 233, 0.6);
      color: #FFFFFF;
      text-decoration: none;
      padding: 1.25rem 1rem;
      border-radius: 8px;
      font-weight: 700;
      font-size: 1.05rem;
      transition: all 0.25s ease;
      letter-spacing: 0.05em;
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      box-shadow: 0 4px 16px rgba(14, 165, 233, 0.15);"""
content = content.replace(old_btn_css, new_btn_css)

old_btn_hover = """      background: rgba(14, 165, 233, 0.25);
      border-color: rgba(14, 165, 233, 0.6);
      box-shadow: 0 6px 16px rgba(14, 165, 233, 0.15);"""
new_btn_hover = """      background: rgba(14, 165, 233, 0.35);
      border-color: rgba(14, 165, 233, 0.8);
      box-shadow: 0 6px 20px rgba(14, 165, 233, 0.25);
      transform: translateY(-2px);"""
content = content.replace(old_btn_hover, new_btn_hover)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
