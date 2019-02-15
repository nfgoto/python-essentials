# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# Create function with default parameter value
def sayHello(name='Floriam'):
    print(f'Hello {name}')
# In JS:
# function sayHello(name='Floriam') { 
#     console.log(`Hello ${name}`);
# }

# call function
sayHello()

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total
# In JS
# function getSum(num1, num2) { 
#   const total = num1 + num2; 
#   return  total;
# }

sum = getSum(11, 99)
print(sum)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2: num1 + num2
# In JS
# let getSum = (num1, num2) => num1 + num2


print(getSum(10, 3))
