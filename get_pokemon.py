import requests
import json

url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url) # .get function gets part of the dictionary that has pokemon names and the links
pokemon_list = json.loads(response.text)['results'] # here the response string will be converted into python dictionary

for pokemon in pokemon_list: # loops through list while displaying pokemon names
    print(pokemon["name"])

print('Enter your pokemon:')

choice = input().lower()

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

for stat in pokemon_data['stats']: # list of dictionaries that contain different stats
    if stat['stat']['name'] == 'hp': # grabbing just the hp stat
        hp = stat['base_stat'] # the pokemon's actual hp stat is assigned to hp variable
        print(f"{choice}'s HP is: {hp}")