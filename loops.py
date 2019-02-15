# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people:
    print(f'Current Person: {person}')
# Un JS, for...of to iterate over iterables (array, set...)
# for(person of people)...

# Break
for person in people:
    if person == 'Sara':
        break
    print(f'Current Person: {person}')

# Continue
for person in people:
    if person == 'Sara':
        continue
    print(f'Current Person: {person}')

# range
for i in range(len(people)):
    print(f'Current Person: {people[i]}')
# In JS, does not exist:
# for(let i = 0; i < people.length; i++)...
# OR people.forEach((person, index) => {...})
# OR for( n of [...people.keys()])...


for i in range(0, 11):
    print(f'Number: {i}')
# In JS,:
# for( n of [...Array(11).keys()])...


# While loops execute a set of statements as long as a condition is true.

count = 0
while count < 10:
    print(f'Count: {count}')
    count += 1
# In JS
# same thing