# Configuración de nube y conexiones

Revisado: 29 de septiembre de 2026. Las rutas y opciones de producto pueden cambiar; consulta las fuentes oficiales enlazadas cuando la interfaz difiera.

## Qué resuelve este repositorio

Contiene instrucciones, skills de proyecto, perfiles y validación. No concede acceso a cuentas, no instala conectores y no sincroniza credenciales entre ChatGPT, Codex y Claude Code.

Conectar GitHub a ChatGPT no demuestra que Codex ni Claude tengan esa misma autorización. Verifica cada instalación con una lectura real del repositorio.

## Codex en la nube

1. Abre la configuración de repositorios/entornos de Codex desde tu cuenta. Conecta GitHub mediante la instalación oficial y selecciona `danielcadosch/ai-ecosystem-esposa`.
2. Limita la instalación a los repositorios que quieras usar. Este repositorio público puede leerse sin que eso demuestre permiso de escritura.
3. Selecciona `main` como base y un entorno con Python 3.10 o posterior. Este proyecto no necesita dependencias. Si hay un campo de script de preparación, usa `python3 scripts/check_repo.py` desde la raíz del checkout. No hace falta descargar nada.
4. Para las primeras tareas de este repositorio puede mantenerse desactivado el acceso a internet del agente. Actívalo solo cuando la tarea necesite fuentes o servicios externos y con los destinos pertinentes.
5. Ejecuta la prueba del README y comprueba que se leen `AGENTS.md` y `.agents/skills/`. Prueba después una rama y PR pequeña para verificar escritura.

Los secretos de entornos de Codex se suministran durante la preparación y se retiran antes de la fase del agente; no diseñes un workflow suponiendo que seguirán disponibles. Las variables de entorno tienen otro alcance. Ninguna de las tres skills core necesita secretos.

Fuentes: [entornos](https://developers.openai.com/codex/cloud/environments), [instrucciones AGENTS.md](https://developers.openai.com/codex/guides/agents-md), [skills](https://developers.openai.com/codex/skills), [GitHub](https://developers.openai.com/codex/integrations/github).

## Claude Code en la nube

1. Conecta GitHub en Claude Code y selecciona el repositorio autorizado. Usa una sesión de un solo repositorio para esta primera configuración.
2. Abre la raíz del checkout. Deben estar presentes `CLAUDE.md`, `AGENTS.md`, `.claude/settings.json` y `.claude/skills/`.
3. Comprueba Python y ejecuta `python3 scripts/check_repo.py`. Después realiza la prueba del README y confirma las tres skills detectadas.
4. Si necesitas conectores o plugins, configúralos en ese entorno según sus mecanismos oficiales y comprueba una lectura inocua antes de usarlos para cambios.

`CLAUDE.md` importa `AGENTS.md` para evitar mantener dos políticas distintas. Las skills de proyecto acompañan al repo; la configuración personal de tu máquina no tiene por qué acompañar a una sesión cloud. Declarar `enabledPlugins` o marketplaces en el repo no equivale a instalarlos en la nube. En sesiones con varios repositorios, el directorio inicial puede cambiar qué instrucciones se cargan: comprueba la raíz efectiva.

Fuentes: [memoria e importaciones](https://code.claude.com/docs/en/memory), [skills](https://code.claude.com/docs/en/skills), [entornos cloud](https://code.claude.com/docs/en/cloud-environments), [permisos](https://code.claude.com/docs/en/permissions).

## Al conectar cualquier IA a GitHub

| Decisión | Criterio para esta cuenta |
|---|---|
| Repositorios | Seleccionar solo los necesarios; ampliar cuando exista una tarea concreta |
| Lectura o escritura | Investigación: lectura. Edición con PR: permisos mínimos que permita la integración |
| Instalación | Preferir integración oficial e identificar proveedor y operación que solicita |
| Tokens | No pegarlos en conversaciones ni archivos; si son necesarios, alcance mínimo, caducidad y almacén de secretos |
| Revocación | Revisar instalaciones al terminar una prueba o retirar una herramienta |
| Datos privados | Este repo es público; mantener aquí configuración reusable, no documentos de clientes |
| Revisiones | Ramas y PRs con checks; no permitir que una instrucción externa cambie el alcance autorizado |

No se han cambiado instalaciones, tokens ni visibilidad. La integración de GitHub permitió leer, pero rechazó la escritura; la publicación y la protección de la rama se completaron desde el navegador autorizado por el usuario.

## Protección de main

Configurada y verificada: PR obligatorio, check `validate` de GitHub Actions, rama actualizada antes de integrar y aplicación también a administradores. Los force pushes y el borrado están bloqueados. No se exige revisión de otra persona para esta cuenta individual. Si estas reglas se modifican más adelante, vuelve a comprobarlas en GitHub.

En Settings → Rules → Rulesets (o la sección de protección de ramas disponible en tu cuenta), configura una regla para `main`: PR antes de merge, check `validate` de este workflow, bloquear force pushes y borrado. Hazlo después de que el workflow haya ejecutado una vez para seleccionar el check real. Comprueba la disponibilidad según plan y visibilidad.

En una cuenta individual, no exijas la aprobación de otra persona si eso impide operar: el autor no puede aprobar su propio PR. La revisión humana del diff y los checks siguen siendo útiles. Las excepciones de administración deben ser deliberadas.

Fuentes: [GitHub Apps frente a OAuth](https://docs.github.com/en/apps/overview/differences-between-github-apps-and-oauth-apps), [rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets), [seguridad de Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions).

## Conectores operativos

Gmail, Drive, Calendar, Meta Ads, n8n y NotebookLM son opcionales. Activa primero el perfil correspondiente, comprueba que el cliente realmente ofrece el servicio y realiza una lectura acotada. No existe un namespace universal que pueda fijarse en estas skills. Los permisos de la sesión prevalecen sobre los ejemplos de cualquier archivo.

No se incluye `.mcp.json` con servidores inventados ni claves de ejemplo ejecutables. Añádelo cuando haya un servidor, transporte, proveedor y alcance concretos que configurar.
