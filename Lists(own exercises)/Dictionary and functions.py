# Just random stuff
person = {'name':'', 'age':'', 'city':''}

person['name'] = input('Name: ')
person['age'] = int(input('Age: '))
person['city'] = input('City: ')

def foo(name, age, city):
    return f'Hello, {name}! You are {age} years-old and your home is {city}.'

print(foo(person['name'], person['age'], person['city']))
