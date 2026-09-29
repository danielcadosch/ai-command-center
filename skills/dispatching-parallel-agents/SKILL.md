---
name: "dispatching-parallel-agents"
description: "Distribuye investigaciones o tareas independientes cuando el usuario solicita trabajo con agentes en paralelo y el entorno lo permite."
---

# Agentes en paralelo

Comprueba autorización y disponibilidad de agentes. Delega únicamente tareas independientes con resultados verificables; ejecuta de forma secuencial cuando compartan estado mutable o dependencias.

Para cada tarea define objetivo, datos, límites y salida. Separa archivos de escritura; evita exponer credenciales o contexto innecesario. Limita concurrencia según recursos y beneficio esperado.

Recoge evidencia, resuelve discrepancias y valida la integración. No declares éxito por el solo reporte de un agente. Si la tarea es pequeña, ejecutarla directamente puede ser más eficaz.

Adaptador local; referencia histórica: https://github.com/obra/superpowers
