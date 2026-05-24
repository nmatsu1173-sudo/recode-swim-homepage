import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_features_html = """
      <style>
        @media (min-width: 768px) {
          #features .grid-cards { grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
        }
        .feature-panel {
          background: #FFFFFF;
          border: 1px solid var(--color-border);
          padding: 2.5rem 1.5rem;
          border-radius: 12px;
          box-shadow: 0 4px 12px rgba(0,0,0,0.03);
          text-align: center;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          gap: 1.2rem;
          transition: all 0.3s ease;
        }
        .feature-panel:hover {
          transform: translateY(-4px); box-shadow: 0 12px 24px rgba(0,0,0,0.08);
          border-color: var(--color-accent-light);
        }
        .feature-panel h3 { font-size: 1.15rem; color: var(--color-heading); margin: 0; line-height: 1.5; font-weight: 700; }
        .feature-panel i { font-size: 2.5rem; color: var(--color-accent); }
        .anti-note {
          width: 100%;
          text-align: center;
          margin-top: 3.5rem;
          padding: 1.5rem;
          background: #F8FAFC;
          border: 1px solid #E2E8F0;
          border-radius: 8px;
          font-size: 0.9rem;
          color: var(--color-secondary);
          line-height: 1.6;
        }
      </style>
      <div class="grid-cards">
        <div class="feature-panel">
          <i class="fas fa-map-marker-alt"></i>
          <h3>現在地と<br>課題の整理</h3>
        </div>
        <div class="feature-panel">
          <i class="fas fa-drafting-compass"></i>
          <h3>練習メニューの<br>設計</h3>
        </div>
        <div class="feature-panel">
          <i class="fas fa-sliders-h"></i>
          <h3>練習ログを<br>活かした調整</h3>
        </div>
      </div>
      
      <div class="anti-note">
        ※ RECODEは「短期間での結果保証」「細かなフォーム修正だけを目的にした指導」「何度も動画添削を繰り返すこと」を主目的にはしていません。<br class="pc-only">目標と現在地から、練習の優先順位と積み上げ方を整理するサービスです。
      </div>
"""

# Replace everything from <div class="grid-cards"> to </p> in the features section
pattern = r'(<div class="grid-cards">.*?<p class="text-center"[^>]*>.*?</p>)'
match = re.search(pattern, html, re.DOTALL)
if match:
    # We only want to replace the match INSIDE the features section
    # Let's be safer:
    section_pattern = r'(<section class="bg-alt" id="features">.*?<h2>サービスの特徴</h2>\s*)(<div class="grid-cards">.*?</p>)'
    html = re.sub(section_pattern, r'\1' + new_features_html, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated Features section layout.")
