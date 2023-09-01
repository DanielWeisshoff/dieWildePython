# Zufällige zahl von 1-100 wird ausgewählt, spieler hat x versuche die zahl zu
# erraten
from random import randrange


zufalls_zahl = randrange(100) + 1
max_versuche = randrange(10) + 5
versuche = max_versuche
liste = []


while True:
    print(f"Schon eingegeben {liste}")
    Userzahl = int(input("Bitte gib eine Zahl ein: "))

    liste.append(Userzahl)
    versuche -= 1

    if versuche == 0:
        print("Du hast verloren!")
        exit()
    elif Userzahl == zufalls_zahl:
        print("Du hast gewonnen!")
        print(
            f"Du hast {max_versuche-versuche} Versuche gebraucht, um die Zahl zu erraten!"
        )
        exit()
    elif Userzahl > zufalls_zahl:
        print(f"Die gesuchte Zahl ist kleiner! Du hast noch {versuche} übrig!")
    elif Userzahl < zufalls_zahl:
        print(f"Die gesuchte Zahl ist größer! Du hast noch {versuche} übrig!")
