from enum import Enum


class PokeType(Enum):
    NORMAL = 1
    FIRE = 2
    WATER = 3
    GRASS = 4
    ELECTRIC = 5
    ICE = 6
    FIGHTING = 7
    POISON = 8
    GROUND = 9
    FLYING = 10
    PSYCHIC = 11
    BUG = 12
    ROCK = 13
    GHOST = 14
    DRAGON = 15
    DARK = 16
    STEEL = 17
    FAIRY = 18


class PokeStats:
    def __init__(self, hp, atk, deff, spatk, spdef, speed):
        self.hp = hp
        self.atk = atk
        self.deff = deff
        self.spatk = spatk
        self.spdef = spdef
        self.speed = speed
        self.total = hp + atk + deff + spatk + spdef + speed


class Pokemon:
    def __init__(self, id, name, type, stats: PokeStats) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.stats = stats

    def info(self):
        filler = "0" * (4 - len(str(self.id)))

        print(f"{self.name}\t#{filler}{self.id}\n")
        for t in self.type:
            print(f"{t}, ", end="")
        print()
        print(f"HP: {self.stats.hp}")
        print(f"ATK: {self.stats.atk}")
        print(f"DEF: {self.stats.deff}")
        print(f"SPATK: {self.stats.spatk}")
        print(f"SPDEF: {self.stats.spdef}")
        print(f"SPD: {self.stats.speed}")
        print(f"TOTAL: {self.stats.total}")


pokedex : Pokemon = {}


def initialize_pokedex():
    temp = []

    stats = PokeStats(78, 84, 78, 109, 85, 100)
    temp.append(Pokemon(6, "Charizard", [PokeType.FLYING, PokeType.FIRE], stats))

    for t in temp:
        pokedex[t.id] = t
