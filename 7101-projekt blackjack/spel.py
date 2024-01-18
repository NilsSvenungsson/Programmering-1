import random

kortlek = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]

player = []

dealer = []

choice = "hit"

random.shuffle(kortlek)


def start():
    player.append(kortlek[0])
    kortlek.pop(0)
    dealer.append(kortlek[0])
    kortlek.pop(0)
    player.append(kortlek[0])
    kortlek.pop(0)
    dealer.append(kortlek[0])
    kortlek.pop(0)
    print(player[0], player[1])
    print(dealer[0], "x")

def chose():
    while choice.lower() == "hit":
        choice = input("hit or stay:")
        if choice.lower() == "hit":
            player.append(kortlek[0])
            kortlek.pop(0)
            print(player[0], player[1], player[2])
        elif choice.lower() == "stay":
            print(sum(player))
        elif sum(player) < 21:
            print("bust")


start()

chose()