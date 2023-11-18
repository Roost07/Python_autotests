import requests
import pytest

HOST = 'https://api.pokemonbattle.me:9104'

def test_status_cod():
    response = requests.get(url=f'{HOST}/trainers', params={'trainer_id': 3073})
    assert response.status_code == 200 
    assert response.json()['trainer_name'] == 'Roost'