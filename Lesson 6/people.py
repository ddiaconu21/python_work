person_0 = {}
person_1 = {}
person_2 = {}

person_0['first_name'] = 'muscatila'
print(person_0['first_name'])
person_0['last_name'] = 'checulet'
print(person_0['last_name'])
person_0['age'] = '3'
print(person_0['age'])
person_0['city'] = 'muscatei'
print(person_0['city'])

person_1['first_name'] = 'cipcirina'
print(person_1['first_name'])
person_1['last_name'] = 'parparel'
print(person_1['last_name'])
person_1['age'] = '4'
print(person_1['age'])
person_1['city'] = 'parparei'
print(person_1['city'])

person_2['first_name'] = 'cipi'
print(person_2['first_name'])
person_2['last_name'] = 'simpaticipi'
print(person_2['last_name'])
person_2['age'] = '5'
print(person_2['age'])
person_2['city'] = 'princhindei'
print(person_2['city'])

people = [person_0, person_1, person_2]

for person in people:
    name = (f"{person['first_name'].title()} {person['last_name'].title()}")
    age = (f"{person['age']}")
    city = (f"{person['city'].title()}")
    print(f"{name} of {city} is {age} years old.")
