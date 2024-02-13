import pytest
import requests

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type': 'application/json'}

def test_get_trainers():
    """
    KTI-1 Приходит статус-код 200
    """
    response = requests.get(url=f'{URL}/trainers', params={'level': 1}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'
    

def test_get_trainer_by_id():
   """
   KTI-2 строчка - имя тренера
   """
   response = requests.get(url=f'{URL}/trainers', params={'trainer_id':219}, timeout=5)
   print(response.json())
   assert response.json()["data"][0]['trainer_name'] == 'Асин' , 'Трейнер не найдет'
