# HD


# Website
Automation:  
 _(Website/Downloading/saving.py)_

Precheck
1. Check if Node.js is on your system
  ```
  Open terminal
  Run npm --version
  Download (if needed): https://nodejs.org/en/download
  ```

2. Optional (to test efficeny of Playwright code)
  ```
  https://youtu.be/IB2P1FBXjcQ?list=PLhW3qG5bs-L9sJKoT1LC5grGT77sfW0Z8&t=302
  ```

3. Install the Playwright package and the browser binaries
  ```bash
  pip install playwright
  playwright install
  ```

Code
1. Line 6, specify your path
2. Line 30, specify your youtube video
  ```
  Video must be in form: 'https://youtubevvv.com/watch/XXXXXXX'
  ('https://' must be inlcuded, 'vvv' must be included)
  ```

  ```
  Otherwise, uncomment lines 29 and comment line 30
  Then input your video into the terminal & code will reformat as necessary
  ```
  
   
# Video Downloader (Youtube Scraper)

A simple and effective way to download videos from a variety of databases. Includes but not limited to: Youtube, Vimeo, Twitch and many more. 

This version of Video Downloader was designed by Isaac Bloomgarden and took heavy inspiration from the work of Arnav Agrawal. Thank you so much :)

## Installation (Credits to Arnav, Modified by Isaac)

- Ensure you have python (3.11) installed
- Clone the repository through GitHub
- Create a virtual environment <code>python3.11 -m venv ytscraper</code>
- Activate the virtual environment <code>source ytscraper/bin/activate</code> (Linux/Mac) or <code>ytscraper\Scripts\activate</code> (Windows)
- Install the requirements <code>pip install -r requirements.txt</code>
- Add the following folders in the Downloader folder if they don't exist (The Downloader folder MUST be in root):
  - logs(titled <code>logs</code>)
  - audio (titled <code>audio</code>)
  - videos (titled <code>videos</code>)
  - folder for processing videos (titled <code>processing</code>)
  - folder for raw downloaded videos (titled <code>raw_videos</code>)
- Additionally, make sure that the file URLs.csv exists and it is within the Downloader folder