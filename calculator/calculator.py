"""
print('La oss beregne naar vil du bli en pensjonist')

yearOfBirth = int(input('Hvilket aar ble du foedt? '))

age = 2019 - yearOfBirth
print(f'Du er {age} aar gammel!')

def retirementCalculator():
    yearsToRetirement = 67 - age
    yearOfRetirement = 2019 + yearsToRetirement
    print(f'Du vil faa din foerste pensjon i {yearOfRetirement}')

retirementCalculator()
"""
#value 1, operator, value2
#vannlig kalkulator

def kalkulator(tall1, operator, tall2):

    utregning = [float(tall1), operator, float(tall2)]

    if utregning[1] == "+":
        resultat = utregning[0] + utregning[2]
    elif utregning[1] == "-":
        resultat = utregning[0] - utregning[2]
    elif utregning[1] == "*":
        resultat = utregning[0] * utregning[2]
    elif utregning[1] == "/":
        resultat = utregning[0] / utregning[2]

    return resultat

def melding(wynik):
    print("Resultatet er:", wynik)

def init(result):
    nesteOper, nesteT2 = input("").split()
    melding(kalkulator(result, nesteOper, nesteT2))
    fortsett(result)

def fortsett(currentResult):

    spors = input("Vil du fortsette med dette resultatet? (ja/nei)\n> ").lower()

    if spors == "ja":
        init(currentResult)
    elif spors == "nei":
        print("Den er grei. Resultatet er:", currentResult)
    else:
        print("Jeg forstar ikke det.")


t1, oper, t2 = input("Skriv inn din operasjon(forste tall, operator, andre tall)\n> ").split()
denneResultatet = kalkulator(t1, oper, t2)
melding(denneResultatet)
fortsett(denneResultatet)
