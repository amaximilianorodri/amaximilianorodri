# Implementación local · Portafolio arcade

## Alcance

El rediseño se preparó inicialmente en la carpeta local `PERFIL`, con Git inicializado y sin commits ni remoto. Después se creó el repositorio público `amaximilianorodri/amaximilianorodri` para alojar el perfil, conforme a la solicitud de publicación de la usuaria.

No se modificaron aplicaciones ni repositorios de los proyectos. No se eliminaron archivos ni se reescribió historial. El encargo de diseño inicialmente excluía commits y push; la solicitud posterior de subir los cambios autorizó la publicación del repositorio del perfil. Los casos de estudio son documentación propia y no reemplazan los README originales.

## Concepto visual

La identidad combina ventanas arcade, tipografía de píxeles dibujada con glifos originales, un robot tecnológico propio, una terminal, corazones, estrellas, monedas y símbolos de categorías. El robot no representa la apariencia personal de la usuaria.

Paleta: morado `#392F4A`, coral `#F74F27`, amarillo `#FFC83C` y crema `#FFF4E6`, con cian `#60DED9` y un fondo oscuro `#241F32` como apoyo. No se utilizan logos oficiales de tecnologías, marcas de afiliación o porcentajes de dominio.

La estructura del README es Pantalla de inicio, Player profile, Skill inventory, Quest log, Project select y Next level. Las metáforas de videojuego son visuales: los objetivos, contribuciones y estados de los proyectos se describen profesionalmente en Markdown.

## Archivos y recursos

| Archivo o grupo | Función |
| --- | --- |
| `README.md` | Narrativa, navegación, inventario y proyectos |
| `assets/cabecera.gif`, `.png`, `.svg` | Cabecera arcade, robot y terminal |
| `assets/intereses.gif`, `.png`, `.svg` | Escritura progresiva: desarrollo, diseño y gestión |
| `assets/separador.gif`, `.png`, `.svg` | Estrella que recorre una línea entre secciones |
| `assets/ashakids.svg`, `jmp.svg`, `edukids.svg`, `utpliteapp.svg` | Tarjetas de selección de proyectos |
| `assets/emblema.svg` | Código y creatividad como emblema propio |
| `assets/inventario.svg` | Categorías web, datos, móvil y colaboración |
| `assets/recorrido.svg` | Inspiración → EduKids → ASHAKids |
| `assets/terminal.svg` | Terminal ilustrada para Next level |
| `assets/heart.svg`, `star.svg`, `coin.svg`, `web.svg`, `data.svg`, `mobile.svg`, `git.svg`, `bot.svg` | Iconos originales reutilizables |
| `tools/arcade.py` | Generador del sistema gráfico |
| `tools/generar_recursos.py` | Punto de entrada para regenerar los recursos |
| `docs/ashakids.md`, `jmp.md`, `edukids.md`, `utpliteapp.md`, `gamelab.md` | Casos de estudio conservados con aportes y limitaciones |
| `docs/IMPLEMENTACION.md` | Informe actualizado de implementación |

Los siete recursos anteriores se rediseñaron; los recursos complementarios y el módulo arcade se añadieron. Se conservaron los casos de estudio y los archivos existentes. Las imágenes son ilustraciones editoriales, no capturas ficticias de productos.

Para regenerar: `python tools/generar_recursos.py`. Requiere Python, Pillow y una fuente del sistema Segoe UI o DejaVu Sans para los textos pequeños. La fuente pixelada se dibuja desde glifos definidos en el generador. No utiliza red, no instala dependencias y solo escribe recursos con nombres definidos en `assets/`.

## Animación y compatibilidad

Se utilizan GIF locales porque GitHub documenta soporte para GIF y advierte que la vista de SVG no admite animación: [formatos y limitaciones](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files).

- Cabecera: 21.813 bytes; robot y elementos decorativos con movimiento suave. El texto queda estable.
- Intereses: 4.330 bytes; escritura progresiva de una frase sobre desarrollo, diseño y gestión.
- Separador: 10.917 bytes; una estrella recorre una línea.

Cada animación dura 4.000 ms y se reproduce una vez, sin extensión de repetición infinita. No hay parpadeos rápidos, servicios de escritura externos ni animaciones de estadísticas.

Cada GIF tiene un PNG alternativo seleccionado con `<picture>` y `prefers-reduced-motion: reduce`. El [formato picture documentado por GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github) se usó sin CSS o JavaScript en el README. Su renderizador conservó los tres elementos picture y las tres reglas de movimiento reducido en la comprobación.

Todos los recursos utilizados tienen texto alternativo. Los conceptos relevantes también aparecen como texto Markdown. El enlace final permite abrir la cabecera estática.

## Proyectos y atribución

ASHAKids destaca por el origen de la idea desde EduKids y el aporte principal a la landing. JMP muestra trabajo en frontend, backend y flujos operativos. EduKids documenta la primera etapa. UTPLiteApp aporta experiencia colaborativa Android.

GAMELAB 4.0 aparece en Quest log como experiencia de equipo. La usuaria confirmó participación en distintas tareas y diseño de la propuesta de juego del equipo sobre Threadbare. El repositorio es un fork del proyecto de Endless, cuyos créditos y licencias se conservan. Está pendiente enlazar evidencia específica de su aporte; no se atribuyen cargos ni autoría del juego base.

Los README públicos de ASHAKids, JMP, EduKids y Threadbare se volvieron a consultar. UTPLiteApp se presenta con la evidencia de código y commits de la revisión anterior; no se inventa un README original inexistente.

MirrorMind sigue fuera de los destacados mientras se revisa el posible secreto señalado en Jenkinsfile. No se reproduce el valor ni se interviene ese repositorio. ProyectoHeDe puede añadirse después de precisar el aporte personal. Los proyectos no accesibles no se describen como revisados o modificados.

JMP se presenta sin datos empresariales, esquemas internos, credenciales, endpoints privados ni capturas de operación. No se han copiado imágenes o código de terceros.

## Comprobaciones

- 64 referencias revisadas: rutas, imágenes y anclas locales correctas.
- Los 19 enlaces externos únicos respondieron HTTP 200.
- 19 SVG válidos, sin scripts, referencias externas o animaciones internas.
- Tres GIF verificados: duración, fotogramas y ausencia de bucle infinito; sus alternativas PNG existen.
- Previsualización en navegador a 1100 y 390 píxeles, en claro y oscuro: imágenes cargadas y sin desbordamiento horizontal.
- Movimiento reducido: el navegador seleccionó los tres PNG en las cuatro combinaciones de tamaño y tema.
- Inspección visual de la cabecera y las vistas de escritorio y móvil.
- Revisión de patrones seleccionados de credenciales y espacios al final de línea, sin incidencias. Esto no sustituye una auditoría completa de secretos.
- Estado Git revisado antes de publicar: solo documentación, recursos y generadores propios del perfil; se preparó una primera versión sin cambios en aplicaciones.

La previsualización utiliza estilos aproximados de lectura de GitHub. La compatibilidad del marcado se comprobó con su renderizador, pero falta revisar el perfil publicado y el comportamiento de las imágenes alojadas allí. No se ejecutaron las aplicaciones ni sus pruebas.

## Pendientes

El repositorio de destino es `amaximilianorodri/amaximilianorodri`. README, assets y docs conservan sus rutas relativas. GitHub exige que el repositorio del perfil sea público: [requisitos oficiales](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme). Se creó un repositorio público nuevo para este fin con autorización de la usuaria; no se cambió la visibilidad de repositorios existentes.

Solo se utiliza la cuenta GitHub como contacto verificado. Las capturas reales de ASHAKids, EduKids y UTPLiteApp pueden prepararse después de comprobar permisos y datos. Para JMP, cualquier captura requiere autorización empresarial y datos sintéticos. No se insertaron imágenes inexistentes.

Para ampliar GAMELAB conviene enlazar un documento de diseño, una rama, cambios o una entrega del equipo que muestre el trabajo confirmado. Los fijados y la biografía de la cuenta siguen sin modificarse.
