import requests
import json

# Download data from the API link
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
response = requests.get(url)
data = response.json()

# Extract relevant information from the data
show_info = {
    'id': data.get('id'),
    'url': data.get('url'),
    'name': data.get('name'),
    'season': data.get('_embedded', {}).get('episodes', [{}])[0].get('season'),
    'number': data.get('_embedded', {}).get('episodes',[{}])[0].get('number'),
    'type': data.get('type'),
    'airdate': data.get('_embedded', {}).get('episodes',[{}])[0].get('airdate'),
    'airtime': data.get('_embedded', {}).get('episodes',[{}])[0].get('airtime'),
    'runtime': data.get('runtime'),
    'average rating': data.get('rating', {}).get('average'),
    'summary': data.get('summary'),
    'medium image link': data.get('image', {}).get('medium'),
    'original image link': data.get('image', {}).get('original')
}

# Print the extracted information
for key, value in show_info.items():
    print(f"{key}: {value}")

