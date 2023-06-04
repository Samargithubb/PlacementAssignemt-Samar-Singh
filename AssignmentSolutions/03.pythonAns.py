import pandas as pd
import requests

# Download the data from given link
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
response = requests.get(url)
data = response.json()

pokemon_list = data["pokemon"]
structured_data = []

for pokemon in pokemon_list:
    pokemon_info = {
        'id': pokemon['id'],
        'num': pokemon['num'],
        'name': pokemon['name'],
        'img': pokemon['img'],
        'type': ', '.join(pokemon['type']),
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'candy': pokemon['candy'],
        'candy_count': pokemon.get('candy_count', 0),
        'egg': pokemon['egg'],
        'spawn_chance': pokemon['spawn_chance'],
        'avg_spawns': pokemon['avg_spawns'],
        'spawn_time': pokemon['spawn_time']
    }

    structured_data.append(pokemon_info)

df = pd.DataFrame(structured_data)

df.to_excel('pokemon.xlsx', index=False)




