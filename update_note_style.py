import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_p_tag = r'<p class="text-center"\s*>\s*掲載内容は、個人が特定されないよう一部編集しています。\s*</p>'
new_p_tag = r"""<p class="text-center" style="font-size: 0.75rem; margin-top: 3rem; opacity: 0.7;">
        ※掲載内容は、個人が特定されないよう一部編集しています。
      </p>"""

html = re.sub(old_p_tag, new_p_tag, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated the note text size and margin.")
