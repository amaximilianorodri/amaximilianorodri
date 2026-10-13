"""Instantáneas públicas de GitHub, sin guardar tokens, correos ni datos privados.

Python estándar. Ejecutar: python tools/actualizar_actividad.py --date AAAA-MM-DD
Usa opcionalmente el gestor de credenciales Git ya configurado, sin interacción.
Los gráficos son instantáneas fechadas; no suman actividad de equipos como propia.
"""
from pathlib import Path
from html.parser import HTMLParser
from html import escape
from datetime import date
import argparse
import json
import os
import re
import subprocess
import urllib.request
import urllib.error

ROOT = Path(__file__).resolve().parents[1]
USER = 'amaximilianorodri'
COLLAB = ['sromansilva/ashakids-platform','luisteransaucedo18-coder/JMP-PINGUS-INVENTARIO','sromansilva/UTPLiteApp','Game-Lab-4-0-UTP-Group-7-Team-2/threadbare','j3zkills/ProyectoHeDe','sromansilva/utp-lite-react']


def headers():
    h = {'User-Agent':'profile-public-snapshot'}
    try:
        env = dict(os.environ, GIT_TERMINAL_PROMPT='0', GCM_INTERACTIVE='never')
        p = subprocess.run(['git','credential','fill'], input='protocol=https\nhost=github.com\n\n', text=True, capture_output=True, timeout=15, env=env)
        values = dict(line.split('=',1) for line in p.stdout.splitlines() if '=' in line)
        if p.returncode == 0 and values.get('password'):
            h['Authorization'] = 'Bearer '+values['password']
    except (OSError, subprocess.TimeoutExpired):
        pass
    return h


class Calendar(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cells, self.tips, self.current, self.content = {}, {}, None, ''

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'td' and a.get('data-date'):
            self.cells[a['id']] = {'date':a['data-date'],'level':int(a['data-level'])}
        if tag == 'tool-tip':
            self.current, self.content = a.get('for'), ''

    def handle_data(self, text):
        if self.current:
            self.content += text

    def handle_endtag(self, tag):
        if tag == 'tool-tip' and self.current:
            m = re.search(r'([\d,]+) contributions?', self.content)
            self.tips[self.current] = int(m.group(1).replace(',','')) if m else 0 if 'No contributions' in self.content else None
            self.current = None


def svg_start(title, height=170):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><rect width="960" height="{height}" rx="14" fill="#110D21"/><rect x="1" y="1" width="958" height="{height-2}" rx="14" fill="none" stroke="#41305F"/><g font-family="Segoe UI,Arial,sans-serif">'


def text(x,y,s,size=14,color='#DAD4EB'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}">{escape(str(s))}</text>'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', default=date.today().isoformat())
    args = parser.parse_args()
    cutoff = date.fromisoformat(args.date)
    h = headers()

    def api(path):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request('https://api.github.com/'+path,headers=h),timeout=25))
        except urllib.error.HTTPError as e:
            return {'unavailable_http':e.code}

    owned = api('users/'+USER+'/repos?type=owner&per_page=100')
    if not isinstance(owned,list):
        raise RuntimeError('No se pudo leer el catálogo público; se conserva la instantánea anterior.')
    repos, languages = [], {}
    for r in owned:
        if r['private']:
            continue
        repos.append({k:r[k] for k in ['full_name','html_url','fork','default_branch','stargazers_count','size','pushed_at']})
        if r['fork']:
            continue
        ls = api('repos/'+r['full_name']+'/languages')
        if 'unavailable_http' in ls:
            raise RuntimeError('Fallo en lenguajes; no se reemplaza por datos vacíos.')
        for lang, count in ls.items():
            languages[lang] = languages.get(lang,0)+count
    calendars = {}
    for year in [cutoff.year-1,cutoff.year]:
        url = f'https://github.com/users/{USER}/contributions?from={year}-01-01&to={year}-12-31'
        raw = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'profile-public-snapshot'}),timeout=25).read().decode()
        cal = Calendar();cal.feed(raw)
        m = re.search(r'([\d,]+)\s+contributions?\s+in',raw)
        if not m or not cal.cells:
            raise RuntimeError('El formato público del calendario cambió; requiere revisión.')
        days=[]
        for identifier, value in sorted(cal.cells.items(),key=lambda i:i[1]['date']):
            if not value['date'].startswith(str(year)):
                raise RuntimeError('El calendario devuelto no corresponde al año solicitado.')
            if cal.tips.get(identifier) is None:
                raise RuntimeError('Falta un conteo oficial de día; no se estima desde el color.')
            days.append(dict(value,count=cal.tips[identifier]))
        total=int(m.group(1).replace(',',''))
        if sum(d['count'] for d in days)!=total:
            raise RuntimeError('El total de GitHub no coincide con los días; requiere revisión.')
        calendars[str(year)]={'total':total,'source':url,'days':days,'scope':'calendario público anual de GitHub'}
    collab=[]
    for name in COLLAB:
        r=api('repos/'+name)
        if r.get('private') or 'unavailable_http' in r:
            continue
        collab.append({k:r[k] for k in ['full_name','html_url','fork','default_branch']})
    samples=[]
    for name,sha in [('sromansilva/ashakids-platform','5dacd55'),('luisteransaucedo18-coder/JMP-PINGUS-INVENTARIO','b316269'),('luisteransaucedo18-coder/JMP-PINGUS-INVENTARIO','128070e'),('luisteransaucedo18-coder/JMP-PINGUS-INVENTARIO','d5b2363'),('sromansilva/UTPLiteApp','d2b4dc3')]:
        c=api('repos/'+name+'/commits/'+sha)
        samples.append({'repository':name,'sha':sha,'associated_account':(c.get('author') or {}).get('login'),'author_date':c.get('commit',{}).get('author',{}).get('date'),'committer_date':c.get('commit',{}).get('committer',{}).get('date')})
    compare=api('repos/sromansilva/ashakids-platform/compare/main...5dacd55')
    snapshot={'updated':args.date,'user':USER,'owned_public_repositories':repos,'languages_bytes_owned_nonfork':languages,'calendars':calendars,'collaborative_repositories_reviewed':collab,'attribution_samples':samples,'ashakids_landing_vs_main':{k:compare.get(k) for k in ['status','ahead_by','behind_by']}}
    target=ROOT/'assets/actividad';target.mkdir(exist_ok=True)
    (target/'datos.json').write_text(json.dumps(snapshot,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for year,cal in calendars.items():
        svg=svg_start(f'Calendario público oficial {year}: {cal["total"]} contribuciones. Instantánea del {args.date}',200)
        svg+=text(24,32,'CONTRIBUTION MAP / '+year,22,'#55ECF4')+text(24,58,f'{cal["total"]} contribuciones oficiales del año · captura {args.date}')
        start=date(int(year),1,1);offset=(start.weekday()+1)%7
        for i,d in enumerate(cal['days']):
            col,row=divmod(i+offset,7);color=['#221A34','#43305D','#694290','#BA4CCA','#F74FB8'][d['level']]
            if d['date']>args.date:
                color='#171223'
            svg+=f'<rect x="{24+col*17}" y="{76+row*13}" width="12" height="9" rx="2" fill="{color}"><title>{d["date"]}: {d["count"]} contribuciones</title></rect>'
        svg+=text(24,184,'Fuente: calendario público de GitHub. No incluye toda la actividad demostrable.')+'</g></svg>\n'
        (target/f'calendario-{year}.svg').write_text(svg,encoding='utf-8')
    top=sorted(languages.items(),key=lambda i:i[1],reverse=True)[:6];height=95+len(top)*29
    svg=svg_start('Lenguajes por bytes en repositorios públicos propios, sin forks; no mide dominio personal',height)
    svg+=text(24,34,'REPOSITORY LANGUAGES',22,'#55ECF4')+text(24,58,'Bytes de código en repositorios propios públicos, sin forks. No mide dominio.')
    maximum=max(languages.values(),default=1)
    for i,(lang,count) in enumerate(top):
        y=85+i*29
        svg+=text(24,y,lang)+f'<rect x="155" y="{y-12}" width="{max(1,int(count/maximum*570))}" height="12" rx="3" fill="#B86AF1"/>'+text(750,y,f'{count:,} bytes')
    svg+='</g></svg>\n';(target/'lenguajes.svg').write_text(svg,encoding='utf-8')
    svg=svg_start('Repositorios propios públicos y sus estrellas; no es un nivel profesional',120)
    svg+=text(24,32,'PLAYER STATS / CATÁLOGO PÚBLICO',22,'#55ECF4')
    svg+=text(24,73,f'{len(repos)} repositorios propios públicos',23)+text(495,73,f'{sum(r["stargazers_count"] for r in repos)} estrellas en esos repositorios',21)
    svg+=text(24,103,'Instantánea '+args.date+' · No suma commits ni estrellas de equipos como propios.')+'</g></svg>\n'
    (target/'resumen.svg').write_text(svg,encoding='utf-8')
    print(json.dumps({'updated':args.date,'owned_public':len(repos),'calendars':{y:c['total'] for y,c in calendars.items()},'ashakids_vs_main':snapshot['ashakids_landing_vs_main']},ensure_ascii=False))


if __name__=='__main__':
    main()
