class Superhero:
    def __init__(self, name, franchise, health, attack, attackCard, healCard, specialCard):
        self.name=name
        self.franchise=franchise
        self.health=health
        self.attack=attack
        self.attackCard=attackCard
        self.healCard=healCard
        self.specialCard=specialCard

class HealCard: 
    def __init__(self, name, healthBonus, description):
        self.name=name
        self.healthBonus=healthBonus
        self.description=description

    def getName(self):
        return self.__class__.__name__

class AttackCard: 
    def __init__(self, name, attackBonus, description):
        self.name=name
        self.attackBonus=attackBonus
        self.description=description

    def getName(self):
        return self.__class__.__name__

class SpecialCard:
    def __init__(self, name, effect, bonus, probability, description):
        self.name=name
        self.effect=effect
        self.bonus=bonus
        self.probability=probability
        self.description=description

    def getName(self):
        return self.__class__.__name__