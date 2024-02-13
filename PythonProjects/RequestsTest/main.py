"""
Pokemon Requests test API
"""
import requests

"""
POST-запрос на создание покемона
"""

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type': 'application/json',
           'Trainer_token': '9848d39189ad1e59b54733714234c2d6'}

body = {
    'name': 'Kukozhik',
    'photo': 'https://dolnikov.ru/pokemons/albums/978.png'}
response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADERS, timeout=5)
print(f'Статус-код: {response.status_code}. Сообщение: {response.json()["message"]}')


"""
PUT-запрос на смену имени покемона
"""

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type': 'application/json',
           'Trainer_token': '9848d39189ad1e59b54733714234c2d6'}

body = {
    'pokemon_id': '360',
    'name': 'Ezhik-Kukozhik',
    'photo': 'https://dolnikov.ru/pokemons/albums/978.png'}
response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADERS, timeout=5)
print(f'Статус-код: {response.status_code}. Сообщение: {response.json()["message"]}')


"""
POST-запрос поймать покемона в покебол
"""

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type': 'application/json',
           'Trainer_token': '9848d39189ad1e59b54733714234c2d6'}

body = {
    'pokemon_id': '360'}
response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADERS, timeout=5)
print(f'Статус-код: {response.status_code}. Сообщение: {response.json()["message"]}')