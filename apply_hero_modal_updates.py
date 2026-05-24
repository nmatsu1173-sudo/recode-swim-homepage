import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. CSS Updates
# Header Transparency & Scrolled State
html = re.sub(r'(\.header\s*\{[^}]*?)background:\s*rgba\(15,\s*23,\s*42,\s*0\.9\);', r'\1background: transparent;', html)
html = re.sub(r'(\.header\s*\{[^}]*?)border-bottom:\s*1px\s*solid\s*rgba\(255,\s*255,\s*255,\s*0\.1\);', r'\1border-bottom: none;\n      transition: background 0.3s ease, box-shadow 0.3s ease;', html)

header_scroll_css = """
    .header.scrolled {
      background: rgba(15, 23, 42, 0.95);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
"""
html = html.replace('/* Hero */', header_scroll_css + '/* Hero */')

# Fullscreen Hero + Image Overlay
html = re.sub(r'(\.hero\s*\{[^}]*?min-height:\s*)80vh;', r'\1100vh;', html)
html = re.sub(r'(\.hero\s*\{[^}]*?background:\s*)linear-gradient\(135deg,\s*#0F172A\s*0%,\s*#0284C7\s*100%\);', 
              r"\1linear-gradient(135deg, rgba(15,23,42,0.85) 0%, rgba(2,132,199,0.75) 100%), url('assets/images/hero_swim_3.png') center/cover no-repeat;", html)

# Flow Card Updates
flow_card_css = """
    .flow-card {
      background: #FFFFFF; padding: 2.5rem 2.5rem;
      border: 1px solid var(--color-border);
      border-left: 4px solid var(--color-border);
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.03);
      display: flex; flex-direction: column;
      transition: all 0.3s ease;
      cursor: pointer;
    }
    .flow-card:hover {
      transform: translateY(-4px); box-shadow: 0 12px 24px rgba(0,0,0,0.08);
      border-left-color: var(--color-accent);
    }
    .flow-card-more {
      align-self: flex-start;
      color: var(--color-accent); font-size: 0.95rem; font-weight: 600;
      margin-top: 1.5rem;
      display: flex; align-items: center; gap: 0.5rem;
      background: var(--color-accent-light);
      padding: 0.4rem 1rem; border-radius: 50px; transition: all 0.3s ease;
    }
    .flow-card:hover .flow-card-more { background: var(--color-accent); color: #FFF; }
"""
html = re.sub(r'\.flow-card\s*\{[^}]*\}', '', html) # remove old flow-card css
html = html.replace('/* Pricing */', flow_card_css + '/* Pricing */')

# Modal CSS
modal_css = """
    /* Modal */
    .modal-overlay {
      position: fixed; top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(4px);
      z-index: 2000; display: flex; justify-content: center; align-items: center;
      opacity: 0; visibility: hidden; transition: all 0.3s ease; padding: 1.5rem;
    }
    .modal-overlay.open { opacity: 1; visibility: visible; }
    .modal-content {
      background: #FFFFFF; width: 100%; max-width: 600px;
      border-radius: 16px; padding: 3rem 2.5rem;
      position: relative; transform: translateY(20px); transition: all 0.3s ease;
      box-shadow: 0 20px 40px rgba(0,0,0,0.1);
      max-height: 90vh; overflow-y: auto;
    }
    .modal-overlay.open .modal-content { transform: translateY(0); }
    .modal-close {
      position: absolute; top: 1.5rem; right: 1.5rem;
      background: var(--color-bg-alt); border: none; width: 36px; height: 36px; border-radius: 50%;
      font-size: 1.2rem; color: var(--color-secondary); display: flex; justify-content: center; align-items: center;
      cursor: pointer; transition: all 0.3s ease;
    }
    .modal-close:hover { background: #E2E8F0; color: var(--color-heading); }
    .modal-title { font-size: 1.5rem; margin-bottom: 1.5rem; color: var(--color-heading); border-bottom: 2px solid var(--color-accent-light); padding-bottom: 0.8rem; }
    .modal-body { color: var(--color-text-main); line-height: 1.8; font-size: 1rem; }
    .modal-body p { margin-bottom: 1.2rem; }
"""
html = html.replace('/* Cinema / Image Grid */', modal_css + '/* Cinema / Image Grid */')

# Cinema Nav Pagination Badges
cinema_nav_css = """
    .cinema-nav {
      display: flex; justify-content: center; align-items: center; margin-top: 2.5rem; gap: 0.8rem; flex-wrap: wrap;
    }
    .cinema-nav-btn {
      background: var(--color-bg-alt); border: 1px solid var(--color-border);
      color: var(--color-secondary); cursor: pointer; padding: 0.6rem 1.2rem;
      border-radius: 50px; display: flex; align-items: center; gap: 0.5rem; transition: all 0.3s ease;
      flex-direction: row; /* reset from column */
    }
    .cinema-nav-btn:hover { background: #E2E8F0; }
    .cinema-nav-btn.active {
      background: var(--color-accent); border-color: var(--color-accent);
      color: #FFFFFF; box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);
    }
    .nav-num { font-size: 0.85rem; font-weight: 700; opacity: 0.9; }
    .nav-text { font-size: 0.95rem; font-weight: 600; }
    .cinema-nav-divider { display: none; }
"""
html = re.sub(r'\.cinema-nav\s*\{[^}]*\}', '', html)
html = re.sub(r'\.cinema-nav-btn\s*\{[^}]*\}', '', html)
html = re.sub(r'\.cinema-nav-btn\.active\s*\{[^}]*\}', '', html)
html = re.sub(r'\.nav-num\s*\{[^}]*\}', '', html)
html = re.sub(r'\.nav-text\s*\{[^}]*\}', '', html)
html = html.replace('/* Footer */', cinema_nav_css + '/* Footer */')


# 2. HTML Updates
# Modify Flow Cards
html = html.replace('<div class="flow-card flow-active">', '<div class="flow-card flow-active" data-step="1">')
html = html.replace('<div class="flow-card">', '<div class="flow-card" data-step="">') # Will fix the numbers manually below
html = html.replace('data-step="">\n          <span class="flow-step">STEP 2</span>', 'data-step="2">\n          <span class="flow-step">STEP 2</span>')
html = html.replace('data-step="">\n          <span class="flow-step">STEP 3</span>', 'data-step="3">\n          <span class="flow-step">STEP 3</span>')
html = html.replace('data-step="">\n          <span class="flow-step">STEP 4</span>', 'data-step="4">\n          <span class="flow-step">STEP 4</span>')
html = html.replace('data-step="">\n          <span class="flow-step">STEP 5</span>', 'data-step="5">\n          <span class="flow-step">STEP 5</span>')

flow_more_html = '\n          <div class="flow-card-more">詳細を見る <i class="fas fa-chevron-right"></i></div>\n        </div>'
html = re.sub(r'</p>\n\s*</div>\n\s*<div class="flow-arrow"></div>', r'</p>' + flow_more_html + '\n        <div class="flow-arrow"></div>', html)
# Final card (STEP 5)
html = re.sub(r'</p>\n\s*</div>\n\s*</div>\n\s*<p class="flow-note', r'</p>' + flow_more_html + '\n      </div>\n      <p class="flow-note', html)

# Add Modal HTML at the bottom
modal_html = """
  <!-- Flow Modal -->
  <div id="flow-modal" class="modal-overlay">
    <div class="modal-content">
      <button class="modal-close"><i class="fas fa-times"></i></button>
      <h3 class="modal-title" id="modal-title">STEP</h3>
      <div class="modal-body" id="modal-body">
        <p>ここに詳細な説明文が入ります。</p>
      </div>
    </div>
  </div>
"""
html = html.replace('</body>', modal_html + '\n</body>')

# 3. JS Updates
js_additions = """
  <!-- Scroll & Modal Script -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      // Header Scroll
      const header = document.querySelector('.header');
      window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
          header.classList.add('scrolled');
        } else {
          header.classList.remove('scrolled');
        }
      });

      // Modal Logic
      const modal = document.getElementById('flow-modal');
      const modalTitle = document.getElementById('modal-title');
      const modalBody = document.getElementById('modal-body');
      const closeBtn = document.querySelector('.modal-close');
      
      const modalData = {
        1: {
          title: "STEP 1: LINEで相談",
          content: "<p>目標や出場予定の大会、現在のタイム、練習で悩んでいることなどをLINEでお送りください。</p><p>「こんなこと相談してもいいのかな？」と思うような些細なことでも構いません。専任のアドバイザーがメッセージを確認し、現状の整理をサポートします。</p>"
        },
        2: {
          title: "STEP 2: 現在地を整理",
          content: "<p>いただいた内容をもとに、現在の練習環境や週の練習回数、フォームの課題などを一緒に確認します。</p><p>目標に対して「何が足りていないか」「どこを改善すべきか」を明確にすることで、迷いなく練習に取り組める基盤をつくります。</p>"
        },
        3: {
          title: "STEP 3: 進め方を提案",
          content: "<p>整理した課題と目標をもとに、あなたに最適なサポート内容と進め方（練習プラン作成、フォーム分析など）をご提案します。</p><p>無理にサービスをおすすめすることはありません。必要だと感じた場合のみご検討ください。</p>"
        },
        4: {
          title: "STEP 4: 申込・お支払い",
          content: "<p>ご提案したサポート内容と料金にご納得いただけましたら、正式にお申し込みとお支払いをお願いいたします。</p><p>お手続き完了後、すぐに初回のヒアリングやメニュー作成に取り掛かります。</p>"
        },
        5: {
          title: "STEP 5: 練習設計を開始",
          content: "<p>アドバイザーがあなたのための専用練習メニュー（設計図）を作成し、共有します。</p><p>日々の練習結果（ログ）を報告いただきながら、目標達成に向けて二人三脚で練習を積み上げていきます。</p>"
        }
      };

      document.querySelectorAll('.flow-card').forEach(card => {
        card.addEventListener('click', () => {
          const step = card.getAttribute('data-step');
          if (modalData[step]) {
            modalTitle.textContent = modalData[step].title;
            modalBody.innerHTML = modalData[step].content;
            modal.classList.add('open');
          }
        });
      });

      closeBtn.addEventListener('click', () => {
        modal.classList.remove('open');
      });

      modal.addEventListener('click', (e) => {
        if (e.target === modal) {
          modal.classList.remove('open');
        }
      });
    });
  </script>
"""
html = html.replace('</body>', js_additions + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated Hero, Header, Flow Modals, and Cinema Pagination.")
