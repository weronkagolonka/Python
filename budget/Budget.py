"""
BUDSJETT
Dette er programmet som samler data om brukerens kostnader og inntekter.
Deretter beregner og skriver ut balansen.
"""

income = {} #lagrer data i ordboker
expense = {}

whatType = input("Hva slags data vil du legge til? (kostnad: K/inntekt: I)\n").lower() #for aa unngaa feil, taster brukeren bare K eller I
info = ["Beskrivelse: ", "Belop: "] #programmet henter riktig sporsmaalet senere


def addItem(type): #fyller ut ordboker med nodvendig informasjon
    if type == "k":
        description = input(info[0])
        amount = int(input(info[1]))
        expense[description] = amount
    elif type == "i":
        description = input(info[0])
        amount = int(input(info[1]))
        income[description] = amount

addItem(whatType) #kaller prosedyren
again = input("Vil du legge til mer data? (J/N) ").lower()

while again == "j": #gjentar intill brukeren skriver nei
    whatType = input("Hva slags data vil du legge til? (kostnad: K/inntekt: I)\n").lower()
    addItem(whatType)
    again = input("Vil du legge til mer data? (J/N) ").lower()

print("Den er grei.\n")
print("Ditt budsjett:\n")
print("Inntekter:", income)
print("Kostander:", expense, "\n") #viser alt som har blitt lagt til ordbokene

def calculate(inc, exp): #beregner summer av kostnader og inntekter
    totalInc = 0
    for x in inc.values(): #gaar bare gjennom innholdsverdier, ikke nokkelverider
        totalInc += x

    totalExp = 0
    for y in exp.values():
        totalExp += y

    balans = totalInc - totalExp #beregner total balans og returnerer
    return balans

print("Balansen er:", calculate(income, expense)) #skriver ut balansen
