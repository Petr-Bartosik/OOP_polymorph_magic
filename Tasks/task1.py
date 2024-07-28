#import pro pí.
from math import pi
#dle zadání
class Shape:
    def plocha(self):
        raise NotImplementedError("Fatal Error!") # :D
class Obdelnik(Shape):
    def __init__(self, sirka, vyska):
        self.sirka = sirka
        self.vyska = vyska
    def plocha(self):
        return self.sirka * self.vyska
class Kruh(Shape):
    def __init__(self, polomer):
        self.polomer = polomer

    def plocha(self):
        return round(pi * self.polomer ** 2, 2) #zaokrouhlil jsem na dve desetinna mista.
                                                #pri testu vyskakoval dlouhy zbytek
class pravouhlytr(Shape):
    def __init__(self, zakladna, vyska):
        self.zakladna = zakladna
        self.vyska = vyska

    def plocha(self):
        return 0.5 * self.zakladna * self.vyska
class Lichobeznik(Shape):
    def __init__(self, zakladna1, zakladna2, vyska):
        self.zakladna1 = zakladna1
        self.zakladna2 = zakladna2
        self.vyska = vyska
    def plocha(self):
        return 0.5 * (self.zakladna1 + self.zakladna2) * self.vyska

#TEST - funguje
if __name__ == "__main__":
    tvary = [
        Obdelnik(1, 2),
        Kruh (1),
        pravouhlytr(1, 2),
        Lichobeznik(1, 1, 1)]

    for tvar in tvary:
        print(f"Plocha tvaru {type(tvar).__name__} je: {tvar.plocha()}")
