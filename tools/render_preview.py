"""Render the repository Markdown as a local, GitHub-like reading preview."""
import html
import os
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import mistune
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'preview'
NAV = [('index.html','Overview'),('docs/section-summaries.html','Section summaries'),
       ('PAPERS.html','Paper library'),('docs/datasets-and-evaluation.html','Datasets & evaluation')]

class GitHubRenderer(mistune.Renderer):
    def block_html(self, value):
        fragment = BeautifulSoup(value, 'html.parser')
        containers = fragment.find_all(['div', 'details'])
        for container in reversed(containers):
            rendered = mistune.markdown(container.decode_contents(), escape=False)
            container.clear()
            for node in list(BeautifulSoup(rendered, 'html.parser').contents):
                container.append(node.extract())
        return str(fragment)

def output_path(source):
    relative = source.relative_to(ROOT)
    return OUT/'index.html' if str(relative)=='README.md' else OUT/relative.with_suffix('.html')

def relative_url(target, output):
    return Path(os.path.relpath(target,output.parent)).as_posix()

def render(source):
    output=output_path(source)
    document=mistune.Markdown(renderer=GitHubRenderer(escape=False))(source.read_text(encoding='utf-8'))
    soup=BeautifulSoup(document,'html.parser')
    slug_counts={}
    for heading in soup.find_all(re.compile('^h[1-6]$')):
        slug=re.sub(r'[^\w\- ]','',heading.get_text().lower()).replace(' ','-')
        n=slug_counts.get(slug,0)
        slug_counts[slug]=n+1
        heading['id']=slug+(f'-{n}' if n else '')
    for element in soup.find_all(['a','img']):
        attr='href' if element.name=='a' else 'src'
        value=element.get(attr,'')
        parsed=urlsplit(value)
        if not value or parsed.scheme or parsed.netloc or not parsed.path:
            continue
        target=(source.parent/unquote(parsed.path)).resolve()
        if not target.is_relative_to(ROOT):
            continue
        target=output_path(target) if target.suffix=='.md' else target
        element[attr]=relative_url(target,output)+(('#'+parsed.fragment) if parsed.fragment else '')
    for table in list(soup.find_all('table')):
        wrapper=soup.new_tag('div',attrs={'class':'table-scroll','tabindex':'0'})
        table.wrap(wrapper)
    title=soup.h1.get_text(' ',strip=True) if soup.h1 else source.stem
    nav=''.join(f'<a href="{relative_url(OUT/path,output)}"'+(' aria-current="page"' if OUT/path==output else '')+f'>{label}</a>' for path,label in NAV)
    css=relative_url(OUT/'preview.css',output)
    content=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} | Building Reconstruction Survey</title><link rel="stylesheet" href="{css}"></head>
<body><header class="site-header"><div class="site-title">Building Reconstruction Survey <span class="private-label">Private preview</span></div>
<nav aria-label="Repository pages">{nav}</nav></header>
<main><div class="file-label">{html.escape(source.relative_to(ROOT).as_posix())}</div><article class="markdown-body">{soup}</article></main>
<footer>Research companion · PE&amp;RS · Download links supplied by the maintainer</footer></body></html>'''
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(content,encoding='utf-8')
    return output

if __name__=='__main__':
    sources=[ROOT/'README.md',ROOT/'PAPERS.md',*sorted((ROOT/'docs').glob('*.md')),
             ROOT/'assets/README.md',ROOT/'data/README.md']
    for source in sources:
        print(render(source).relative_to(ROOT))
