# Rediseño anime retrofuturista · AMPI.EXE

Preparado el 14 de octubre de 2026 en la rama `codex/anime-retrofuturista`. La autora autorizó publicar este rediseño en GitHub el 14 de octubre de 2026, después de revisar y aprobar la vista previa.

## Diseño y contenido

La referencia aportada por la autora guía la paleta celeste, azul Doraemon, rosa y azul noche; el escritorio panorámico, la ciudad, las nubes y la puerta dimensional conectan las secciones. Los paneles propios usan títulos retro y texto legible. El README utiliza HTML y Markdown compatibles con GitHub: imágenes enlazadas, tablas, anclas y desplegables.

El orden es JMP PINGUS; EduKids → ASHAKids; LifeXperience y MANKA+; LOOKMI y MirrorMind; NeuroEcho y GAMELAB 4.0; otras experiencias. Se conservan los casos, los aportes, los créditos, los estados y las tecnologías del README anterior. Las imágenes decorativas no se presentan como capturas de aplicaciones. Las tres capturas auténticas permanecen en un desplegable.

Las estadísticas originales no se modifican: resumen y lenguajes conservan su instantánea del 13 de octubre de 2026. Los calendarios anuales archivados no se insertan en el README.

## Recursos nuevos

- `assets/anime/arte-original.png`: ilustración original generada con imagegen tomando la imagen adjunta como referencia visual. Tres escenas: escritorio, aventura y noche.
- `assets/anime/escritorio.webp`, `aventura.webp`, `noche.webp`: franjas extraídas y optimizadas de esa ilustración.
- `banner.png`, `identidad.png`, `hola.png`: banner con identidad y frase exacta, presentación y panel de saludo.
- Seis `proyecto-*.png`: tarjetas ilustradas con nombres, propósito y tecnologías reales.
- `sobre-mi.png`, `enfoque.png`, `actualmente.png`: paneles de enfoque personal.
- `herramientas.svg`: cuadrícula construida con los diez logotipos existentes y sus créditos.
- `separador.gif` y `separador.png`: estrellas y puerta dimensional, animación finita con alternativa estática.

Los textos de las tarjetas también se incluyen en HTML legible y seleccionable. Los casos y los recursos anteriores permanecen disponibles.

## Mantenimiento y vista previa

`python tools/anime.py` regenera los paneles y el GIF desde el arte guardado, sin nuevas llamadas de generación de imágenes. Requiere Pillow y las fuentes Segoe UI de Windows. Edita los textos de las tarjetas en ese archivo y sus equivalentes accesibles en el README.

`tools/preparar_anime_readme.py` es una migración única del README anterior: rechaza sobrescribir un README ya migrado. No es necesario ejecutarla para mantener esta versión.

`python tools/verificar_anime.py` comprueba rutas y movimiento, y solicita el HTML al renderizador público de Markdown de GitHub. Produce `preview/README.html`, que se sirve desde la raíz del repositorio. Sus estilos son una aproximación local a GitHub; no constituyen una captura del perfil publicado.

## Validación realizada

- 54 referencias locales del README resueltas, sin archivos faltantes.
- HTML procesado por el renderizador público de GitHub; las tablas, los nueve desplegables y los dos elementos `<picture>` se conservan.
- 22 imágenes cargadas en la vista de escritorio; sin imágenes rotas al abrir los desplegables.
- Vista previa a 1200, 390 y 320 píxeles sin desbordamiento horizontal. Inspección visual de las capturas de escritorio y móvil y revisión del modo oscuro con los desplegables abiertos.
- El GIF tiene 24 fotogramas distintos, pesa 38 154 bytes y dura 2,88 segundos por el redondeo temporal del formato. No contiene repetición. Al activar movimiento reducido, ambos separadores seleccionan el PNG.
- Cuatro anclas explícitas para navegación, incluidas las secciones con títulos acentuados.
- `git diff --check` sin errores de espacios. No se modificaron las estadísticas ni se añadieron calendarios duplicados.

## Compatibilidad y límites

GitHub no permite CSS personalizado, JavaScript, paneles fijos ni transiciones interactivas en el README. La composición usa tablas e imágenes enlazadas. En pantallas estrechas las tarjetas permanecen en dos columnas; el texto HTML y los casos permiten leer la información con independencia del texto dibujado. No se simulan botones de navegación de una aplicación.

La alternativa estática usa `<picture>` con `prefers-reduced-motion`; también se enlaza directamente el PNG. El GIF no se repite y mantiene el movimiento fuera de los párrafos. Los enlaces de Figma se conservan y pueden requerir permisos del propietario; no se han acreditado nuevos despliegues ni funcionalidades.

[Volver al perfil](../README.md)
