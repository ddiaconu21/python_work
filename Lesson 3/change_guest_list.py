names = ['Michael Jackson', 'Ado', 'Eminem']

print(f"Hello, {names[0]}, would you like to come to dinner?")

name = names[1].title()

print(f"Hello, {name}, would you like to come to dinner?")

print("Hello, " + names[2] + " would you like to come to dinner?")

print(f"Sadly, {name} can't make it to the dinner.")

names[1] = 'Steve Jobs'

print(f"Hello, {names[0]}, would you like to come to dinner?")
print(f"Hello, {names[1]}, would you like to come to dinner?")
print(f"Hello, {names[2]}, would you like to come to dinner?")

print(len(names))
