cat = 'putila'
cat2 = 'Basila'
kg = 100

print("Is cat == 'putila' ? I predict True.")
print(cat == 'putila')

print("\nIs cat == 'basila' ? I predict False.")
print(cat == 'basila')

print("Is cat == 'putila' and kg == 100 ? I predict True.")
print((cat == 'putila') and (kg == 100))

print("Is cat == 'putila' and kg < 100 ? I predict False.")
print((cat == 'putila') and (kg < 100))

print("Is cat == 'putila' and kg >= 99 ? I predict True.")
print((cat == 'putila') and (kg >= 99))

print("Is cat == 'putila' and kg <= 99 ? I predict False.")
print((cat == 'putila') and (kg <= 99))

print("Is cat == 'putila' or kg < 99 ? I predict True.")
print((cat == 'putila') or (kg < 99))

print("Is cat == 'basila' or kg < 99 ? I predict False.")
print((cat == 'basila') or (kg < 99))

print("Is cat == 'basila' or kg < 99 ? I predict True.")
print((cat == 'basila') or (kg > 99))

print("Is cat == 'basila' and kg < 99 ? I predict False.")
print((cat == 'basila') and (kg < 99))

print("Is cat != 'putila' ? I predict False.")
print(cat != 'putila')

print("Is cat2 == 'basila' ? I sprect False.")
print(cat2 == 'basila')

print("Is cat2 == 'Basila' ? I sprect True.")
print(cat2.lower() == 'basila')

cats = ['basila', 'putila', 'belu']
cat = 'tazz'

if cat not in cats:
    print(f"{cat.title()}, iesi acasa!")

cat = 'belu'

if cat in cats:
    print(f"{cat.title()}, hai in Pastele ma-tii!")