# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

# core module
import json

#  mock JSON
userJSON = '{"first_name": "Toto", "last_name": "Doe", "age": 45}'

# Parse to dict - returns a dictionary
user = json.loads(userJSON)
# In JS:
# JSON.parse(userJSON)


print(user)
print(f"First user: {user['first_name']}")

# serialize to JSON formatted string

spaceship = {'make': 'Popo', 'model': 'Kubwa', 'year': 2070}

spaceshipJSON = json.dumps(spaceship)
# In JS:
# JSON.stringify(spaceship)

print(spaceshipJSON)
print(f'Type of carJSO{type(spaceshipJSON)}')