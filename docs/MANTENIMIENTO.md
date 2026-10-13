# Mantenimiento del perfil

## Actualizar la actividad

Desde la carpeta del repositorio, con Python disponible:

```powershell
python tools/actualizar_actividad.py --date AAAA-MM-DD
```

Sustituye la fecha por la fecha real de consulta. El generador consulta calendarios públicos anuales de GitHub, repositorios públicos propios, lenguajes y evidencia de colaboración. Guarda datos y gráficos en `assets/actividad/`. No calcula experiencia ni dominio a partir del número de repositorios.

Puede utilizar una sesión existente de Git Credential Manager sin guardar ni imprimir credenciales; también admite consultas públicas sujetas a los límites de GitHub. No pegues tokens en el repositorio.

Después de ejecutarlo, actualiza la fecha escrita en el README y revisa las cifras y el año de sus imágenes. Si cambia el año, enlaza el nuevo calendario y conserva los anteriores. Una respuesta fallida no constituye una actualización válida. Las cifras no se actualizan automáticamente al abrir el perfil.

## Regenerar el diseño

```powershell
python tools/cyberpunk.py
```

Requiere Pillow. Utiliza los glifos originales de `tools/arcade.py` y el arte conservado en `assets/cyberpunk/ciudad-original.png`. Produce SVG animados para visores compatibles y GIF con ciclos suaves de cuatro segundos y alternativas PNG. En el README se utilizan GIF porque GitHub no reproduce las animaciones SVG. Para actualizar textos no es necesario volver a generar el arte con inteligencia artificial.

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
