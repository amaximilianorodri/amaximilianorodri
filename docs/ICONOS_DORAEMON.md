# Iconos de tecnologías y detalles de Doraemon

Iteración en `codex/iconos-doraemon`. La autora autorizó publicar estos cambios junto con las escenas individuales, las animaciones y el ajuste de «Next Adventure» después de revisar la vista previa.

## Tecnologías dentro de cada proyecto

Las 18 etiquetas de tecnologías ahora incluyen un símbolo junto al nombre, en vez del punto decorativo. Se reutilizan los diez logotipos locales existentes y se completan Tailwind CSS, PostgreSQL, Python, FastAPI y Kotlin desde Simple Icons, y Java desde Devicon. Los archivos fuente y su procedencia están en `assets/logos/tecnologias/`.

XML utiliza un símbolo propio de etiquetas de código; pdf-lib, un documento. Son símbolos de formato y biblioteca, sin atribuirles logotipos oficiales. Las etiquetas SVG son locales, contienen sus iconos embebidos y no requieren peticiones a servicios externos al leer el perfil.

Los proyectos, tecnologías y atribuciones son los mismos que en la versión anterior. El backend de ASHAKids continúa identificado como trabajo del equipo. Los cinco destacados y la experiencia secundaria de UTPLiteApp mantienen sus enlaces.

## Doraemon y gadgets

Se generó con imagegen integrado un atlas transparente de seis stickers, usando las dos referencias compartidas como guía visual. El [prompt completo](../assets/anime/PROMPT_STICKERS.txt) se conserva junto al [atlas original](../assets/anime/stickers/atlas-original.png). El empaquetado extrae las seis celdas y las optimiza a 256 píxeles, sin redibujar el arte.

- Saludo con campanita: identidad y MirrorMind.
- Vuelo con gorrocóptero: saludo inicial y UTPLiteApp.
- Puerta dimensional: LifeXperience y enfoque.
- Dorayaki: EduKids → ASHAKids y sobre mí.
- Laptop e idea: JMP PINGUS y actualidad.
- Astronauta en pixel art: GAMELAB y ambas tarjetas de frases.

Los paneles conservan el fondo azul profundo y el texto claro. Se reserva espacio para los stickers, sin cubrir los párrafos. La barra de actualidad es un adorno de interfaz; no representa un porcentaje de progreso medido. Las ilustraciones no acreditan funcionalidades de los proyectos.

## Mantenimiento y validación

`python tools/anime.py` regenera etiquetas, recortes del atlas y paneles. `python tools/actualizar_iconos.py` descarga los seis logotipos complementarios desde sus repositorios fuente; solo es necesario para actualizarlos. `python tools/verificar_anime.py` valida rutas y prepara la vista previa con HTML renderizado por GitHub.

Se comprueban carga de imágenes, anclas y lectura a 1200, 390 y 320 píxeles, el modo claro y la alternativa estática para movimiento reducido. Se mantienen las estadísticas y la documentación original.

[Volver al perfil](../README.md) · [Refinamiento oscuro anterior](REFINAMIENTO_DARK.md)
