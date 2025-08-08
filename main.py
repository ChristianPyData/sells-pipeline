import pandas as pd
import os
from datetime import datetime
import duckdb  

FECHA = datetime.now().strftime("%Y%m%d")
PATH = "./data/ventas.csv"

df = pd.read_csv(PATH)
errores =[]

print(" Pipeline ejecutado con éxito.")
# Fecha inválida
df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
errores.append(df[df['fecha'].isna()].assign(error='Fecha inválida'))

# Montos negativos
errores.append(df[df['monto'] < 0].assign(error='Monto negativo'))

# IDs duplicados
errores.append(df[df.duplicated('id')].assign(error='ID duplicado'))

# Valores nulos
errores.append(df[df.isna().any(axis=1)].assign(error='Nulos'))

# Unir errores
errores_df = pd.concat(errores).drop_duplicates()
#crear carpetas si no existen
os.makedirs("logs", exist_ok=True)
os.makedirs("data/limpio", exist_ok=True)
os.makedirs("kpis", exist_ok=True)

# Guardar log de errores
errores_df.to_csv(f"logs/errores_{FECHA}.csv", index=False)

# Dataset limpio
df_limpio = df[~df.index.isin(errores_df.index)]
df_limpio.to_csv(f"data/limpio/ventas_limpias_{FECHA}.csv", index=False)

# KPIs
kpis = {
    "fecha_corte": FECHA,
    "total_ventas": df_limpio["monto"].sum(),
    "promedio_ventas": df_limpio["monto"].mean(),
    "ticket_maximo": df_limpio["monto"].max(),
    "region_top": df_limpio.groupby("region")["monto"].sum().idxmax()
}
pd.DataFrame([kpis]).to_csv(f"kpis/resumen_kpis_{FECHA}.csv", index=False)

# Carga a DuckDB
con = duckdb.connect("db/ventas.db")
tabla = f"ventas_limpias_{FECHA}"

con.execute(f"""
CREATE TABLE IF NOT EXISTS {tabla} AS
SELECT * FROM read_csv_auto('data/limpio/ventas_limpias_{FECHA}.csv')
""")
con.close()

print("Archivos creados correctamente.")

