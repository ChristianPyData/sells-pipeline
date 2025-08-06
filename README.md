# 🧼 Ventas Data Pipeline

Pipeline simple de procesamiento de datos de ventas con control de calidad, generación de KPIs, carga a DuckDB y automatización con n8n.

## ⚙️ ¿Qué hace?

1. Carga datos desde un CSV.
2. Aplica validaciones:
   - Fechas inválidas
   - Montos negativos
   - IDs duplicados
   - Valores nulos
3. Genera un log de errores.
4. Crea un dataset limpio.
5. Calcula KPIs:
   - Total ventas
   - Promedio de ticket
   - Ticket más alto
   - Región más vendida
6. Guarda los datos limpios en DuckDB.
7. Automatización posible con n8n (schedule + mail/logs).

## 📊 Visualización en Power BI

- Total de ventas por mes
- Ticket promedio por canal
- Errores detectados (dataset control de calidad)

## 💥 Impacto

- Simula entorno real de un Data Engineer.
- Valida datos antes de ser visualizados.
- Fácil de escalar a BigQuery, APIs u otros.
