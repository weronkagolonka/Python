class Leilighet:
    def __init__(self, num, etasje):
        self._num = num
        self._etasje = etasje

    def hentNum(self):
        return self._num
    
    def hentEtasje(self):
        return self._etasje

    def hentInfo(self):
        print("Leilighets nummer: " + str(self._num))
        print("Etasje: " + str(self._etasje))
        print(" ")


class Bygaard:
    def __init__(self):
        self._leiligheter = []

    def antEtasjer(self, ant):
        for etasje in range(ant):
            self._leiligheter.append([]) #legg til en liste

    def leggTil(self, leilighet):
        self._leiligheter[(leilighet.hentEtasje() - 1)].append(leilighet)

    def sjekkNr(self, leilNr):
        for el in self._leiligheter:
            if el.hentNum() == leilNr:
                return True
        return None 

    def henInfo(self):
        print("------INFO OM LEILIGHETER------")
        for i in range(len(self._leiligheter)):
            print("\nDu er naa i " + str(i + 1) + " etasje.\n")
            for cur in self._leiligheter[i]:
                cur.hentInfo()

