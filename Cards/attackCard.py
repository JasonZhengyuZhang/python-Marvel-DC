# import os,sys,inspect
# sys.path.insert(1, os.path.join(sys.path[0], '..'))
# import classes

from classes import AttackCard

Attack1 = AttackCard("Batman's dart", 150, "Batman's darts are fast and deadly, dealing 150 in damage")
Attack2 = AttackCard("Flash Fast", 200, "Flash comes running in, dealing 200 in damage")
Attack3 = AttackCard("Zeus' Lighting", 200, "Zeus sends down a lighting strike, dealing 200 in damage")

AttackCardList = [Attack1, Attack2, Attack3]