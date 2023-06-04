import pandas as pd
import requests

url = "https://data.nasa.gov/resource/y77d-th95.json"

response = requests.get(url)
data = response.json()

structured_data = []
for item in data:
    data_info = {
        'Name of Earth Meteorite': item.get('name'),
        'ID of Earth Meteorite': item.get('id'),
        'nametype': item.get('nametype'),
        'recclass': item.get('recclass'),
        'Mass of Earth Meteorite': item.get('mass'),
        'Year at which Earth Meteorite was hit':pd.to_datetime(item.get('year'), errors='coerce'),
        'reclat': (item.get('reclat')),
        'reclong':(item.get('reclong')),
        'Coordinates': item.get('geolocation', {}).get('coordinates', [])
    }
    structured_data.append(data_info)

df = pd.DataFrame(structured_data)
df.to_csv('earth.csv', index=False)

