import requests
from bs4 import BeautifulSoup
import subprocess
from pathlib import Path
import re
import json

# URL of the web page

m3u8DL_RE = 'N_m3u8DL-RE'
showName = input("enter show name")

# Send an HTTP GET request to the URL
def process_url(url):
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        divs = soup.find_all('div', class_='season-layout-episode-title season-layout-mweb-only')
        li_elements = soup.find_all('li', class_='season-layout-season-count-item active')

        # Extract and print the values inside the div elements

        cookies = {
            'vl-user': 'undefined',
            'CookieConsent': '{stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:1%2Cutc:1697088822682%2Cregion:%27IN%27}',
            'hc-cc': 'IN',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            # 'Cookie': 'vl-user=undefined; CookieConsent={stamp:%27-1%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27implied%27%2Cver:1%2Cutc:1697088822682%2Cregion:%27IN%27}; hc-cc=IN',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        response = requests.get(
            url,
            cookies=cookies,
            headers=headers,
        )

        html_content = response.text
        soup = BeautifulSoup(response.text, "html.parser")

        
        season_pattern = r'Season (\d+)'
        episode_pattern = r'Episode (\d+)'
        episode_name_pattern = r'"name" (.*?),'

        # Extract season number
        season_match = re.search(season_pattern, html_content)
        season_number = season_match.group(1) if season_match else None

        # Extract episode number
        episode_match = re.search(episode_pattern, html_content)
        episode_number = episode_match.group(1) if episode_match else None

        # Extract episode name
        episode_name_match = re.search(episode_name_pattern, html_content)
        episode_name = episode_name_match.group(1) if episode_name_match else None


        # Find the button element with the specified data attribute
        button = soup.find("button", {"data-plus-icon": True})

        # Extract the data attribute and parse it as JSON
        data_attr = button["data-plus-icon"]

        # Parse the JSON data

        data = json.loads(data_attr)

        # Extract the contentId value
        content_id = data.get("contentId", None)


        if content_id:
            print("Content ID:", content_id)

            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-US,en;q=0.5',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzaXRlIjoiaG9pY2hvaXR2Iiwic2l0ZUlkIjoiN2ZhMGVhOWEtOTc5OS00NDE3LTk5ZjUtY2JiNTM0M2M1NTFkIiwiYW5vbnltb3VzSWQiOiI3ZGYwZGJkNDhkMGQ0NjE0NTJkNzY5ODA2Y2ZiMGE5ZjhkMTU1ZjhjNTUzMjI3MDUzODBlNDM2OWYyMzMwYzY0IiwiaWQiOiIwZGM3YzUyMi00YmFmLTExZWUtYWIyNS03ZDVmYTAyOTg5MDEiLCJ1c2VySWQiOiIwZGM3YzUyMi00YmFmLTExZWUtYWIyNS03ZDVmYTAyOTg5MDEiLCJpcGFkZHJlc3MiOiI0OS40My4xNTUuMCIsImlwYWRkcmVzc2VzIjoiNDkuNDMuMTU1LjAsIDEwLjEyMC4zOC4yMjIsIDM1LjE3NC4xMjkuNzcsIDEzMC4xNzYuOTguMTQ5IiwidXNlcm5hbWUiOiJhbm9ueW1vdXMiLCJjb3VudHJ5Q29kZSI6IklOIiwicG9zdGFsY29kZSI6IjI0ODAwMSIsInByb3ZpZGVyIjoidmlld2xpZnQiLCJkZXZpY2VJZCI6ImF1dG8tMGRjN2M1MjEtNGJhZi0xMWVlLWFiMjUtN2Q1ZmEwMjk4OTAxIiwiaWF0IjoxNjkzODkyNTcxLCJleHAiOjE3MjU0Mjg1NzF9.iZvQhDr8Eq0oySF1VSRbzW-_L3Dmu6otVAzYsjyWX2w',
                'Origin': 'https://www.hoichoi.tv',
                'Connection': 'keep-alive',
                'Referer': 'https://www.hoichoi.tv/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                # Requests doesn't support trailers
                # 'TE': 'trailers',
            }

            params = {
                'id': content_id,
                'deviceType': 'web_browser',
                'contentConsumption': 'web',
            }

            response = requests.get('https://prod-api.viewlift.com/entitlement/video/status', params=params,
                                    headers=headers)
            data = response.json()
            mpd = data["video"]["streamingInfo"]["videoAssets"]["hlsDetail"]["url"]
            print(mpd)
            subprocess.run([m3u8DL_RE,
                            '-M', 'format=mkv:muxer=ffmpeg',
                            '--concurrent-download',
                            '--log-level', 'INFO',
                            '-sv', 'best',
                            '-sa', 'best', '-ss', 'lang="en":for=all',
                            '--save-name', 'video', mpd])
            title = f'{showName} - S{season_number} - E{episode_number}'


            try:
                Path('video.mkv').rename('' + title + '.mkv')
                print(f'{title}.mkv \nall done!\n')

            except FileNotFoundError:
                print("[ERROR] no mkv file")


        else:
            print("Content ID not found on the page.")
    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)

with open("hoichoi.txt", "r") as file:
    urls = file.read().splitlines()

# Loop through the URLs and process each one
for url in urls:
    # Remove leading/trailing whitespaces and newline characters
    url = url.strip()
    # Call the function to process the URL
    process_url(url)
