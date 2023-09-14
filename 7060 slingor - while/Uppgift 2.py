antal = int(input("Hur många tal vill du ha? "))
tal = int(input("Skriv in det lägsta talet: "))
i = tal + antal

while tal < i:
    print(tal)
    tal = tal + 1