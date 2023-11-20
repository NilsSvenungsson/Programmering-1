import random
tre = 0

for tal in range(20):
    tal = random.randint(1, 6)
    print(tal)
    if tal == 3:
        tre = tre + 1
print("antal 3:or:", tre)
