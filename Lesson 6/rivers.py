rivers = {'The Amazon' : 'Brazil', 'The Ganges' : 'India', 
          'The Thames' : 'England'}

for key, value in rivers.items():
    print(f"{key} river runs through {value}.")

for key in rivers:
    print(key)

for values in rivers.values():
    print(values)