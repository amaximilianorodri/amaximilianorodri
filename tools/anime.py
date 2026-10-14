"""Paneles originales y empaquetado del arte anime; no requiere red.

python tools/anime.py --art RUTA  (solo la primera vez)
python tools/anime.py            (regenerar textos y paneles)
"""
from pathlib import Path
import argparse, math, shutil, base64, re
from PIL import Image, ImageDraw, ImageFont, ImageOps
from arcade import GLYPHS

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/anime'
INK, BLUE, LINE = '#104487', '#008fe5', '#91d9ff'

def font(size, bold=False):
    return ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf' if bold else 'C:/Windows/Fonts/segoeui.ttf', size)

def panel(w,h):
    im=Image.new('RGB',(w,h),'#f4fbff'); d=ImageDraw.Draw(im)
    d.rounded_rectangle((1,1,w-2,h-2),22,fill='#f4fbff',outline=LINE,width=2)
    d.line((22,h-10,w-22,h-10),fill='#d5f2ff',width=2)
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
    d.rounded_rectangle((305,20,895,137),18,fill='#eefaff',outline=LINE,width=2)
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
    cards=[('jmp','01  JMP PINGUS','Prácticas · Desarrollo de inventario','React · TypeScript · Supabase','escritorio'),('ashakids','02  EduKids → ASHAKids','Una idea familiar que creció en equipo','HTML / CSS / JS → React / TS','aventura'),('impacto','03  LifeXperience · MANKA+','Innovación educativa e impacto social','Propuestas y prototipos · Figma','aventura'),('diseno','04  LOOKMI · MirrorMind','Diseño, prototipado y experimentación','Figma · React · TypeScript','escritorio'),('gamelab','05  NeuroEcho · GAMELAB 4.0','Diseño de la propuesta del juego en equipo','Godot · Fork de Threadbare / Endless','noche'),('otros','Otras aventuras','UTPLiteApp · ProyectoHeDe','Kotlin / Java / XML · HTML / CSS / JS','escritorio')]
    for name,title,body,tags,art in cards:
        im,d=panel(700,330); scene=Image.open(OUT/(art+'.webp')); im.paste(ImageOps.fit(scene,(668,150)),(16,16));d=ImageDraw.Draw(im)
        d.text((25,185),title,font=font(30,True),fill=INK)
        d.text((25,232),body,font=font(23),fill=INK)
        d.rounded_rectangle((25,277,650,311),16,fill='#e0f2ff',outline=LINE)
        d.text((39,280),tags,font=font(21),fill=INK);save(im,'proyecto-'+name)
    # Cuadrícula de iconos: reutiliza los logotipos locales y sus créditos.
    items=['javascript','typescript','react','html','css','supabase','git','github','figma','godot']
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="700" height="285" viewBox="0 0 700 285"><rect x="1" y="1" width="698" height="283" rx="22" fill="#f4fbff" stroke="#91d9ff"/><text x="25" y="42" fill="#104487" font-family="Segoe UI,Arial,sans-serif" font-size="26" font-weight="bold">Mi caja de herramientas</text>']
    for i,item in enumerate(items):
        source=(ROOT/f'assets/logos/{item}.svg').read_text(encoding='utf-8')
        icon=re.search(r'href="(data:image/svg\+xml;base64,[^"]+)"',source).group(1)
        x=22+(i%5)*136;y=64+(i//5)*104
        svg.append(f'<rect x="{x}" y="{y}" width="116" height="92" rx="12" fill="white"/><image x="{x+39}" y="{y+10}" width="38" height="38" href="{icon}"/><text x="{x+58}" y="{y+73}" text-anchor="middle" fill="#104487" font-family="Segoe UI,Arial,sans-serif" font-size="17">{item if item in ["HTML","CSS"] else {"javascript":"JavaScript","typescript":"TypeScript","html":"HTML","css":"CSS","github":"GitHub","supabase":"Supabase"}.get(item,item.capitalize())}</text>')
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
