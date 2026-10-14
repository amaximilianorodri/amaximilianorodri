"""Valida rutas/animación y prepara una vista previa con el renderizador de GitHub."""
from pathlib import Path
from html import unescape
import json,re,urllib.request,subprocess,hashlib
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
text=(ROOT/'README.md').read_text(encoding='utf-8')
refs=re.findall(r'(?:src|srcset|href)="([^"]+)"|\]\(([^)]+)\)',text)
local=[]; external=[]
for pair in refs:
    link=unescape(next(x for x in pair if x))
    if link.startswith(('http:','https:')): external.append(link)
    elif not link.startswith('#'): local.append(link)
missing=[x for x in local if not (ROOT/x.split('#')[0]).is_file()]
assert not missing,missing
assert 'calendario-202' not in text
assert 'assets/cyberpunk/' not in text
# Los enlaces de casos retirados de la portada se conservan en la documentación.
assert all(s not in text for s in ['LOOKMI','MANKA+','Historias, créditos y evidencia','Relacionar tecnologías con la evidencia'])
project_order=re.findall(r'alt="(0[1-5] · [^"]+)"',text)
assert project_order==['01 · JMP PINGUS','02 · EduKids → ASHAKids','03 · LifeXperience','04 · MirrorMind','05 · GAMELAB 4.0'],project_order
assert not subprocess.check_output(['git','diff','--','assets/actividad'],cwd=ROOT).strip()
card_names=['jmp','ashakids','lifexperience','mirrormind','gamelab','utpliteapp']
card_hashes=[hashlib.sha256(Image.open(ROOT/f'assets/anime/proyecto-{name}.png').convert('RGB').tobytes()).hexdigest() for name in card_names]
assert len(set(card_hashes))==6,'Las seis tarjetas deben tener ilustraciones distintas.'
lab_path=ROOT/'assets/anime/animaciones/laboratorio.gif'
lab=Image.open(lab_path); lab_loop=lab.info.get('loop')
lab_frames=[];lab_duration=0
for i in range(lab.n_frames):
    lab.seek(i);lab_duration+=lab.info.get('duration',0);lab_frames.append(hashlib.sha256(lab.convert('RGB').tobytes()).hexdigest())
assert len(set(lab_frames))>1 and lab_loop==0
assert lab_path.stat().st_size<1_000_000
assert (ROOT/'assets/anime/animaciones/laboratorio.png').is_file()
print(json.dumps({'ilustraciones_distintas':len(set(card_hashes)),'laboratorio_bytes':lab_path.stat().st_size,'laboratorio_fotogramas':lab.n_frames,'laboratorio_duracion_ms':lab_duration,'laboratorio_repeticion':'continua'},ensure_ascii=False))
gif=Image.open(ROOT/'assets/anime/separador.gif')
frames=[]; duration=0
for i in range(gif.n_frames):
    gif.seek(i); duration+=gif.info.get('duration',0); frames.append(gif.convert('RGB').tobytes())
assert len(set(frames))>1
assert (ROOT/'assets/anime/separador.gif').stat().st_size<500_000
print(json.dumps({'rutas_locales':len(local),'faltantes':missing,'GIF_bytes':(ROOT/'assets/anime/separador.gif').stat().st_size,'fotogramas':gif.n_frames,'duracion_ms':duration,'repeticion':gif.info.get('loop','sin repetición'),'enlaces_externos_conservados':len(set(external))},ensure_ascii=False))
payload=json.dumps({'text':text,'mode':'gfm','context':'amaximilianorodri/amaximilianorodri'}).encode()
req=urllib.request.Request('https://api.github.com/markdown',data=payload,headers={'Content-Type':'application/json','User-Agent':'AMPI-README-preview'})
with urllib.request.urlopen(req,timeout=40) as r: rendered=r.read().decode()
# GitHub prefija las anclas explícitas al sanear HTML y su página resuelve los
# enlaces sin prefijo. En el visor local conservar el prefijo como nombre y
# añadir el id original reproduce esa navegación sin JavaScript.
rendered=re.sub(r'name="user-content-([^"]+)"',lambda m:m.group(0)+' id="'+m.group(1)+'"',rendered)
preview=ROOT/'preview';preview.mkdir(exist_ok=True)
css='''body{margin:0;background:#fff;color:#1f2328;font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}article{max-width:980px;margin:0 auto;padding:28px}a{color:#0969da;text-decoration:none}a:hover{text-decoration:underline}img{max-width:100%;height:auto;vertical-align:middle}table{width:100%;border-spacing:0;border-collapse:collapse;margin:16px 0;table-layout:fixed}td{padding:12px;border:1px solid #d1d9e0;overflow-wrap:anywhere}h2{font-size:24px;border-bottom:1px solid #d1d9e0;padding-bottom:8px;margin-top:28px}h3{font-size:20px}details{padding:8px 0}summary{cursor:pointer}p{margin:16px 0}picture{display:block}code{background:#eff1f3;padding:2px 4px;border-radius:4px}.dark{background:#0d1117;color:#f0f6fc}.dark a{color:#4493f8}.dark td,.dark h2{border-color:#3d444d}.dark code{background:#252a30}@media(max-width:500px){article{padding:12px}td{padding:7px;font-size:13px}h2{font-size:22px}}'''
(preview/'README.html').write_text('<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><base href="../"><title>AMPI.EXE · Vista previa README</title><style>'+css+'</style><body class="dark"><article class="markdown-body">'+rendered+'</article></body></html>',encoding='utf-8')
print('Vista previa: preview/README.html (HTML renderizado por GitHub, estilos locales aproximados).')
