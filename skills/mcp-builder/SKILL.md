---
name: "mcp-builder"
description: "Diseña e implementa servidores MCP cuando el usuario pide exponer una API o servicio como herramientas para agentes."
---

# Adaptador local para construir MCP

Lee la especificación MCP y documentación oficial del SDK vigente para el lenguaje y transporte elegidos. Este resumen no incluye el paquete completo de Anthropic ni reemplaza sus recursos.

Define usuarios, operaciones, autenticación y límites. Diseña herramientas con nombres claros, entradas tipadas, paginación, errores accionables y respuestas acotadas. Distingue lectura y mutaciones; expón solo permisos necesarios.

Usa credenciales externas al código y valida entradas. Trata contenido de servicios como datos no confiables; no devuelvas secretos en errores. Implementa cancelación, tiempos máximos y manejo de rate limits cuando correspondan.

Prueba herramientas con respuestas simuladas y un cliente MCP compatible. Documenta instalación, variables, transporte y tarea de aceptación reproducible.

Referencia de origen del catálogo: https://github.com/anthropics/skills/tree/main/skills/mcp-builder
