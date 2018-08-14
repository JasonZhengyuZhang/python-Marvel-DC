# python-Marvel-DC

this is a quick command line terminal game 

Gamemode 1: 
* The player is randomly assigned a Marvel or DC superhero for his or her own control. 
* The computer will get a superhero as well, picked randomly. 
* The player and computer will be dealt a deck of cards (of 4 each), and at the beginning of each round, a new card will be dealt to the player. There are three type of cards, attack, heal, special. 
* Each superhero will have attack and health stats. They can only attack when they have a attack card, and only heal when they have a heal card. 
* The player can only play one attack or one heal per round, specials can be played in addition to the heal and attack, 
* Once a player has dealt enough damage to the opposing superhero, he wins


After the deck has been dealt, either the computer or the player will start, and they will alternate in rounds. At the beginning of each new round, both the player and computer will be dealt a new card.

In each round, a player have 6 choices (granted they have the cards)
*attack
*heal
*special
*attack and special
*heal and special
*do nothing 


while the player or the computer's health is above 0, the game will continue.
Inside of the while loop, there is a "if or else" for whethetr the current turn is the player's turn or the computer's turn. the turn number gets incremented, it is declared outside of the while loop. inside 