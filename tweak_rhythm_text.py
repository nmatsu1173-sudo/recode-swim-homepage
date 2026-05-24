import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Background Tone adjustments
css_bg_alt = """    .bg-alt {
      background-color: rgba(255, 255, 255, 0.02);
    }"""
new_css_bg_alt = """    .bg-alt {
      background-color: rgba(255, 255, 255, 0.035);
    }
    .bg-alt-2 {
      background-color: rgba(0, 0, 0, 0.2);
    }"""
content = content.replace(css_bg_alt, new_css_bg_alt)

# Apply classes
content = content.replace('<!-- お客様の声 -->\n  <section>', '<!-- お客様の声 -->\n  <section class="bg-alt-2">')
# サービスの特徴 is currently bg-alt
content = content.replace('<!-- 4. サービスの特徴 -->\n  <section class="bg-alt">', '<!-- 4. サービスの特徴 -->\n  <section class="bg-alt-2">')
# Flow is currently <section>
content = content.replace('<!-- Flow (ご相談からの流れ) -->\n  <section>', '<!-- Flow (ご相談からの流れ) -->\n  <section class="bg-alt-2">')


# 2. Customer Voices text and highlight compression
old_voice_intro = """      <p class="text-center" style="margin-bottom: 2.5rem; color: var(--color-secondary); font-size: 1.02rem; line-height: 1.6;">
        練習量を増やすことより、<span class="highlight nowrap">何を意識して積み上げるか</span>。<br>
        RECODEを通して生まれた変化の一部です。
      </p>"""
new_voice_intro = """      <p class="text-center" style="margin-bottom: 2.5rem; color: var(--color-secondary); font-size: 1.02rem; line-height: 1.6;">
        <span class="ib">練習量を増やすことより、</span><span class="nowrap">何を意識して積み上げるか</span>。<br>
        <span class="ib">RECODEを通して生まれた変化の一部です。</span>
      </p>"""
content = content.replace(old_voice_intro, new_voice_intro)

old_voice1_txt = """毎回のテーマや次への課題があることで、<span class="highlight nowrap">目的を持って練習</span>に取り組みやすくなりました。<br><br>ログを送るたびに状態に合わせたアドバイスをもらえ、違短感を客観的に見られるようになったため、無理をしすぎる前に練習量を調整できるようになったのが大きな変化です。"""
# wait, there's a typo in the file? "違和感" vs "違短感"? Ah, my previous prompt might have had it. Let's just regex replace the voice texts entirely.

voice1_pattern = r'<div class="voice-text">毎回のテーマや次への課題があることで.*?</div>'
new_voice1_txt = """<div class="voice-text">毎回のテーマや次への課題があることで、<span class="nowrap">目的を持って練習</span>に取り組みやすくなりました。<br><br>ログを送るたびにアドバイスをもらえ、客観的に自分の状態を見られるようになったため、無理をする前に調整できるようになったのが大きな変化です。</div>"""
content = re.sub(voice1_pattern, new_voice1_txt, content, flags=re.DOTALL)

voice2_pattern = r'<div class="voice-text">以前は「もっと頑張らないと」と考えすぎていましたが.*?</div>'
new_voice2_txt = """<div class="voice-text">以前は「もっと頑張らないと」と考えすぎていましたが、やり切ることよりも良い感覚を守ることの大切さに気づきました。<br><br>タイムだけでなく、力みなどの反応にも目を向けられるようになり、<span class="nowrap">身体と向き合う練習</span>へと変わりつつあります。</div>"""
content = re.sub(voice2_pattern, new_voice2_txt, content, flags=re.DOTALL)


# 3. Emotion Cards texts
emotion_desc_1_old = '<p class="emotion-desc">一人で練習していて、<span class="highlight nowrap">何を優先すればいいか</span>迷っている方。</p>'
emotion_desc_1_new = '<p class="emotion-desc">一人で練習していて、何を優先すればいいか迷っている方。</p>'
content = content.replace(emotion_desc_1_old, emotion_desc_1_new)

emotion_desc_2_old = '<p class="emotion-desc">大会や記録に向けて、<span class="highlight nowrap">目標から逆算</span>して練習したい方。</p>'
emotion_desc_2_new = '<p class="emotion-desc">大会や記録に向けて、目標から逆算して練習したい方。</p>'
content = content.replace(emotion_desc_2_old, emotion_desc_2_new)

emotion_desc_3_old = '<p class="emotion-desc">40代以降も、<span class="highlight nowrap">身体と向き合い</span>ながら泳ぎ続けたい方。</p>'
emotion_desc_3_new = '<p class="emotion-desc">40代以降も、身体と向き合いながら泳ぎ続けたい方。</p>'
content = content.replace(emotion_desc_3_old, emotion_desc_3_new)

emotion_desc_4_old = '<p class="emotion-desc">練習量を増やすだけでなく、<span class="highlight nowrap">振り返りながら積み上げたい</span>方。</p>'
emotion_desc_4_new = '<p class="emotion-desc">練習量を増やすだけでなく、振り返りながら積み上げたい方。</p>'
content = content.replace(emotion_desc_4_old, emotion_desc_4_new)

# Compress Emotion Cards padding
content = content.replace('padding: 2rem 1.5rem;', 'padding: 1.5rem 1.25rem;')

# 4. Flow Steps update Step 4
old_step4_desc = '<p class="flow-desc">内容に納得いただいたうえで、正式にお申し込み</p>'
new_step4_desc = '<p class="flow-desc">内容に納得いただいたうえで、正式にお申し込み・お支払いへ進む</p>'
content = content.replace(old_step4_desc, new_step4_desc)

old_flow_note = """      <p class="flow-note text-center">
        <span class="flow-note-main">まずは整理だけでも大丈夫です。</span>
        <span class="flow-note-sub">必要な場合のみ、合う進め方をご案内します。</span>
      </p>"""
new_flow_note = """      <p class="flow-note text-center">
        <span class="flow-note-main" style="display:block; margin-bottom: 0.25rem;">まずは整理だけでも大丈夫です。</span>
        <span class="flow-note-sub">必要な場合のみ、合う進め方をご案内します。</span>
      </p>"""
content = content.replace(old_flow_note, new_flow_note)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
