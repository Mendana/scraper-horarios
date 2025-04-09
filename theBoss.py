import pandas as pd

def unir_infor_mates(path_infor, path_mates, path_salida):
    try:
        df_infor = pd.read_csv(path_infor)
        df_mates = pd.read_csv(path_mates)

        # Unirlos
        df_total = pd.concat([df_infor, df_mates], ignore_index=True)

        # Parsear fechas y horas
        df_total["Day"] = pd.to_datetime(df_total["Day"], dayfirst=True, errors="coerce")
        df_total["Start"] = pd.to_datetime(df_total["Start"], format="%H:%M", errors="coerce").dt.time

        # Ordenar
        df_total = df_total.sort_values(by=["Day", "Start"])

        # Volver a texto
        df_total["Day"] = df_total["Day"].dt.strftime("%d/%m/%Y")
        df_total["Start"] = df_total["Start"].apply(lambda t: t.strftime("%H:%M") if pd.notnull(t) else "")

        df_total.to_csv(path_salida, index=False)
        print(f"✅ CSV final combinado guardado en: {path_salida}")
    except Exception as e:
        print(f"❌ Error al combinar: {e}")

# Ejecutar
unir_infor_mates(
    "dataI/horario_informatica_final.csv",
    "dataM/horario_matematicas_final.csv",
    "horario_final_completo.csv"
)
