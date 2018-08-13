class Superhero:
    def __init__(self, name, franchise, health, attack):
        self.name=name
        self.franchise=franchise
        self.health=health
        self.attack=attack


class HealCard: 
    def __init__(self, name, healthBonus):
        self.name=name
        self.healthBonus=healthBonus

class AttackCard: 
    def __init__(self, name, attackBonus):
        self.name=name
        self.attackBonus=attackBonus

class SpecialCard:
    def __init__(self, name, effect, probability):
        self.name=name
        self.effect=effect
        self.probability=probability

Shazam = Superhero("Shazam", "DC", 5000, 2000)

def startGame():
    print("\n\n"+"Welcome to the battle!")

startGame()