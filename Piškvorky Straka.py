"""
projekt_2.py – Piškvorky (Tic Tac Toe)
autor: Jan Novak
email: jan_novak@email.cz
discord: jan_novak#1234
"""

# Úvodní text a pravidla
print("Vítej ve hře Piškvorky")
print("=" * 40)
print("PRAVIDLA HRY:")
print("Hráči se střídají v tazích.")
print("V každém tahu hráč umístí svůj znak (X nebo O).")
print("Vyhrává ten, kdo má tři stejné znaky")
print("v řadě (vodorovně, svisle nebo diagonálně).")
print("=" * 40)
print("Začínáme hru")
print("-" * 40)

# Herní pole - seznam o 9 prvcích (3x3)
pole = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Funkce pro vypsání herního pole
def vypis_pole():
    print("+---+---+---+")
    print("|", pole[0], "|", pole[1], "|", pole[2], "|")
    print("+---+---+---+")
    print("|", pole[3], "|", pole[4], "|", pole[5], "|")
    print("+---+---+---+")
    print("|", pole[6], "|", pole[7], "|", pole[8], "|")
    print("+---+---+---+")

# První vypsání prázdného pole
vypis_pole()

# Začíná hráč O
hrac = "O"

# Hlavní smyčka hry
while True:
    print("=" * 40)
    tah = input("Hráč " + hrac + " | Zadej číslo pole (1-9): ")
    print("=" * 40)
    
    # Kontrola, zda byl zadán číselný vstup
    if not tah.isdigit():
        print("Chyba: musíš zadat číslo!")
        continue
    
    tah = int(tah)
    
    # Kontrola rozsahu 1-9
    if tah < 1 or tah > 9:
        print("Chyba: zadej číslo od 1 do 9!")
        continue
    
    # Kontrola, zda pole není obsazené
    if pole[tah - 1] != " ":
        print("Chyba: toto pole je už obsazené!")
        continue
    
    # Provádíme tah hráče
    pole[tah - 1] = hrac
    vypis_pole()
    
    # Kontrola výhry - řádky
    if pole[0] == hrac and pole[1] == hrac and pole[2] == hrac:
        print("Vyhrál hráč", hrac)
        break
    if pole[3] == hrac and pole[4] == hrac and pole[5] == hrac:
        print("Vyhrál hráč", hrac)
        break
    if pole[6] == hrac and pole[7] == hrac and pole[8] == hrac:
        print("Vyhrál hráč", hrac)
        break
    
    # Kontrola výhry - sloupce
    if pole[0] == hrac and pole[3] == hrac and pole[6] == hrac:
        print("Vyhrál hráč", hrac)
        break
    if pole[1] == hrac and pole[4] == hrac and pole[7] == hrac:
        print("Vyhrál hráč", hrac)
        break
    if pole[2] == hrac and pole[5] == hrac and pole[8] == hrac:
        print("Vyhrál hráč", hrac)
        break
    
    # Kontrola výhry - diagonály
    if pole[0] == hrac and pole[4] == hrac and pole[8] == hrac:
        print("Vyhrál hráč", hrac)
        break
    if pole[2] == hrac and pole[4] == hrac and pole[6] == hrac:
        print("Vyhrál hráč", hrac)
        break
    
    # Kontrola remízy - pokud není žádné volné pole
    if " " not in pole:
        print("Remíza!")
        break
    
    # Změna hráče
    if hrac == "O":
        hrac = "X"
    else:
        hrac = "O"