# Methodendefinition: <def> Methodenname ( Argumente ):
# Methodenaufruf:Methodennamen ( Parameter )


from soldat import Soldat


soldat1 = Soldat(4, 3)
soldat2 = Soldat(2, 4)

print(soldat2.life)
soldat1.attack(soldat2)
print(soldat2.life)
