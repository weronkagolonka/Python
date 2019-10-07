"""
Dette programmet tar inn data fra fil og skriver ut statistikk for et telefonsalg-firma.
Det viser hvem som hadde solgt mest denne maaneden, alle aktive selgere, total og gjennomsnittlig antall salg.
"""

minFil = open("sale_statistics.txt") #apner filen

def innlesning(filnavn): #funksjon som leser inn data fra filen
    selgere = {} #tom ordbok for alle selgere
    for linje in filnavn:
        linjeListe = linje.split() #deler linje i to elementer
        selgere[linjeListe[0]] = int(linjeListe[1]) #loekke gaar gjennom filen og legger til selgers navn og dens antall salg til ordboken
    return selgere #returnerer ordboken

def maanedensSalgsperson(ordbok): #prosedyren som tar imot en ordbok
    stoersteSalg = 0
    bestSelgersNavn = ""
    for noekkel, verdi in ordbok.items(): #deler ordbokens elementer ved bruk av .items() metode
        if verdi > stoersteSalg: #loekke sjekker alle verdiene for aa finne stoerste antall salg
            stoersteSalg = verdi
            bestSelgersNavn = noekkel #best selgers navn blir noekelen av den stoerste verdien
    print("Maaneds ansatte er:", bestSelgersNavn.upper(), "med", stoersteSalg, "salg.") #skriver ut hvem som solgte mest

def totaltAntallSalg(ordbok): #funksjon tar imot en ordbok og beregner summen av alle salg
    sum = 0
    for noekkel in ordbok: #loekke adderer alle elementene
        sum += ordbok[noekkel]
    return sum #returnerer summen

def gjennomsnittSalg(ordbok): #funksjonen tar imot en ordbok og beregner gjennomsnittlig salg
    sum = totaltAntallSalg(ordbok) #kaller funksjonen for aa hente totalsalg
    antallElementer = len(ordbok) #ordbokens lengde = antall elementer = antall selgere/salg
    return round(sum / antallElementer, 2) #returnerer gjennomsnittet med 2 desimaler

def hovedProgram(ordbok): #prosedyren som setter alt i verk, tar imot ordoboken
    maanedensSalgsperson(ordbok) #kaller funksjonen som skriver ut maaneds ansatte
    print(" ")
    print("Aktive selgere denne maaneden:", len(ordbok)) #skriver ut antall selgere
    print("Total antall salg:", totaltAntallSalg(ordbok)) #kaller funskjonen for aa faa summen av salg
    print("Gjennomsnittlig antall salg per salgsperson:", gjennomsnittSalg(ordbok)) #kaller funksjon for aa faa gjennomsnittlig salg

hovedProgram(innlesning(minFil)) #kaller hovedprosedyren og tar innlesning funksjon som argumentet. Funksjonen tar filen som argumentet, og setter alt i verk
