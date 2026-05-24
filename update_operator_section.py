import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# CSS for the new modern profile section
profile_css = """
    /* Modern Profile Section */
    .profile-modern-container {
      display: flex;
      flex-direction: column;
      gap: 3rem;
      background: #FFFFFF;
      padding: 3rem 2rem;
      border-radius: 16px;
      box-shadow: 0 10px 40px rgba(0,0,0,0.06);
      margin-top: 2rem;
    }
    @media (min-width: 768px) {
      .profile-modern-container {
        flex-direction: row;
        align-items: flex-start;
        padding: 4rem;
        gap: 5rem;
      }
    }
    .profile-identity {
      flex: 1;
      text-align: center;
      position: sticky;
      top: 100px;
    }
    .profile-photo-wrapper {
      margin: 0 auto 1.5rem;
      width: 220px;
      height: 220px;
      border-radius: 50%;
      overflow: hidden;
      box-shadow: 0 12px 30px rgba(0,0,0,0.15);
      border: 6px solid #FFFFFF;
      position: relative;
    }
    .profile-photo-main {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transform: scale(1.05); /* Slight zoom for premium feel */
    }
    .profile-name {
      font-size: 1.8rem;
      font-weight: 700;
      color: var(--color-heading);
      margin-bottom: 0.2rem;
      letter-spacing: 0.05em;
    }
    .profile-name-en {
      font-size: 0.85rem;
      color: var(--color-accent);
      letter-spacing: 0.15em;
      margin-bottom: 1.5rem;
      text-transform: uppercase;
      font-weight: 600;
    }
    .profile-title {
      font-weight: 700;
      color: var(--color-secondary);
      margin-bottom: 0.5rem;
      font-size: 0.95rem;
      background: #F1F5F9;
      display: inline-block;
      padding: 0.4rem 1rem;
      border-radius: 20px;
    }
    .profile-caption {
      font-size: 0.8rem;
      color: #94A3B8;
      margin-top: 1rem;
    }
    
    .profile-story {
      flex: 1.8;
    }
    .profile-story p {
      font-size: 1.05rem;
      line-height: 2;
      color: #334155;
      margin-bottom: 3.5rem;
      text-align: left;
    }
    
    .polaroid-wrapper {
      background: #FFFFFF;
      padding: 0.8rem 0.8rem 3rem 0.8rem;
      box-shadow: 0 4px 15px rgba(0,0,0,0.1);
      transform: rotate(2deg);
      max-width: 340px;
      margin: 0 auto;
      transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .polaroid-wrapper:hover {
      transform: rotate(0deg) scale(1.03);
      box-shadow: 0 12px 30px rgba(0,0,0,0.15);
    }
    .polaroid-img {
      width: 100%;
      height: auto;
      display: block;
      filter: sepia(20%) contrast(110%);
    }
    .polaroid-caption {
      text-align: center;
      font-family: 'Zen Kaku Gothic New', "Hiragino Kaku Gothic ProN", sans-serif;
      position: relative;
      top: 1.2rem;
      font-size: 0.95rem;
      color: #475569;
    }
"""

html = html.replace('/* Footer */', profile_css + '\n/* Footer */')

new_html = """  <!-- 7. 運営者プロフィール -->
  <section class="bg-alt-light" id="operator">
    <div class="container">
      <h2>運営者</h2>
      
      <div class="profile-modern-container">
        <!-- Left: Identity -->
        <div class="profile-identity">
          <div class="profile-photo-wrapper">
            <img src="assets/images/recode_operator_current.png" alt="松下 典功" class="profile-photo-main">
          </div>
          <div class="profile-name">松下 典功</div>
          <div class="profile-name-en">Norikatsu Matsushita</div>
          <div class="profile-title">RECODE運営者 / マスターズスイマー</div>
          <div class="profile-caption">2023年 世界マスターズ福岡にて</div>
        </div>
        
        <!-- Right: Story -->
        <div class="profile-story">
          <p>
            RECODEを運営する松下典功は、マスターズ水泳で日本一、世界大会5位入賞を経験し、現在も記録更新に挑戦している現役マスターズスイマーです。<br><br>
            仕事と競技を両立する中で、自分自身の練習内容・食事・睡眠・ログ分析も研究対象とし、「目標から逆算した練習設計」を長年実践し続けてきました。<br><br>
            机上の空論ではなく、限られた時間と環境の中でいかに着実に積み上げるか。<br>
            そのリアルな葛藤と工夫を知る実践者の視点から、あなたにとって最適なパフォーマンス設計を一緒に整理します。
          </p>

          <div class="polaroid-wrapper">
            <img src="assets/images/recode_operator_origin.jpg" alt="競技の原点" class="polaroid-img">
            <div class="polaroid-caption">水泳は、積み上げ方を学んできた原点です。</div>
          </div>
        </div>
      </div>
      
    </div>
  </section>"""

pattern = r'<!-- 7\. 運営者プロフィール -->.*?</section>'
html = re.sub(pattern, new_html, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated Operator section to modern profile layout.")
