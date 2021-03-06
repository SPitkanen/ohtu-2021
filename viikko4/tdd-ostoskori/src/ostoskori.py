from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = []

    def tavaroita_korissa(self):
        maara = 0
        for tuote in self.kori:
            maara += tuote.lukumaara()

        return maara

    def hinta(self):
        hinta = 0
        for ostos in self.kori:
            hinta += ostos.hinta()

        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.kori:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return

        ostos = Ostos(lisattava)
        self.kori.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.kori:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self.kori.remove(ostos)
                return

    def tyhjenna(self):
        self.kori = []

    def ostokset(self):
        return self.kori
