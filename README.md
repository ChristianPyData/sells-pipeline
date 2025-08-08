# 🧼 Ventas Data Pipeline

📌 Qué hace:
Este script automatiza un pipeline de análisis y generación de reportes. Ejecuta un conjunto de tareas en Python que incluyen carga de datos, análisis, visualización y creación de archivos finales, todo dentro de una estructura organizada por carpetas. Al finalizar, imprime un mensaje de éxito, permitiendo integración directa con flujos workflows de n8n, los cuales tras esto enviarán vía Gmail los resúmenes KPIs y los errores log presentados.

⚡ Impacto medible:

Ahorro de tiempo: El proceso que antes tomaba varias horas en realizarse manualmente, ahora se ejecuta en segundos desde una única acción en n8n, lo cual da como resultado un proceso de alrededor de 10 segundos que ahorra 230 horas humanas anuales sin errores.

Reducción de errores: Minimiza el riesgo de fallos humanos al estandarizar el pipeline.

Integración directa con automatizaciones: Listo para integrarse con flujos de notificación o envío automático (correo, almacenamiento, backup, etc.) sin intervención humana.

Escalabilidad: Se adapta fácilmente para múltiples fuentes de datos o múltiples reportes, sin modificar la lógica base.


🧠 Habilidades aplicadas:

Python avanzado: Manejo de rutas dinámicas, generación de archivos, visualización, y automatización de scripts.

Pandas avanzado: Manejo e integración de Dataframes para la manipulación de los datos para posteriormente lógica aplicada a ellos.

DuckDB: Consultas y recolección de datos vía conexión SQL desde Python.

Automatización con n8n: Orquestación del código con nodos como Execute Command, permitiendo integración low-code con otros sistemas.

Control de versiones y estructura modular: Organización del proyecto por carpetas y scripts independientes.

DevOps básico: Uso de entornos virtuales y ejecución desde consola automatizada.

Lógica de reporting: Preparación de reportes generados automáticamente con análisis y resultados listos para envío.
