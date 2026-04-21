import re, json
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texts = []
    def handle_data(self, data):
        c = data.strip()
        if c and re.search(r'[\u0590-\u05FF]', c):
            self.texts.append(c)

with open('all_content.md', 'w', encoding='utf-8') as out:
    for f in ['public/index.html', 'public/services/automations.html', 'public/services/crm-systems.html', 'public/services/landing-pages.html', 'public/services/training.html']:
        out.write(f'# {f}\n')
        p = P()
        with open(f, 'r', encoding='utf-8') as html:
            p.feed(html.read())
        for text in p.texts:
            out.write(f'- {text}\n')
