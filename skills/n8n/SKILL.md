---
name: "n8n"
description: "Diseña, crea y depura workflows de n8n cuando el usuario solicita automatizaciones entre servicios, webhooks o tareas programadas."
---

# Automatización n8n

Inspecciona la instancia y capacidades disponibles. Consulta la referencia y esquemas de nodos reales antes de generar parámetros; nombres de herramientas y versiones cambian entre entornos.

Define disparador, entradas, transformaciones, salidas, credenciales necesarias, zona horaria y comportamiento ante duplicados/errores. Usa referencias a credenciales gestionadas; no incrustes secretos.

Prepara el workflow inactivo, valida estructura y prueba con datos sintéticos o un destino de prueba. Una ejecución de prueba puede enviar mensajes o consumir recursos: delimita esos efectos antes de correrla.

Activa/publica solo si el pedido autoriza esa puesta en marcha y las verificaciones relevantes pasaron. No publiques como consecuencia automática de crear un borrador. Comprueba estado y registra cómo pausar y recuperar ante errores.
