pet_0 = {'name':'basila', 'owner': 'prichi', 'type': 'cat'}
pet_1 = {'name':'putila', 'owner': 'cipi', 'type': 'cat'}
pet_2 = {'name':'belu', 'owner': 'parpi', 'type': 'cat'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    name = (f"{pet['name'].title()}")
    owner = (f"{pet['owner'].title()}")
    type = (f"{pet['type'].title()}")

    print(f"{owner} has a pet {type} named {name}")

