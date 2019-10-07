"""
Forslag fra oppgaven 6:

Skriv en klasse Person med en konstruktør som tar imot navn og alder.
I tillegg skal konstruktøren ha en tom liste hobbyer.
Skriv en metode leggTilHobby som tar imot en tekststreng og legger den til i hobbyer-listen.
Skriv også en metode skrivHobbyer. Denne metoden skal skrive alle hobbyene etter hverandre på en linje.
Gi deretter Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og alder kaller på metoden skrivHobbyer.
Test klassen i en ny fil. La brukeren skrive inn navn og alder, og lag et Person-objekt med informasjonen du får.
Deretter skal brukeren ved hjelp av en løkke få legge til så mange hobbyer de vil.
Når brukeren ikke lenger ønsker å oppgi hobbyer skal statistikk om brukeren skrives ut.
"""

class Person: #oppretter klassen
    def __init__(self, navn, alder): #oppretter konstruktoeren som tar imot navn og alder
        self._navn = navn
        self._alder = alder
        self._hobbyer = [] #tom liste av hobbyer som blir fylt ut av brukeren

    def leggTilHobby(self, tekst): #metoden som tar imot en tekststreng og legger den til lista
        self._hobbyer.append(tekst)

    def skrivHobbyer(self): #metoden som itererer gjennom lista og skriver hobbyer paa hver sin linje
        for hobby in self._hobbyer:
            print(hobby)

    def skrivUt(self): #metoden som skriver ut total informasjon om objektet
        print("PERSON:")
        print("Navn:", self._navn)
        print("Alder:", self._alder)
        print("\nHOBBYER:")
        self.skrivHobbyer()
