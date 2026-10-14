# Ilustraciones propias por proyecto y laboratorio animado

Iteración sobre `codex/iconos-doraemon`, que incluye los iconos y stickers de la revisión anterior. La autora autorizó publicar el conjunto de cambios después de revisar las escenas, las animaciones y el ajuste de «Next Adventure».

## Cada tarjeta tiene una escena distinta

Se sustituyen las ilustraciones repetidas por seis escenas generadas individualmente con imagegen integrado:

| Proyecto | Concepto decorativo |
| --- | --- |
| JMP PINGUS | Taller de materiales, cajas organizadas y pequeños robots de logística. |
| EduKids → ASHAKids | Juegos con bloques, un libro ilustrado y materiales hechos a mano sobre una isla de nubes. |
| LifeXperience | Mundo en miniatura con escuela, jardín, puentes y caminos cotidianos por explorar. |
| MirrorMind | Observatorio nocturno, espejo de constelaciones y luces de colores. |
| GAMELAB 4.0 | Aventura espacial con plataformas, estrellas y portal en pixel art. |
| UTPLiteApp | Campus y gadget móvil con pictogramas de calendario, anuncios y acceso. |

Las seis son imágenes conceptuales decorativas. No representan pantallas reales, funcionalidades verificadas, mecánicas de NeuroEcho ni recursos de Threadbare. Las descripciones, tecnologías y enlaces reales del README no se modifican.

Los archivos finales se conservan en `assets/anime/proyectos/`, optimizados a WebP de 1200 × 600 píxeles, y los prompts completos en [PROMPTS.json](../assets/anime/proyectos/PROMPTS.json). Las miniaturas con marco las produce `tools/anime.py`; su mayor altura permite reconocer el escenario y al personaje.

## Laboratorio de aventuras

La nueva sección del README reúne tres escenas: vuelo con gorrocóptero, resplandor alrededor de una puerta dimensional y astronauta entre estrellas. Se reutilizan los stickers existentes para una animación de interfaz propia, sin nuevos fotogramas de IA ni servicios externos.

El GIF es de 900 × 320 píxeles, parte de 48 fotogramas y guarda 47 tras optimizar los coincidentes, con un ciclo continuo de 4,8 segundos. Pesa 695 297 bytes, aproximadamente 679 KiB. Se evitan destellos bruscos; el movimiento se mantiene en esta sección y en los separadores existentes. `<picture>` selecciona la imagen estática al activar movimiento reducido y también se ofrece un enlace directo a ella.

Para regenerarlo: `python tools/animaciones.py`. Para las tarjetas: `python tools/anime.py`. Ambos usan recursos locales. `python tools/verificar_anime.py` comprueba las seis imágenes diferentes, las rutas, el peso del GIF y sus fotogramas, y crea la vista previa mediante el renderizador de GitHub.

## Comprobación visual

La tarjeta «Next Adventure» usa ahora un lienzo de 700 × 780 píxeles para ocupar el alto de la fila de GAMELAB en escritorio. «Pequeños pasos, nuevas aventuras» queda integrado dentro del mismo marco, con el personaje y el paisaje ampliados. Mantiene su proporción al reducirse en móvil.

Se inspeccionan las seis ilustraciones y su integración en escritorio y móvil, la carga de imágenes, las anclas, los modos claro y oscuro, y la alternativa sin movimiento. Los datos de actividad y las tecnologías se conservan.

[Volver al perfil](../README.md) · [Iconos y stickers](ICONOS_DORAEMON.md)
