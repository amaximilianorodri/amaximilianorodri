"""Migración única del README anterior; conserva su texto en desplegables.

Se ejecuta una vez antes de modificar manualmente el README anime.
"""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'README.md'
old=path.read_text(encoding='utf-8')
if '## Player profile' not in old:
    raise SystemExit('El README ya se migró; edítalo directamente. No se sobrescribe.')

def block(start,end): return old.split(start,1)[1].split(end,1)[0].strip()
def clean(s):
    s=re.sub(r'<a [^\n]*<img[^\n]*</a>\s*','',s)
    s=re.sub(r'<picture>.*?</picture>\s*','',s,flags=re.S)
    return s.strip()
def more(label,s): return f'<details>\n<summary><strong>{label}</strong></summary>\n\n{clean(s)}\n\n</details>\n'
def pic(name,alt,width='100%'): return f'<img src="assets/anime/{name}.png" width="{width}" alt="{alt}">'
def motion(): return '<picture><source media="(prefers-reduced-motion: reduce)" srcset="assets/anime/separador.png"><img src="assets/anime/separador.gif" width="100%" alt="Estrellas flotantes y una puerta dimensional rosa; animación breve de tres segundos."></picture>'

out=f'''<!-- AMPI.EXE · Diseño anime retrofuturista. El texto de las tarjetas también existe debajo de cada imagen. -->
{pic('banner','AMPI.EXE. Un futuro mejor también se construye con pequeñas ideas. Doraemon, un escritorio tecnológico, ciudad futurista y puerta dimensional.')}

<p align="center"><a href="#sobre-mi">💙 Sobre mí</a> · <a href="#proyectos-destacados">📂 Proyectos</a> · <a href="#herramientas-y-tecnologias">🧰 Herramientas</a> · <a href="#actividad-de-github">✨ Actividad</a></p>

<a name="sobre-mi"></a>

## Sobre mí

<table>
<tr>
<td width="29%" valign="top">

{pic('identidad','AMPI.EXE. Ideas del futuro, soluciones de hoy. Estudiante de Ingeniería de Sistemas e Informática. Desarrollo, gestión, diseño, innovación e impacto social.')}

<a href="https://github.com/amaximilianorodri">@amaximilianorodri</a>

</td>
<td width="71%" valign="top">

{pic('hola','¡Hola! Soy AMPI. Me gusta entender una necesidad, darle forma a una idea y colaborar para construir una solución. Tecnología, personas, creatividad y propósito.')}

<strong>Estudiante de Ingeniería de Sistemas e Informática.</strong><br>
Combino desarrollo, diseño de interfaces, análisis de procesos y organización de proyectos. Impulsé EduKids, que evolucionó hacia ASHAKids desde una experiencia familiar.

<br><br>
<img src="assets/anime/aventura.webp" width="100%" alt="Ilustración decorativa anime: Doraemon, nubes, ciudad del futuro y una puerta rosa hacia nuevas aventuras.">

</td>
</tr>
</table>

<a name="proyectos-destacados"></a>

## Proyectos destacados

Experiencia actual → una idea que creció → innovación e impacto → diseño → videojuegos.

Las ilustraciones de las tarjetas son **arte decorativo**; las capturas reales y la evidencia están en los casos. Cada enlace distingue mi participación del trabajo del equipo.

<table>
<tr>
<td width="50%" valign="top">

<a href="docs/jmp.md">{pic('proyecto-jmp','01 · JMP PINGUS. Prácticas y desarrollo del sistema de inventario. React, TypeScript y Supabase.')}</a>

<strong>01 · JMP PINGUS</strong><br>
Mi experiencia actual como practicante. Participo en frontend, backend, servicios y lógica de datos del inventario.<br><br>
React · TypeScript · Tailwind CSS · Supabase · PostgreSQL · pdf-lib<br><br>
<a href="https://github.com/luisteransaucedo18-coder/JMP-PINGUS-INVENTARIO">Repositorio ↗</a> · <a href="docs/jmp.md">Mi participación →</a>

</td>
<td width="50%" valign="top">

<a href="docs/ashakids.md">{pic('proyecto-ashakids','02 · EduKids a ASHAKids. Una idea familiar que creció en equipo. Prototipo inicial HTML, CSS y JavaScript; interfaz colaborativa React y TypeScript.')}</a>

<strong>02 · EduKids → ASHAKids</strong><br>
De acompañar a mis hermanitos con actividades hechas a mano a una propuesta construida en equipo. Idea original y trabajo principalmente en la landing.<br><br>
EduKids: HTML · CSS · JavaScript<br>
ASHAKids: React · TypeScript; backend del equipo: FastAPI · PostgreSQL<br><br>
<a href="https://amaximilianorodri.github.io/EduKids/">Demo inicial ↗</a> · <a href="https://github.com/sromansilva/ashakids-platform/tree/dev">ASHAKids ↗</a> · <a href="docs/ashakids.md">Historia →</a>

</td>
</tr>
<tr>
<td width="50%" valign="top">

<a href="docs/lifexperience.md">{pic('proyecto-impacto','03 · LifeXperience y MANKA+. Innovación educativa e impacto social. Propuestas y prototipos en Figma.')}</a>

<strong>03 · LifeXperience · MANKA+</strong><br>
Simulaciones educativas y gamificación en LifeXperience; abastecimiento y seguimiento de beneficiarios de ollas comunes en MANKA+.<br><br>
Mi participación: propuesta y prototipos en Figma.<br><br>
<a href="https://www.figma.com/make/PEM0hl8lFPZMcPFT7gFbYG/Next-steps-discussion">LifeXperience ↗</a> · <a href="https://www.figma.com/proto/E2MQIJzdnrB3AHdduSVq4r/Manka-3.0?node-id=22-2&amp;starting-point-node-id=22%3A2">MANKA+ ↗</a><br>
<a href="docs/lifexperience.md">Caso LifeXperience →</a> · <a href="docs/manka.md">Caso MANKA+ →</a>

</td>
<td width="50%" valign="top">

<a href="docs/lookmi.md">{pic('proyecto-diseno','04 · LOOKMI y MirrorMind. Diseño, prototipado y experimentación. Figma, React y TypeScript.')}</a>

<strong>04 · LOOKMI · MirrorMind</strong><br>
Avatares de mascotas y exploración visual en LOOKMI; interfaces y simulaciones de análisis emocional en MirrorMind.<br><br>
LOOKMI: prototipo en Figma Make durante el Makethon de Trujillo.<br>
MirrorMind: React · TypeScript; revisión técnica pendiente.<br><br>
<a href="https://www.figma.com/make/QWhvi0W8B2Do0OfQGDDvJZ/Idea-Development-Support">LOOKMI ↗</a> · <a href="https://github.com/amaximilianorodri/MirrorMind">MirrorMind ↗</a> · <a href="docs/lookmi.md">Caso LOOKMI →</a>

</td>
</tr>
<tr>
<td width="50%" valign="top">

<a href="docs/gamelab.md">{pic('proyecto-gamelab','05 · NeuroEcho y GAMELAB 4.0. Diseño de la propuesta del juego en equipo. Godot; fork de Threadbare y créditos de Endless.')}</a>

<strong>05 · NeuroEcho · GAMELAB 4.0</strong><br>
Juego creado con mi equipo, Grupo 7, equipo 2. Participé en distintas tareas y en el diseño de la propuesta.<br><br>
Godot · Proyecto sobre Threadbare · Créditos originales de Endless conservados.<br><br>
<a href="https://github.com/Game-Lab-4-0-UTP-Group-7-Team-2/threadbare">Repositorio ↗</a> · <a href="docs/gamelab.md">Contexto y contribución →</a>

</td>
<td width="50%" valign="top">

<a href="docs/utpliteapp.md">{pic('proyecto-otros','Otras aventuras. UTPLiteApp y ProyectoHeDe. Desarrollo colaborativo Android y web.')}</a>

<strong>Otras aventuras en equipo</strong><br>
UTPLiteApp: prototipo académico Android; mis cambios incluyen calendario, anuncios y login.<br>
ProyectoHeDe: sitio institucional estático; aporte detallado pendiente de precisar.<br><br>
Kotlin · Java · XML / HTML · CSS · JavaScript<br><br>
<a href="https://github.com/sromansilva/UTPLiteApp">UTPLiteApp ↗</a> · <a href="https://github.com/j3zkills/ProyectoHeDe">ProyectoHeDe ↗</a> · <a href="docs/utpliteapp.md">Mis contribuciones →</a>

</td>
</tr>
</table>

### Historias, créditos y evidencia

'''
out+=more('01 · JMP PINGUS: alcance y enlaces a mis cambios',block('### 01 · JMP PINGUS · Prácticas y desarrollo de inventario','### 02 · EduKids'))
out+='\n'+more('02 · EduKids → ASHAKids: de dónde nació la idea',block('### 02 · EduKids → ASHAKids · Una idea que creció','### Innovación e impacto social'))
impact=block('### Innovación e impacto social','### Diseño y prototipado')
# Mantener las capturas auténticas además de las ilustraciones decorativas.
out+='\n'+more('03 · LifeXperience y MANKA+: prototipos y estado',impact)
out+='\n'+more('04 · LOOKMI y MirrorMind: prototipos y límites',block('### Diseño y prototipado','## Team mode'))
out+='\n'+more('05 · NeuroEcho, GAMELAB y otras experiencias: créditos del equipo',block('### NeuroEcho · GAMELAB 4.0 · Grupo 7, equipo 2','## Contribution map'))
# Reinsertar las capturas auténticas retiradas por clean(), sin repetir descripciones.
out+='\n<details>\n<summary><strong>Capturas reales de mis prototipos</strong></summary>\n\n'
for name,label,width in [('lifexperience','LifeXperience','420'),('manka','MANKA+','110'),('lookmi','LOOKMI','420')]:
    out+=f'<a href="docs/{name}.md"><img src="assets/proyectos/{name}.png" width="{width}" alt="Captura real del prototipo {label}. Ver el caso para consultar su estado y la pantalla completa."></a>\n\n'
out+='</details>\n\n'+motion()+'''\n\n## Herramientas y tecnologías

<img src="assets/anime/herramientas.svg" width="100%" alt="Cuadrícula de herramientas: JavaScript, TypeScript, React, HTML, CSS, Supabase, Git, GitHub, Figma y Godot.">

'''+block('## Skill tree','### Next level').replace('![JavaScript](assets/logos/javascript.svg) ![TypeScript](assets/logos/typescript.svg) ![React](assets/logos/react.svg) ![HTML](assets/logos/html.svg) ![CSS](assets/logos/css.svg)','').replace('![Supabase](assets/logos/supabase.svg) ![Git](assets/logos/git.svg) ![GitHub](assets/logos/github.svg) ![Figma](assets/logos/figma.svg) ![Godot](assets/logos/godot.svg)','')
out+='\n\n<table><tr>\n'
for name,alt in [('sobre-mi','Sobre mí: aprender, crear y organizar proyectos que conecten personas, ideas y oportunidades.'),('enfoque','Mi enfoque: soluciones, gestión, diseño, trabajo en equipo e impacto social.'),('actualmente','Actualmente: estudiando Ingeniería de Sistemas e Informática y participando en JMP PINGUS.')]:
    out+=f'<td width="33%" valign="top">{pic(name,alt)}</td>\n'
out+='</tr></table>\n\n### Mi próxima aventura\n\n'+block('### Next level','[GitHub · @amaximilianorodri]')+'\n\n'+motion()+'\n\n## Actividad de GitHub\n\n'+block('## Contribution map','## Skill tree')
out+='''\n\n<img src="assets/anime/noche.webp" width="100%" alt="Pequeños pasos también te llevan a grandes lugares. Escena decorativa de Doraemon, escritorio tecnológico y estrellas en azul noche.">

<p align="center"><strong>Pequeños pasos también te llevan a grandes lugares. 💙</strong></p>

[GitHub · @amaximilianorodri](https://github.com/amaximilianorodri) · [Versión estática del separador](assets/anime/separador.png) · [Mantenimiento](docs/MANTENIMIENTO.md) · [Créditos visuales](docs/CREDITOS_VISUALES.md) · [Informe del rediseño](docs/REDISENO_ANIME.md)
'''
path.write_text(out,encoding='utf-8')
