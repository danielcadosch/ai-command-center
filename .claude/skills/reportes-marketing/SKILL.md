---
name: "reportes-marketing"
description: "Analiza métricas de campañas, gasto, CPC, CPM, CPA y ROAS; úsala para informes de marketing y comparaciones de rendimiento con datos aportados o conectados."
---

# Reportes de marketing

1. Define cuenta, período, moneda, zona horaria, objetivo y ventana de atribución con el contexto disponible. Pide solo datos que cambien la conclusión. Identifica fuente y fecha de extracción; distingue datos observados de supuestos.
2. Usa archivos aportados o el conector realmente disponible. No presupongas acceso a Meta ni a Drive. Si faltan datos, entrega la estructura y las carencias concretas sin inventar resultados.
3. Comprueba duplicados, granularidad (campaña/conjunto/anuncio), totales, períodos comparables, gasto y unidades. No sumes filas de distintos niveles que representen el mismo gasto. No sumes alcance único entre segmentos solapados.
4. Calcula sobre totales compatibles: CTR = clics/impresiones × 100; CPC = gasto/clics; CPM = gasto/impresiones × 1000; CPA = gasto/conversiones; ROAS = ingresos atribuidos/gasto. Especifica qué tipo de clic y conversión se usa. Denominador cero o dato ausente: N/D, nunca cero inventado. No promedies ratios sin ponderarlos.
5. Para variaciones: (actual/anterior − 1) × 100; base cero: N/D y diferencia absoluta. En tasas diferencia puntos porcentuales de cambio relativo. No mezcles monedas ni ventanas de atribución sin normalización documentada.
6. Entrega resumen, tabla de métricas con fórmula/unidad, calidad de datos, hipótesis y acciones priorizadas. Separa correlación de causalidad. No declares ganadores estadísticos solo por diferencias descriptivas.
7. Genera el informe en el formato solicitado; guardar en Drive requiere que el destino esté identificado y el conector exista. Analizar no autoriza cambiar presupuestos ni campañas.
