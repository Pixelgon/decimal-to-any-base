# Vytvoril Matej Matejka
# Prevod desitkove soustavy na jakoukoliv

print("|Převod desítkové soustavy|")
# Zadame cislo v desitkove soustave ktere chceme prevest do cilov soustavy(zaklad)
cislo = int(input("Zadejte číslo v desítkové soustavě: "))
# Zadame cilouvou soustavu do ktere chceme prevest (cislo)
zaklad = int(input("Zadejte soustavu: "))
vysledek = ""
# Dokud cislo je vetsi nez nula
while cislo > 0:
    # Zbytek je roven zbytku po deleni cisla zakladem
    zbytek = int(cislo % zaklad)
    # Pokud je zbytek mensi nez 10
    if zbytek < 10:
        # Zbytek priradime do vysledku
        vysledek += str(zbytek)
    else:
        # Zbytek nahradime cislem a priradime do vysledku
        vysledek += chr(ord('A')+zbytek-10)
    # Cislo vydelime zakladem
    cislo //= zaklad
vysledek = vysledek[::-1]
# Vysledek vypiseme
print(vysledek)
exit()