from random import randint
from celle import Celle

class Spillebrett:
#klassen definerer spillebrett som blir fyllt med celle-objekter
#klassen utfoerer det selve spillet - bestemmer hvilke celler overlever og oppdaterer nytt generert spillebrett

    def __init__(self, rader, kolonner):
    #konstruktoeren definerer spillebretes egenskaper og paa grunnlag av dem genererer selve brettet
        self._rader = rader
        self._kolonner = kolonner
        self._ruteNett = []
        self._generasjonsnummer = 0
        self._generer()

    def tegnBrett(self):
    #tegn spillebrettet i terminalen - skriv ut alle celle-objekter i ruteNett liste
    #tegner fra 1 til brettes maaler; + 1 fordi vi oppretter en ekstra rad og kolonne som ikke skal skrives ut
        print()
        for rad in range(1, (self._rader + 1)):
            for celle in range(1, (self._kolonner + 1)):
                print(self._ruteNett[rad][celle].hentStatusTegn(), end = "")
            print()
    
    def oppdatering(self):
    #oppdaterer spillebrettet i henhold til spillets regler

        #lister inneholder bare de cellene som endrer sin status
        levende = []
        doed = []

        #finner naboer for hver celle paa spillebrettet ved bruk av finnNabo() metode
        for i in range(1, self._rader + 1):
            for j in range(1, self._kolonner + 1):
                cellsNaboer = self.finnNabo(i, j)
                teller = 0
                for nabo in cellsNaboer:
                    if nabo.erLevende():
                        teller += 1

                #telleren oekes hver gang naar nabo er levende. 
                #slik finner vi antall levende naboer og bestemmer om cellen skal overleve (avhengig av statusen)
                if not self._ruteNett[i][j].erLevende() and teller == 3:
                    levende.append(self._ruteNett[i][j]) #reproduksjon
                elif self._ruteNett[i][j].erLevende() and teller < 2:
                    doed.append(self._ruteNett[i][j]) # underpopulasjon
                elif self._ruteNett[i][j].erLevende() and teller > 3:
                    doed.append(self._ruteNett[i][j]) # overpopulasjon

        #endrer status til celler
        for celle in levende:
            celle.settLevende()
        
        for celle in doed:
            celle.settDoed()

        #oppdaterer og returnerer generasjons nummer
        self._generasjonsnummer += 1
        return self._generasjonsnummer

    def finnAntallLevende(self):
    #metoden finner alle levende celler paa spillebrettet
        
        #her er min idee om at metoden legger levende celler til en liste, og for aa faa antall levende celler sjekker vi listens lengde
        #jeg implementerte det fordi det kan hende at noen celler overlever og spillebrettet endrer seg ikke.
        #da vil jeg vite hvilke celler overlevde og gi beskjed til brukeren at 'livet vant'.
        #det kan hende at antall levende celler forblir samme fra generasjon tli generasjon, men det betyr alltid ikke at spillet er avslutett.
        levendeCeller = []

        for i in range(1, self._rader + 1):
            for j in range(1, self._kolonner + 1):
                if self._ruteNett[i][j].erLevende():
                    levendeCeller.append(self._ruteNett[i][j])

        #returnerer liste med levende celler
        return levendeCeller

    def _generer(self):
    #metoden genererer spillebrettet paa grunnlag av antall rader og kolonner
    
        #ruteNett = [[[celle],[celle]], [[celle], [celle]]]
        #ruteNett[rad][cellens posisjon = kolonne]
        #metoden genererer en rad (og kollone) ekstra - de printes ikke til terminalen
        #jeg gjorde det for aa slippe aa analysere hver mulig kombinasjon i finnNabo() metode
        
        for rad in range(0, self._rader + 1):
        #legger rad til ruteNett
            self._ruteNett.append([])

        for antallRader in range(0, (self._rader + 1)):
            for cellInRad in range(0, (self._kolonner + 1)):
            #oppretter celle og legger til riktig rad-liste
            #sannsynlighet til at cellen er levende er 1/3
                nyCelle = Celle()
                sjanse = randint(0, 2)
                if sjanse == 0:
                    nyCelle.settLevende()
                else:
                    nyCelle.settDoed()    
                self._ruteNett[antallRader].append(nyCelle)

            
    def finnNabo(self, rad, kolonne):
    #metoden finner alle naboer til en gitt celle, legger dem til liste og returnerer denne listen
        
        naboer = []

        #alle celler blir med - bortsett fra celler i "ghost" rad og kolonne. 
        #det gjoer at alle "relevante" celler har 8 naboer. 
        #loekke tar til hensyn kun de naboene som befinner seg i spillebrettet (1-antall rader, 1-antall kolonner)

        for i in range(rad-1, rad+2):
            for j in range(kolonne-1, kolonne+2):
                if i != 0 and i != (self._rader + 1) and j != 0 and j != (self._kolonner + 1):
                    if self._ruteNett[i][j] != self._ruteNett[rad][kolonne]:
                        naboer.append(self._ruteNett[i][j])
        return naboer
