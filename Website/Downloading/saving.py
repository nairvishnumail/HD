from playwright.sync_api import sync_playwright
import re
import time

def handle_download(download):
    # Save the download to a specified path
    download_path = "C:/Users/nairv/Downloads/video.mp4"
    download.save_as(download_path)
    print(f"File downloaded to {download_path}")

def modify_youtube_url(url):
    # Check if the URL starts with 'https://', if not, prepend it
    if not url.startswith('https://'):
        url = 'https://' + url

    # Check if 'youtube' is followed by 'vvv.com', if not, insert 'vvv'
    url = re.sub(r'(youtube)(\.com)', r'\1vvv\2', url)

    return url

with sync_playwright() as p:
    # Create browser
    browser = p.chromium.launch(headless=False, slow_mo=100)
    page = browser.new_page();

    # Set up download event listener before triggering the download
    page.on('download', handle_download)

    # link = modify_youtube_url(input().strip())
    link = 'https://www.youtubevvv.com/watch?v=7l520bGKuxA&ab_channel=MovieRecaps'
    page.goto(link)
    page.is_visible('div.sc-1vkjw2x-1 embFVV') #div class name

    # find the Download button
    button_selector = 'button.b0kwwh-0.dkrhAU.uxhyop-2.TPBMx:not([disabled])'
    
    # Once the Download button is ready, download
    enabled_button = page.wait_for_selector(button_selector)
    time.sleep(5)
    enabled_button.click()
    print('downloading')

    # Wait for downloading to finish (change time if needed)
    page.wait_for_timeout(30000)
