from random import randrange

def nakresli_mapu(souradnice, ovoce, delka_pole, vyska_pole):
    """Vykreslí hrací pole, kde na zadaných souřadnicích bude had a na další
       ovoce pro hada. Zbytek pole budou tečky.
    """
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

def pohyb(souradnice, strana, delka_pole, vyska_pole):
    """S hadem se hýbe pomocí kláves swda. Pokud had vyjede z pole nebo narazí
       do sebe, hra se ukončí. Když had sní ovoce, objeví se na náhodném místě
       nové. Taky se objeví nové ovoce po každých třiceti tazích.
    """
    posledni_bod = souradnice[-1]
    x, y = posledni_bod
    if strana == "s":
        novy_bod = x, y + 1
    elif strana == "w":
        novy_bod = x, y - 1
    elif strana == "d":
        novy_bod = x + 1, y
    elif strana == "a":
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
    """Dokud jsou v poli volná místa (tečky), tak na náhodném místě vyroste
       nové ovoce a přidá se do seznamu ovoce.
    """
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

souradnice = [(0, 0), (1, 0), (2, 0)]
ovoce = [(2, 3)]
pocet = 0
delka_pole = 10
vyska_pole = 10
while True:
    pocet = pocet + 1
    nakresli_mapu(souradnice, ovoce, delka_pole, vyska_pole)
    strana = input("Zadej stranu (w, s, a, d): ")
    pohyb(souradnice, strana, delka_pole, vyska_pole)
    print (souradnice)
    if (delka_pole * vyska_pole) == (len(souradnice)):
        nakresli_mapu(souradnice, ovoce, delka_pole, vyska_pole)
        print("Vyhrál jsi.")
        break
