"""Sistema gráfico arcade original. Python + Pillow; sin red ni fuentes externas."""

from pathlib import Path
from html import escape
import math
import unicodedata
from PIL import Image, ImageDraw, ImageFont

ASSETS = Path(__file__).resolve().parents[1] / "assets"
P, D, C, Y, R, N = "#392F4A", "#241F32", "#FFF4E6", "#FFC83C", "#F74F27", "#60DED9"
GLYPHS = {
    "A":"01110/10001/10001/11111/10001/10001/10001", "B":"11110/10001/10001/11110/10001/10001/11110",
    "C":"01111/10000/10000/10000/10000/10000/01111", "D":"11110/10001/10001/10001/10001/10001/11110",
    "E":"11111/10000/10000/11110/10000/10000/11111", "F":"11111/10000/10000/11110/10000/10000/10000",
    "G":"01111/10000/10000/10111/10001/10001/01111", "H":"10001/10001/10001/11111/10001/10001/10001",
    "I":"11111/00100/00100/00100/00100/00100/11111", "J":"00111/00010/00010/00010/10010/10010/01100",
    "K":"10001/10010/10100/11000/10100/10010/10001", "L":"10000/10000/10000/10000/10000/10000/11111",
    "M":"10001/11011/10101/10101/10001/10001/10001", "N":"10001/11001/10101/10011/10001/10001/10001",
    "O":"01110/10001/10001/10001/10001/10001/01110", "P":"11110/10001/10001/11110/10000/10000/10000",
    "Q":"01110/10001/10001/10001/10101/10010/01101", "R":"11110/10001/10001/11110/10100/10010/10001",
    "S":"01111/10000/10000/01110/00001/00001/11110", "T":"11111/00100/00100/00100/00100/00100/00100",
    "U":"10001/10001/10001/10001/10001/10001/01110", "V":"10001/10001/10001/10001/10001/01010/00100",
    "W":"10001/10001/10001/10101/10101/10101/01010", "X":"10001/10001/01010/00100/01010/10001/10001",
    "Y":"10001/10001/01010/00100/00100/00100/00100", "Z":"11111/00001/00010/00100/01000/10000/11111",
    "0":"01110/10001/10011/10101/11001/10001/01110", "1":"00100/01100/00100/00100/00100/00100/01110",
    "2":"01110/10001/00001/00010/00100/01000/11111", "3":"11110/00001/00001/01110/00001/00001/11110",
    "4":"00010/00110/01010/10010/11111/00010/00010", "5":"11111/10000/10000/11110/00001/00001/11110",
    "6":"01110/10000/10000/11110/10001/10001/01110", "7":"11111/00001/00010/00100/01000/01000/01000",
    "8":"01110/10001/10001/01110/10001/10001/01110", "9":"01110/10001/10001/01111/00001/00001/01110",
    ".":"00000/00000/00000/00000/00000/00110/00110", "/":"00001/00001/00010/00100/01000/10000/10000",
    "-":"00000/00000/00000/11111/00000/00000/00000", ":":"00000/00110/00110/00000/00110/00110/00000",
    ">":"10000/01000/00100/00010/00100/01000/10000", "<":"00001/00010/00100/01000/00100/00010/00001",
    " ":"00000/00000/00000/00000/00000/00000/00000",
}
SPRITES = {
    "heart":["0110110","1111111","1111111","0111110","0011100","0001000"],
    "star":["0001000","0001000","1111111","0111110","0011100","0110110","0100010"],
    "coin":["0011100","0111110","1101011","1101011","1101011","0111110","0011100"],
    "web":["111111111","100000001","111111111","100000001","101010101","100101001","101010101","100000001","111111111"],
    "data":["011111110","110000011","111111111","100000001","111111111","100000001","111111111","100000001","011111110"],
    "mobile":["001111100","001000100","001000100","001000100","001000100","001000100","001010100","001111100"],
    "git":["001100000","001100000","000100110","000111110","000100000","001100000","001100000"],
    "bot":["000001100000","000001100000","001111111100","011111111110","011001100110","011001100110","011111111110","001110011100","000111111000","001111111100","001111111100","001100001100"],
}


class Canvas:
    def __init__(self, width, height, title, bg=P):
        self.w, self.h, self.title = width, height, title
        self.im = Image.new("RGB", (width, height), bg)
        self.draw = ImageDraw.Draw(self.im)
        self.parts = [f'<rect width="{width}" height="{height}" fill="{bg}"/>']

    def rect(self, x, y, w, h, color):
        x, y, w, h = map(int, (x, y, w, h))
        if w <= 0 or h <= 0:
            return
        self.draw.rectangle((x, y, x + w - 1, y + h - 1), fill=color)
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>')

    def pixel(self, x, y, text, size=1, color=C):
        text = ''.join(c for c in unicodedata.normalize('NFD', text.upper()) if not unicodedata.combining(c))
        for letter in text:
            if letter not in GLYPHS:
                raise ValueError(f"Glifo no definido: {letter}")
            for row, bits in enumerate(GLYPHS[letter].split('/')):
                for col, bit in enumerate(bits):
                    if bit == '1':
                        self.rect(x + col * size, y + row * size, size, size, color)
            x += size * 6

    def text(self, x, y, text, size=13, color=C):
        choices = ['C:/Windows/Fonts/segoeui.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']
        file = next((p for p in choices if Path(p).is_file()), None)
        if file is None:
            raise RuntimeError('Se requiere Segoe UI o DejaVu Sans.')
        self.draw.text((x, y), text, font=ImageFont.truetype(file, size), fill=color, anchor='lt')
        self.parts.append(f'<text x="{x}" y="{y + size}" font-size="{size}" fill="{color}" font-family="Segoe UI,Arial,sans-serif">{escape(text)}</text>')

    def sprite(self, name, x, y, size=2, color=Y):
        for row, bits in enumerate(SPRITES[name]):
            for col, bit in enumerate(bits):
                if bit == '1':
                    self.rect(x + col * size, y + row * size, size, size, color)

    def window(self, label, accent=N):
        self.rect(4, 4, self.w - 8, self.h - 8, accent)
        self.rect(6, 6, self.w - 12, self.h - 12, D)
        self.rect(6, 6, self.w - 12, 14, P)
        self.pixel(12, 10, label, color=C)
        for x, c in zip([self.w-32,self.w-24,self.w-16], [Y,R,N]):
            self.rect(x, 10, 4, 4, c)

    def terminal(self, x, y, size=1):
        self.rect(x, y, 54 * size, 40 * size, N)
        self.rect(x + 3 * size, y + 3 * size, 48 * size, 32 * size, D)
        self.pixel(x + 8 * size, y + 12 * size, '</>', size, Y)
        self.rect(x + 23 * size, y + 40 * size, 8 * size, 5 * size, C)
        self.rect(x + 11 * size, y + 45 * size, 32 * size, 3 * size, C)

    def png(self):
        return self.im.resize((self.w * 2, self.h * 2), Image.Resampling.NEAREST)

    def svg(self):
        return f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w*2}" height="{self.h*2}" viewBox="0 0 {self.w} {self.h}" role="img" aria-labelledby="title"><title id="title">{escape(self.title)}</title>' + ''.join(self.parts) + '</svg>\n'


def hero(t=1):
    c = Canvas(480, 190, 'Cabecera arcade: ideas con propósito, tecnología con sentido')
    c.window('START / PORTFOLIO')
    c.text(22, 29, '@amaximilianorodri', 14, N)
    c.pixel(22, 56, 'IDEAS CON', 3, C)
    c.pixel(22, 84, 'PROPOSITO.', 3, Y)
    c.text(22, 116, 'Tecnología con sentido. Soluciones con propósito.', 12)
    c.rect(22, 150, 275, 23, P)
    c.pixel(30, 158, 'DESARROLLO / DISENO / GESTION', 1, N)
    drift = round(math.sin(t * math.pi * 2) * 3)
    c.terminal(365, 48)
    c.sprite('bot', 338, 105 + drift, 4, N)
    c.sprite('heart', 410, 124, 3, R)
    c.sprite('star', 325, 48 - drift, 2, Y)
    c.sprite('coin', 438, 76 + drift, 2, Y)
    for x in [334,350,366,382,398,414,430]:
        c.rect(x, 165, 8, 2, P)
    c.pixel(331, 176, 'CREATE / COLLABORATE', 1, C)
    return c


def interests(t=1):
    c = Canvas(480, 34, 'Intereses: desarrollo, diseño y gestión')
    c.rect(4, 4, 472, 26, N)
    c.rect(5, 5, 470, 24, D)
    c.pixel(16, 10, '>', 2, Y)
    phrase = 'DESARROLLO / DISENO / GESTION'
    c.pixel(44, 10, phrase[:int(len(phrase)*min(1,t*1.25))], 2, C)
    return c


def separator(t=1):
    c = Canvas(480, 22, 'Separador arcade con una estrella que recorre una línea')
    for x in range(12,470,12):
        c.rect(x, 10, 7, 2, N if x < 444*t else D)
    c.sprite('star', 12 + round(432*t), 4, 2, Y)
    return c


def save_motion(name, make):
    still = make(1)
    still.png().save(ASSETS / (name+'.png'), optimize=True)
    (ASSETS / (name+'.svg')).write_text(still.svg(), encoding='utf-8')
    frames = [make(i/39).png() for i in range(40)]
    palette = still.png().quantize(colors=32)
    frames = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f in frames]
    frames[0].save(ASSETS/(name+'.gif'), save_all=True, append_images=frames[1:], duration=100, optimize=True, disposal=1)


def main():
    ASSETS.mkdir(exist_ok=True)
    for name, make in [('cabecera',hero),('intereses',interests),('separador',separator)]:
        save_motion(name,make)
    for number,name,title,subtitle,icon,accent in [
        ('01','ashakids','ASHAKIDS','INICIATIVA CON PROPOSITO','heart',R),
        ('02','jmp','JMP','DESARROLLO Y PROCESOS','data',Y),
        ('03','edukids','EDUKIDS','EXPLORAR Y APRENDER','star',Y),
        ('04','utpliteapp','UTPLITEAPP','CONSTRUIR EN EQUIPO','mobile',N),
    ]:
        c=Canvas(480,76,title+' — '+subtitle)
        c.window('PROJECT SELECT / '+number,accent)
        c.pixel(20,30,title,3,C)
        c.pixel(20,59,subtitle,1,accent)
        c.sprite(icon,413,31,4,accent)
        (ASSETS/(name+'.svg')).write_text(c.svg(),encoding='utf-8')
    c=Canvas(480,86,'Inventario: web, datos, móvil y colaboración')
    c.window('SKILL INVENTORY')
    for x,name,label,accent in [(36,'web','WEB',N),(148,'data','DATOS',Y),(261,'mobile','MOVIL',R),(375,'git','GIT',N)]:
        c.sprite(name,x,30,3,accent)
        c.pixel(x-4,66,label,1,C)
    (ASSETS/'inventario.svg').write_text(c.svg(),encoding='utf-8')
    for name in ['heart','star','coin','web','data','mobile','git','bot']:
        c=Canvas(40,40,'Icono pixel original: '+name)
        c.sprite(name,8,8,2,N if name in ['web','git','bot'] else Y)
        (ASSETS/(name+'.svg')).write_text(c.svg(),encoding='utf-8')
    c=Canvas(48,48,'Emblema original: código y creatividad')
    c.rect(2,2,44,44,N);c.rect(4,4,40,40,D)
    c.pixel(8,10,'<',2,Y);c.pixel(31,10,'>',2,Y)
    c.sprite('heart',17,28,2,R)
    (ASSETS/'emblema.svg').write_text(c.svg(),encoding='utf-8')
    c=Canvas(80,65,'Ilustración original de una terminal de programación')
    c.terminal(13,8)
    (ASSETS/'terminal.svg').write_text(c.svg(),encoding='utf-8')
    c=Canvas(480,62,'Recorrido: inspiración, EduKids y ASHAKids; no es una medida de dominio')
    c.window('QUEST LOG / RECORRIDO')
    for x,name,label in [(22,'heart','INSPIRACION'),(184,'web','EDUKIDS'),(346,'star','ASHAKIDS')]:
        c.sprite(name,x,31,2,Y)
        c.pixel(x+25,36,label,1,C)
    c.pixel(154,35,'>',2,N);c.pixel(316,35,'>',2,N)
    (ASSETS/'recorrido.svg').write_text(c.svg(),encoding='utf-8')
    print('Recursos arcade generados: cabecera, intereses, separador, portadas, inventario, iconos, emblema, terminal y recorrido.')


if __name__ == '__main__':
    main()
