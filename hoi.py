import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
# Define the URL
url = input("enter show url: ")
base_url = "https://www.hoichoi.tv"
full_urls = []
episodes = int(input("Enter the number of episodes"))

# Extract the desired text using a regular expression
match = re.search(r'/shows/([^/]+)', url)
if match:
    desired_text = match.group(1)

    # Send an HTTP GET request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all anchor (<a>) elements with an 'href' attribute
        links = soup.find_all('a', href=True)

        # Extract and print the 'href' values that contain the desired text
        for link in links:
            href = link['href']
            full_url = urljoin(base_url, href)
            print(f"{full_url}")
            full_urls.append(full_url)

    else:
        print(f"Failed to retrieve the URL. Status code: {response.status_code}")
else:
    print("Desired text not found in the URL.")
with open('hoichoi.txt', 'w') as file:
    for full_url in full_urls[6:6+episodes]:
        file.write(f"{full_url}\n")
