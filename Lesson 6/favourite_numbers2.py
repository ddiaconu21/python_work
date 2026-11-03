favourite_numbers = { 'cipicel': [1, 2, 3, 4],
                      'parparel': [2, 3, 4, 5],
                      'capacel': [3, 4, 5, 6],
                      'checulet': [5, 6, 7, 8],
                      'papi': [6, 7, 8, 9],
                    }

for name, numbers in favourite_numbers.items():
    print(f"\n{name.title()}'s favourite numbers are:")
    for number in numbers:
        print(f"\t{number}")