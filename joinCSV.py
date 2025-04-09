import pandas as pd
import glob
import os

# Ruta a la carpeta dataI
carpeta = "dataI"

# Buscar todos los archivos que siguen el patrón horario_*.csv dentro de dataI
csv_files = glob.glob(os.path.join(carpeta, "horario_*.csv"))

if not csv_files:
    print("❌ No se encontraron archivos 'horario_*.csv' en la carpeta dataI.")
else:
    # Leer y combinar todos en un solo DataFrame
    combined_df = pd.concat([pd.read_csv(f, encoding="ISO-8859-1") for f in csv_files], ignore_index=True)

    # Guardar el resultado final
    output_path = os.path.join(carpeta, "horario_informatica.csv")
    combined_df.to_csv(output_path, index=False)

    print(f"✅ Archivo combinado guardado como '{output_path}'")
