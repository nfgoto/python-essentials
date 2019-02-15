# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# In JS, does not exist but you can create objects with unchangeable properties
# let fruits = Object.defineProperties({}, {
#     0: {
#         value: "Apples",
#         writable: false
#     }, 1: {
#         value: "Oranges",
#         writable: false
#     }, 2: {
#         value: "Grapes",
#         writable: false
#     }
# });


# Using a constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)
# In JS, does not exist but you can create objects with unchangeable properties
# const fruits = Object.defineProperty({}, 0, {
#   value: "Apples",
#   writable: false
# });


# Get value
print(fruits[1])

# Can't change value, throws an error
# fruits[0] = 'Pears'

# Delete tuple
del fruits2
# In JS, delete a reference:
# delete fruits2


# Get length
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}
# In JS:
# const fruitsSet = new Set(['Apples', 'Oranges', 'Mango'])


# Check if in set
print('Apples' in fruits_set)
# In JS:
# fruitsSet.has('Apples')


# Add to set
fruits_set.add('Grape')
print(fruits_set)
# In JS:
# same thing


# Remove from set
fruits_set.remove('Grape')
print(fruits_set)
# In JS:
# fruitsSet.delete('Grape')


# Add duplicate, will not add
fruits_set.add('Apples')
print(fruits_set)

# Clear set = empty set
fruits_set.clear()
print(fruits_set)
# In JS:
# same thing


# Delete / dereference
del fruits_set
# In JS, cannot use the delete operator on a set:
# fruitsSet = undefined


# throws not defined error
# print(fruits_set)
