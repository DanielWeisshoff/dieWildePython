class Soldat:
    def __init__(self, life, damage):
        self.life = life
        self.damage = damage

    def attack(self, enemy):
        enemy.life -= self.damage
        if enemy.life <= 0:
            enemy.life = 0
            print("Herbert ist gestorben!")
