import random
import time 

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
IronMan = Superhero("Iron Man", "Marvel", 4000, 3000)
CaptainAmerica = Superhero("Captain America", "Marvel", 3000, 3000)


HeroList = [Shazam, IronMan, CaptainAmerica]

def countdown(t):
    while t:
        print(str(t) + ", ")
        time.sleep(1)
        t-=1

def startGamemode1(playerName):
    print("\n" + "A hero will be selected for you ")
    countdown(10)

    playerHero = random.choice(HeroList)
    print("Your hero is " + playerHero.name)

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