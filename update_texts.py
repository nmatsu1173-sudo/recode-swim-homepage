import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero Subtext
old_hero_sub = """        <div style="margin-top: 1.25rem; font-size: 0.95rem; color: #CBD5E1; line-height: 1.6;">
          相談前に、3つの質問で<span class="highlight nowrap">現在地を整理</span>できます。<br>
          <span class="highlight nowrap">まずは整理だけでも大丈夫です。</span>
        </div>"""
new_hero_sub = """        <div style="margin-top: 1.25rem; font-size: 0.95rem; color: #CBD5E1; line-height: 1.6;">
          まずは現在地の整理から。<br>いきなり申し込みでなくても大丈夫です。
        </div>"""
content = content.replace(old_hero_sub, new_hero_sub)

# 2. Voices note
old_voice_note = "掲載内容は、個人が特定されない形に一部編集しています。"
new_voice_note = "掲載内容は、個人が特定されないよう一部編集しています。"
content = content.replace(old_voice_note, new_voice_note)

# 3. Emotion Icons removal
# We want to remove <div class="emotion-icon-wrap"> ... </div> blocks.
# Let's use regex.
content = re.sub(r'<div class="emotion-icon-wrap">.*?</div>', '', content, flags=re.DOTALL)

# 4. RECODEとは
old_about = """          RECODEは、<span class="highlight nowrap">フォーム添削ではなく、練習設計を</span>提供するサポートです。<br><br>
          目標・現在地・練習環境を整理し、限られた時間の中で<span class="highlight nowrap">何を優先して積み上げるか</span><span class="nowrap">を一緒に整えていきます。</span>"""
new_about = """          <span class="ib">RECODEは、</span><span class="highlight nowrap">フォーム添削ではなく、</span><br><span class="ib">目標に向けた練習設計を</span><span class="ib">整えるサポートです。</span><br><br>
          <span class="ib">目標・現在地・練習環境を整理し、</span><br><span class="ib">限られた時間の中で</span><span class="highlight nowrap">何を優先して積み上げるか</span>を<br><span class="ib">一緒に明確にしていきます。</span>"""
content = content.replace(old_about, new_about)

# 5. Pricing Intro
old_pricing_intro = """        RECODEは、目標・現在地・練習環境に合わせて進め方を整理する、相談型の練習設計サポートです。<br>
        まずはLINEで現在地を整理したうえで、必要に応じて合うプランをご案内します。"""
new_pricing_intro = """        <span class="ib">RECODEは、目標・現在地・練習環境に合わせて、</span><br class="sp-only">
        <span class="ib">進め方を整理する</span><span class="ib">相談型の練習設計サポートです。</span><br><br>
        <span class="ib">まずはLINEで現在地を整理したうえで、</span><br class="sp-only">
        <span class="ib">必要に応じて合うプランを</span><span class="ib">ご案内します。</span>"""
content = content.replace(old_pricing_intro, new_pricing_intro)

# 6. Pricing 3-month
old_pricing_3m = """<div class="pricing-price">28,000円/月 × 3ヶ月 <span style="font-size: 1rem; font-weight: normal; color: var(--color-secondary);">(または 一括 84,000円)</span></div>"""
new_pricing_3m = """<div class="pricing-price">28,000円/月 × 3ヶ月<br class="sp-only"><span style="font-size: 1rem; font-weight: normal; color: var(--color-secondary);">(または 一括 84,000円)</span></div>"""
content = content.replace(old_pricing_3m, new_pricing_3m)

# 7. Payment Note
old_payment = """          お支払い方法は、ご相談後にご案内します。<br>
          銀行振込のほか、クレジットカード決済など、できるだけ手間の少ない方法で進められるよう準備しています。"""
new_payment = """          <span class="ib">お支払い方法は、ご相談後にご案内します。</span><br>
          <span class="ib">銀行振込を基本に、</span><span class="ib">今後はクレジットカード決済にも</span><span class="ib">対応できるよう準備しています。</span>"""
content = content.replace(old_payment, new_payment)

# 8. & 9. Flow section Intro and List
old_flow_section = """      <p class="text-center" style="margin-bottom: 1.5rem;">
        <span class="ib">はじめから申し込みを</span><span class="ib">前提にする必要はありません。</span><br>
        <span class="ib">まずは今の目標と練習の迷いを</span><span class="ib">整理するところから始めます。</span>
      </p>
      <p class="text-center" style="font-size: 1.02rem; margin-bottom: 2.5rem; color: var(--color-secondary);">
        <span class="ib">相談 → 整理 → 提案 → 積み上げ。</span><br>
        <span class="ib">この流れで進みます。</span>
      </p>
      <div class="flow-list">
        <div class="flow-card flow-card--start">
          <span class="flow-step">STEP 1</span>
          <h3 class="flow-title">LINEで相談</h3>
          <p class="flow-desc">目標や大会、今の練習状況を送る</p>
        </div>
        <div class="flow-arrow"></div>
        <div class="flow-card">
          <span class="flow-step">STEP 2</span>
          <h3 class="flow-title"><span class="highlight nowrap">現在地を整理</span></h3>
          <p class="flow-desc">練習環境、回数、課題を一緒に確認する</p>
        </div>
        <div class="flow-arrow"></div>
        <div class="flow-card">
          <span class="flow-step">STEP 3</span>
          <h3 class="flow-title">進め方を提案</h3>
          <p class="flow-desc">必要に応じて、合うサポート内容を案内する</p>
        </div>
        <div class="flow-arrow"></div>
        <div class="flow-card">
          <span class="flow-step">STEP 4</span>
          <h3 class="flow-title">練習設計を開始</h3>
          <p class="flow-desc">メニューとログで、練習を積み上げる</p>
        </div>
      </div>"""
new_flow_section = """      <p class="text-center" style="margin-bottom: 1.5rem;">
        <span class="ib">はじめから申し込みを</span><span class="ib">前提にする必要はありません。</span><br>
        <span class="ib">まずは今の目標と練習の迷いを整理し、</span><span class="ib">必要な場合のみ合う進め方を</span><span class="ib">ご案内します。</span><br><br>
        <span class="ib">内容に納得いただいたうえで、</span><span class="ib">正式な申込後に</span><span class="ib">練習設計を開始します。</span>
      </p>
      <div class="flow-list">
        <div class="flow-card flow-card--start">
          <span class="flow-step">STEP 1</span>
          <h3 class="flow-title">LINEで相談</h3>
          <p class="flow-desc">目標や大会、今の練習状況を送る</p>
        </div>
        <div class="flow-arrow"></div>
        <div class="flow-card">
          <span class="flow-step">STEP 2</span>
          <h3 class="flow-title"><span class="highlight nowrap">現在地を整理</span></h3>
          <p class="flow-desc">練習環境、回数、課題を一緒に確認する</p>
        </div>
        <div class="flow-arrow"></div>
        <div class="flow-card">
          <span class="flow-step">STEP 3</span>
          <h3 class="flow-title">進め方を提案</h3>
          <p class="flow-desc">必要に応じて、合うサポート内容をご案内する</p>
        </div>
        <div class="flow-arrow"></div>
        <div class="flow-card">
          <span class="flow-step">STEP 4</span>
          <h3 class="flow-title">申込・お支払い</h3>
          <p class="flow-desc">内容に納得いただいたうえで、正式にお申し込み</p>
        </div>
        <div class="flow-arrow"></div>
        <div class="flow-card">
          <span class="flow-step">STEP 5</span>
          <h3 class="flow-title">練習設計を開始</h3>
          <p class="flow-desc">メニューとログをもとに、練習を積み上げる</p>
        </div>
      </div>"""
content = content.replace(old_flow_section, new_flow_section)

# 10. Mid CTA
old_mid_cta = """        <h3>迷いをなくし、今やるべき練習を明確にするために。</h3>
        <p>
          目標に向けた最適な練習プランを一緒に整理しましょう。<br>
          ご相談から設計の開始まで、すべてオンライン（LINE）で完結します。
        </p>"""
new_mid_cta = """        <h3><span class="ib">迷いを減らし、</span><span class="ib">今やるべき練習を明確にするために。</span></h3>
        <p>
          <span class="ib">目標に向けた進め方を、</span><br class="sp-only">
          <span class="ib">一緒に整理していきましょう。</span><br><br>
          <span class="ib">ご相談から練習設計の開始まで、</span><br class="sp-only">
          <span class="ib">オンラインで進められます。</span>
        </p>"""
content = content.replace(old_mid_cta, new_mid_cta)

# Add .sp-only css
sp_only_css = """
    @media (min-width: 768px) {
      .sp-only {
        display: none;
      }
    }
"""
content = content.replace('    .ib {', sp_only_css + '    .ib {')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
