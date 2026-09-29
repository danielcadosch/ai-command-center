# Trabajo cotidiano y mantenimiento

## Codex y Claude sobre el mismo proyecto

GitHub mantiene el estado compartido. Cada agente trabaja en su rama o checkout; una herramienta puede implementar y otra revisar el diff. Evita dos agentes modificando los mismos archivos simultáneamente sin asignación explícita.

Una petición útil:

> Lee AGENTS.md y el perfil activo. Implementa [objetivo] en una rama, conserva cambios ajenos, ejecuta las comprobaciones pertinentes y abre un PR con lo observado. No actives servicios externos fuera del alcance de esta tarea.

Para una segunda revisión:

> Revisa el PR [número] contra [criterios]. Identifica fallos concretos con evidencia. No cambies archivos ni publiques comentarios sin que te lo pida; entrega el análisis aquí.

No es necesario instalar un puente entre modelos para coordinarse mediante PRs. Si más adelante se instala uno, delimita número de rondas, coste y criterio de parada para evitar revisiones circulares.

## Editar y sincronizar

1. Edita las fuentes en `skills/`.
2. Actualiza `configs/provenance.json` si cambia el origen y `configs/skills.json` si cambia el catálogo.
3. Ejecuta `python3 scripts/sync_skills.py`.
4. Ejecuta `python3 scripts/check_repo.py` y las pruebas si cambian scripts/perfiles.
5. Revisa el diff, publica en una rama y comprueba Actions antes de integrar.

Si una copia generada fue editada, el script se detendrá para no perderla. Guarda el cambio en la fuente, revisa el diff y restaura solo esa copia generada al estado conocido antes de sincronizar. No borres carpetas completas para resolver una colisión.

El manifiesto `configs/generated-skills.json` registra hashes de los archivos gestionados. Cambiar de perfil retira solo esos archivos y conserva los archivos ajenos. Pueden quedar carpetas vacías, que no contienen una skill activa.

## Actualizar

Revisa periódicamente fuentes oficiales, cambios de formatos y necesidad de cada skill. Dependabot propone actualizaciones del action de checkout; revisa versión y checks antes de integrar. No hay actualización automática de plugins ni código upstream.

Para revertir una mejora utiliza un commit de reversión mediante el mismo flujo de PR. Los cambios anteriores siguen en Git; no hace falta reescribir historia.
