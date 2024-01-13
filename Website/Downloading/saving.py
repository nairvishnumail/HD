from playwright.sync_api import sync_playwright
import time

def handle_download(download):
    # Save the download to a specified path
    download_path = "C:/Users/nairv/Downloads/video.mp4"
    download.save_as(download_path)
    print(f"File downloaded to {download_path}")

with sync_playwright() as p:
    # Create browser
    browser = p.chromium.launch(headless=False, slow_mo=100)
    page = browser.new_page();

    # Set up download event listener before triggering the download
    page.on('download', handle_download)

    page.goto('https://www.youtubevvv.com/watch?v=7l520bGKuxA&ab_channel=MovieRecaps')
    page.is_visible('div.sc-1vkjw2x-1 embFVV') #div class name

    # find the Download button
    button_selector = 'button.b0kwwh-0.dkrhAU.uxhyop-2.TPBMx:not([disabled])'
    
    # Once the Download button is ready, download
    enabled_button = page.wait_for_selector(button_selector)
    time.sleep(5)
    enabled_button.click()
    print('downloading')

    # Wait for downloading to finish
    page.wait_for_timeout(30000)


# <button class="b0kwwh-0 dkrhAU uxhyop-2 TPBMx"><span class="uxhyop-1 iCoEVA">Download</span></button>