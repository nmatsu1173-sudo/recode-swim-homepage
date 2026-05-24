import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the cinema slides by injecting the style attributes with the images
slides_html = """
          <!-- STEP 1 -->
          <div class="cinema-slide active" style="background-image: url('assets/images/recode_step01_goal.png');"></div>

          <!-- STEP 2 -->
          <div class="cinema-slide" style="background-image: url('assets/images/recode_step02_current.png');"></div>

          <!-- STEP 3 -->
          <div class="cinema-slide" style="background-image: url('assets/images/recode_step03_blueprint.png');"></div>

          <!-- STEP 4 -->
          <div class="cinema-slide" style="background-image: url('assets/images/recode_step04_action.png');"></div>

          <!-- STEP 5 -->
          <div class="cinema-slide" style="background-image: url('assets/images/recode_step05_adjust.png');"></div>
"""

# Pattern to find the current slide div structure
old_slides_pattern = r'<!-- STEP 1 -->\s*<div class="cinema-slide active"\s*>\s*</div>\s*<!-- STEP 2 -->\s*<div class="cinema-slide"\s*>\s*</div>\s*<!-- STEP 3 -->\s*<div class="cinema-slide"\s*>\s*</div>\s*<!-- STEP 4 -->\s*<div class="cinema-slide"\s*>\s*</div>\s*<!-- STEP 5 -->\s*<div class="cinema-slide"\s*>\s*</div>'

html = re.sub(old_slides_pattern, slides_html.strip(), html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Restored background images for cinema slides.")
