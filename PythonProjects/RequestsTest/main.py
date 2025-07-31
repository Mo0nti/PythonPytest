import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '345e55a7e2a30e539cc842db1c15d27d'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_create_pokemon = {
    "name": "Бульбазавр",
    "photo_id": 566
}



response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response_create_pokemon.json())

response_json = response_create_pokemon.json()
IDF = response_json.get('id')

body_change_pokemon = {
    "pokemon_id": IDF,
    "name": "кепым",
    "photo_id": 2
}

body_catch_pokeball = {
    "pokemon_id": IDF
}

response_changepokemon = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_pokemon)
print(response_changepokemon.json())

response_catch_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch_pokeball)
print(response_catch_pokeball.json())



