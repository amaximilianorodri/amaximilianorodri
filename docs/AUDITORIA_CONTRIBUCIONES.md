# Auditoría de contribuciones · 13 de octubre de 2026

## Qué se comprobó

Cuenta autenticada: `amaximilianorodri`. Se consultaron el catálogo público, los repositorios colaborativos accesibles, muestras de commits, ramas y el calendario público anual. La organización `Game-Lab-4-0-UTP-Group-7-Team-2` aparece en la membresía de la cuenta; su relación con la experiencia fue confirmada por la autora.

No se publicaron direcciones de correo, tokens, nombres de repositorios privados o datos de la empresa. El acceso existente no permite consultar la lista de correos de la cuenta: no se pudo comprobar cuáles están añadidos o verificados.

## Hallazgos y soluciones

| Caso | Evidencia | Qué explica y qué hacer |
| --- | --- | --- |
| ASHAKids | `5dacd55` está vinculado a la cuenta, pero al compararlo con `main` hay divergencia: 33 commits por delante y uno por detrás | Esa línea de desarrollo aún no está integrada en la rama predeterminada. El equipo puede integrar el trabajo mediante una PR cuando corresponda; no se cambia la rama principal solo para aumentar estadísticas |
| JMP | `b316269`, `128070e` y `d5b2363` tienen autora sin cuenta asociada; comparten un correo de autor distinto del usado en la muestra vinculada de ASHAKids | La autora confirmó esos commits. La causa probable es una dirección no vinculada a esta cuenta; debe comprobarse en Settings → Emails. No se puede confirmar el registro de correos con el permiso actual |
| UTPLiteApp | `d2b4dc3` sí está vinculado a la cuenta y está fechado en junio de 2025 | No pertenece al calendario anual 2026; elegir el año correcto evita confundir actividad de distintos periodos |
| GAMELAB | El repositorio del equipo es un fork. La consulta en su rama principal por esta cuenta no devolvió commits | La participación confirmada incluye diseño del juego y tareas diversas. Puede estar representada por documentos o ramas; los commits en forks tienen criterios distintos para aparecer en el calendario |
| Perfil propio | El commit inicial publicado está en `main`; se utilizó el noreply correspondiente a la cuenta | La configuración local quedó fijada con esa identidad para futuros commits del perfil. No se alteró la configuración global ni el historial |

Las fechas de autor y de integración de las muestras de JMP difieren solo en segundos o coinciden; no se observó en esas muestras una diferencia de fechas que explique por sí sola la falta de atribución. El examen es una muestra, no una certificación de todo el historial.

[GitHub explica los criterios de rama, correo y repositorio para contar contribuciones](https://docs.github.com/en/account-and-profile/reference/profile-contributions-reference). [Su guía de contribuciones ausentes detalla cómo revisar la atribución](https://docs.github.com/en/account-and-profile/how-tos/contribution-settings/troubleshooting-missing-contributions).

## Revisión de atribución durante el refinamiento

El 13 de octubre se volvió a comprobar el commit publicado del perfil `9faae28`: GitHub lo vincula a `amaximilianorodri`. La identidad local de esta carpeta coincide con el noreply de la cuenta autenticada. Esto confirma una corrección válida para nuevos commits del perfil, sin modificar los de otras personas.

Los tres commits de JMP siguen sin cuenta asociada. La consulta autenticada de la lista de correos devuelve HTTP 404 con este acceso, por lo que no se puede comprobar ni corregir desde aquí la vinculación de la dirección histórica. El 404 no demuestra que la cuenta carezca de direcciones configuradas.

Pasos que pueden resolver el caso sin reescribir historial:

1. En tu copia local de JMP, revisa el correo de un commit confirmado como propio: `git show --no-patch --format="%ae" b316269`. No pegues esa dirección en el README ni en un informe público.
2. Si la dirección te pertenece, revisa [Settings → Emails](https://github.com/settings/emails). Añádela o completa la verificación cuando corresponda. Si no te pertenece o no puedes asociarla a esta cuenta, no atribuyas ese correo mediante una reescritura del equipo.
3. Para nuevos cambios, configura el noreply que muestra GitHub en cada checkout propio: `git config --local user.email "TU_NOREPLY_DE_GITHUB"`. Sustituye el marcador antes de ejecutarlo. La configuración del perfil no se aplica automáticamente a JMP.
4. Después del procesamiento de GitHub, vuelve a comprobar la cuenta de autor del commit y el calendario. No se promete un aumento de cifras: también deben cumplirse los criterios de rama, repositorio y fecha.

En ASHAKids, la comparación continúa mostrando 33 commits por delante y uno por detrás de `main`. La integración requiere la revisión normal del equipo; queda fuera del alcance de este refinamiento. No se cambió su rama predeterminada ni se abrió una PR en su nombre.

Se volvió a consultar el calendario público y se conservaron sus resultados: 14 en 2025 y 2 en 2026. Se actualizó el catálogo público y los bytes de lenguajes reales; no se mezclaron aportes pendientes de atribución con el calendario.

## Los correos históricos

Para JMP, abrir uno de los commits propios y revisar localmente el correo de autor, sin publicarlo en informes. Si es una dirección propia, comprobar si está asociada a esta cuenta y seguir las instrucciones de GitHub para añadirla. No se añade una dirección de otra persona ni se cambia la autoría del equipo.

Para nuevos commits en cada checkout, configurar localmente el correo noreply que ofrece GitHub en Settings → Emails. La configuración de esta carpeta no modifica los otros proyectos. No hace falta crear commits vacíos, alterar fechas ni reescribir historiales para preparar el portafolio.

No se modificaron correos de la cuenta, ajustes de visibilidad de contribuciones, ramas de ASHAKids ni repositorios colaborativos. Si se desea mostrar actividad privada anonimizada, debe decidirlo la autora desde sus ajustes; no se publica información privada en este perfil.

## Tres clases de actividad

1. **Calendario oficial público:** GitHub devolvió 14 contribuciones para 2025 y 2 para 2026, en consultas anuales separadas. No es una suma de todos los commits ni toda la experiencia profesional.
2. **Actividad adicional demostrable:** los commits propios sin atribución, el trabajo en `dev`, el diseño en GAMELAB y los prototipos en Figma se presentan con su evidencia y contexto. No se suman al calendario oficial como si ya estuvieran contabilizados.
3. **Tarjetas externas:** pueden usar otras ventanas, filtros y caché. El README anterior no incluía tarjetas externas, por lo que ninguna tarjeta estaba ocultando allí actividad.

Se probó GitHub Readme Stats: respondió HTTP 200 sin una tarjeta de error detectable. Sin embargo, su [repositorio advierte que el proyecto ya no se mantiene y que el servicio público puede ser poco fiable](https://github.com/anuraghazra/github-readme-stats). No se utiliza como única fuente ni como medida de dominio.

## Implementación realizada

- Calendarios locales generados con conteos diarios y niveles reales de GitHub; no se estiman cantidades desde los colores.
- Resumen del catálogo público propio y estrellas de esos repositorios, separado de los proyectos del equipo.
- Lenguajes por bytes de repositorios públicos propios, excluyendo forks; no es un porcentaje de habilidad ni código escrito exclusivamente por la autora.
- Enlaces a commits y casos de estudio colaborativos para representar lo que el calendario no recoge.
- Instantánea JSON con fuentes y fecha, sin credenciales o correos.
- Actualizador manual que falla si el calendario no se puede interpretar; no sustituye errores por números inventados.

No se añadió un workflow: por ahora, una actualización manual evita permisos adicionales y commits automáticos decorativos.

[Datos de la instantánea](../assets/actividad/datos.json) · [Instrucciones de mantenimiento](MANTENIMIENTO.md) · [Volver al perfil](../README.md)
