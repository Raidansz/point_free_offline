import requests
from bs4 import BeautifulSoup
import os

# Loading cookies from the file
cookies = {}
with open("cookies-pointfree.txt", "r") as f:
    for line in f:
        if not line.startswith("#") and line.strip():
            fields = line.split("\t")
            cookies[fields[5].strip()] = fields[6].strip()

# Put the URL of the first video down here of the collection and it will download for you all the videos of the collection
collection_url = "https://www.pointfree.co/collections/parsing/composable-parsing-map-zip-flat-map/ep59-composable-parsing-map"

# Sending a request to the collection page
headers = {
    "Referer": "https://www.pointfree.co/",
}
response = requests.get(collection_url, cookies=cookies, headers=headers)

# Checking if the response is successful
if response.status_code != 200:
    print(f"Error: Failed to fetch the collection page. Status code: {response.status_code}")
    print(response.text)
    exit(1)


# print("Fetched HTML content from the collection page:")
# print(response.text[:500])  # for dubugiing

soup = BeautifulSoup(response.text, "html.parser")

# this loop iterates through all episode URLs on the collection page
episode_urls = []
for a in soup.find_all('a', href=True):
    href = a['href']
    if "/episodes/" in href:
        full_url = "https://www.pointfree.co" + href
        episode_urls.append(full_url)

# if there is, it them prints out 
if not episode_urls:
    print("No episode URLs found.")
else:
    print("Found episodes:")
    for url in episode_urls:
        print(url)

# Downloading each episode using yt-dlp
for url in episode_urls:
    command = f'yt-dlp --cookies cookies-pointfree.txt --add-header "Referer:https://www.pointfree.co/" "{url}"'
    print(f"Running command: {command}") 
    os.system(command)




"""
README:
How to download Point-Free videos?

0 - Make sure to have Python.
===============================
1 - Put the python file in an empty folder.
===============================
2 - Download the dependecies by executing on the terminal { pip install requests beautifulsoup4 yt-dlp }.
    This will download all the packages for you.
===============================
3 - Go to google chrome and download an extension called {Get cookies.txt Clean}
===============================
4 - Go to Point-Free website and signin, and then run the (Get cookies.txt Clean) extension,
    and export the cookies of Point-Free into a .txt file under the name {cookies-pointfree.txt}.
===============================
5 - Copy the the cookies-pointfree.txt file to the same folder of the python file
===============================
6 - Go to the collection that you want to download, then go to the first video of the collection and copy the link and paste it where indicated
    in the python file. Note that, if you want to download only one video, then you can copy its link and paste it AND exculde the loop that finds episodes.
===============================
7 - Through the terminal, CD into the folder and run { python3 download_collection.py }
"""