svar = "ja"

while svar.lower() == "ja":
    print("Du är bäst!")
    svar = input("Vill du höra det igen?")
if svar.lower() == "nej":
    print("tack och hej")