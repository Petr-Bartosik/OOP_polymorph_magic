from math import pi
from task1 import Shape


# Trida pro plochY tvary dle zadani
class DRS(Shape):
    def __init__(self, name):
        self.name = name

    def plocha(self):
        raise NotImplementedError("Self-destruct activated")

    def Show(self):
        print(f"Tvar: {self.name}, Plocha: {self.plocha()}")

    def Save(self):
        filename = f"{self.name.lower()}.txt"
        with open(filename, 'w') as file:
            file.write(self.__str__() + "\n")

    @classmethod
    def Load(cls, nazev_souboru):
        with open(nazev_souboru, 'r') as file:
            data = file.readline().strip().split(',')
            name = data[0].split(': ')[1]
            vstupy = [float(value.split(': ')[1]) for value in data[1:-1]]

            if name == 'Ctverec':
                return Ctverec(*vstupy)
            elif name == 'Obdelnik':
                return Obdelnik(*vstupy)
            elif name == 'Kruznice':
                return Kruznice(*vstupy)
            elif name == 'Elipsa':
                return Elipsa(*vstupy)
            else:
                raise ValueError("This is a bad choice. You have one last chance.")
#CTVEREC
class Ctverec(DRS):
    def __init__(self, x, y, strana):
        super().__init__('Ctverec')
        self.x = x
        self.y = y
        self.strana = strana

    def plocha(self):
        return self.strana ** 2

    def __str__(self):
        return f"Tvar: {self.name}, x: {self.x}, y: {self.y}, strana: {self.strana}, Plocha: {self.plocha()}"
#OBDELNIK
class Obdelnik(DRS):
    def __init__(self, x, y, sirka, vyska):
        super().__init__('Obdelnik')
        self.x = x
        self.y = y
        self.sirka = sirka
        self.vyska = vyska

    def plocha(self):
        return self.sirka * self.vyska

    def __str__(self):
        return f"Tvar: {self.name}, x: {self.x}, y: {self.y}, sirka: {self.sirka}, vyska: {self.vyska}, Plocha: {self.plocha()}"


##KRUZNICE
class Kruznice(DRS):
    def __init__(self, x, y, polomer):
        super().__init__('Kruznice')
        self.x = x
        self.y = y
        self.polomer = polomer

    def plocha(self):
        return round(pi * self.polomer ** 2, 2)

    def __str__(self):
        return f"Tvar: {self.name}, x: {self.x}, y: {self.y}, polomer: {self.polomer}, Plocha: {self.plocha()}"


#ELIPSA
class Elipsa(DRS):
    def __init__(self, x, y, sirka, vyska):
        super().__init__('Elipsa')
        self.x = x
        self.y = y
        self.sirka = sirka
        self.vyska = vyska

    def plocha(self):
        return round(pi * (self.sirka / 2) * (self.vyska / 2), 2)

    def __str__(self):
        return f"Tvar: {self.name}, x: {self.x}, y: {self.y}, sirka: {self.sirka}, vyska: {self.vyska}, Plocha: {self.plocha()}"

if __name__ == "__main__":
#VYTVORENI SEZNAMU OBRAZCU
    obrazce = [
        Ctverec(0, 0, 0),
        Obdelnik(1, 1, 1, 1),
        Kruznice(2, 2, 3),
        Elipsa(3, 3, 6, 4)]

    #SAVE
    for obrazec in obrazce:
        obrazec.Save()

    #NACTENI Z .TXT
    soubory = [
        "ctverec.txt",
        "obdelnik.txt",
        "kruznice.txt",
        "elipsa.txt"
    ]
    nactene_obrazce = [DRS.Load(soubor) for soubor in soubory]

    for obrazec in nactene_obrazce:
        obrazec.Show()


