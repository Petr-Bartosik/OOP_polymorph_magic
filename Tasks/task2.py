from Tasks.task1 import Obdelnik, Kruh, pravouhlytr, Lichobeznik

#import z task1 pro int a str
class Obdelnik(Obdelnik):
    def __int__(self):
        return int(self.plocha())

    def __str__(self):
        return f"Tvar: Obdélník, Šířka: {self.sirka}, Výška: {self.vyska}, Plocha: {self.plocha()}"
class Kruh(Kruh):
    def __int__(self):
        return int(self.plocha())

    def __str__(self):
        return f"Tvar: Kruh, Poloměr: {self.polomer}, Plocha: {self.plocha()}"
class pravouhlytr(pravouhlytr):
    def __int__(self):
        return int(self.plocha())
    def __str__(self):
        return f"Tvar: Pravoúhlý trojúhelník, Základna: {self.zakladna}, Výška: {self.vyska}, Plocha: {self.plocha()}"
class Lichobeznik(Lichobeznik):
    def __int__(self):
        return int(self.plocha())

    def __str__(self):
        return f"Tvar: Lichoběžník, Základna 1: {self.zakladna1}, Základna 2: {self.zakladna2}, Výška: {self.vyska}, Plocha: {self.plocha()}"


#uzivatelske rozhrani pro vstupy. je to spis opakovani.
def uzivatelske_rozhrani():
    while True:
        print("Vyber tvar (1-Obdélník, 2-Kruh, 3-Pravoúhlý trojúhelník, 4-Lichoběžník, 5-Konec): ")
        volba = input()

        if volba == '1':
            sirka = float(input("Zadej šířku obdélníku: "))
            vyska = float(input("Zadej výšku obdélníku: "))
            tvar = Obdelnik(sirka, vyska)
            print(str(tvar))
            print(f"Plocha jako celé číslo: {int(tvar)}")
        elif volba == '2':
            polomer = float(input("Zadej poloměr kruhu: "))
            tvar = Kruh(polomer)
            print(str(tvar))
            print(f"Plocha jako celé číslo: {int(tvar)}")
        elif volba == '3':
            zakladna = float(input("Zadej základnu trojúhelníku: "))
            vyska = float(input("Zadej výšku trojúhelníku: "))
            tvar = pravouhlytr(zakladna, vyska)
            print(str(tvar))
            print(f"Plocha jako celé číslo: {int(tvar)}")
        elif volba == '4':
            zakladna1 = float(input("Zadej první základnu lichoběžníku: "))
            zakladna2 = float(input("Zadej druhou základnu lichoběžníku: "))
            vyska = float(input("Zadej výšku lichoběžníku: "))
            tvar = Lichobeznik(zakladna1, zakladna2, vyska)
            print(str(tvar))
            print(f"Plocha jako celé číslo: {int(tvar)}")
        elif volba == '5':
            break
        else:
            print("Špatný vstup.")


#testovani - vyhovuje, funguje. testovano zvlast po objektech
if __name__ == "__main__":
    uzivatelske_rozhrani()
