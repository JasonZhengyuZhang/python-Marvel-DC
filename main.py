import random
import time 

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

Shazam = Superhero("Shazam", "DC", 5000, 2000)
IronMan = Superhero("Iron Man", "Marvel", 4000, 3000)
CaptainAmerica = Superhero("Captain America", "Marvel", 3000, 3000)

Heal1 = HealCard("Cap's Shield", 200, "2% reduced on enemy next attack")
Heal2 = HealCard("Mantis's Spell", 300, "Mantis put the enemy to sleep for a brief time, giving you time to recover")
Heal3 = HealCard("Dr.Strange's shield", 500, "")

Attack1 = AttackCard("Batman's dart", 150, "")
Attack2 = AttackCard("Flash Fast", 200, "")
Attack3 = AttackCard("Zeus' Lighting", 200, "")

Special1 = SpecialCard("Thor's Hammer", "Attack", 0, 30, "extra 30% on your attack")
Special2 = SpecialCard("Warmachine above", "Attack", 300, 0, "Warmachine drops bomb over your enemies's head")
Special3 = SpecialCard("Scarlet's Spell", 0, 20, "Scarlet get in to the head of your opponent, leaving them confused and reduced 20% damage on next attack")

HeroList = [Shazam, IronMan, CaptainAmerica]

def countdown(t):
    while t:
        print(str(t) + ", ")
        time.sleep(1)
        t-=1

def heroAndComputerSelection():
    print("\n" + "A hero will be selected for you ")
    countdown(3)

    playerHero = random.choice(HeroList)
    print("Your hero is " + playerHero.name)

    print("\n" + "A opponent will be selected for you ")
    countdown(3)

    computerHero = random.choice(HeroList)
    print("Your opponent is " + computerHero.name)

def initialCardDeal():
    deckList = []

    while len(deckList) != 4:


def startGamemode1(playerName):
    heroAndComputerSelection()

    

def startGame():
    print("\n\n"+"Welcome to the battle!")
    playerName=raw_input("Hero, please enter your name: ")

    gamemode = 0

    while gamemode != 1:
        gamemode=input("\n" + "Which gamemode would you like to play: ")
        print(gamemode)

    if gamemode == 1:
        startGamemode1(playerName)


startGame()