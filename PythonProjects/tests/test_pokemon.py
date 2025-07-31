import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '345e55a7e2a30e539cc842db1c15d27d'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '38083'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
      response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
      assert response_get.json()["data"][0]['id'] == '38083'
