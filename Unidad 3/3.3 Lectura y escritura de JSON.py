import requests
import json

# GitHub raw URL
url="https://raw.githubusercontent.com/LearnWebCode/json-example/master/animals-1.json"
# Hacer el GET request a la URL
response = requests.get(url)
print(response)

# Cargar data
data = json.loads(response.text)
print(data)
print(json.dumps(data,indent=4))

# Abrir
with open("Data_json.json", 'r') as f:
    data = json.load(f) # cargar
print(json.dumps(data,indent=4))


person = {
    "name": "David",
    "age": 24,
    "city": "CH",
    "languages": ["English", "Spanish", "French"],
    "pets": 3,
    "dogs": [
        {"name": "Ringo", "age": 5},
        {"name": "Bobby", "age": 7},
        {"name": "Sam", "age": 10}
    ]
}
print(type(person))
print(json.dumps(person,indent=4))

with open("David_json_x.json", "w") as outfile:
    json.dump(person, outfile,indent=4)

# Escritura
"""
person = {
    "name": "David",
    "age": 24,
    "city": "CH",
    "languages": ["English", "Spanish", "French"],
    "pets": 3,
    "dogs": [
        {"name": "Ringo", "age": 5},
        {"name": "Bobby", "age": 7},
        {"name": "Sam", "age": 10}
    ]
}

with open("David_json.json", "w") as outfile:
    json.dump(person, outfile,indent=4)
"""    