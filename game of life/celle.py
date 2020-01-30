class Celle:
#klassen definerer et celle objekt som har evne til aa vaere doed eller levende
#cellen faar status "doed" i utgangspunktet

    def __init__(self):
        self._status = "doed"

    def settDoed(self):
    #cellens status endres - den doer
        self._status = "doed"

    def settLevende(self):
    #cellens status endres - den blir levende
        self._status = "levende"

    def erLevende(self):
    #metode sjekker om cellen er levende eller doed
        if self._status == "levende":
            return True
        elif self._status == "doed":
            return False

    def hentStatusTegn(self):
    #gi et tegn avhengig av cellens status
        if self._status == "levende":
            return "O"
        elif self._status == "doed":
            return "."