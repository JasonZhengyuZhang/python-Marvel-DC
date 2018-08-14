import random
import time 

from superhero import HeroList
from Cards.attackCard import AttackCardList 
from Cards.healCard import HealCardList
from Cards.specialCard import SpecialCardList
from classes import *

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
    
    time.sleep(1)

    print("Deck are being split... \n")

    while len(playerDeckList) != 4 or len(opponentDeckList) != 4:
        currentRoundPlayerCardType = random.choice(fullDeckList)
        currentRoundPlayerCard = random.choice(currentRoundPlayerCardType)
        playerDeckList.append(currentRoundPlayerCard)

        currentRoundOpponentCardType = random.choice(fullDeckList)
        currentRoundOpponentCard = random.choice(currentRoundOpponentCardType)
        opponentDeckList.append(currentRoundOpponentCard)

    initalCard = [playerDeckList, opponentDeckList]
    return initalCard

def DeckSort(deck):
    availableHeal = []
    availableAttack = []
    availableSpecial = []

    for card in deck:
        if card.getName()=="AttackCard":
            availableAttack.append(card)
        elif card.getName()=="HealCard":
            availableHeal.append(card)
        else:
            availableSpecial.append(card)

    sortedDeck = [availableAttack, availableHeal, availableSpecial]
    return sortedDeck

def deckStatus(attackDeck, healDeck, specialDeck):
    numberOfAttack = len(attackDeck)
    numberOfHeal = len(healDeck)
    numberOfSpecial = len(specialDeck)

    AttackDes = ""
    HealDes = ""
    SpecialDes = ""

    if numberOfAttack > 0:
        for card in attackDeck:
            AttackDes+="\t\t"+card.name + ": " + card.description + "\n"
    
    if numberOfHeal > 0:
        for card in healDeck:
            HealDes+="\t\t"+card.name + ": " + card.description + "\n"
    
    if numberOfSpecial > 0:
        for card in specialDeck:
            SpecialDes+="\t\t"+card.name + ": " + card.description + "\n"

    print ("\nYour Current Deck: \n" + "\t" + str(numberOfAttack) + " Attack Card(s) \n" + AttackDes + "\t" + str(numberOfHeal) + " Healing Card(s) \n" + HealDes + "\t" + str(numberOfSpecial) + " Special Cards(s) \n" + SpecialDes)

def startGamemode1(playerName):
    player = heroAndComputerSelection("hero")
    computer = heroAndComputerSelection("opponent")
    initialDeck = initialCardDeal()

    playerDeckSorted = DeckSort(initialDeck[0])
    computerDeckSorted = DeckSort(initialDeck[1])

    player.attackCard=playerDeckSorted[0]
    player.healCard=playerDeckSorted[1]
    player.specialCard=playerDeckSorted[2]

    computer.attackCard=computerDeckSorted[0]
    computer.healCard=computerDeckSorted[1]
    computer.specialCard=computerDeckSorted[2]

    deckStatus(player.attackCard, player.healCard, player.specialCard)

    turn = random,choice([1,2])

    if turn==0:
        print("A dice was tossed and you will go first")
    else:
        print("A dice was tossed and the computer will go first")

    turnNumber = 0

    while player.health > 0 or computer.health > 0:
        if turn == 0:
            print("h")
        else:
            print("e")
            
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