import random
import time 

from superhero import HeroList

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

    # while len(deckList) != 4:


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