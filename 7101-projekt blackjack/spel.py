import random

kortlek = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]

player = []

dealer = []



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

def bust():
    print("bust", player, sum(player))

def dealerbust():
    print("bust", dealer, sum(dealer))

def chose():
    choice = "hit"
    while choice == "hit":
        if sum(player) > 21:
            print(bust())
        choice = input("hit or stay:")
        if choice.lower() == "hit":
            player.append(kortlek[0])
            kortlek.pop(0)
            print(player[0], player[1], player[2])
        elif choice.lower() == "stay":
            print(sum(player))

def dealer():
    while sum(dealer) < 16:
        dealer.append(kortlek[0])
        kortlek.pop(0)
        print(dealer, sum(dealer))
    if sum(dealer) > 21:
        dealerbust()



start()

chose()

dealer()