"""Paneles originales y empaquetado del arte anime; no requiere red.

python tools/anime.py --art RUTA  (solo la primera vez)
python tools/anime.py            (regenerar textos y paneles)
"""
from pathlib import Path
import argparse, math, shutil, re, base64
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

def sticker(im,name,box):
    asset=Image.open(OUT/f'stickers/{name}.png').convert('RGBA')
    asset.thumbnail((box[2],box[3]),Image.Resampling.LANCZOS)
    im.paste(asset,(box[0],box[1]),asset)

def tech_icon(key):
    source=ROOT/f'assets/logos/{key}.svg'
    if source.exists():
        match=re.search(r'href="(data:image/svg\+xml;base64,[^"]+)"',source.read_text(encoding='utf-8'))
        if match:return match.group(1)
    source=ROOT/f'assets/logos/tecnologias/{key}.svg'
    if source.exists(): svg=source.read_text(encoding='utf-8')
    else:
        # Símbolos propios para el formato XML y la biblioteca pdf-lib: no
        # representan un logotipo oficial ni se añaden tecnologías nuevas.
        shape='<path d="m8 6-6 6 6 6m8-12 6 6-6 6m-3-14-2 16"/>' if key=='xml' else '<path d="M5 2h9l5 5v15H5zM14 2v6h5M8 13h8M8 17h6"/>'
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#a7caff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{shape}</svg>'
    return 'data:image/svg+xml;base64,'+base64.b64encode(svg.encode()).decode()

def main():
    p=argparse.ArgumentParser(); p.add_argument('--art',type=Path); a=p.parse_args(); OUT.mkdir(parents=True,exist_ok=True)
    if a.art: shutil.copy2(a.art,OUT/'arte-original.png')
    # Empaquetado del atlas: recortes de sus seis celdas, sin retocar el arte.
    atlas=Image.open(OUT/'stickers/atlas-original.png').convert('RGBA')
    sw,sh=atlas.size
    names=['saludo','volando','puerta','dorayaki','laptop','astronauta']
    for i,name in enumerate(names):
        cell=atlas.crop((round(i%3*sw/3),round(i//3*sh/2),round((i%3+1)*sw/3),round((i//3+1)*sh/2)))
        cell.thumbnail((256,256),Image.Resampling.LANCZOS)
        cell.save(OUT/f'stickers/{name}.png',optimize=True)
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
    sticker(im,'saludo',(348,17,60,60)); save(im,'identidad')
    im,d=panel(900,250); pixel(d,'HOLA! SOY AMPI',30,30,4)
    wrap(d,'Me gusta entender una necesidad, darle forma a una idea y colaborar para construir una solución.',(30,91),660,27)
    wrap(d,'Tecnología + personas + creatividad + propósito',(30,185),820,25,BLUE,True)
    sticker(im,'volando',(710,15,155,155));save(im,'hola')
    for name,title,body in [('sobre-mi','Sobre mí','Me encanta aprender, crear y organizar proyectos que conecten personas, ideas y oportunidades.'),('enfoque','Mi enfoque','Desarrollo de soluciones · Gestión de proyectos · Diseño de interfaces · Trabajo en equipo · Impacto social'),('actualmente','Actualmente…','Estudiando Ingeniería de Sistemas e Informática. Participando en JMP PINGUS y construyendo nuevas ideas.')]:
        im,d=panel(440,340)
        pose={'sobre-mi':'dorayaki','enfoque':'puerta','actualmente':'laptop'}[name]
        sticker(im,pose,(23,10,52,52));d.text((89,20),title,font=font(29,True),fill=INK);d.line((26,70,414,70),fill=LINE,width=2)
        wrap(d,body,(26,91),380,25)
        sticker(im,pose,(315,235,105,100))
        if name=='actualmente':
            d.rounded_rectangle((26,289,288,300),5,fill='#1c334f',outline=LINE)
            d.rounded_rectangle((28,291,198,298),3,fill='#86b8f6')
        else:
            star(d,45,290,9,'#ffd37a');star(d,275,285,6,BLUE)
        save(im,name)
    cards=['jmp','ashakids','lifexperience','mirrormind','gamelab','utpliteapp']
    for name in cards:
        # El nombre y la descripción permanecen como HTML legible en móvil.
        im,d=panel(700,340)
        scene=Image.open(OUT/f'proyectos/{name}.webp')
        # Cada tarjeta usa una escena propia; se conserva más altura para
        # reconocer el concepto y evitar recortar al personaje principal.
        im.paste(ImageOps.fit(scene,(668,304)),(16,16))
        save(im,'proyecto-'+name)
    # Tarjeta de frase, sin añadir un sexto proyecto destacado.
    # Proporción vertical ajustada al alto completo de la fila de GAMELAB;
    # la frase inferior forma parte del marco, sin un párrafo suelto debajo.
    im,d=panel(700,780)
    pixel(d,'NEXT ADVENTURE',194,42,4)
    wrap(d,'No se trata de ser el mejor, sino de ser una mejor versión de ti cada día.',(76,119),550,36,INK,True)
    scene=Image.open(OUT/'noche.webp')
    im.paste(ImageOps.fit(scene,(652,190)),(24,496))
    sticker(im,'astronauta',(180,310,320,320))
    for x,y,r in [(46,56,12),(650,73,9),(70,382,12),(622,359,10)]: star(d,x,y,r,'#ffd37a')
    d.text((350,700),'Pequeños pasos,',anchor='mt',font=font(28,True),fill=BLUE)
    d.text((350,736),'nuevas aventuras.',anchor='mt',font=font(28,True),fill=INK)
    save(im,'frase')
    im,d=panel(700,270)
    wrap(d,'Pequeños pasos también te llevan a grandes lugares.',(260,55),380,33,INK,True)
    sticker(im,'astronauta',(28,15,215,215))
    star(d,660,210,11,'#ffd37a');star(d,255,230,6,BLUE)
    save(im,'frase-pasos')
    # Etiquetas locales: colores suaves, tipografía legible y texto accesible.
    badges=OUT/'badges';badges.mkdir(exist_ok=True)
    labels={'html':'HTML','css':'CSS','javascript':'JavaScript','react':'React','typescript':'TypeScript','tailwind':'Tailwind CSS','supabase':'Supabase','postgresql':'PostgreSQL / SQL','pdf-lib':'pdf-lib','figma':'Figma','godot':'Godot','python':'Python','fastapi':'FastAPI','kotlin':'Kotlin','java':'Java','xml':'XML','git':'Git','github':'GitHub'}
    for key,label in labels.items():
        f=font(24); width=round(f.getlength(label))+56
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="44" viewBox="0 0 {width} 44" role="img" aria-label="{label}"><title>{label}</title><rect x="1" y="1" width="{width-2}" height="42" rx="16" fill="#1c334f" stroke="#385b80"/><image x="10" y="10" width="24" height="24" href="{tech_icon(key)}"/><text x="42" y="29" font-family="Segoe UI,Arial,sans-serif" font-size="22" fill="#e3efff">{label}</text></svg>'
        (badges/(key+'.svg')).write_text(svg,encoding='utf-8')
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
