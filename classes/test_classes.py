"""
Dette programmet skal teste klassen 'Person'.
"""

from test_classes import Person #importerer klassen fra filen 'egenOppgave'

def hovedProgram(): #prosedyren som lar brukeren legge til sin data
    navn1 = input("Hva heter du?\n>")
    alder1 = input("Hvor gammel er du?\n>")
    person1 = Person(navn1, alder1) #lager et objekt ved bruk av de to brukerens input

    hobbyer = input("Hva er din hobby?\n>") #brukeren skriver inn sin hobby

    while hobbyer != "nei": #inntil bruker sier nei, vil loekken fortsette aa spoerre om andre hobbyer og legger dem til lista
        person1.leggTilHobby(hobbyer) #kaller metoden
        hobbyer = input("Skriv en hobby til. Skriv 'nei' hvis du vil avslutte.\n>")

    person1.skrivUt() #etter at loekken har avslutett, skriver programmet ut objektets informasjon

hovedProgram() #kaller prosedyren
