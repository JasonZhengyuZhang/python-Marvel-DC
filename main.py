import random
import time 

from superhero import HeroList
from Cards.attackCard import AttackCardList 
from Cards.healCard import HealCardList
from Cards.specialCard import SpecialCardList

def countdown(t):
    while t:
        print(str(t) + ", ")
        time.sleep(1)
        t-=1

def heroAndComputerSelection(character):
    print("\n" + "A " + character +" will be selected for you ")
    countdown(3)
    Hero = random.choice(HeroList)
    print("Your " + character + " is " + Hero.name)

def initialCardDeal():
    playerDeckList=[]
    opponentDeckList=[]

    fullDeckList = [AttackCardList, HealCardList, SpecialCardList]

    while len(playerDeckList) != 4 or len(opponentDeckList) != 4:
        currentRoundPlayerCard = random.choice(random.choice.fullDeckList)
        print("here")


def startGamemode1(playerName):
    heroAndComputerSelection("hero")
    heroAndComputerSelection("opponent")

    

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