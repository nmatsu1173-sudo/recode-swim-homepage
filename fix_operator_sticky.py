import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove position: sticky; and top: 100px; from base .profile-identity
html = html.replace(
"""    .profile-identity {
      flex: 1;
      text-align: center;
      position: sticky;
      top: 100px;
    }""",
"""    .profile-identity {
      flex: 1;
      text-align: center;
    }"""
)

# 2. Add position: sticky; to .profile-identity inside the media query
media_query_target = """    @media (min-width: 768px) {
      .profile-modern-container {
        flex-direction: row;
        align-items: flex-start;
        padding: 4rem;
        gap: 5rem;
      }
    }"""

media_query_replacement = """    @media (min-width: 768px) {
      .profile-modern-container {
        flex-direction: row;
        align-items: flex-start;
        padding: 4rem;
        gap: 5rem;
      }
      .profile-identity {
        position: sticky;
        top: 100px;
      }
    }"""

html = html.replace(media_query_target, media_query_replacement)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed sticky positioning overlapping on mobile.")
