x = int(input("Jag ska ställa upp de tal du skriver i storleksordning, skriv ett tal: "))
y = int(input("Skriv ett till tal: "))
z = int(input("Skriv ett sista tal: "))

if x < y < z:
    print(x, y, z)
elif x < z < y:
    print(x, z, y)
elif y < x < z:
    print(y, x, z)
elif y < z < x:
    print(y, z, x)
elif z < x < y:
    print(z, x, y)
elif z < y < x:
    print(z, y, x)