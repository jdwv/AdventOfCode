#!/usr/bin/env python3

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input.txt')

with open(filename, "r") as file:
    input = [line.strip() for line in file]

points = {
    'A': 1,
    'B': 2,
    'C': 3
}

# [print(x) for x in input if x.startswith('A')]
# [print(x) for x in input if x.startswith('B')]
# [print(x) for x in input if x.startswith('C')]

# RockResponse     = [x.split() for x in input if x.startswith('A')]
# PaperResponse    = [x.split() for x in input if x.startswith('B')]
# ScissorsResponse = [x.split() for x in input if x.startswith('C')]

Games = [x.split() for x in input]

# Scores were X=Rock, Y=Paper, Z=Scissors
ConvertMap = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

TotalPoints = 0

for x in Games:
    player1 = x[0]
    player2 = ConvertMap[x[1]]
    
    print("##########\nGame: ", x)
    print("Player1: {0} | Player2: {1}".format(player1, player2))
    
    if player1 == player2: # A A
        print("draw")
        BonusPoints = 3
    elif player1 == 'A' and player2 == 'C':
        print("loss")
        BonusPoints = 0
    elif player2 == 'A' and player1 == 'C':
        print("win")
        BonusPoints = 6
    elif (points[player1] > points[player2]): 
        print("loss")
        BonusPoints = 0
    elif (points[player2] > points[player1]):
        print("win")
        BonusPoints = 6
    else:
        print(">>>>>{0} vs {1}<<<<<".format(player1, player2))

    GamePoints = points[(ConvertMap[x[1]])] + BonusPoints
    TotalPoints += GamePoints
    print("Points: {0} + {1} = {2}".format(points[(ConvertMap[x[1]])], BonusPoints, GamePoints))
    print("Total Points: ", TotalPoints)

