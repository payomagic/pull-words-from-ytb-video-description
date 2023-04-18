#Python script to pull an exact words from a youtube video description
#payomag 3/2023
import requests
import json

# Replace YOUR_API_KEY with your actual API key
api_key = "YOUR_API_KEY"

# Replace VIDEO_ID with the ID of the video you want to get the description from
video_id = "VIDEO_ID"

url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"

response = requests.get(url)

data = json.loads(response.text)

description = data['items'][0]['snippet']['description']

# Split the description into a list of words
words = description.split()

# Extract the first, third, and fifth words
first_word = words[0]
third_word = words[2]
fifth_word = words[4]

# Print the extracted words
print(f"First word: {first_word}")
print(f"Third word: {third_word}")
print(f"Fifth word: {fifth_word}")
