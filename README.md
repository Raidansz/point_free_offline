# Point-Free Video Downloader

This script allows you to download videos from Point-Free collections easily by fetching all episode URLs from a collection and downloading them using `yt-dlp`.

## Prerequisites

- Python 3.x installed on your system.
- The following Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `yt-dlp`

## Setup and Usage

### Step 1: Clone the Repository
Clone this repository or copy the script to an empty folder on your machine.

### Step 2: Install Dependencies
Install the required Python libraries by running the following command in your terminal:

```bash
pip install requests beautifulsoup4 yt-dlp
```

### Step 3: Export Cookies
1. Install the Chrome extension **[Get cookies.txt Clean](https://chrome.google.com/webstore/detail/get-cookiestxt-clean/)**.
2. Go to the [Point-Free](https://www.pointfree.co/) website and log in to your account.
3. Use the **Get cookies.txt Clean** extension to export your cookies to a file named `cookies-pointfree.txt`.
4. Move the `cookies-pointfree.txt` file to the same folder as the Python script.

### Step 4: Configure the Script
Open the Python script and locate the `collection_url` variable. Replace its value with the URL of the first video in the collection you want to download.

```python
collection_url = "<URL of the first video in the collection>"
```

### Step 5: Run the Script
Navigate to the folder containing the script and `cookies-pointfree.txt` file using the terminal. Then run the script with the following command:

```bash
python3 download_collection.py
```

The script will:
- Fetch all episode URLs from the collection.
- Print the episode URLs found.
- Download each episode using `yt-dlp`.

### Notes
- To download only a single video, replace the `collection_url` variable with the URL of the desired video and comment out or remove the loop that finds additional episodes.
- Ensure you have sufficient disk space to store the downloaded videos.

## Troubleshooting

1. **Error: Failed to fetch the collection page**
   - Ensure the `cookies-pointfree.txt` file is up-to-date and contains valid cookies.
   - Check the `collection_url` to ensure it points to a valid Point-Free video.

2. **No episodes found**
   - Verify that the collection URL is correct and accessible.
   - Ensure you are logged in and have access to the content.

3. **Command not found: yt-dlp**
   - Make sure `yt-dlp` is installed. If not, install it using:

     ```bash
     pip install yt-dlp
     ```

## Disclaimer
This script is intended for personal use only to save videos for offline viewing by people who already have a subscription to Point-Free. Ensure you have the right to download content from Point-Free before using this tool. Unauthorized use may violate the terms of service of Point-Free.

Downloading videos and distributing them without proper authorization/permission may result in serious legal consequences. It is your responsibility to adhere to the terms of service of Point-Free and any applicable copyright laws. 

