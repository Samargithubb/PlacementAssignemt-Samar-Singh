import requests

# API URL
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

# Send GET request to the API and retrieve the data
response = requests.get(url)
data = response.json()

# Extract information from the data
show_id = data['id']
show_name = data['name']

episodes = data['_embedded']['episodes']
episode_data = []

# Iterate over each episode and extract the required attributes
for episode in episodes:
    episode_id = episode['id']
    episode_url = episode['url']
    episode_name = episode['name']
    season_number = episode['season']
    episode_number = episode['number']
    episode_type = episode['type']
    airdate = episode['airdate']
    airtime = episode['airtime']
    runtime = episode['runtime']
    average_rating = episode['rating']['average']
    summary = episode['summary']
    medium_image = episode['image']['medium']
    original_image = episode['image']['original']

    # Clean the summary by removing HTML tags
    clean_summary = summary.strip('<p>').strip('</p>')

    # Create a dictionary of episode data
    episode_info = {
        'id': episode_id,
        'url': episode_url,
        'name': episode_name,
        'season': season_number,
        'number': episode_number,
        'type': episode_type,
        'airdate': airdate,
        'airtime': airtime,
        'runtime': runtime,
        'average_rating': average_rating,
        'summary': clean_summary,
        'medium_image': medium_image,
        'original_image': original_image
    }

    episode_data.append(episode_info)

# Print the extracted episode data
for episode in episode_data:
    print(episode)
