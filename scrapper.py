from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        # Go to the website
        page.goto("https://gobierno.ingenieriainformatica.uniovi.es/grado/plan/?y=24-25&t=s1", wait_until="load")

        # Wait for the page to load
        page.wait_for_selector("form#theForm")
        
        # Select all the checkboxes
        checkboxes = page.query_selector_all("input[type='checkbox']")
        
        # Activate all checkboxes
        for checkbox in checkboxes[:20]:
            if not checkbox.is_checked():
                checkbox.click()
        
        # Select the csv button option
        csv_button = page.query_selector("input[value='csv']")
        csv_button.click()
        
        # Download the file
        with page.expect_download() as download_info:
            submit_button = page.query_selector("input[type='submit'][value='Enviar']")
            submit_button.click()
            
        download = download_info.value
        download.save_as("horario.csv")
        print("File downloaded successfully as horario.csv")


        browser.close()

run()
