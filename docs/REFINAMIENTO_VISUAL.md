# Refinamiento visual de AMPI.EXE · 13 de octubre de 2026

## Estado y alcance

Se revisó un checkout limpio y se consultó `origin/main`. La rama `codex/refine-cyberpunk-profile` parte de la versión publicada `9faae28`. No se publicó esta segunda pasada, se reescribió historial ni se modificaron repositorios colaboradores.

Se conservan identidad, ciudad original, GIF, banners, paneles arcade, anclas, proyectos, calendarios y casos. No se eliminaron archivos. Las tarjetas repetidas de los prototipos y primeras etapas se trasladaron a sus casos, donde siguen disponibles con movimiento y alternativa estática.

## Cambios

- Cabecera protagonista: ciclo continuo de ocho segundos. Las catorce animaciones secundarias duran seis segundos, se reproducen una vez y quedan en reposo.
- Paneles de navegación más compactos, con etiquetas mayores y enlaces de texto equivalentes.
- ASHAKids, JMP y GAMELAB conservan tarjetas arcade de hasta 480 píxeles; LifeXperience y LOOKMI muestran capturas reales de hasta 420; MANKA+ muestra una miniatura vertical enlazada a su captura completa.
- Los seis proyectos principales mantienen propósito, estado, contribución personal y casos de estudio. Las capturas no se presentan como prueba de integraciones funcionales.
- Origen desde EduKids, otras colaboraciones, calendario 2025, lenguajes y evidencia detallada de tecnologías quedan en desplegables. El calendario 2026 y la auditoría siguen visibles.

## Resultados medidos

Comparación con el mismo estilo aproximado de GitHub, desplegables cerrados y las mismas dimensiones:

| Vista | Antes | Después | Reducción |
| --- | ---: | ---: | ---: |
| Escritorio, 1100 px | 7406 px | 4462 px | 39,8 % |
| Móvil, 390 px | 7793 px | 5237 px | 32,8 % |

Es altura de la previsualización, no una medición prometida para todos los navegadores de GitHub.

## Comprobaciones

- Se decodificaron los archivos PNG, WebP y GIF reales; se revisaron 18 GIF contando los tres de la primera edición arcade conservada. Tienen fotogramas distintos, duraciones válidas y rutas locales existentes.
- Los 89 archivos gráficos locales se decodificaron en el navegador. Se comprobó el movimiento declarativo de los quince SVG cyberpunk comparando su posición en dos instantes.
- Los 48 SVG se analizaron como XML y no contienen scripts ni objetos HTML incrustados. Los quince SVG cyberpunk conservan movimiento declarativo compatible con visores que lo admiten.
- El renderizador de GitHub preservó las diez alternativas de movimiento reducido del README. Los cinco casos con tarjetas trasladadas también conservan sus alternativas.
- Se inspeccionó el README en temas claro y oscuro a 320, 390 y 1100 píxeles. Sus 28 imágenes cargan, tienen texto alternativo y no producen desbordamiento horizontal. Los desplegables abiertos tampoco lo producen.
- Se validaron las ocho referencias a las cuatro anclas principales contra las secciones del README. La previsualización asigna identificadores siguiendo los títulos; la prueba se limita al render local del marcado de GitHub.
- Los casos de estudio se previsualizaron a 320 píxeles con movimiento reducido e imágenes decodificadas. Se inspeccionaron visualmente la portada móvil y la vista completa de escritorio.
- El texto principal y los acentos del sistema gráfico tienen relaciones de contraste entre 6,18:1 y 14,76:1 sobre `#100C20`. Esto no constituye certificación de accesibilidad de capturas de productos o de toda la interfaz de GitHub. Los textos esenciales también están en Markdown y las miniaturas enlazan a imágenes completas.
- De los 19 enlaces externos únicos del README, 16 respondieron HTTP 200. Los tres enlaces de Figma devolvieron 404 al acceso automatizado y el navegador de consulta tampoco pudo abrirlos. Se conservan los enlaces aportados sin inventar sustitutos: requieren comprobación manual de dirección y permisos. Las capturas locales cargan independientemente de Figma.

## Atribución y pendientes

La cuenta de autor del commit publicado del perfil está correctamente vinculada. Los tres commits revisados de JMP siguen sin atribución automática. La lista de correos de la cuenta no es accesible con el permiso actual; se documentaron pasos de comprobación y corrección sin reescritura de historial en la [auditoría](AUDITORIA_CONTRIBUCIONES.md).

Se actualizaron datos públicos reales sin modificar los conteos oficiales ni sumar commits no atribuidos. La integración de ASHAKids, la asociación del correo histórico de JMP y la revisión de enlaces Figma requieren intervención de sus responsables; no se simulan como resueltas.

Al terminar esta revisión, la publicación quedó pendiente de autorización. La autora autorizó posteriormente publicar el refinamiento junto con la reorganización de proyectos el 13 de octubre de 2026.

[Volver al perfil](../README.md)
