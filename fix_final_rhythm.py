import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update alternating backgrounds
# 運営者: <section class="bg-alt operator-profile-section"> is already there. Let's make it bg-alt.
# FAQ is <section> -> <section>
# 最終CTA is <section class="cta-section"> -> <section class="cta-section bg-alt-2">
content = content.replace('<section class="cta-section">', '<section class="cta-section bg-alt-2">')

# 2. Update "こんな方へ" clean up rhythms
content = content.replace('class="emotion-card rhythm-circle"', 'class="emotion-card"')
content = content.replace('class="emotion-card rhythm-line"', 'class="emotion-card"')
content = content.replace('class="emotion-card rhythm-dots"', 'class="emotion-card"')
content = content.replace('class="emotion-card rhythm-wave"', 'class="emotion-card"')

# 3. RECODEとは
old_about = """          <span class="ib">RECODEは、</span><span class="highlight nowrap">フォーム添削ではなく、</span><br><span class="ib">目標に向けた練習設計を</span><span class="ib">整えるサポートです。</span><br><br>
          <span class="ib">目標・現在地・練習環境を整理し、</span><br><span class="ib">限られた時間の中で</span><span class="highlight nowrap">何を優先して積み上げるか</span>を<br><span class="ib">一緒に明確にしていきます。</span>"""
new_about = """          <span class="ib">RECODEは、</span><span class="highlight nowrap">フォーム添削ではなく、</span><br>
          <span class="ib">練習設計を提供するサポートです。</span><br><br>
          <span class="ib">目標・現在地・練習環境を整理し、</span><br>
          <span class="ib">限られた時間の中で</span><span class="highlight nowrap">何を優先して積み上げるか</span>を<br>
          <span class="ib">一緒に明確にしていきます。</span>"""
content = content.replace(old_about, new_about)

# 4. Payment method text
old_payment = """          <span class="ib">お支払い方法は、ご相談後にご案内します。</span><br>
          <span class="ib">銀行振込を基本に、</span><span class="ib">今後はクレジットカード決済にも</span><span class="ib">対応できるよう準備しています。</span>"""
new_payment = """          <span class="ib">お支払い方法は、ご相談後にご案内します。</span><br>
          <span class="ib">現在は銀行振込を基本に、</span><span class="ib">今後はクレジットカード決済にも</span><span class="ib">対応できるよう準備しています。</span>"""
content = content.replace(old_payment, new_payment)

# 5. Flow step 4 desc
old_step4 = """<p class="flow-desc">内容に納得いただいたうえで、正式にお申し込み・お支払いへ進む</p>"""
new_step4 = """<p class="flow-desc">内容に納得したら正式に申込・お支払い</p>"""
content = content.replace(old_step4, new_step4)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
