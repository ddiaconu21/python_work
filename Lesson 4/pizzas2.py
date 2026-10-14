pizzas = ['Quatro Stagioni', 'Margherita', 'Prosciutto e Funghi']

friend_pizzas = pizzas[:]

pizzas.append('Diavola')
friend_pizzas.append('Carnivora')

for pizza in pizzas:
    print(f"My favourite pizza is {pizza}")

for pizza in friend_pizzas:
    print(f"My friend's favourite pizza is {pizza}")
