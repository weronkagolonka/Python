"""
EGEN OPPGAVE
Lag en BMI kalkulator ved bruk av lister eller ordboeker. Les inn vekt og hoyde fra brukeren og beregn dens BMI.
Sjekk om brukeren er i god form og skriv ut resultatet. Du kan ogsaa sjekke om brukeren gikk ned i vekt ved aa
sammenligne to siste bmi verdier. 
"""

"""
Dette er en personlig BMI kalkulator.
Programmet lagrer informasjon om brukerens vekt og hoyde.
Deretter beregner dens BMI, sammenligner med den forrige verdien(om den finnes),
og forteller om brukeren har gjort en fremskritt.
"""
vekt = []
hoyde = int(input("Hvor hoy er du? (cm)\n")) # vi forutsetter at hoyde er en konstant verdi(det er kun for voksne!)
bmi = []

def getInfo(kg, cm, balans):
    oppdaterVekt = int(input("Hvor mye veier du i dag? (kg)\n"))
    kg.append(oppdaterVekt) # vi lagrer vekt fra i dag i en liste
    cm = cm / 100 # for aa beregne BMI trenger man hoyde i meter, brukeren oppgir den i cm for det er enklere(tror jeg)
    resultat = kg[len(kg) - 1] / (cm * cm) # vi berenger BMI med aktuell vekt
    balans.append(resultat) # vi lagrer denne bmi i lista

def rekkefolge(sp): # denne prosedyren gjor at man bestemmer om man vil legge til mer data(f.eks. etter aa ha veiet seg)
    if sp == "ja":
        oversikt()
    elif sp == "nei":
        print("Den er grei.")
    else:
        print("Det forsto jeg ikke.") # hvis det er f.eks. en stavefeil, saa faar man oppgi opplysninger paa nytt
        forstette()

def forstette():
    hvis = input("Vil du legge til mer data?\n")
    rekkefolge(hvis) # programmet er paa en maate uendelig hvis brukeren ikke stopper det selv

def sjekkBmi(bmiVerdi): #Denne prosedyren sjekker om brukeren har god BMI
    if bmiVerdi < 18.5:
        print("Det er for lite. Du burde besoke en lege og finne en god plan for deg.")
    elif bmiVerdi >= 18.5 and bmiVerdi < 25:
        print("Den er en abolutt normal verdi. Du er i god form!")
    elif bmiVerdi >= 25 and bmiVerdi < 30:
        print("Det er litt for mye. Kanskje kutte ut cola?")
    else:
        print("Det er deinifitvt for mye. Du burde besoke en lege og finne en god plan for deg.")

def oversikt(): #Denne prosedyren setter i gang hele programmet
    getInfo(vekt, hoyde, bmi) # faa informasjon
    print("La oss se pa din BMI:", round(bmi[len(bmi) - 1], 2)) # brukeren faar se bmi-en sin
    sjekkBmi(bmi[len(bmi) - 1]) # sjekk BMI
    if len(bmi) == 1: # sammenlign to siste verdier og sjekk om brukeren har gjort en fremskritt
        print("Keep on going! Vi trenger mer data!")
    elif len(bmi) > 1:
        if bmi[len(bmi) - 1] < bmi[len(bmi) - 2]:
            print("Bra jobba! Du har gjort et fremskritt!")
        elif bmi[len(bmi) - 1] == bmi[len(bmi) - 2]:
            print("Det er akurrat samme som den forrige verdien. Du er pa vei!")
        else:
            print("Det er litt mer enn for. Ikke bekymre deg! Du vil oppna det!")
    forstette() # spoer om brukeren vil legge til mer data


oversikt()
