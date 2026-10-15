"""Botones locales del encabezado, compatibles con GitHub Markdown."""
from pathlib import Path
from html import escape
import re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/anime'

def button(name,brand,action,color,icon):
    title=escape(f'{brand} · {action}')
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="590" height="76" viewBox="0 0 590 76" role="img" aria-label="{title}">
<title>{title}</title>
<rect x="1" y="1" width="588" height="74" rx="9" fill="#303945" stroke="{color}" stroke-width="2"/>
<path d="M213 2H580a8 8 0 0 1 8 8v56a8 8 0 0 1-8 8H213Z" fill="{color}"/>
{icon}
<g fill="#f2f7ff" font-family="Consolas,monospace" font-weight="bold" font-size="23" letter-spacing="2">
<text x="62" y="46">{brand}</text><text x="400" y="46" text-anchor="middle">{action}</text>
</g></svg>'''
    (OUT/f'barra-{name}.svg').write_text(svg,encoding='utf-8')

def main():
    source=(ROOT/'assets/logos/github.svg').read_text(encoding='utf-8')
    github=re.search(r'href="(data:image/svg\+xml;base64,[^"]+)"',source).group(1)
    button('linkedin','LINKEDIN','CONECTEMOS','#008cac','<rect x="19" y="24" width="27" height="27" rx="3" fill="#f2f7ff"/><text x="22" y="46" fill="#303945" font-family="Arial,sans-serif" font-size="23" font-weight="bold">in</text>')
    button('github','GITHUB','MIS PROYECTOS','#7544d9',f'<image x="19" y="24" width="27" height="27" href="{github}"/>')

if __name__=='__main__':main()
