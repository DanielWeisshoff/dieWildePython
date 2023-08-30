name = input("Bitte Namen eingeben: ")


alter = ""

# Schleife
while alter == "":
    try:
        alter = int(input("Bitte alter eingeben: "))
    except:
        alter = ""
        print("Eingabe war keine Zahl")


print(f"Hallo ich bin {name} und bin {alter} Jahre alt!")

# Kontrollstrukturen
# Bist du alt genug für den Club?
if alter < 18:
    print("Du kommst nicht rein")
if alter >= 18:
    print("Du kommst rein ;-)")
