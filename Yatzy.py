import random

def yatzy():
    if sum(tärningar) == 30:
        print("Du fick Yatzy!")
        return True
    else:
        return False

def kåk():
    if tärningar[0] == tärningar[1] == tärningar[2] and tärningar[3] == tärningar[4] or tärningar[0] == tärningar[1] and tärningar[2] == tärningar[3] == tärningar[4]:
        print("Du fick kåk!")
        return True
    else:
        return False

def stor_stege():
    if tärningar[0] == 2 and tärningar[1] == 3 and tärningar[2] == 4 and tärningar[3] == 5 and tärningar[4] == 6 and kåk() == False:
        print("Du fick stor stege!")
        return True
    else:
        return False


def liten_stege():
    if tärningar[0] == 1 and tärningar[1] == 2 and tärningar[2] == 3 and tärningar[3] == 4 and tärningar[4] == 5 and stor_stege() == False:
        print("Du fick liten stege!")
        return True
    else:
        return False

def fyrtal():
    if tärningar[0] == tärningar[1] == tärningar[2] == tärningar[3] and liten_stege() == False or tärningar[1] == tärningar[2] == tärningar[3] == tärningar[4] and liten_stege() == False:
        print("Du fick fyrtal!")
        return True
    else:
        return False

def triss():
    if tärningar[0] == tärningar[1] == tärningar[2] and fyrtal() == False and kåk() == False or tärningar[1] == tärningar[2] == tärningar[3] and fyrtal() == False and kåk() == False or tärningar[2] == tärningar[3] == tärningar[4] and fyrtal() == False and kåk() == False:
        print("Du fick triss!")
        return True
    else:
        return False

def två_par():
    if tärningar[0] == tärningar[1] and triss() == False or tärningar[1] == tärningar[2] and triss() == False or tärningar[2] == tärningar[3] and triss() == False or tärningar[3] == tärningar[4] and triss() == False:
        print("Du fick tvåpar")
    else:
        return False

def ett_par():
    if tärningar[0] == tärningar[1] and två_par() == False or tärningar[1] == tärningar[2] and två_par() == False or tärningar[2] == tärningar[3] and två_par() == False or tärningar[3] == tärningar[4] and två_par() == False:
        print("Du fick ettpar!")



#spelet

for tärningar in range(1000):
    tärningar = []

    t1 = random.randint(1, 6)
    t2 = random.randint(1, 6)
    t3 = random.randint(1, 6)
    t4 = random.randint(1, 6)
    t5 = random.randint(1, 6)

    tärningar.append(t1)
    tärningar.append(t2)
    tärningar.append(t3)
    tärningar.append(t4)
    tärningar.append(t5)
    tärningar.sort()
    print(tärningar)
    yatzy()
    kåk()
    stor_stege()
    liten_stege()
    fyrtal()
    triss()
    två_par()
    ett_par()