import requests
import json

# Replace YOUR_API_KEY with your actual API key
api_key = "YOUR_API_KEY"

# Replace VIDEO_ID with the ID of the video you want to get the comments from
video_id = "VIDEO_ID"

# Replace USERNAME with the username of the user you want to get the comments from
username = "USERNAME"

url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}"

response = requests.get(url)

data = json.loads(response.text)

for item in data['items']:
    comment = item['snippet']['topLevelComment']['snippet']
    if comment['authorDisplayName'] == username:
        print(comment['textDisplay'])
