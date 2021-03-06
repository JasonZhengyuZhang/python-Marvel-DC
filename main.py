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

def heroAndComputerSelection():
    Hero = random.choice(HeroList)
    Computer = random.choice(HeroList)

    while Hero == Computer:
        Hero = random.choice(HeroList)
        Computer = random.choice(HeroList)
    
    heroAndComputer=[Hero, Computer]
    return heroAndComputer

def initialCardDeal():
    playerDeckList=[]
    opponentDeckList=[]

    fullDeckList = []
    fullDeckList.append(AttackCardList)
    fullDeckList.append(HealCardList)
    fullDeckList.append(SpecialCardList)
    
    time.sleep(1)

    print("\nDeck are being split...")
    time.sleep(1)
    
    while len(playerDeckList) != 4 or len(opponentDeckList) != 4:
        currentRoundPlayerCardType = random.choice(fullDeckList)
        currentRoundPlayerCard = random.choice(currentRoundPlayerCardType)
        playerDeckList.append(currentRoundPlayerCard)

        currentRoundOpponentCardType = random.choice(fullDeckList)
        currentRoundOpponentCard = random.choice(currentRoundOpponentCardType)
        opponentDeckList.append(currentRoundOpponentCard)

    initalCard = [playerDeckList, opponentDeckList]
    return initalCard

def drawCard():
    fullDeckList = []
    fullDeckList.append(AttackCardList)
    fullDeckList.append(HealCardList)
    fullDeckList.append(SpecialCardList)

    currentRoundCardType = random.choice(fullDeckList)
    currentRoundCard = random.choice(currentRoundCardType)

    return [currentRoundCard.getName(), currentRoundCard]

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

def choices(attacker, defender):
    choices = {"1": choiceOne, "2": choiceTwo}
    print("What would you like to do?\n\t1.Attack 2.Heal 3.Special 4.Attack and Special 5.Heal and Special 6.Do Nothing")
    userChoice = input("->")
    choices[str(userChoice)](attacker, defender)

def choiceOne(attacker, defender):
    if len(attacker.attackCard)==0:
        print("you cannot attack")
        choices(attacker, defender)
    else:
        print("\nWhich attack card would you like to use?")
        for card in attacker.attackCard:
            print("\n-"+card.name+"\n")
        choosenCard=input(">")-1
        totalDamage=attacker.attackCard[choosenCard].attackBonus + attacker.attack
        del attacker.attackCard[choosenCard]
        defender.health-=totalDamage
        print(attacker.name + "have dealt " + str(totalDamage) + " damage to " + defender.name)
        print("\n" + attacker.name + " current health: " + str(attacker.health))
        print("\n" + defender.name + " current health: " + str(defender.health))

def choiceTwo(attacker, defender):
    if len(attacker.attackCard)==0:
        print("you cannot heal")
        choices(attacker, defender)
    else:
        print("\nWhich heal card would you like to use?")
        for card in attacker.healCard:
            print("\n-"+card.name+"\n")
        choosenCard=input(">")-1
        totalHeal=attacker.healCard[choosenCard].healthBonus 
        del attacker.healCard[choosenCard]
        attacker.health+=totalHeal
        print(attacker.name + " have healed for " + str(totalHeal))
        print("\n" + attacker.name + " current health: " + str(attacker.health))
        print("\n" + defender.name + " current health: " + str(defender.health))

def choiceThree(attacker, defender):
    if len(attacker.attackCard)==0:
        print("you cannot perform a special")
        choices(attacker, defender)
    else:
        print("\nWhich heal card would you like to use?")
        for card in attacker.healCard:
            print("\n-"+card.name+"\n")
        choosenCard=input(">")-1
        totalHeal=attacker.healCard[choosenCard].healthBonus 
        del attacker.healCard[choosenCard]
        attacker.health+=totalHeal
        print(attacker.name + " have healed for " + str(totalHeal))
        print("\n" + attacker.name + " current health: " + str(attacker.health))
        print("\n" + defender.name + " current health: " + str(defender.health))

def startGamemode1(playerName):

    heroAndComputer = heroAndComputerSelection()

    player = heroAndComputer[0]
    computer = heroAndComputer[1]

    print("\nA hero will be selected for you")
    countdown(3)
    print("Your hero is " + player.name)
    time.sleep(1)

    print("\nA opponent will be selected for you")
    countdown(3)
    print("Your opponent is " + computer.name)
    time.sleep(1) 


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

    turn = random.choice([1,2])
    turnDict = {"player": False, "computer": False}

    time.sleep(1)
    if turn==0:
        turnDict["player"]=True
        print("A dice was tossed and you will go first")
    else:
        turnDict["computer"]=True
        print("A dice was tossed and the computer will go first")
    time.sleep(1)

    while player.health > 0 and computer.health > 0:
        if turnDict["player"]==True:
            print("\nIt is your turn")
            time.sleep(2)
            newCard = drawCard()

            if newCard[0] == "AttackCard":
                player.attackCard.append(newCard[1])
            elif newCard[0] == "HealCard":
                player.healCard.append(newCard[1])
            else:
                player.specialCard.append(newCard[1])

            print("You have drawn your card and below is your current deck")
            time.sleep(2)
            deckStatus(player.attackCard, player.healCard, player.specialCard)
            time.sleep(1)
            
            choices(player, computer)

        else:
            print("\ncomputer's turn")

        turnDict["player"] = not turnDict["player"]
        turnDict["computer"] = not turnDict["computer"]

            
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