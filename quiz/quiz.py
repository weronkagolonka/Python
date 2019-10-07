"""
Dette programmet er en quiz som sjekker brukerens kjennskap om Polen.
"""

print("Velkommen til quizen om Polen!\nSvar paa disse fire spoersmaalene for aa se hvor mye du vet om dette landet.\nVelg et svar du synes er riktig - a, b eller c.\n")
input("Trykk paa ENTER for aa fortsette.\n ") #tekstformattering ved bruk av \n

poeng = 0

print("Hva er Polens hovedstad?")
print("A. Warszawa")
print("B. Gdansk")
print("C. Katowice")
spoersmal1 = input().lower() #forsikrer meg at input er en liten bokstave uansett hva blir tastet inn i terminalen
if spoersmal1 == "a":
    print("Det var riktig!\n ")
    poeng += 1
else:
    print("Polens hovedstad er Warszawa.\n ")
    poeng += 0

print("Har Polen en grense med Russland?")
print("A. Ja")
print("B. Nei")
spoersmal2 = input().lower()
if spoersmal2 == "a":
    print("Riktig!\n ")
    poeng += 1
else:
    print("Vi deler en kort grense med en liten russisk by - Kaliningrad.\n ")
    poeng += 0

print("Hvilken valuta brukes det i Polen?")
print("A. Euro")
print("B. Rubel")
print("C. Zloty")
spoersmal3 = input().lower()
if spoersmal3 == "c":
    print("Veldig bra!\n ")
    poeng +=1
else:
    print("I polen er valutaen zloty(PLN).\n ")
    poeng += 0

print("Har Polen tilgang til havet?")
print("A. Nei")
print("B. Ja")
spoersmal4 = input().lower()
if spoersmal4 == "b":
    print("Det var riktig!\n ")
    poeng += 1
else:
    print("Polen ligger ved havet, det er Ostersjoen.\n ")
    poeng += 0

def resultat(allePoeng):
    if allePoeng == 0 or allePoeng == 1:
        print("Ser ut som Polen er det minst viktige landet i verden din.")
    elif allePoeng == 2 or allePoeng == 3:
        print("Gennerelt kjennskap om Polen er noe som kjennetegner deg.")
    elif allePoeng == 4:
        print("Du burde vurdere aa flytte til Polen!")

resultat(poeng)
