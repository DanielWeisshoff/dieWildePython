weakness_chart = {}
strength_chart = {}

from pokemon import PokeType


def init_typechart():
    weakness_chart[PokeType.NORMAL] = [PokeType.ROCK, PokeType.STEEL]
    weakness_chart[PokeType.FIRE] = [PokeType.FIRE, PokeType.WATER,PokeType.ROCK,PokeType.DRAGON]
    #TODO...
    weakness_chart[PokeType.WATER] = [PokeType.ROCK, PokeType.STEEL]
    weakness_chart[PokeType.GRASS] = [PokeType.ROCK, PokeType.STEEL]
    weakness_chart[PokeType.ELECTRIC] = [PokeType.ROCK, PokeType.STEEL]
    weakness_chart[PokeType.ICE] = [PokeType.ROCK, PokeType.STEEL]
    weakness_chart[PokeType.FIGHTING] = [PokeType.ROCK, PokeType.STEEL]
    weakness_chart[PokeType.POISON] = [PokeType.ROCK, PokeType.STEEL]
    weakness_chart[PokeType.GROUND] = [PokeType.ROCK, PokeType.STEEL]
    weakness_chart[PokeType.FLYING] = [PokeType.ROCK, PokeType.STEEL]
    weakness_chart[PokeType.PSYCHIC] = [PokeType.ROCK, PokeType.STEEL]
    weakness_chart[PokeType.BUG] = [PokeType.ROCK, PokeType.STEEL]
    weakness_chart[PokeType.ROCK] = [PokeType.ROCK, PokeType.STEEL]
    weakness_chart[PokeType.GHOST] = [PokeType.ROCK, PokeType.STEEL]
    weakness_chart[PokeType.DRAGON] = [PokeType.ROCK, PokeType.STEEL]
    weakness_chart[PokeType.DARK] = [PokeType.ROCK, PokeType.STEEL]
    weakness_chart[PokeType.STEEL] = [PokeType.ROCK, PokeType.STEEL]
    weakness_chart[PokeType.FAIRY] = [PokeType.ROCK, PokeType.STEEL]

def get_weakness(type : PokeType):
    return weakness_chart[type]