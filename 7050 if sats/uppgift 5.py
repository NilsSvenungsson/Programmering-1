x = int(input("Skriv ett tal: "))
y = int(input("Skriv ett till tal: "))
z = int(input("Skriv ett sista tal: "))

if x < y and x < z:
    print(x, "är minst")
elif y < x and y < z:
    print(y, "är minst")
elif z < x and z < y:
    print(z, "är minst")