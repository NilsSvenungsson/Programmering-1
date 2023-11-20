import random

lista = []

tre = 0

for tal in range(20):
    tal = random.randint(1, 6)
    lista.append(tal)
    if tal == 3:
        tre = tre + 1
print(lista)
print("antalet 3:or är:", tre)