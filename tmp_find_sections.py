import re

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all section tags and their IDs
sections = re.findall(r'<section[^>]*>', html, re.IGNORECASE)
for sec in sections:
    print(sec)
