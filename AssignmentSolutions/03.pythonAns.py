import requests

# Download the data from the provided link
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
response = requests.get(url)
data = response.json()

# Extract relevant information from the JSON data
pokemon_list = data["pokemon"]
pokemon_data = []
all_columns = set()

for pokemon in pokemon_list:
    pokemon_info = []
    for key, value in pokemon.items():
        if isinstance(value, (str, int, float)):
            pokemon_info.append((key,value, type(value)))
            all_columns.add(key)
    pokemon_data.append(pokemon_info)
print(pokemon_data[0])
