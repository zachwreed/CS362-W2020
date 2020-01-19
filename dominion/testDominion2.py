# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:42:42 2019

@author: reedz
"""

import Dominion
import random
from collections import defaultdict
import testUtility

# Get intialized values
player_names = testUtility.GetPlayerNames()
nC = testUtility.GetnC(player_names)
nV = testUtility.GetnV(player_names)
players = testUtility.InitPlayers(player_names)

box = testUtility.GetBoxes(nV)
supply = testUtility.GetSupply(box, player_names, nC, nV)
supply_order = testUtility.GetSupplyOrder()
turn = testUtility.InitTurn()
trash = testUtility.InitTrash()

supply["Estate"]=[Dominion.Duchy()]*nV


#Play the game
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)