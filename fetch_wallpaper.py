import requests
import os
from datetime import datetime

# Fetch the Unsplash API access key from GitHub Secrets
access_key = os.getenv('UNSPLASH_ACCESS_KEY')

if not access_key:
    raise ValueError('UNSPLASH_ACCESS_KEY not set in environment variables.')

url = f'https://api.unsplash.com/photos/random?client_id={access_key}'

response = requests.get(url)
data = response.json()
image_url = data['urls']['full']

# Generate a unique filename based on the current timestamp
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
filename = f'wallpaper_{timestamp}.jpg'

# Download the image
image_response = requests.get(image_url)
with open(filename, 'wb') as f:
    f.write(image_response.content)

# Move the downloaded image to the desired folder
os.makedirs('wallpapers', exist_ok=True)
os.rename(filename, os.path.join('wallpapers', filename))
