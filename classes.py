# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age

  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
    self.age += 1


# Extend class
class Customer(User):
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance

  # method overring
  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

#  Init user object
florian = User('Florian GOTO', 'florian@gmail.com', 99)
# Init customer object
tatu = Customer('Tatu KENYATTA', 'tatu@yahoo.com', 25)

tatu.set_balance(500)
print(tatu.greeting())

florian.has_birthday()
print(florian.greeting())