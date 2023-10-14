tal = int(input("Skriv ett tal: "))

if 0 <= tal <= 9:
    print("Ensiffrigt tal")
elif 10 <= tal <= 99:
    print("Tvåsiffrigt tal")
elif 100 <= tal <= 999:
    print("tresiffrigt tal")
elif tal >= 1000:
    print("minst ett fyrsiffrigt tal")
elif tal < 0:
    print("negativt tal")