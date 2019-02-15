# Strings in python are surrounded by either single or double quotation marks.

name = 'Florian'
age = 37

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

#  Positional arguments
print('My name is {name} and I am {age}'.format(name=name, age=age))
# in JS:
# console.log('My name is %s and I am %i', name, age)


# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')
# in JS (template literals):
# console.log(`My name is ${name} and I am ${age}`);


# String Methods

s = 'helloworld'

# Capitalize string
print(s.capitalize())


# Make all uppercase
print(s.upper())
# in JS:
# s.toUpperCase()


# Make all lower
print(s.lower())
# in JS:
# s.toLowerCase()


# Swap case
print(s.swapcase())

# Get length
print(len(s))
# in JS:
# s.length

# Replace
print(s.replace('world', 'everyone'))
# in JS:
# same thing

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))
# in JS:
# same thing


# Ends with
print(s.endswith('d'))
# in JS:
# same thing


# Split into a list
print(s.split())
# in JS:
# same thing


# Find position
print(s.find('r'))
# in JS:
# s.indexOf('r')


# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
# in JS - careful because of coercion to number before check:
# isNaN(s)