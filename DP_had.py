"""ovládání pomocí kláves wsad bez entru"""

import msvcrt
from random import randrange

def nakresli_mapu(souradnice, ovoce, delka_pole, vyska_pole):
    print(20*"-")
    for radek in range(0, vyska_pole):
        for sloupec in range(0, delka_pole):
            if (sloupec, radek) in souradnice:
                print("X", end=" ")
            elif (sloupec, radek) in ovoce:
                print("?", end=" ")
            else:
                print(".", end=" ")
        print()
    if delka_pole < 4 or vyska_pole < 1:
        raise ValueError("Nastav hrací pole.")

def pohyb(souradnice, delka_pole, vyska_pole):
    posledni_bod = souradnice[-1]
    x, y = posledni_bod
    key = msvcrt.getch().decode("utf-8").lower()
    if key == "s":
        novy_bod = x, y + 1
    elif key == "w":
        novy_bod = x, y - 1
    elif key == "d":
        novy_bod = x + 1, y
    elif key == "a":
        novy_bod = x - 1, y
    else:
        raise ValueError(strana)
    x, y = novy_bod
    if x < 0 or y < 0 or x >= delka_pole or y >= vyska_pole:
        raise ValueError("Game Over")
    if novy_bod in souradnice:
        raise ValueError("Game Over")
    souradnice.append(novy_bod)
    if novy_bod in ovoce:
        ovoce.remove(novy_bod)
        pridej_ovoce(souradnice, ovoce, delka_pole, vyska_pole)
    else:
        del souradnice[0]
    if pocet % 30 == 0:
        pridej_ovoce(souradnice, ovoce, delka_pole, vyska_pole)

def pridej_ovoce(souradnice, ovoce, delka_pole, vyska_pole):
    velikost_pole = delka_pole * vyska_pole
    velikost_ovoce = len(ovoce)
    velikost_souradnice = len(souradnice)
    if velikost_pole > (velikost_ovoce + velikost_souradnice):
        nove_ovoce = souradnice[0]
        while ((nove_ovoce in souradnice) or (nove_ovoce in ovoce)):
            x = randrange(0, delka_pole)
            y = randrange(0, vyska_pole)
            nove_ovoce = x, y
        ovoce.append(nove_ovoce)


print()
print("Hra se ovládá pomocí kláves wsad")
souradnice = [(0, 0), (1, 0), (2, 0)]
ovoce = [(2, 3)]
pocet = 0
delka_pole = 8
vyska_pole = 8
while True:
    pocet = pocet + 1
    nakresli_mapu(souradnice, ovoce, delka_pole, vyska_pole)
    #strana = input("Zadej stranu (w, s, a, d): ")
    pohyb(souradnice, delka_pole, vyska_pole)
    if (delka_pole * vyska_pole) == (len(souradnice)):
        nakresli_mapu(souradnice, ovoce, delka_pole, vyska_pole)
        print("Vyhrál jsi.")
        break
