# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person = {
    "first_name": 'Eoto',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
person2 = dict(first_name='Malua', last_name='Eolofu')
# In JS:
# let person2 = Object.defineProperties({}, {
#     first_name: {value: 'Malua'},
#     last_name: {value: 'Eolofu'},
#     age: {value: 453}
# });
# let person2 = Object.create(); / new Object();
# person2.first_name = 'Malua';
# person2.last_name = 'Eolofu';
# person2.age = 453;

# Get value
print(person['first_name'])
print(person.get('last_name'))
# In JS:
# the same or person.first_name


# Add key/value
person['phone'] = '555-555-5555'
# In JS:
# the same or person.phone = 555-555-5555'


# Get dict keys
# returns a dict_keys object, not a list
# to get list: list(person.ikeys())
print(person.keys())
# In JS:
# Object.keys(person)


# Get dict items
# returns a dict_items object, not a list
# to get list: list(person.items())
print(person.items())
# In JS:
# Object.values(person)


# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'
# In JS:
# person2 = {...person};


# Remove item
del(person['age'])
person.pop('phone')
# In JS:
# delete person.age;


# Clear
person.clear()
# In JS, does not exist:
# person = {};
# you can empty all values but keep the keys:
# for(let p in person) Object.defineProperty(person, p, {value: undefined});


# Get length
print(len(person2))
# In JS:
# Object.keys(person2).length
# Object.values(person2).length
# Object.entries(person2).length


# List of dict
people = [
    {'name': 'Tutu', 'age': 30},
    {'name': 'Soso', 'age': 25}
]
# In JS:
# same thing


print(people[1]['name'])
