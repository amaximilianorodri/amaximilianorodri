"""Descarga únicamente los logotipos que faltaban, de sus repositorios fuente."""
from pathlib import Path
import urllib.request,json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/logos/tecnologias'
SOURCES={
 'tailwind':('tailwindcss','#38BDF8'),
 'postgresql':('postgresql','#7DB5DE'),
 'python':('python','#75B8EA'),
 'fastapi':('fastapi','#3ED6BE'),
 'kotlin':('kotlin','#BA8BFF'),
}

def main():
    OUT.mkdir(parents=True,exist_ok=True); manifest={}
    for name,(slug,color) in SOURCES.items():
        url=f'https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/{slug}.svg'
        req=urllib.request.Request(url,headers={'User-Agent':'AMPI-profile-icons'})
        with urllib.request.urlopen(req,timeout=30) as r: svg=r.read().decode()
        svg=svg.replace('<svg ','<svg fill="'+color+'" ',1)
        (OUT/(name+'.svg')).write_text(svg,encoding='utf-8');manifest[name]={'source':url,'collection':'Simple Icons, CC0-1.0; marcas de sus titulares'}
    url='https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg'
    with urllib.request.urlopen(url,timeout=30) as r: svg=r.read().decode()
    (OUT/'java.svg').write_text(svg,encoding='utf-8');manifest['java']={'source':url,'collection':'Devicon, MIT; marca de su titular'}
    for name,url in [('LICENSE-DEVICON.txt','https://raw.githubusercontent.com/devicons/devicon/master/LICENSE'),('LICENSE-SIMPLE-ICONS.txt','https://raw.githubusercontent.com/simple-icons/simple-icons/develop/LICENSE.md')]:
        with urllib.request.urlopen(url,timeout=30) as r: license_text=r.read().decode()
        (OUT/name).write_text(license_text,encoding='utf-8')
    (OUT/'fuentes.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Se guardaron seis logotipos y su procedencia en assets/logos/tecnologias/.')

if __name__=='__main__':main()
