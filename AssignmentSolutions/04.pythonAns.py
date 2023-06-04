import pandas as pd
import requests

url = "https://data.nasa.gov/resource/y77d-th95.json"

response = requests.get(url)
data = response.json()

structured_data = []
for item in data:
    data_info = {
        'name': item.get('name'),
        'id': item.get('id'),
        'nametype': item.get('nametype'),
        'recclass': item.get('recclass'),
        'mass': item.get('mass'),
        'fall': item.get('fall'),
        'year': item.get('year'),
        'reclat': item.get('reclat'),
        'reclong': item.get('reclong'),
        'geolocation': item.get('geolocation')
    }
    structured_data.append(data_info)
df = pd.DataFrame(structured_data)
df.to_csv('data1.csv', index=False)
