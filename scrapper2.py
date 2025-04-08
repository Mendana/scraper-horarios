from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        # Ir a la web
        page.goto("https://gobierno.ingenieriainformatica.uniovi.es/grado/plan/?y=24-25&t=s1", wait_until="load")
        page.wait_for_selector("form#theForm")

        # Obtener todos los checkboxes
        all_checkboxes = page.query_selector_all("input[type='checkbox']")
        total = len(all_checkboxes)
        print(f"Total de checkboxes encontrados: {total}")

        # Dividir en bloques de 100
        chunk_size = 100
        for i in range(0, total, chunk_size):
            print(f"\n🧩 Procesando bloque {i} - {i + chunk_size - 1}")

            # Recargar la página en cada iteración para empezar limpio
            page.goto("https://gobierno.ingenieriainformatica.uniovi.es/grado/plan/?y=24-25&t=s1", wait_until="load")
            page.wait_for_selector("form#theForm")

            # Seleccionar los checkboxes otra vez (porque la página se recarga)
            checkboxes = page.query_selector_all("input[type='checkbox']")

            # Marcar el bloque actual
            for checkbox in checkboxes[i:i+chunk_size]:
                if not checkbox.is_checked():
                    checkbox.check()

            # Seleccionar opción CSV
            page.query_selector("input[value='csv']").click()

            # Descargar el archivo
            with page.expect_download() as download_info:
                page.query_selector("input[type='submit'][value='Enviar']").click()

            download = download_info.value
            filename = f"horario_{i}-{min(i+chunk_size, total)-1}.csv"
            download.save_as(filename)
            print(f"✅ Descargado como {filename}")

            # Esperar un poco por seguridad (opcional)
            time.sleep(1)

        browser.close()

run()
