# Implementación del perfil cyberpunk

El perfil reúne desarrollo, diseño, innovación social y colaboración bajo la identidad creativa AMPI.EXE. La primera versión arcade publicada se conserva en el commit `e79f601`; esta revisión se desarrolla en `codex/cyberpunk-profile` y su publicación fue autorizada por la autora.

El cambio afecta al README, documentación, recursos y generadores del perfil. No modifica aplicaciones, repositorios de equipos, visibilidad, biografía ni fijados. Los recursos anteriores se conservan.

## Contenido

ASHAKids conserva el origen de la idea desde EduKids y el aporte principal a la landing. JMP describe trabajo en frontend y backend. GAMELAB presenta el diseño de la propuesta del equipo sobre Threadbare, con créditos del proyecto base y pertenencia a la organización comprobada.

LifeXperience, MANKA+ y LOOKMI incorporan capturas aportadas por su autora y enlaces a Figma. MANKA+ se plantea para abastecimiento y registro de familias beneficiarias de ollas comunes en Perú. LOOKMI propone transformar la foto de una mascota en un avatar editable para explorar estilos y cortes. Los objetivos del prototipo no se presentan como resultados operativos verificados.

Las primeras etapas se incluyen en una sección desplegable. Las herramientas se muestran con logotipos sin porcentajes de dominio o certificaciones inventadas.

## Recursos

| Recurso | Función |
| --- | --- |
| `assets/cyberpunk/` | Ciudad, cabecera, animaciones y tarjetas |
| `assets/proyectos/` | Capturas reales de tres prototipos |
| `assets/logos/` | Diez insignias locales |
| `assets/actividad/` | Datos públicos y gráficos fechados |
| `docs/AUDITORIA_CONTRIBUCIONES.md` | Evidencia y soluciones |
| `docs/lifexperience.md`, `manka.md`, `lookmi.md` | Casos de prototipos |
| `docs/MANTENIMIENTO.md` | Actualización de recursos y datos |
| `docs/CREDITOS_VISUALES.md` | Procedencia y prompt |
| `tools/cyberpunk.py` | Generador visual |
| `tools/actualizar_actividad.py` | Estadísticas públicas |

## Contribuciones

La consulta del 13 de octubre de 2026 encontró 14 contribuciones públicas en el calendario anual de 2025 y 2 en el de 2026. El perfil diferencia esos datos oficiales de la evidencia adicional de colaboración.

El trabajo de ASHAKids revisado está fuera de la rama predeterminada. Los commits de JMP confirmados por la autora no aparecen vinculados automáticamente a su cuenta; la asociación del correo requiere comprobación en GitHub. UTPLiteApp tiene commits vinculados de 2025. Threadbare es un fork y el diseño no se deduce de un calendario de commits.

Se configuró la identidad Git local del perfil con el usuario autenticado y su correo noreply. No se reescribió historial ni se generaron contribuciones artificiales.

## Verificación y límites

- Rutas locales comprobadas y 48 SVG válidos, sin scripts ni objetos HTML incrustados.
- Quince GIF: ciclos de cuatro segundos, con alternativas PNG y equivalentes SVG animados sin scripts.
- El renderizador de Markdown de GitHub conservó los quince elementos picture y sus reglas de movimiento reducido.
- Previsualizaciones a 1100 y 390 píxeles en tema claro y oscuro: 33 imágenes cargadas, sin desbordamiento horizontal.
- En las cuatro combinaciones, el navegador seleccionó los quince PNG al activar movimiento reducido.
- Sintaxis de los generadores validada y diff sin errores de espacios.


La revisión comprueba rutas, SVG, GIF y previsualización en escritorio y móvil, con alternativas de movimiento reducido. El README no incluye JavaScript ni hojas de estilo incrustadas.

Los gráficos son instantáneas locales. El acceso automatizado a Figma no pudo inspeccionar el contenido de los enlaces: la evidencia visual son las capturas proporcionadas. Los informes no se han recibido y las aplicaciones no se ejecutaron como parte de este rediseño.

[Volver al perfil](../README.md)
