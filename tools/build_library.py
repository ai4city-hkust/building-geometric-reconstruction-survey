"""Regenerate the reading library from the catalog and verified official paper URLs."""
import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = [
    ('background', 'Background and Related Surveys', 'Foundational geometry, related reviews, and urban-modeling context.'),
    ('footprints', '2D Building Footprints', 'Image-based polygon prediction, point-cloud boundary recovery, and regularization.'),
    ('roofs', '2.5D Roof Structure and Wireframes', 'Roof topology, plane and height inference, structural parsing, and learning from points.'),
    ('models', '3D Building Models', 'Photogrammetry, primitive assembly, mesh generation, and structured abstraction.'),
    ('fusion', 'Image-LiDAR Fusion', 'Complementary appearance and metric geometry for building reconstruction.'),
    ('datasets', 'Datasets and Supporting Benchmarks', 'Resources for structured geometry, multimodal semantics, and building instances.'),
    ('outlook', 'Foundation Models and Dynamic Urban Analysis', 'Vision-language models, neural representations, change detection, and future workflows.'),
]

def escape(value):
    return str(value).replace('|','\\|').replace('\n',' ')

def main():
    refs = json.loads((ROOT/'data/references.json').read_text(encoding='utf-8'))
    links = json.loads((ROOT/'data/paper-links.json').read_text(encoding='utf-8'))
    ids = {ref['id'] for ref in refs}
    if set(links) != ids:
        raise ValueError('Paper-link manifest must contain exactly the catalog reference IDs.')
    for key,url in links.items():
        if not url or urlsplit(url).scheme not in {'https','http'} or not urlsplit(url).netloc:
            raise ValueError(f'{key}: enter a verified full HTTP(S) official paper address.')
    ready = sum(bool(url) for url in links.values())
    lines = ['# Paper Library', '', '[Home](README.md) · [Section summaries](docs/section-summaries.md) · [Datasets & evaluation](docs/datasets-and-evaluation.md)', '',
             f'**{len(refs)} bibliography entries · 7 reading collections · {ready} official paper links**', '',
             'The full bibliography of the supplied survey and maintainer-supplied additions are preserved here. Collections are organized for reading; a study may be relevant to more than one chapter.', '',
             '> **Official sources:** links lead to publisher or conference pages, official preprint records, or university repositories. Full-text access depends on the source; a paper link does not imply a free PDF download.', '',
             '| Collection | Entries |', '| :--- | ---: |']
    for key,title,_ in COLLECTIONS:
        lines.append(f'| [{title}](#{key}) | {sum(r["collection"]==key for r in refs)} |')
    for key,title,description in COLLECTIONS:
        lines += ['',f'<a id="{key}"></a>',f'## {title}', '',description,'',
                  '| ID / Year | Paper | Official Link |', '| :--- | :--- | :---: |']
        for ref in sorted((r for r in refs if r['collection']==key),key=lambda r:(-int(r['year'][:4]),r['id'])):
            identifier=ref['id']
            url=links[identifier].replace(' ','%20').replace('(','%28').replace(')','%29')
            link=f'[Official source]({url})'
            detail=f'**[{escape(ref["title"])}]({url})**<br>{escape(ref["authors"])}<br><sub>{escape(ref["venue"])}</sub>'
            if ref.get('editorial_note'):
                detail+=f'<br><sub>Note: {escape(ref["editorial_note"])}</sub>'
            lines.append(f'| <a id="{identifier.lower()}"></a>**{identifier}**<br>{ref["year"]} | {detail} | {link} |')
    lines += ['', '---', '', 'Reference IDs are stable: original PDF entries keep their source order, and later additions are appended. Source citations, available PDF page numbers, and citation locations for additions are retained in [the reference catalog](data/references.json). Bibliographic details needing review are recorded in [editorial notes](docs/editorial-notes.md).', '']
    (ROOT/'PAPERS.md').write_text('\n'.join(lines),encoding='utf-8')
    print(f'Built PAPERS.md: {len(refs)} references, {ready} official paper links.')

if __name__=='__main__':
    main()
