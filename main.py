import os
import shutil

def limpiar_temporales():
    for carpeta in ["dataI", "dataM"]:
        if os.path.exists(carpeta):
            shutil.rmtree(carpeta)
            print(f"🧹 Carpeta '{carpeta}' eliminada.")

def run_script(path):
    print(f"\n▶️ Ejecutando: {path}")
    result = os.system(f"python {path}")
    if result != 0:
        print(f"❌ Error al ejecutar {path}")
        exit(1)

def main():
    print("🧠 Iniciando proceso completo de horarios...\n")

    # 1. Scrapers
    run_script("InforScrapper.py")
    run_script("MathScrapper.py")

    # 2. Unir CSVs individuales de informática
    run_script("joinCSV.py") 

    # 3. Formatear al formato final
    run_script("InforFormatter.py")
    run_script("MathFormatter.py")

    # 4. Unir los finales en uno solo
    run_script("theBoss.py")

    print("\n🗂️ Archivos finales generados. Eliminando carpetas temporales...")
    #limpiar_temporales()

    print("\n✅ Proceso completo finalizado. ¡Listo!")

if __name__ == "__main__":
    main()
