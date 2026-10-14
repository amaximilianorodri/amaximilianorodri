"""Escena animada propia con los stickers guardados; compatible con GitHub."""
from pathlib import Path
import math
from PIL import Image,ImageDraw
from anime import OUT,INK,BLUE,LINE,font,panel,sticker,star

def frame(t):
    im,d=panel(900,320)
    labels=[('IDEAS EN VUELO','Imagina'),('PUERTAS A LO NUEVO','Explora'),('SIGUIENTE AVENTURA','Crea')]
    for i,(title,caption) in enumerate(labels):
        x=15+i*295
        d.rounded_rectangle((x,15,x+280,301),18,fill='#102039',outline=LINE)
        d.text((x+140,31),title,anchor='mt',font=font(19,True),fill=BLUE)
        d.text((x+140,268),caption,anchor='mt',font=font(21,True),fill=INK)
        for j in range(5):
            sx=x+28+j*53;sy=78+(j%3)*62
            r=3+2*(.5+.5*math.sin(t*math.tau+j+i))
            star(d,sx,sy,r,'#ffd37a' if j%2 else '#85d0ff')
    sticker(im,'volando',(69+round(5*math.sin(t*math.tau)),79+round(7*math.sin(t*math.tau)),180,180))
    # Un resplandor móvil sutil rodea la puerta; no hay destellos bruscos.
    glow=round(3+3*(1+math.sin(t*math.tau)))
    d.rounded_rectangle((375-glow,82-glow,516+glow,249+glow),12,outline='#69486f',width=2)
    sticker(im,'puerta',(362,78,180,180))
    sticker(im,'astronauta',(657,78+round(6*math.sin(t*math.tau+1.5)),180,180))
    return im

def main():
    folder=OUT/'animaciones';folder.mkdir(exist_ok=True)
    images=[frame(i/48) for i in range(48)]
    images[0].save(folder/'laboratorio.png',optimize=True)
    palette=images[0].quantize(colors=128)
    frames=[im.quantize(palette=palette,dither=Image.Dither.NONE) for im in images]
    frames[0].save(folder/'laboratorio.gif',save_all=True,append_images=frames[1:],duration=100,loop=0,optimize=True,disposal=1)
    print('Laboratorio: 48 fotogramas, ciclo suave de 4,8 segundos, alternativa PNG.')

if __name__=='__main__':main()
