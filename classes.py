class Superhero:
    def __init__(self, name, franchise, health, attack):
        self.name=name
        self.franchise=franchise
        self.health=health
        self.attack=attack

class HealCard: 
    def __init__(self, name, healthBonus, description):
        self.name=name
        self.healthBonus=healthBonus
        self.description=description

class AttackCard: 
    def __init__(self, name, attackBonus, description):
        self.name=name
        self.attackBonus=attackBonus
        self.description=description

class SpecialCard:
    def __init__(self, name, effect, bonus, probability, description):
        self.name=name
        self.effect=effect
        self.bonus=bonus
        self.probability=probability
        self.description=description