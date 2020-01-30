from spillebrett import Spillebrett

def hovedProgram():
#brukeren oppgir maaler paa spillebrettet og bestemmer om hun vil opprette neste generasjon eller avslutte spillet

    rader = int(input("Oppgi antall rader: "))
    kolonner = int(input("Oppgi antall kolonner: "))

    #oppretter spillebrett-objekt som generer rutenettet automatisk. Deretter skriver ut brettet til terminalen
    spilleBrett1 = Spillebrett(rader, kolonner)
    spilleBrett1.tegnBrett()

    #info om foerste generasjon
    print("Generasjon 0. Antall levende celler: " + str(len(spilleBrett1.finnAntallLevende())))
    fortsette = input("Trykk ENTER for aa fortsette. Skriv inn 'q' og trykk ENTER for aa avslutte: ")

    #denne listen brukes for aa sammenligne naboer fra den forrige og naavaarende generasjonen dersom antall levende celler er samme
    #hvis de to listene er samme, betyr det at ingenting har endret seg paa brettet - livet har vunnet
    sammenlignLevende = []

    while fortsette == "" and len(spilleBrett1.finnAntallLevende()) != 0 and len(sammenlignLevende) == 0:
    #loekke fortsetter saa lenge brukeren taster 'enter', antall levende celler er ikke 0 og listen med identiske levende celler er tom
        
        lenvendeCeller0 = spilleBrett1.finnAntallLevende()                      #levende celler foer oppdateringen
        generasjon = spilleBrett1.oppdatering()                                 #spillebrettet oppdateres            
        antallLevende = len(spilleBrett1.finnAntallLevende())                   #antall levende celler etter oppdateringen      
        spilleBrett1.tegnBrett()                                                #spillebrettet tegnes
        lenvendeCeller1 = spilleBrett1.finnAntallLevende()                      #levende celler etter oppdateringen
        if antallLevende != 0 and lenvendeCeller0 == lenvendeCeller1:
        #hvis levende celler er samme som i den forrige generasjonen:
            sammenlignLevende.append(lenvendeCeller0)                           #legger levende celler til lista
            sammenlignLevende.append(lenvendeCeller1)
        elif antallLevende != 0 and lenvendeCeller0 != lenvendeCeller1:
        #Det er noen levende celler som skiller seg fra de fra forrige generasjonen, spillet fortsetter
            print("Generasjon: " + str(generasjon) + ". Antall levende celler: " + str(antallLevende) + ".")
            fortsette = input("Trykk ENTER for aa fortsette. Skriv inn 'q' og trykk ENTER for aa avslutte: ")      
    
    #to mulige avslutninger naar spillet er over:

    if len(sammenlignLevende) != 0:
    #naar noen celler overlevde og ingenting har endret seg paa brettet:
        print("VI OVERLEVDE! LIVET HAR VUNNET!")
    else:
    #naar alle cellene har doed:
        print("GAME OVER!")
        print()
        print("Takk for spillet!")

    #skriver ut statistikk:
    print("Totalt antall generasjoner: " + str(generasjon) + ".")
        
hovedProgram()

