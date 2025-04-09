import pandas as pd
import os

def convertir_informatica_csv(entrada, salida):
    # Leer archivo
    df = pd.read_csv(entrada, encoding="latin1")  # por si hay ñ o acentos raros

    # Normalizar columnas (por si hay espacios raros)
    df.columns = [col.strip() for col in df.columns]

    # Renombrar columnas y quedarnos con las necesarias
    df = df.rename(columns={
        "Subject": "Subject",
        "Start Date": "Day",
        "Start Time": "Start",
        "End Time": "End",
        "Location": "Room"
    })

    # Función robusta para formatear HH.MM → HH:MM
    def normalizar_hora(hora):
        try:
            h = float(str(hora).strip().replace(",", "."))
            hora_entera = int(h)
            minutos = int(round((h - hora_entera) * 60))
            return f"{hora_entera:02d}:{minutos:02d}"
        except:
            return ""

    df["Start"] = df["Start"].apply(normalizar_hora)
    df["End"] = df["End"].apply(normalizar_hora)

    # Filtrar columnas necesarias y reordenar
    df_final = df[["Day", "Start", "End", "Subject", "Room"]]

    # Guardar CSV final
    df_final.to_csv(salida, index=False)
    print(f"✅ Archivo convertido guardado en: {salida}")

# Ruta del CSV combinado de informática
input_file = "dataI/horario_informatica.csv"
output_file = "dataI/horario_informatica_final.csv"

convertir_informatica_csv(input_file, output_file)
