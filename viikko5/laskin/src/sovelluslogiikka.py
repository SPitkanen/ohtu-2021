class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.previous_value = 0

    def miinus(self, arvo):
        self.previous_value = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.previous_value = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def get_previous_value(self):
        self.tulos = self.previous_value
