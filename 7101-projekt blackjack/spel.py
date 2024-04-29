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

has_bust = False

def bust():
    print("bust", player, sum(player))
    print("dealern vann! ", sum(dealer), dealer)
    return True


#Dealer bust
def dealerbust():
    print("bust", dealer, sum(dealer))
    print("Du vann! ", sum(player), player)


#Välj

def chose(has_bust):
    choice = "hit"
    if sum(player) > 21:
        choice = "stay"
    while choice == "hit":
        if sum(player) > 21:
            choice = "stay"
            has_bust = bust()
        else:
            choice = input("hit or stay:")
        if choice.lower() == "hit":
            player.append(kortlek[0])
            kortlek.pop(0)
            print_player_hand()
            
        elif choice.lower() == "stay" and has_bust == False:
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

def winner():
    if 21 <= sum(player) > sum(dealer) and sum(dealer) < 21:
        print("Du vann!", "Din summa: ", sum(player), "Dina kort: ", player, "Dealerns summa: ", sum(dealer), "Dealerns kort: ", dealer)
    elif sum(player) == sum(dealer):
        print("Dealer vann!", "Din summa: ", sum(player), "Dina kort: ", player, "Dealerns summa: ", sum(dealer), "Dealerns kort: ", dealer)
    elif 21 <= sum(dealer) > sum(player):
        print("Dealern vann", "Din summa: ", sum(player), "Dina kort: ", player, "Dealerns summa: ", sum(dealer), "Dealerns kort: ", dealer)



while spela.lower() == "ja":
    #Variabler och listor
    kortlek = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
    dealer = []
    player = []
    #Blandar kortleken
    random.shuffle(kortlek)
    start(player, dealer)
    chose(has_bust)
    dealer_play()
    winner()
    spela = str(input("Vill du spela igen?: "))