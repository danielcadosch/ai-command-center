# AI Command Center

Espacio de trabajo de Daniel para marketing, automatización y desarrollo asistidos por IA. Las instrucciones y skills viajan con el repositorio y se mantienen desde una sola fuente.

## Empieza aquí

1. Abre este repositorio en Codex o Claude Code, desde su raíz.
2. Pide: **«Lee las instrucciones del proyecto y dime qué skills del perfil activo puedes usar. No cambies servicios externos.»**
3. Prueba: **«Usa reportes-marketing: gastamos 120 USD, tuvimos 10.000 impresiones, 200 clics, 8 compras y 400 USD de ingresos atribuidos. Calcula las métricas y señala qué contexto falta.»**

Las tres skills iniciales ya están incluidas para ambos clientes: **reportes-marketing**, **brief-creativo** y **copy-marketing**. Tenerlas disponibles no exige conectar servicios ni compartir credenciales. Confirma su detección efectiva en cada cliente.

## Organización

| Ruta | Función |
|---|---|
| [AGENTS.md](AGENTS.md) | Instrucciones compartidas |
| [CLAUDE.md](CLAUDE.md) | Entrada de Claude; importa las instrucciones compartidas |
| `skills/` | Fuente canónica de las 24 skills |
| `.agents/skills/` | Copias del perfil activo para Codex |
| `.claude/skills/` | Copias del perfil activo para Claude Code |
| [configs/skills.json](configs/skills.json) | Perfiles y selección activa |
| [configs/provenance.json](configs/provenance.json) | Procedencia de cada guía |
| `scripts/`, `tests/` | Sincronización y comprobaciones locales |
| `.github/workflows/validate.yml` | Comprobaciones en GitHub Actions |

## Perfiles

| Perfil | Skills | Uso |
|---|---:|---|
| `core` | 3 | Reportes, briefs y copy; activo inicialmente |
| `marketing` | 9 | Core, experimentos, audiencias, calendario, email, Meta y X |
| `automation` | 9 | Core, GitHub, Gmail, Calendar, Drive, n8n y NotebookLM |
| `engineering` | 10 | Desarrollo, planes, verificación, skills, MCP y agentes |
| `full` | 24 | Catálogo completo; habilitar solo si aporta valor |

Pide al agente: **«Activa el perfil marketing, comprueba el repositorio y guarda el cambio en una rama.»** O ejecuta:

```bash
python3 scripts/sync_skills.py --profile marketing
python3 scripts/check_repo.py
```

El script modifica únicamente archivos gestionados dentro del proyecto. Conserva archivos ajenos y se detiene si una copia generada fue editada manualmente. La selección queda registrada en Git y aplica a ambos clientes. Una sesión abierta puede necesitar reiniciarse para redescubrir skills.

## Comprobaciones

Python 3.10 o posterior. No hay paquetes que instalar ni llamadas a servicios externos.

```bash
python3 scripts/check_repo.py
python3 -m unittest discover -s tests -v
```

En Windows sustituye `python3` por `py -3`. Al editar una skill, cambia `skills/<nombre>/SKILL.md` y ejecuta `python3 scripts/sync_skills.py` antes de verificar.

## Conectar y ampliar

- [Configuración de nube y conexiones](docs/CLOUD_SETUP.md)
- [Catálogo, procedencia y curaduría](docs/CATALOG.md)
- [Mantenimiento y trabajo entre Codex y Claude](docs/WORKFLOW.md)
- [Estado y pruebas de aceptación](docs/READINESS.md)
- [Atribuciones](NOTICE.md)

El antiguo `configs/settings.json` queda vacío por compatibilidad de ruta. No lo copies sobre tu configuración personal: modelos, plugins y credenciales pertenecen a cada entorno. La configuración de proyecto de Claude está en `.claude/settings.json`.
