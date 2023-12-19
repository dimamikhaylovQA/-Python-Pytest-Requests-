import requests

token="7b088769f7be8c931ffd5b9030b99511"

'''response_create=requests.post('https://api.pokemonbattle.me:9104/pokemons', json={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers={"Content-Type":"application/json","trainer_token":token})

print(response_create.text)

response_change_name=requests.put('https://api.pokemonbattle.me:9104/pokemons', json={
    "pokemon_id": "21852",
    "name": "nataha",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers={"Content-Type":"application/json","trainer_token":token})

print(response_change_name.text)'''

response_change_name=requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json={
    "pokemon_id": "21852"
}, headers={"Content-Type":"application/json","trainer_token":token})

print(response_change_name.text)