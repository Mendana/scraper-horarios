from playwright.sync_api import sync_playwright
import time
import pandas as pd
import os

def run():
    asignaturas = ["AF", "AI", "AII", "ALG", "AMatI", "AMatII", "AMatIII", "ANM", "CDI", "EDI", "EDII", "EstyProb", "GCS", "IAMat", "IE", "MDFEDP", "MNumer","MOR", "ProgM", "PyE", "RNEDO", "TopI", "TopII", "VC"]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        page.goto("https://unioviedo-my.sharepoint.com/:f:/g/personal/perezfernandez_uniovi_es/EkoB-YbUl4lOmAk5ScKSQyYBiQlBPNHdqLtaT05dv254Gw?e=wGjzEK", wait_until="load")
        page.wait_for_selector("[role='row']")
        scroll_container = page.query_selector("div[class^='list_']")

        downloaded_files = set()
        scroll_attempts = 0
        max_scroll_attempts = 100

        while scroll_attempts < max_scroll_attempts:
            visible_rows = page.query_selector_all("[role='row']")

            for row in visible_rows:
                try:
                    file_name = row.inner_text().split("\n")[0].strip()

                    if file_name in downloaded_files:
                        continue

                    if not any(file_name == f"{asig}_Listado_de_clases.xls" for asig in asignaturas):
                        continue

                    print(f"📄 Descargando: {file_name}")

                    row.click(button="right")
                    page.wait_for_timeout(500)

                    with page.expect_download() as download_info:
                        page.click("text=Descargar")

                    download = download_info.value
                    safe_filename = file_name.replace(" ", "_")
                    xls_path = f"temp_{safe_filename}"
                    download.save_as(xls_path)

                    # Convertir a CSV
                    csv_path = safe_filename.replace(".xls", ".csv")
                    try:
                        df = pd.read_excel(xls_path)
                        df.to_csv(csv_path, index=False)
                        print(f"✅ Guardado como CSV: {csv_path}")
                        os.remove(xls_path)  # borrar archivo temporal
                    except Exception as e:
                        print(f"⚠️ Error al convertir {xls_path}: {e}")

                    downloaded_files.add(file_name)
                    time.sleep(1)

                except Exception as e:
                    print(f"⚠️ Error con '{file_name}': {e}")
                    continue

            scroll_container.evaluate("el => el.scrollBy(0, el.scrollHeight)")
            page.wait_for_timeout(1000)
            scroll_attempts += 1

        print(f"✅ Archivos procesados: {len(downloaded_files)}")
        browser.close()

run()