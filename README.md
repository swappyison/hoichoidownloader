# Hoichoi Video Downloader

## Overview

This Python script allows you to download both paid and free videos from the Hoichoi website. The process involves scraping Hoichoi show URLs using `hoi.py` and then downloading the videos from the generated list using `hoichoidownloader.py`.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `BeautifulSoup`

Install the required packages using the following command:

^^^bash
pip install requests beautifulsoup4
^^^

## How to Use

### Step 1: Scraping Hoichoi Show URLs

1. Run `hoi.py` using the following command:

    ```bash
    python3 hoi.py
    ```

2. Enter the Hoichoi show URL when prompted.

3. Enter the number of episodes you want to scrape.

4. The script will generate a file named `hoichoi.txt` containing the URLs of the episodes.

### Step 2: Downloading Hoichoi Videos

1. Open `hoichoidownloader.py` in a text editor.

2. Make sure to have the required Python packages installed.

3. Run `hoichoidownloader.py` using the following command:

    ```bash
    python3 hoichoidownloader.py
    ```

4. The script will read the URLs from `hoichoi.txt` and download the videos.

## Notes

- Ensure that you have the necessary permissions to download and access the content from the Hoichoi website.

- The downloader script uses the `m3u8DL-RE` tool, make sure it's available in your environment.

- This script is provided for educational purposes only. Respect the terms of service of the Hoichoi website.

## Disclaimer

Use this script responsibly and in accordance with the terms and conditions of the Hoichoi website. The developers are not responsible for any misuse or violation of terms.
