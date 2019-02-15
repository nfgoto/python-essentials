
# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))
# In JS:
# const numbers2 = new Array(1, 2, 3, 4, 5);

# Get a value
print(fruits[1])

# Get length
print(len(fruits))
# In JS:
# fruits.length


# Append to list
fruits.append('Mangos')
# In JS:
# fruits.push('Mangos')


# Remove from list
fruits.remove('Grapes')
# In JS:
# fruits.splice(fruits.indexOF('Grapes'), 1);


# Insert into position
fruits.insert(2, 'Strawberries')
# In JS:
# fruits.splice(2, 0, 'Strawberries');


# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)
# In JS:
# fruits.splice(2, 1);


# Reverse list
fruits.reverse()
# In JS:
# same thing


# Sort list
fruits.sort()
# In JS:
# same thing


# Reverse sort
fruits.sort(reverse=True)
# In JS:
# fruits.sort().reverse()


print(fruits)
