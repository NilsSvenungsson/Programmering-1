tal = int(input("Skriv ett tal: "))

if 0 < tal <= 9:
    print(tal, "är ett ensiffrigt tal")
elif 10 < tal <= 99:
    print(tal, "är ett tvåsiffrigt tal")
elif 100 < tal <= 999:
    print(tal, "är ett tresiffrigt tal")
elif tal >= 1000:
    print(tal, "är minst ett fyrsiffrigt tal")
elif tal < 0:
    print(tal, "är ett negativt tal")