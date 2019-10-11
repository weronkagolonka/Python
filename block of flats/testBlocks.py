from blockOfFlats import Leilighet, Bygaard


def hovedProgram():
    bygaard = Bygaard()

    cnt = 0
    antallEtasjer = 5
    bygaard.antEtasjer(antallEtasjer)
    for etasje in range(1, 6):
        for i in range(1, 11):
            leilighet = Leilighet(i, etasje)
            bygaard.leggTil(leilighet)
            cnt += 1 #ile mieszkan

    bygaard.henInfo()

hovedProgram()