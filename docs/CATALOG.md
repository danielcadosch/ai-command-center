# Catálogo y curaduría

La fuente editable es `skills/`. Las copias del perfil activo se generan para ambos clientes. Los encabezados usan `name` y `description` escritos como strings JSON, válidos en YAML; este formato acotado permite validación sin instalar librerías.

## Las 24 guías

| Grupo | Skills |
|---|---|
| Core | reportes-marketing, brief-creativo, copy-marketing |
| Marketing adicional | ab-testing-ads, audiencias-meta, calendario-contenido, email-marketing, meta-ads, x-twitter-growth |
| Integraciones | github, gmail, google-calendar, google-drive, n8n, notebooklm |
| Desarrollo y curaduría | agentation, find-skills, mcp-builder, skill-creator, skill-judge, writing-plans, verification-before-completion, subagent-driven-development, dispatching-parallel-agents |

## Procedencia

[provenance.json](../configs/provenance.json) conserva la referencia del catálogo anterior y el commit de partida. Las versiones actuales son guías locales revisadas, no distribuciones completas ni certificadas de Anthropic, OpenAI o terceros. No se conoce la revisión upstream exacta de las copias históricas; se registra `null` en vez de inventar un SHA.

Las referencias a fuentes no instalan paquetes ni conceden licencias. No se añadió una licencia global que pretendiera relicenciar material de terceros. Al importar código o archivos upstream en el futuro, fija un commit, conserva el texto de licencia y avisos aplicables y registra los archivos incorporados. Consulta [NOTICE.md](../NOTICE.md).

## Qué instalar después

El punto de partida deliberado es tres skills sin dependencias. Amplía cuando una tarea real lo necesite.

| Necesidad | Candidato | Decisión inicial |
|---|---|---|
| Usar Codex desde Claude Code | [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) | Evaluar primero el plugin oficial en un entorno compatible; no instalado por este repo |
| Usar Claude Code desde Codex | [sendbird/cc-plugin-codex](https://github.com/sendbird/cc-plugin-codex) | Alternativa comunitaria; revisar versión, autenticación y límites |
| Flujos de ingeniería | [obra/superpowers](https://github.com/obra/superpowers) | Adoptar módulos concretos; evitar solapamientos con las guías locales |
| Operaciones GitHub por MCP | [github/github-mcp-server](https://github.com/github/github-mcp-server) | Solo si la integración nativa es insuficiente |
| Navegador automatizado | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Añadir para tareas de navegador con alcance explícito |
| Más skills | [openai/skills](https://github.com/openai/skills), [anthropics/skills](https://github.com/anthropics/skills) | Importar selectivamente con licencia y revisión fijada |
| Orquestación de modelos | [nyldn/claude-octopus](https://github.com/nyldn/claude-octopus) | Posponer hasta medir necesidad, costes y complejidad |

No se fija aquí una versión futura como 'la mejor'. Antes de instalar: revisar release, incidencias, dependencias, permisos, licencia y compatibilidad cloud. No asumir que un plugin disponible en el CLI funciona igual en una sesión web.

## Criterios para nuevas skills

1. Tarea recurrente concreta y descripción que permita activarla correctamente.
2. Ventaja observable frente a capacidades ya existentes.
3. Instrucciones cortas, sin promesas falsas ni herramientas de sesión fijadas.
4. Procedencia y permisos claros; scripts inspeccionados si existen.
5. Una prueba representativa, otra con datos incompletos y ausencia de efectos externos inesperados.
6. Perfil seleccionado, copias sincronizadas y comprobaciones verdes.
