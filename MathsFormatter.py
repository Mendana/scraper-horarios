import pandas as pd
import glob
import os
from datetime import datetime

def procesar_matematicas(data_folder, salida_final):
    archivos = glob.glob(os.path.join(data_folder, "*_Listado_de_clases.csv"))

    filas_finales = []

    for archivo in archivos:
        nombre_archivo = os.path.basename(archivo)
        cod_asig = nombre_archivo.split("_")[0]  # Ej: 'AI'

        print(f"📄 Procesando {nombre_archivo}...")

        try:
            # Leer saltando 3 filas de encabezado
            df = pd.read_csv(archivo, skiprows=3)
            df.columns = [c.strip() for c in df.columns]

            # Buscar columnas clave por nombre aproximado
            col_fecha = next((col for col in df.columns if "Fecha" in col), None)
            col_hora = next((col for col in df.columns if "Hora" in col), None)
            col_grupo = next((col for col in df.columns if "Grupo" in col), None)
            col_aula = next((col for col in df.columns if "Aula" in col), None)

            if not all([col_fecha, col_hora, col_grupo, col_aula]):
                print(f"❌ Saltando {nombre_archivo} por columnas faltantes.")
                continue

            # Filtrar solo filas útiles
            df = df[df[col_fecha].notna() & df[col_hora].notna() & df[col_grupo].notna()]

            for _, row in df.iterrows():
                try:
                    # Fecha → dd/mm/yyyy
                    fecha_raw = str(row[col_fecha]).split(" ")[0]
                    fecha = datetime.strptime(fecha_raw, "%Y-%m-%d").strftime("%d/%m/%Y")

                    # Hora → separar y normalizar
                    hora_raw = str(row[col_hora]).replace("h", "").replace("'", "").strip()
                    if "-" not in hora_raw:
                        continue
                    start_raw, end_raw = hora_raw.split("-")

                    def normalizar_hora(h):
                        h = h.strip()
                        h = h.replace(":", "")
                        if len(h) == 3:
                            h = "0" + h
                        return h[:2] + ":" + h[2:]

                    start = normalizar_hora(start_raw)
                    end = normalizar_hora(end_raw)

                    # Aula → quitar "Aula" y espacios
                    aula_raw = str(row[col_aula])
                    room = aula_raw.replace("Aula", "").strip()

                    grupo = str(row[col_grupo]).strip()
                    subject = f"{cod_asig}.{grupo}"

                    filas_finales.append({
                        "Day": fecha,
                        "Start": start,
                        "End": end,
                        "Subject": subject,
                        "Room": room
                    })

                except Exception as e:
                    print(f"⚠️ Error en fila del archivo {nombre_archivo}: {e}")
                    continue

        except Exception as e:
            print(f"❌ Error al procesar {nombre_archivo}: {e}")
            continue

    # Guardar resultado final
    df_final = pd.DataFrame(filas_finales)
    df_final.to_csv(salida_final, index=False)
    print(f"\n✅ Archivo final de matemáticas guardado en: {salida_final}")

# Ejecutar
procesar_matematicas("dataM", "dataM/horario_matematicas_final.csv")
