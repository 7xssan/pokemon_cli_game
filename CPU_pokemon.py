import requests
import json
import random

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']


# Get the CPU pokemon at random
random_pokemon = random.randint(0, len(pokemon_list) - 1)

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(random_pokemon)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# print(pokemon_data["name"], pokemon_data["abilities"][0], pokemon_data["stats"][0])


# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# get hp
hp = int(pokemon_data["stats"][0]["base_stat"])

# get one move

moves = []

for move in pokemon_data["moves"][0:4]:
    moves.append(move["move"]["name"])

chosen_pokemon = {"pokemon": pokemon_data["name"], "hp": hp, "moves": moves}

