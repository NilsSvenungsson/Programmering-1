import random

spela = "ja"

#Delar ut kort

def start(player, dealer):
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

#Bust

def bust():
    print("bust", player, sum(player))
    print("Dealern vann!")

#Dealer bust

def dealerbust():
    print("Dealer bust", dealer, sum(dealer))
    print("Du vann!")


#Välj

def chose():
    choice = "hit"
    while choice == "hit":
        if sum(player) > 21:
            choice = "stay"
            print(bust())
        elif choice.lower() == "hit":
            choice = input("hit or stay:")
            if choice == "hit":
                player.append(kortlek[0])
                kortlek.pop(0)
                print_player_hand()
            
            elif choice.lower() == "stay":
                print(sum(player))


def print_player_hand():
    print(player[0], player[1], player[2])
    # skriv ut handen på en rad
    for card in player:
        print(card, end = ", ")


#Dealern tar kort

def dealer_play():
    while sum(dealer) < 16:
        dealer.append(kortlek[0])
        kortlek.pop(0)
        print(dealer, sum(dealer))
    if sum(dealer) > 21:
        dealerbust()


#Vet ej

def end():
    if 0 == 0:
        print("tjenare")


#Avgör vem som vann

def winner(pengar):
    if 21 > sum(player) > sum(dealer):
        print("Du vann! Du vann", pengar, "kr", "Din summa: ", sum(player), "Dealerns summa: ", sum(dealer))
    elif 21 > sum(player) == sum(dealer):
        print("Dealern vann! Du förlorade", pengar, "kr", "Din summa: ", sum(player), "Dealerns summa: ", sum(dealer))
    elif 21 > sum(dealer) > sum(player):
        print("Dealern vann! Du förlorade", pengar, "kr", "Din summa: ", sum(player), "Dealerns summa: ", sum(dealer))


#Hur mycket ska du betta

def bet():
    pengar = ""
    while pengar.isdigit() == False:
        pengar = input("Hur mycket vill du betta i kronor?: ") 
    return int(pengar)


while spela.lower() == "ja":
    #Variabler och listor

    kortlek = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]

    dealer = []

    player = []

    #Blandar kortleken

    pengar = bet()

    random.shuffle(kortlek)

    start(player, dealer)

    chose()

    if sum(player) <= 21:
        dealer_play()

    winner(pengar)
    spela = input(str("Vill du spela igen?: "))