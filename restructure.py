import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Operator Mini Block
content = re.sub(r'  <!-- 1\.5 運営者メッセージミニブロック -->.*?  </section>\n', '', content, flags=re.DOTALL)

# 2. Voices Section update (2 columns, new text)
new_voices = """  <!-- お客様の声 -->
  <section>
    <div class="container">
      <h2 style="text-align: center; margin-bottom: 1rem;">RECODEを受けた方の声</h2>
      <p class="text-center" style="margin-bottom: 2.5rem; color: var(--color-secondary); font-size: 0.95rem; line-height: 1.6;">
        練習量を増やすことより、何を意識して積み上げるか。<br>
        RECODEを通して生まれた変化の一部です。
      </p>

      <div class="voices-grid">
        <!-- Voice 1 -->
        <div class="voice-card">
          <h3 class="voice-card-title">一人でも、目的を持って練習できるようになった</h3>
          <div class="voice-text">一人で練習していても、毎回のテーマや次への課題があることで、目的を持って取り組みやすくなりました。<br><br>練習ログを送るたびに、その時の状態に合わせたアドバイスや次回のメニューをもらえたので、無理なく続けられました。<br><br>記録と振り返りを続けることで、疲労や違和感を客観的に見られるようになり、無理をしすぎる前に練習量を調整できるようになったことが大きな変化です。</div>
          <div class="voice-meta">
            <span>60代女性｜トライアスロン</span>
          </div>
        </div>

        <!-- Voice 2 -->
        <div class="voice-card">
          <h3 class="voice-card-title">頑張りすぎる練習から、身体と向き合う練習へ</h3>
          <div class="voice-text">以前は「もっと頑張らないと」と考えすぎてしまい、泳いだ後に疲れや張りが残ることがありました。<br><br>RECODEを続ける中で、やり切ることよりも、良い感覚を守ることの大切さに気づきました。<br><br>タイムやストローク数だけではなく、力みや身体の反応にも目を向けられるようになり、練習との向き合い方が少しずつ変わってきています。</div>
          <div class="voice-meta">
            <span>60代女性｜成人スイマー</span>
          </div>
        </div>
      </div>
      
      <p class="text-center" style="font-size: 0.8rem; color: var(--color-secondary); margin-top: 2rem;">
        掲載内容は、個人が特定されない形に一部編集しています。
      </p>
    </div>
  </section>"""
content = re.sub(r'  <!-- お客様の声 -->.*?  </section>', new_voices, content, flags=re.DOTALL)

# 3. Replace "こんな迷いはありませんか？" with "こんな方へ"
new_target = """  <!-- 2. こんな方へ -->
  <section class="bg-alt">
    <div class="container">
      <h2>こんな方へ</h2>
      
      <div class="emotion-cards-grid">
        <div class="emotion-card rhythm-circle">
          <div class="emotion-icon-wrap">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="9" stroke-dasharray="2 2" stroke-width="1"></circle>
              <circle cx="12" cy="12" r="4" stroke-width="1.5"></circle>
            </svg>
          </div>
          <h3 class="emotion-title">一人練習で優先順位に迷う方</h3>
          <p class="emotion-desc">一人で練習していて、何を優先すればいいか迷っている方。</p>
        </div>

        <div class="emotion-card rhythm-line">
          <div class="emotion-icon-wrap">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
              <line x1="4" y1="6" x2="20" y2="6" stroke-width="1"></line>
              <line x1="4" y1="12" x2="14" y2="12" stroke-width="1"></line>
              <line x1="4" y1="18" x2="18" y2="18" stroke-width="1"></line>
              <circle cx="17" cy="12" r="1.5" fill="currentColor" stroke="none"></circle>
            </svg>
          </div>
          <h3 class="emotion-title">目標から逆算して設計したい方</h3>
          <p class="emotion-desc">大会や記録に向けて、目標から逆算して練習したい方。</p>
        </div>

        <div class="emotion-card rhythm-dots">
          <div class="emotion-icon-wrap">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
              <path d="M5 8h14M8 16h8" stroke-width="1"></path>
              <circle cx="12" cy="12" r="1" fill="currentColor" stroke="none"></circle>
            </svg>
          </div>
          <h3 class="emotion-title">身体と向き合い長く泳ぎたい方</h3>
          <p class="emotion-desc">40代以降も、身体と向き合いながら泳ぎ続けたい方。</p>
        </div>

        <div class="emotion-card rhythm-wave">
          <div class="emotion-icon-wrap">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
              <path d="M4 10c2-1 4-1 6 0s4 1 6 0 2-1 4-1M4 14h16" stroke-width="1"></path>
            </svg>
          </div>
          <h3 class="emotion-title">振り返りながら積み上げたい方</h3>
          <p class="emotion-desc">練習量を増やすだけでなく、振り返りながら積み上げたい方。</p>
        </div>
      </div>
    </div>
  </section>"""
content = re.sub(r'  <!-- 2\. 一人練習者の悩み -->.*?  </section>', new_target, content, count=1, flags=re.DOTALL)

# Remove "主な対象者"
content = re.sub(r'  <!-- 6\. 対象者 -->.*?  </section>\n\n', '', content, flags=re.DOTALL)

# 4. Shorten "RECODEとは"
new_about = """  <!-- 3. RECODEとは -->
  <section class="about-section">
    <div class="container">
      <h2>RECODEとは</h2>
      <div class="about-wrapper" style="display: block; text-align: center; max-width: 620px; margin: 0 auto;">
        <p style="font-size: 1rem; line-height: 1.8; margin-bottom: 0;">
          RECODEは、マスターズスイマーや成人スイマーに向けた、目標逆算型の練習設計サポートです。<br><br>
          細かなフォーム修正だけを目的にするのではなく、現在地・課題・練習環境を整理し、限られた時間の中で何を優先して積み上げるかを一緒に整えていきます。
        </p>
      </div>
    </div>
  </section>"""
content = re.sub(r'  <!-- 3\. RECODEとは -->.*?  </section>', new_about, content, flags=re.DOTALL)

# 5. Shorten "サービスの特徴"
new_features = """  <!-- 4. サービスの特徴 -->
  <section class="bg-alt">
    <div class="container">
      <h2>サービスの特徴</h2>

      <div class="features-wrapper" style="grid-template-columns: 1fr;">
        <div class="feature-box anti" style="max-width: 500px; margin: 0 auto;">
          <h3 style="text-align: center;"><span style="display: inline-block; white-space: nowrap;">RECODEが</span><span style="display: inline-block; white-space: nowrap;">主目的にしないこと</span></h3>
          <ul>
            <li>結果の即効性や短期間での結果保証</li>
            <li>細かなフォーム修正だけを目的にした指導</li>
            <li>何度も動画添削を繰り返すサービス</li>
          </ul>
        </div>
      </div>
      
      <p class="text-center" style="margin-top: 2rem; color: var(--color-secondary);">
        RECODEは、目標と現在地から、練習の優先順位と積み上げ方を整理するサービスです。
      </p>
    </div>
  </section>"""
content = re.sub(r'  <!-- 4\. RECODEでできること / 5\. やらないこと -->.*?  </section>', new_features, content, flags=re.DOTALL)

# 6. Extract and Move Mid CTA
cta_match = re.search(r'  <!-- 中盤CTA -->.*?  </section>\n', content, flags=re.DOTALL)
if cta_match:
    cta_html = cta_match.group(0)
    content = content.replace(cta_html, '') # Remove from original position
    
    # Insert after ご相談からの流れ
    flow_end_str = 'まずは整理だけでも大丈夫です。</span>\n        <span class="flow-note-sub">必要な場合のみ、合う進め方をご案内します。</span>\n      </p>\n    </div>\n  </section>\n'
    content = content.replace(flow_end_str, flow_end_str + '\n' + cta_html)

# 7. FAQ Accordion HTML & CSS
new_faq_css = """    /* FAQ Accordion */
    .faq-item {
      margin-bottom: 1rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.15);
    }

    .faq-item:last-child {
      border-bottom: none;
      margin-bottom: 0;
    }

    .faq-details {
      width: 100%;
    }

    .faq-summary {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1.25rem 0;
      cursor: pointer;
      font-weight: 600;
      color: var(--color-heading);
      position: relative;
      padding-left: 2rem;
      list-style: none; /* Hide default arrow */
      line-height: 1.5;
    }

    .faq-summary::-webkit-details-marker {
      display: none;
    }

    .faq-summary::before {
      content: "Q.";
      position: absolute;
      left: 0;
      top: 1.25rem;
      color: var(--color-accent);
      font-weight: 700;
      font-size: 1.1rem;
    }

    .faq-summary::after {
      content: "＋";
      color: var(--color-secondary);
      font-weight: 300;
      font-size: 1.2rem;
      transition: transform 0.3s ease;
    }

    .faq-details[open] .faq-summary::after {
      content: "−";
    }

    .faq-a {
      padding: 0 0 1.5rem 2rem;
      position: relative;
      color: var(--color-text-main);
      line-height: var(--line-height-base);
    }

    .faq-a::before {
      content: "A.";
      position: absolute;
      left: 0;
      top: 0;
      color: var(--color-secondary);
      font-weight: 700;
      font-size: 1.1rem;
    }"""
content = re.sub(r'    /\* FAQ \*/.*?    \.faq-a::before {.*?\n    }', new_faq_css, content, flags=re.DOTALL)

new_faq_html = """  <!-- 9. FAQ -->
  <section>
    <div class="container">
      <h2>よくあるご質問</h2>

      <div class="faq-item">
        <details class="faq-details">
          <summary class="faq-summary">フォームの動画を送ることはできますか？</summary>
          <div class="faq-a">はい。必要に応じて、現在地を整理するための参考材料として活用します。ただし、RECODEは細かなフォーム添削そのものを主目的とするサービスではありません。</div>
        </details>
      </div>

      <div class="faq-item">
        <details class="faq-details">
          <summary class="faq-summary">週に何回練習できれば対象になりますか？</summary>
          <div class="faq-a">回数に決まりはありません。週1回でも、その1回を目標につながる練習にするための組み立て方を一緒に整理します。</div>
        </details>
      </div>

      <div class="faq-item">
        <details class="faq-details">
          <summary class="faq-summary">チーム練習やスクールに通っていても利用できますか？</summary>
          <div class="faq-a">はい。チームやスクールでの練習を否定するものではありません。自分の目標に合わせて、何を補い、どう積み上げるかを整理したい方に向いています。</div>
        </details>
      </div>

      <div class="faq-item">
        <details class="faq-details">
          <summary class="faq-summary">相談だけでも大丈夫ですか？</summary>
          <div class="faq-a">はい。まずは現在地や課題を整理するだけでも構いません。必要に応じて、合う進め方をご案内します。</div>
        </details>
      </div>

    </div>
  </section>"""
content = re.sub(r'  <!-- 9\. FAQ -->.*?  </section>', new_faq_html, content, flags=re.DOTALL)

# Voice grid columns CSS update (3 -> 2)
content = content.replace('grid-template-columns: repeat(3, 1fr);', 'grid-template-columns: repeat(2, 1fr);')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
