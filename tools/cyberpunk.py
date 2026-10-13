"""HUD, paneles y GIF propios; conserva los recursos arcade de versiones anteriores."""
from pathlib import Path
from PIL import Image
from arcade import Canvas
import math

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/cyberpunk'
BG, INK, CYAN, PINK, YELLOW = '#100C20','#DED8EE','#55ECF4','#F74FB8','#FFC83C'


def panel(w,h,title):
    c=Canvas(w,h,title,bg=BG)
    c.rect(0,0,w,1,'#403052');c.rect(0,h-1,w,1,'#403052')
    return c


def header(t=1):
    c=panel(600,70,'AMPI.EXE · Estudiante de Ingeniería de Sistemas e Informática')
    c.sprite('web',16,22,3,PINK)
    c.text(56,13,'AMPI.EXE',24,INK)
    c.text(56,44,'SYSTEMS ENGINEERING / CREATIVE TECH',12,CYAN)
    c.rect(491,20,92,21,'#2B1846');c.text(500,25,'PLAYER 01',11,'#C596F8')
    c.rect(16,66,round(568*t),2,PINK)
    return c


def typing(t=1):
    c=panel(600,31,'Desarrollo / Diseño / Innovación / Gestión')
    c.pixel(16,9,'>',2,CYAN)
    phrase='DESARROLLO / DISENO / INNOVACION / GESTION'
    c.pixel(39,10,phrase[:int(len(phrase)*min(1,t*1.3))],1,INK)
    return c


def divider(t=1):
    c=panel(600,16,'Separador de circuitos animado')
    c.rect(12,7,576,1,'#3E2459')
    c.rect(12+round(548*t),5,28,5,CYAN)
    return c


def motion(name,draw,color=CYAN,continuous=False):
    c=draw(1);c.png().save(OUT/(name+'.png'),optimize=True)
    # SVG animado para visores compatibles; GitHub muestra el GIF equivalente.
    seconds=8 if continuous else 6
    repeat='indefinite' if continuous else '1'
    svg=c.svg().replace('</svg>',f'<g aria-hidden="true"><rect x="8" y="{c.h-2}" width="20" height="2" fill="{color}"><animate attributeName="x" from="8" to="{c.w-28}" dur="{seconds}s" repeatCount="{repeat}" fill="freeze"/></rect></g></svg>')
    (OUT/(name+'.svg')).write_text(svg,encoding='utf-8')
    palette=c.png().quantize(colors=32)
    frames=[]
    for i in range(40):
        frame=draw(i/39)
        frame.rect(8+round((frame.w-36)*i/39),frame.h-2,20,2,color)
        frames.append(frame.png().quantize(palette=palette,dither=Image.Dither.NONE))
    options={'loop':0} if continuous else {}
    frames[0].save(OUT/(name+'.gif'),save_all=True,append_images=frames[1:],duration=seconds*25,optimize=True,disposal=1,**options)


def main():
    OUT.mkdir(exist_ok=True)
    for name,draw in [('identidad',header),('intereses',typing),('circuito',divider)]:
        motion(name,draw,continuous=name=='identidad')
    nav=[('profile','PLAYER PROFILE','Formación, intereses y enfoque','web',CYAN),('missions','MISSION SELECT','Proyectos, prototipos y aportes','star',PINK),('activity','CONTRIBUTION MAP','Actividad oficial y colaboración','git','#B7F46B'),('skills','SKILL TREE','Herramientas y aprendizaje','coin',YELLOW)]
    for name,title,subtitle,icon,color in nav:
        def draw_nav(t):
            c=panel(300,49,title+' / '+subtitle)
            c.sprite(icon,12,15+round(math.sin(t*math.tau)*2),2,color)
            c.text(40,14,title,20,INK)
            return c
        motion('nav-'+name,draw_nav,color)
    cards=[('ashakids','ASHAKids','IDEA PROPIA / DESARROLLO EN EQUIPO',PINK),('lifexperience','LifeXperience','SIMULACION EDUCATIVA / FIGMA',CYAN),('manka','MANKA+','OLLAS COMUNES / PROTOTIPO',YELLOW),('lookmi','LOOKMI','AVATAR Y ESTILOS / MAKETHON',PINK),('jmp','JMP','FRONTEND / DATOS / COLABORACION',CYAN),('gamelab','GAMELAB 4.0','DISENO DE JUEGO / THREADBARE','#B7F46B'),('edukids','EduKids','EL ORIGEN / PROTOTIPO WEB',YELLOW),('utpliteapp','UTPLiteApp','ANDROID / PROTOTIPO ACADEMICO',CYAN)]
    for i,(name,title,tag,color) in enumerate(cards,1):
        def draw_card(t):
            c=panel(600,65,title+' / '+tag)
            c.rect(0,0,4,65,color);c.pixel(17,15,f'{i:02}',2,color)
            c.text(55,11,title,23,INK);c.pixel(55,45,tag,1,color)
            c.rect(562,15,20,20,'#261B38');c.pixel(567+round(math.sin(t*math.tau)*2),20,'>',1,color)
            return c
        motion('mission-'+name,draw_card,color)
    # Conversión de formato para entrega ligera; conserva el original generado.
    with Image.open(OUT/'ciudad-original.png') as im:
        im.save(OUT/'ciudad.webp',format='WEBP',quality=85,method=6)
    print('HUD y paneles cyberpunk generados; ilustración original conservada.')


if __name__=='__main__':
    main()
