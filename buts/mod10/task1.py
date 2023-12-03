import requests
import json

url = 'https://swapi.dev/api/starships/10/'
response = requests.get(url)
data = response.json()

pilots = []
for pilot_url in data['pilots']:
    pilot_response = requests.get(pilot_url)
    pilot_data = pilot_response.json()
    
    homeworld_response = requests.get(pilot_data['homeworld'])
    homeworld_data = homeworld_response.json()

    pilot_info = {
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'mass': pilot_data['mass'],
        'homeworld': {
            'name': homeworld_data['name'],
            'link': pilot_data['homeworld']
        }
    }
    pilots.append(pilot_info)

ship_info = {
    'name': data['name'],
    'max_speed': data['max_atmosphering_speed'],
    'class': data['starship_class'],
    'pilots': pilots
}
print(json.dumps(ship_info, indent=4))
with open('millennium_falcon_info.json', 'w') as f:
    json.dump(ship_info, f, indent=4)
