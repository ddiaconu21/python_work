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

print("I found a bigger table! Three more people will come!")

names.insert(0, 'Tatsuki Fujimoto')
names.insert(2, 'Adam Gontier')
names.insert(6, 'Keanu Reeves')

print(f"Hello, {names[0]}, would you like to come to dinner?")
print(f"Hello, {names[1]}, would you like to come to dinner?")
print(f"Hello, {names[2]}, would you like to come to dinner?")
print(f"Hello, {names[3]}, would you like to come to dinner?")
print(f"Hello, {names[4]}, would you like to come to dinner?")
print(f"Hello, {names[5]}, would you like to come to dinner?")

print("Sadly I can invite only 2 people to dinner after all. Sorry!")

first_guest = names.pop(5)
second_guest = names.pop(4)
third_guest = names.pop(3)
fourth_guest = names.pop(2)

print(f"Hello, {names[0]}, would you like to come to dinner?")
print(f"Hello, {names[1]}, would you like to come to dinner?")

del names[1]
del names[0]

print(names)