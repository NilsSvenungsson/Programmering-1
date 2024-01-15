import random

kortlek = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]

spelare = []

dealer = []

random.shuffle(kortlek)


def start():
    spelare.append(kortlek[0])
    kortlek.pop(0)
    dealer.append(kortlek[0])
    kortlek.pop(0)
    spelare.append(kortlek[0])
    kortlek.pop(0)
    dealer.append(kortlek[0])


start()

print(kortlek)

print(spelare)

print(dealer[0], "x")