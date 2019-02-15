# If/ Else conditions are used to decide to do something based on something being true or false

x = 43
y = 22

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x > y:
    print(f'{x} is greater than {y}')

# If/else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is not greater than {x}')

# elif
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is less than {x}')

# Nested if's
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')


# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')
# In JS:
# if( x > 2  &&  x <= 10 )...


# or
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 or less than or equal to 10')
# In JS:
# if ( x > 2 || x <= 10 )...

# not
if not(x == y):
    print(f'{x} is not equal to {y}')
# In JS:
# if ( x !== y )...

# Membership Operators (in, not in) - Membership operators are used to test if a value exists in a sequence or not

numbers = [1, 2, 3, 4, 5, 43]

#  in
if x in numbers:
    print(f'{x} is in numbers: {x in numbers}')

# not in
if x not in numbers:
    print(f'{x} is not in numbers: {x not in numbers}')

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location, also used to determine whether a value is of a certain class or type:

# is
if x is x:
    print(f'x is x: {x is x}')

if type(x) is int:
    print(f'type of x is int: {type(x) is int}')
    # In JS
    # if(typeof x === 'number')...
    # if(anOject instanceof aConstructorFunc / class)... (prototype property of a constructor appears anywhere in the prototype chain of an object.)


# is not
if x is not y:
    print(f'x is not y: {x is not y}')
