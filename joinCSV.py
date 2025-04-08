import pandas as pd
import glob

# Buscar todos los archivos que siguen el patrón horario_*.csv
csv_files = glob.glob("horario_*.csv")

# Leer y combinar todos en un solo DataFrame
combined_df = pd.concat([pd.read_csv(f, encoding="ISO-8859-1") for f in csv_files], ignore_index=True)

# Guardar el resultado final
combined_df.to_csv("horario_completo.csv", index=False)

print("✅ Archivo combinado guardado como 'horario_completo.csv'")
