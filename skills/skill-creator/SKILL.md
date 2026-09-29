---
name: "skill-creator"
description: "Crea o mejora skills de este repositorio cuando el usuario pide nuevas instrucciones reutilizables, correcciones o evaluaciones."
---

# Crear skills del repositorio

Define una tarea recurrente y ejemplos reales de activación. Comprueba si ya existe una capacidad equivalente. Mantén una skill por responsabilidad útil.

Edita la fuente en skills/<nombre>/SKILL.md. Incluye frontmatter con name y description; la descripción debe indicar cuándo usarla. Mantén el cuerpo conciso, con decisiones, límites, verificaciones y recursos solo cuando aporten valor. No incluyas secretos ni namespaces de una sesión.

En este catálogo los dos campos del encabezado se escriben como strings JSON, un subconjunto de YAML, para validarlos sin dependencias. Registra la skill en configs/provenance.json y en los perfiles correspondientes de configs/skills.json.

Prueba con una tarea normal, datos incompletos y una petición fuera de alcance. Cuando el entorno permita subagentes, usa una ejecución independiente con la tarea y la skill, sin proporcionar la respuesta esperada.

Ejecuta python3 scripts/sync_skills.py y python3 scripts/check_repo.py. Publica el cambio mediante el flujo Git del proyecto; no copies configuraciones globales como paso incidental.

Esta es una guía local. Referencia del catálogo original: https://github.com/anthropics/skills/tree/main/skills/skill-creator
