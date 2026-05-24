import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update button styling
old_btn = """    .btn {
      display: block;
      width: 100%;
      max-width: 320px;
      margin: 0 auto;
      text-align: center;
      background: linear-gradient(135deg, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.02) 100%);
      border: 1px solid rgba(255, 255, 255, 0.3);
      color: var(--color-heading);
      text-decoration: none;
      padding: 1.15rem 1rem;
      border-radius: 6px;
      font-weight: 500;
      font-size: 1.02rem;
      transition: transform 0.2s, background 0.2s, border-color 0.2s;
      letter-spacing: 0.05em;
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }

    .btn:hover {
      background: rgba(255, 255, 255, 0.15);
      border-color: rgba(255, 255, 255, 0.5);
    }"""
new_btn = """    .btn {
      display: block;
      width: 100%;
      max-width: 340px;
      margin: 0 auto;
      text-align: center;
      background: linear-gradient(135deg, rgba(14, 165, 233, 0.15) 0%, rgba(14, 165, 233, 0.05) 100%);
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
      box-shadow: 0 4px 12px rgba(15, 23, 42, 0.3);
    }

    .btn:hover {
      background: rgba(14, 165, 233, 0.25);
      border-color: rgba(14, 165, 233, 0.6);
      box-shadow: 0 6px 16px rgba(14, 165, 233, 0.15);
    }"""
content = content.replace(old_btn, new_btn)

# 2. Hero CTA Subtext
old_hero_sub_cta = """        <div class="hero-sub-cta-wrap">
          <a href="#" class="hero-sub-cta">相談前に、3つの質問で<span class="highlight nowrap">現在地を整理</span>する</a>
        </div>"""
new_hero_sub_cta = """        <div style="margin-top: 1.25rem; font-size: 0.95rem; color: #CBD5E1; line-height: 1.6;">
          相談前に、3つの質問で<span class="highlight nowrap">現在地を整理</span>できます。<br>
          <span class="highlight nowrap">まずは整理だけでも大丈夫です。</span>
        </div>"""
content = content.replace(old_hero_sub_cta, new_hero_sub_cta)

# 3. Voice text reduction (using triple quotes so we don't need to escape HTML quotes)
old_voice1 = """一人で練習していても、毎回のテーマや次への課題があることで、目的を持って取り組みやすくなりました。<br><br>練習ログを送るたびに、その時の状態に合わせたアドバイスや次回のメニューをもらえたので、無理なく続けられました。<br><br>記録と振り返りを続けることで、疲労や違和感を客観的に見られるようになり、無理をしすぎる前に練習量を調整できるようになったことが大きな変化です。"""
new_voice1 = """毎回のテーマや次への課題があることで、<span class="highlight nowrap">目的を持って練習</span>に取り組みやすくなりました。<br><br>ログを送るたびに状態に合わせたアドバイスをもらえ、違和感を客観的に見られるようになったため、無理をしすぎる前に練習量を調整できるようになったのが大きな変化です。"""
content = content.replace(old_voice1, new_voice1)

old_voice2 = """以前は「もっと頑張らないと」と考えすぎてしまい、泳いだ後に疲れや張りが残ることがありました。<br><br>RECODEを続ける中で、やり切ることよりも、良い感覚を守ることの大切さに気づきました。<br><br>タイムやストローク数だけではなく、力みや身体の反応にも目を向けられるようになり、練習との向き合い方が少しずつ変わってきています。"""
new_voice2 = """以前は「もっと頑張らないと」と考えすぎていましたが、やり切ることよりも良い感覚を守ることの大切さに気づきました。<br><br>タイムやストローク数だけでなく、力みなどの反応にも目を向けられるようになり、<span class="highlight nowrap">身体と向き合う練習</span>へと変わりつつあります。"""
content = content.replace(old_voice2, new_voice2)

# 4. RECODEとは reduction & highlight
old_about = """          RECODEは、マスターズスイマーや成人スイマーに向けた、目標逆算型の練習設計サポートです。<br><br>
          細かなフォーム修正だけを目的にするのではなく、現在地・課題・練習環境を整理し、限られた時間の中で<span class="highlight nowrap">何を優先して積み上げるか</span>を一緒に整えていきます。"""
new_about = """          RECODEは、<span class="highlight nowrap">フォーム添削ではなく、練習設計を</span>提供するサポートです。<br><br>
          目標・現在地・練習環境を整理し、限られた時間の中で<span class="highlight nowrap">何を優先して積み上げるか</span>を一緒に整えていきます。"""
content = content.replace(old_about, new_about)

# 5. Features side-by-side restoration
old_features = """      <div class="features-wrapper" style="grid-template-columns: 1fr;">
        <div class="feature-box anti" style="max-width: 500px; margin: 0 auto;">
          <h3 style="text-align: center;"><span style="display: inline-block; white-space: nowrap;">RECODEが</span><span style="display: inline-block; white-space: nowrap;">主目的にしないこと</span></h3>
          <ul>
            <li>結果の即効性や短期間での結果保証</li>
            <li>細かなフォーム修正だけを目的にした指導</li>
            <li>何度も動画添削を繰り返すサービス</li>
          </ul>
        </div>
      </div>"""
new_features = """      <div class="features-wrapper">
        <div class="feature-box">
          <h3><span style="display: inline-block; white-space: nowrap;">RECODEで</span><span style="display: inline-block; white-space: nowrap;">整えること</span></h3>
          <ul>
            <li>目標に向けた現在地と課題の整理</li>
            <li>環境に合わせた練習メニューの設計</li>
            <li>練習ログを活かした週ごとの調整</li>
          </ul>
        </div>

        <div class="feature-box anti">
          <h3><span style="display: inline-block; white-space: nowrap;">RECODEが</span><span style="display: inline-block; white-space: nowrap;">主目的にしないこと</span></h3>
          <ul>
            <li>短期間での結果保証</li>
            <li>細かなフォーム修正だけを目的にした指導</li>
            <li>何度も動画添削を繰り返すサービス</li>
          </ul>
        </div>
      </div>"""
content = content.replace(old_features, new_features)

# 6. Delete Pricing CTA
pricing_cta_regex = r'      <!-- \n        【LINE公式アカウント URL設定箇所 \(料金セクション\).*?</a>'
content = re.sub(pricing_cta_regex, '', content, flags=re.DOTALL)

# 7. Add .line-cta-btn to all CTA and unify text
content = content.replace('class="btn"', 'class="btn line-cta-btn"')

# 8. Append JS Script
script = """
  <!-- LINE CTA Setup -->
  <script>
    // 【LINE公式アカウント URL一括設定】
    // ここに本番のLINE公式アカウントURLを設定してください。
    const LINE_URL = "#"; 
    
    document.addEventListener('DOMContentLoaded', () => {
      document.querySelectorAll('.line-cta-btn').forEach(btn => {
        btn.href = LINE_URL;
      });
    });
  </script>
</body>
"""
content = content.replace('</body>', script)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
