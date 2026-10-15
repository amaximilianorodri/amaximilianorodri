# Mantenimiento del perfil

## Diseño actual: anime retrofuturista

La barra sobre el banner enlaza al [LinkedIn confirmado por la autora](https://www.linkedin.com/in/amparito-maximiliano-rodriguez) y a sus repositorios de GitHub. `python tools/barra_contacto.py` regenera sus dos botones SVG locales. Para cambiar los destinos, edita los enlaces del primer párrafo del README.

Las tarjetas actuales usan seis [escenas distintas y un laboratorio animado](ESCENAS_Y_ANIMACIONES.md). Sus fuentes optimizadas están en `assets/anime/proyectos/`; `python tools/anime.py` regenera las miniaturas y `python tools/animaciones.py` regenera el GIF y la alternativa estática del laboratorio. Ambos comandos funcionan sin red.

Los [iconos y detalles de Doraemon](ICONOS_DORAEMON.md) añaden etiquetas SVG con logotipos y stickers transparentes. `tools/anime.py` necesita el atlas conservado en `assets/anime/stickers/atlas-original.png` y los logotipos de `assets/logos/tecnologias/`; no requiere volver a generar imágenes ni descargarlas al ejecutarlo.

La iteración actual adapta los paneles al modo oscuro y limita los destacados a cinco proyectos. Consulta el [refinamiento oscuro](REFINAMIENTO_DARK.md). Las tecnologías se mantienen dentro de las tarjetas del README; al editarlas, actualiza también sus etiquetas locales si corresponde. `python tools/verificar_anime.py` prepara ahora la vista previa oscura por defecto.

El rediseño local del 14 de octubre de 2026 usa `assets/anime/`. Ejecuta `python tools/anime.py` para regenerar sus paneles y `python tools/verificar_anime.py` para validar rutas y crear `preview/README.html`. Consulta el [informe del rediseño](REDISENO_ANIME.md). Las instrucciones cyberpunk que siguen se conservan como historial y no regeneran el diseño actual.

## Actualizar la actividad

Desde la carpeta del repositorio, con Python disponible:

```powershell
python tools/actualizar_actividad.py --date AAAA-MM-DD
```

Sustituye la fecha por la fecha real de consulta. El generador consulta calendarios públicos anuales de GitHub, repositorios públicos propios, lenguajes y evidencia de colaboración. Guarda datos y gráficos en `assets/actividad/`. No calcula experiencia ni dominio a partir del número de repositorios.

Puede utilizar una sesión existente de Git Credential Manager sin guardar ni imprimir credenciales; también admite consultas públicas sujetas a los límites de GitHub. No pegues tokens en el repositorio.

Después de ejecutarlo, actualiza la fecha escrita en el README y revisa las cifras y el año de sus imágenes. El README utiliza los gráficos de repositorios y lenguajes. Los calendarios generados se conservan como archivo para la auditoría; no los vuelvas a insertar en el README porque GitHub ya muestra su calendario oficial. Una respuesta fallida no constituye una actualización válida. Las cifras no se actualizan automáticamente al abrir el perfil.

## Regenerar el diseño

```powershell
python tools/cyberpunk.py
```

Requiere Pillow. Utiliza los glifos originales de `tools/arcade.py` y el arte conservado en `assets/cyberpunk/ciudad-original.png`. Produce SVG animados para visores compatibles y GIF con alternativas PNG: cabecera continua de ocho segundos y animaciones secundarias de seis segundos sin repetición. En el README se utilizan GIF porque GitHub no reproduce las animaciones SVG. Para actualizar textos no es necesario volver a generar el arte con inteligencia artificial.

Los recursos arcade anteriores siguen disponibles; su generador es `python tools/generar_recursos.py`.

## Incorporar evidencia

- Conserva el origen de ASHAKids desde EduKids y diferencia la idea propia del desarrollo colaborativo.
- Añade pantallas de abastecimiento y familias de MANKA+, y flujos de LifeXperience y LOOKMI; indica su estado de prototipo o aplicación operativa.
- Comprueba los permisos de visualización de los enlaces de Figma.
- Antes de publicar informes, revisa datos personales, datos de familias y material del equipo.
- Para GAMELAB, añade una entrega o documento de diseño del juego del equipo.

Los contactos deben estar confirmados. Las insignias identifican herramientas, no certificaciones. Los logotipos están guardados localmente.

## Revisar y publicar

Comprueba rutas, anclas y renderizado en escritorio y móvil. Activa movimiento reducido y verifica las alternativas estáticas. Revisa el diff antes de publicar.

La primera versión publicada está en el commit `e79f601`. Esta revisión se prepara en `codex/cyberpunk-profile`, conservando la versión anterior como referencia. No reescribas commits de proyectos colaboradores para modificar el calendario: utiliza las soluciones de la [auditoría](AUDITORIA_CONTRIBUCIONES.md).

[Volver al perfil](../README.md)

La segunda pasada visual se prepara en `codex/refine-cyberpunk-profile`, partiendo de la versión publicada `9faae28`. El informe de [refinamiento](REFINAMIENTO_VISUAL.md) recoge comprobaciones y límites. La publicación de esta revisión fue autorizada por la autora el 13 de octubre de 2026.

La reorganización de proyectos se prepara sobre ese refinamiento en `codex/project-categories`. Consulta [su informe](PROYECTOS_REORGANIZADOS.md). La autora autorizó publicar ambas revisiones el 13 de octubre de 2026.
