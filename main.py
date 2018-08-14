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
    time.sleep(1)
    return Hero

def initialCardDeal():
    playerDeckList=[]
    opponentDeckList=[]

    fullDeckList = []
    fullDeckList.append(AttackCardList)
    fullDeckList.append(HealCardList)
    fullDeckList.append(SpecialCardList)
    

    while len(playerDeckList) != 4 or len(opponentDeckList) != 4:
        currentRoundPlayerCardType = random.choice(fullDeckList)
        currentRoundPlayerCard = random.choice(currentRoundPlayerCardType)
        playerDeckList.append(currentRoundPlayerCard)

        currentRoundOpponentCardType = random.choice(fullDeckList)
        currentRoundOpponentCard = random.choice(currentRoundOpponentCardType)
        opponentDeckList.append(currentRoundOpponentCard)

    initalCard = [playerDeckList, opponentDeckList]
    return initalCard

def countDeck(deck, type):
    print("ds")


def startGamemode1(playerName):
    player = heroAndComputerSelection("hero")
    computer = heroAndComputerSelection("opponent")
    initialDeck = initialCardDeal()

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