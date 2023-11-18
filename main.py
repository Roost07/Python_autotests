import requests
HOST = 'https://api.pokemonbattle.me:9104'

response = requests.post(url=f'{HOST}/pokemons',
                         json={'name': 'Python',
                               'photo': 'https://dolnikov.ru/pokemons/albums/092.png'},
                         headers={'Content-Type': 'application/json','trainer_token': 'Токен в тикете'}
                        )
print (response.text)

response = requests.put(url=f'{HOST}/pokemons',
                         json={'pokemon_id':response.json()['id'], 
                               'name': 'PythonNew',
                               'photo': 'https://dolnikov.ru/pokemons/albums/091.png'},
                         headers={'Content-Type': 'application/json','trainer_token': 'Токен в тикете'}
                       )
print(response.text)

response = requests.post(url=f'{HOST}/trainers/add_pokeball',
                         json={'pokemon_id':response.json()['id']},
                         headers={'Content-Type': 'application/json','trainer_token': 'Токен в тикете'}
                        )
print(response.text)