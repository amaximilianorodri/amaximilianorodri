"""Paneles originales y empaquetado del arte anime; no requiere red.

python tools/anime.py --art RUTA  (solo la primera vez)
python tools/anime.py            (regenerar textos y paneles)
"""
from pathlib import Path
import argparse, math, shutil, re
from PIL import Image, ImageDraw, ImageFont, ImageOps
from arcade import GLYPHS

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/anime'
INK, BLUE, LINE = '#e3efff', '#85d0ff', '#304d72'
BG, SURFACE, MUTED = '#0d1117', '#132238', '#b4c9e3'

def font(size, bold=False):
    return ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf' if bold else 'C:/Windows/Fonts/segoeui.ttf', size)

def panel(w,h):
    im=Image.new('RGB',(w,h),BG); d=ImageDraw.Draw(im)
    d.rounded_rectangle((1,1,w-2,h-2),22,fill=SURFACE,outline=LINE,width=2)
    d.line((22,h-10,w-22,h-10),fill='#1c3552',width=2)
    return im,d

def pixel(d,text,x,y,s=5):
    for char in text.upper():
        for row,line in enumerate(GLYPHS.get(char,GLYPHS[' ']).split('/')):
            for col,v in enumerate(line):
                if v=='1': d.rectangle((x+col*s,y+row*s,x+(col+1)*s-1,y+(row+1)*s-1),fill=INK)
        x+=6*s

def star(d,x,y,r,color):
    d.polygon([(x,y-r),(x+r*.3,y-r*.3),(x+r,y),(x+r*.3,y+r*.3),(x,y+r),(x-r*.3,y+r*.3),(x-r,y),(x-r*.3,y-r*.3)],fill=color)

def wrap(d,text,xy,width,size=23,color=INK,bold=False):
    x,y=xy; f=font(size,bold); line=''
    for word in text.split():
        candidate=(line+' '+word).strip()
        if d.textlength(candidate,font=f)>width and line:
            d.text((x,y),line,font=f,fill=color); y+=size+9; line=word
        else: line=candidate
    if line: d.text((x,y),line,font=f,fill=color); y+=size+9
    return y

def save(im,name): im.save(OUT/(name+'.png'),optimize=True)

def main():
    p=argparse.ArgumentParser(); p.add_argument('--art',type=Path); a=p.parse_args(); OUT.mkdir(parents=True,exist_ok=True)
    if a.art: shutil.copy2(a.art,OUT/'arte-original.png')
    sheet=Image.open(OUT/'arte-original.png').convert('RGB'); w,h=sheet.size
    # Extraer las tres franjas solicitadas sin alterar el contenido artístico.
    for name,top,bottom in [('escritorio',0,.3223),('aventura',.3262,.666),('noche',.671,1)]:
        ImageOps.fit(sheet.crop((0,round(h*top),w,round(h*bottom))),(1200,270)).save(OUT/(name+'.webp'),quality=88)
    im=Image.open(OUT/'escritorio.webp').convert('RGB'); d=ImageDraw.Draw(im)
    d.rounded_rectangle((305,20,895,137),18,fill=SURFACE,outline=LINE,width=2)
    pixel(d,'AMPI.EXE',330,34,4)
    wrap(d,'Un futuro mejor también se construye con pequeñas ideas',(330,78),535,22,bold=True)
    save(im,'banner')
    im,d=panel(420,450); pixel(d,'AMPI.EXE',28,28,5)
    y=wrap(d,'Ideas del futuro, soluciones de hoy.',(28,92),355,28,bold=True)
    y=wrap(d,'Estudiante de Ingeniería de Sistemas e Informática',(28,y+16),355,24)
    y=wrap(d,'Desarrollo · Gestión · Diseño · Innovación · Impacto social',(28,y+18),355,23)
    d.line((28,y+13,390,y+13),fill=LINE,width=2)
    wrap(d,'¡Hola! Gracias por estar aquí',(28,y+30),350,24,BLUE)
    star(d,375,50,15,'#ffc94e'); save(im,'identidad')
    im,d=panel(900,250); pixel(d,'HOLA! SOY AMPI',30,30,4)
    wrap(d,'Me gusta entender una necesidad, darle forma a una idea y colaborar para construir una solución.',(30,91),800,27)
    wrap(d,'Tecnología + personas + creatividad + propósito',(30,185),820,25,BLUE,True); save(im,'hola')
    for name,title,body in [('sobre-mi','Sobre mí','Me encanta aprender, crear y organizar proyectos que conecten personas, ideas y oportunidades.'),('enfoque','Mi enfoque','Desarrollo de soluciones · Gestión de proyectos · Diseño de interfaces · Trabajo en equipo · Impacto social'),('actualmente','Actualmente…','Estudiando Ingeniería de Sistemas e Informática. Participando en JMP PINGUS y construyendo nuevas ideas.')]:
        im,d=panel(440,285); d.text((26,20),title,font=font(29,True),fill=INK);d.line((26,66,414,66),fill=LINE,width=2)
        wrap(d,body,(26,87),380,25); star(d,398,250,12,BLUE);save(im,name)
    cards=[('jmp','01  JMP PINGUS','Prácticas · Inventario y procesos','escritorio'),('ashakids','02  EduKids → ASHAKids','Una idea familiar que creció en equipo','aventura'),('lifexperience','03  LifeXperience','Practica la vida antes de vivirla','aventura'),('mirrormind','04  MirrorMind','Interfaces, diseño y experimentación','escritorio'),('gamelab','05  GAMELAB 4.0','NeuroEcho · Una aventura en equipo','noche'),('utpliteapp','UTPLiteApp','Desarrollo colaborativo · Android','escritorio')]
    for name,title,body,art in cards:
        # El nombre y la descripción permanecen como HTML legible en móvil.
        im,d=panel(700,185); scene=Image.open(OUT/(art+'.webp')); im.paste(ImageOps.fit(scene,(668,150)),(16,16))
        save(im,'proyecto-'+name)
    # Tarjeta de frase, sin añadir un sexto proyecto destacado.
    im,d=panel(700,285)
    pixel(d,'NEXT ADVENTURE',35,30,3)
    wrap(d,'No se trata de ser el mejor, sino de ser una mejor versión de ti cada día.',(35,89),560,32,INK,True)
    d.rounded_rectangle((619,171,665,260),5,fill='#c77eae',outline='#f0bad9',width=2)
    d.rectangle((627,181,657,250),outline='#f0bad9',width=2)
    for x,y,r in [(600,48,12),(565,244,9),(42,247,8)]: star(d,x,y,r,'#ffd37a')
    save(im,'frase')
    # Etiquetas locales: colores suaves, tipografía legible y texto accesible.
    badges=OUT/'badges';badges.mkdir(exist_ok=True)
    labels={'html':'HTML','css':'CSS','javascript':'JavaScript','react':'React','typescript':'TypeScript','tailwind':'Tailwind CSS','supabase':'Supabase','postgresql':'PostgreSQL / SQL','pdf-lib':'pdf-lib','figma':'Figma','godot':'Godot','python':'Python','fastapi':'FastAPI','kotlin':'Kotlin','java':'Java','xml':'XML','git':'Git','github':'GitHub'}
    for key,label in labels.items():
        f=font(24); width=round(f.getlength(label))+56
        badge=Image.new('RGB',(width,44),BG); bd=ImageDraw.Draw(badge)
        bd.rounded_rectangle((1,1,width-2,42),16,fill='#1c334f',outline='#385b80')
        bd.ellipse((13,18,21,26),fill='#f5abc9' if key in ['figma','css','fastapi'] else BLUE)
        bd.text((31,5),label,font=f,fill=INK)
        badge.save(badges/(key+'.png'),optimize=True)
    # Cuadrícula de iconos: reutiliza los logotipos locales y sus créditos.
    items=['javascript','typescript','react','html','css','supabase','git','github','figma','godot']
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="700" height="285" viewBox="0 0 700 285"><rect x="1" y="1" width="698" height="283" rx="22" fill="#132238" stroke="#304d72"/><text x="25" y="42" fill="#e3efff" font-family="Segoe UI,Arial,sans-serif" font-size="26" font-weight="bold">Mi caja de herramientas</text>']
    for i,item in enumerate(items):
        source=(ROOT/f'assets/logos/{item}.svg').read_text(encoding='utf-8')
        icon=re.search(r'href="(data:image/svg\+xml;base64,[^"]+)"',source).group(1)
        x=22+(i%5)*136;y=64+(i//5)*104
        svg.append(f'<rect x="{x}" y="{y}" width="116" height="92" rx="12" fill="#1c334f"/><image x="{x+39}" y="{y+10}" width="38" height="38" href="{icon}"/><text x="{x+58}" y="{y+73}" text-anchor="middle" fill="#e3efff" font-family="Segoe UI,Arial,sans-serif" font-size="17">{item if item in ["HTML","CSS"] else {"javascript":"JavaScript","typescript":"TypeScript","html":"HTML","css":"CSS","github":"GitHub","supabase":"Supabase"}.get(item,item.capitalize())}</text>')
    (OUT/'herramientas.svg').write_text(''.join(svg)+'</svg>',encoding='utf-8')
    # Animación de interfaz original: estrellas y puerta, finita y ligera.
    frames=[]
    for i in range(24):
        im,d=panel(900,85);d.line((26,43,820,43),fill=LINE,width=2)
        d.rounded_rectangle((830,10,869,75),4,fill='#f599ce',outline='#bd5eac',width=3)
        d.rectangle((837,18,862,68),outline='#ffdcf0',width=2);d.ellipse((855,43,859,47),fill='#ffc94e')
        for j in range(9): star(d,45+j*88,43+round(5*math.sin(i/24*math.tau+j)),5+2*math.sin(i/24*math.tau+j),'#008fe5' if j%2 else '#ffc94e')
        frames.append(im.quantize(colors=32))
    frames[-1].convert('RGB').save(OUT/'separador.png',optimize=True)
    frames[0].save(OUT/'separador.gif',save_all=True,append_images=frames[1:],duration=125,optimize=True,disposal=2)

if __name__=='__main__': main()
