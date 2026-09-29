# Estado y pruebas de aceptación

Fecha de preparación: 29 de septiembre de 2026.

## Preparado en el repositorio

- Instrucciones compartidas y entrada específica de Claude.
- 24 guías con encabezados válidos y procedencia documentada.
- Cinco perfiles; `core` selecciona tres skills, materializadas para ambos clientes.
- Validación de estructura, JSON, perfiles, enlaces locales y sincronización.
- Pruebas para cambios de perfil, colisiones, modificaciones locales y rutas no permitidas.
- Workflow de GitHub Actions con permisos de lectura y checkout fijado por SHA.

El resultado de CI de cada revisión se consulta en Actions o en sus checks de PR. Un check de estructura no demuestra por sí solo la calidad de las respuestas de un modelo.

## Evidencia de preparación

En la revisión inicial pasaron `check_repo.py`, las ocho pruebas de `unittest` y la validación del encabezado de las 24 skills con el validador de skill-creator del entorno de preparación. Este último es una comprobación adicional del autor y no una dependencia del proyecto.

Se realizaron dos ejercicios independientes de instrucciones, sin servicios externos:

- Reporte con dos campañas y una fila de total: calculó ratios sobre totales, no duplicó el gasto y trató denominadores cero e ingresos desconocidos como N/D cuando correspondía.
- Brief y tres copies para un curso con datos incompletos: produjo entregables, distinguió supuestos y pendientes y evitó inventar precio, fechas o testimonios.

Estos ejercicios prueban el comportamiento de las instrucciones en el entorno de preparación. No sustituyen pruebas de detección nativa ni autenticación en las sesiones cloud de cada producto.

## Pruebas dentro de cada cliente

| Prueba | Criterio observable |
|---|---|
| Detección | El cliente identifica las tres skills core y las instrucciones compartidas |
| Reporte | Gasto 120, impresiones 10.000, clics 200, compras 8 e ingresos 400: CTR 2%, CPC 0,60, CPM 12, CPA 15 y ROAS ≈ 3,33; moneda y atribución explícitas |
| Datos incompletos | Sin clics o ingresos, muestra N/D en métricas dependientes |
| Brief | Borrador con pendientes diferenciados; no inventa testimonios ni garantías |
| Copy | Variantes basadas en hechos disponibles; no publica ni inventa oferta |
| Escritura GitHub | Crea una rama/PR autorizada y confirma el estado remoto |

Las conexiones y la detección nativa en tus sesiones de Codex/Claude requieren verificarse allí. Las comprobaciones locales no autentican esos productos.

## Pendiente de configuración de cuenta

- Selección de repositorio y entorno dentro de cada producto, según las conexiones existentes.
- Protección de `main` mediante ajustes de GitHub.
- Conectores operativos y plugins solo cuando exista una necesidad concreta.

Consulta [CLOUD_SETUP.md](CLOUD_SETUP.md). No se registran como completadas operaciones de cuenta que esta integración no permite realizar.
