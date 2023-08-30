class Pokemon:
    def __init__(self, pokedex, name, type, stats):
        self.pokedex = pokedex
        self.name = name
        self.type = type
        self.stats = stats


class Stats:
    def __init__(self, hp, atk, defense, spatk, spdef, spd):
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.spatk = spatk
        self.spdef = spdef
        self.spd = spd
        self.total = hp + atk + defense + spatk + spdef + spd


pokemon4 = Pokemon(4, "Charmander", ["Fire"], Stats(39, 52, 43, 60, 50, 65))
pokemon5 = Pokemon(5, "Charmeleon", ["Fire"], Stats(58, 64, 58, 80, 65, 80))
pokemon6 = Pokemon(6, "Charizard", ["Fire", "Flying"], Stats(78, 84, 78, 109, 85, 100))

# Dictionary erstellen       {<Schlüssel>: ""}
pokedex = {}

pokedex[4] = pokemon4
pokedex[5] = pokemon5
pokedex[6] = pokemon6

typechart = {}
typechart[
    "Fire"
] = "Fire: x2dmg against: Grass, Ice, Bug ; 1/2dmg against: Fire, Water, Rock, Dragon ; 0dmg against: nothing"
typechart[
    "Flying"
] = "Flying: x2dmg against: Grass, Fighting, Bug ; 1/2dmg against: Electric, Rock, Steel ; 0dmg against: nothing"

# print(typechart["Normal"])

id = int(input("Bitte gib eine Nummer ein: "))


obj = pokedex.get(id)
if obj == None:
    print("Keinen Eintrag gefunden.")
else:
    get_pokemon = pokedex[id]
    get_stats = pokedex[id].stats
    get_typechart = typechart["Fire"]
    get_typechart2 = typechart["Flying"]

    print(
        f"Pokedex data:\nNational No. {get_pokemon.pokedex}\nName: {get_pokemon.name}\nType: {get_pokemon.type}\nTypechart"
    )
    for type in pokedex[id].type:
        print(typechart[type])

    print(
        f"Stats:\nHP({get_stats.hp})\nATK({get_stats.atk})\nDef({get_stats.defense})\nSpATK({get_stats.spatk})\nSpDef({get_stats.spdef})\nSpeed({get_stats.spd})\nTotal({get_stats.total})"
    )
