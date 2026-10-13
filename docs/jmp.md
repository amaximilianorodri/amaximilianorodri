# JMP · Mi participación en un sistema de inventario

## Propósito

JMP-PINGUS-INVENTARIO es un proyecto colaborativo orientado a organizar materiales y procesos operativos. Esta presentación describe mi experiencia de desarrollo y las funciones observables en el código público, sin reproducir información empresarial, datos de usuarios o capturas de operaciones.

## Funciones identificadas

- Solicitudes de materiales.
- Devoluciones y actualización de información de inventario.
- Generación de documentos PDF.
- Perfiles y pantallas según las necesidades del sistema.
- Servicios de acceso a datos y migraciones SQL.

El repositorio incluye pruebas automatizadas. Su existencia no equivale a afirmar que todas las pruebas se han ejecutado o que el sistema está certificado para producción.

## Mi contribución

Participé en distintas iteraciones del frontend y backend. Mis aportes incluyen cambios en solicitudes, devoluciones, documentos PDF y perfiles, además de ajustes en servicios y lógica de datos.

Estos cambios permiten consultar parte de ese trabajo:

- [Flujo de solicitudes, PDF y devoluciones](https://github.com/luisteransaucedo18-coder/JMP-PINGUS-INVENTARIO/commit/b316269).
- [Presentación del PDF de materiales](https://github.com/luisteransaucedo18-coder/JMP-PINGUS-INVENTARIO/commit/128070e).
- [Ajustes del perfil](https://github.com/luisteransaucedo18-coder/JMP-PINGUS-INVENTARIO/commit/d5b2363).

Confirmé que esos commits firmados con mi nombre son míos. Algunos no aparecen vinculados automáticamente a mi cuenta de GitHub. Esta participación no implica autoría exclusiva de la arquitectura ni de todo el proyecto.

## Arquitectura y tecnologías

La interfaz utiliza **React, TypeScript, Tailwind CSS y Vite**. El acceso a datos se organiza en servicios por funcionalidad y utiliza **Supabase y PostgreSQL**, con funciones de base de datos y migraciones SQL. La generación de documentos utiliza **pdf-lib**.

Esta descripción es deliberadamente general: no incluye esquemas internos, endpoints, credenciales, reglas operativas detalladas ni datos de la empresa.

## Estado y límites

El código contiene una implementación con pruebas y migraciones. La revisión estática no acredita su despliegue, la aplicación de todas las migraciones en una base de datos real ni los resultados de operación.

La documentación del proyecto señala dependencias de un esquema previo para las migraciones. Por eso no se ofrecen aquí instrucciones que prometan reproducir todo el sistema desde una base vacía.

## Créditos y presentación pública

El desarrollo es colaborativo. El historial del repositorio distingue las contribuciones del equipo.

Esta página es un caso de estudio propio y resumido; no reemplaza ni modifica la documentación del repositorio empresarial. Cualquier futura captura o ampliación con detalles de operación deberá contar con la autorización correspondiente.

[Repositorio público](https://github.com/luisteransaucedo18-coder/JMP-PINGUS-INVENTARIO) · [Volver al perfil](../README.md)
