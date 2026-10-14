# Refinamiento anime para modo oscuro

Iteración del 14 de octubre de 2026 en `codex/refinar-anime-dark`. La autora autorizó su publicación en GitHub después de revisar la vista previa.

## Contenido

La portada destaca únicamente JMP PINGUS, EduKids → ASHAKids, LifeXperience, MirrorMind y GAMELAB 4.0, en ese orden. UTPLiteApp permanece como experiencia secundaria desplegable con sus etiquetas Android y los enlaces existentes; ProyectoHeDe conserva una mención secundaria.

LOOKMI y MANKA+ dejan de aparecer en el README. Sus documentos, capturas, créditos y recursos históricos siguen en el repositorio. Se retira por completo el apartado «Historias, créditos y evidencia» y el listado independiente que relacionaba tecnologías con proyectos. Los casos originales siguen accesibles desde las tarjetas.

Las etiquetas se colocan dentro de cada tarjeta, con texto alternativo y archivos locales. En EduKids → ASHAKids se distinguen la primera etapa HTML/CSS/JavaScript, la interfaz React/TypeScript y el backend Python/FastAPI/PostgreSQL del equipo. LifeXperience solo muestra Figma; no se añade Supabase como integración verificada. GAMELAB utiliza Godot, con el aporte de diseño y los créditos de Threadbare/Endless identificados.

## Diseño

Se reutiliza el arte anime existente sin nuevas llamadas de generación de imágenes. El generador `tools/anime.py` cambia únicamente la interfaz propia: superficies azul profundo `#132238`, azul medio `#1c334f`, celeste `#85d0ff`, blanco azulado `#e3efff`, bordes discretos `#304d72` y pequeños acentos rosa y amarillo. El fondo exterior de los PNG coincide con `#0d1117`, el fondo oscuro de GitHub.

Los nombres y las descripciones de proyectos quedan en HTML seleccionable y legible en móvil; las miniaturas se concentran en las ilustraciones. Las etiquetas se renderizan a 22 píxeles de alto, mantienen el nombre de la tecnología y no declaran nivel de dominio. Se conserva la identidad, la puerta dimensional, las estrellas, el cierre nocturno y las frases; una tarjeta con frase completa la cuadrícula junto al quinto proyecto sin añadir otro proyecto destacado.

## Recursos y mantenimiento

- `README.md`: estructura más corta, cinco destacados y tecnologías integradas.
- `tools/anime.py`: generador de paneles oscuros, miniaturas, frase y etiquetas.
- `assets/anime/`: paneles actualizados; nuevas miniaturas de LifeXperience, MirrorMind y UTPLiteApp, `frase.png` y `badges/`.
- `tools/verificar_anime.py`: validación del orden de proyectos, ausencia de apartados retirados y vista previa oscura por defecto.

Para regenerar los recursos: `python tools/anime.py`. Después: `python tools/verificar_anime.py`. El script de migración `tools/preparar_anime_readme.py` corresponde a la primera versión y no debe ejecutarse sobre este README.

## Verificación

La vista previa usa HTML procesado por el renderizador de Markdown de GitHub con estilos locales aproximados. Se revisan escritorio y móvil a 1200, 390 y 320 píxeles, con todos los gráficos cargados, sin desbordamiento horizontal, anclas navegables y PNG seleccionado al activar movimiento reducido. También se inspecciona en modo claro y con los desplegables abiertos. Los paneles mantienen su paleta oscura en ambos temas.

Se conservan las estadísticas y su fecha del 13 de octubre de 2026. No se añaden calendarios de contribuciones. El arte original y los archivos de actividad no cambian. Los enlaces a Figma mantienen sus destinos anteriores; sus permisos de acceso no se han vuelto a acreditar.

[Volver al perfil](../README.md) · [Primer rediseño](REDISENO_ANIME.md)
