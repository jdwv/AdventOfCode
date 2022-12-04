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

ActionMap = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

Games = [x.split() for x in input]

TotalPoints = 0
for x in Games:
    player1 = x[0]
    action = ActionMap[x[1]]  
    print("##########\nGame: ", x)
    if action == "draw":
        player2 = player1
        print("draw")
        BonusPoints = 3
    elif player1 == 'A':    
        if action == "lose":
            player2 = 'C'
            print("lose")
            BonusPoints = 0
        elif action == "win":
            player2 = 'B'
            print("win")
            BonusPoints = 6
    elif player1 == 'B':    
        if action == "lose":
            player2 = 'A'
            print("lose")
            BonusPoints = 0
        elif action == "win":
            player2 = 'C'
            print("win")
            BonusPoints = 6
    elif player1 == 'C':    
        if action == "lose":
            player2 = 'B'
            print("lose")
            BonusPoints = 0
        elif action == "win":
            player2 = 'A'
            print("win")
            BonusPoints = 6

    GamePoints = points[player2] + BonusPoints
    TotalPoints += GamePoints
    print("Player1: {0} ({3}) | Action: {1} ({5}) | Player 2: {2} ({4}) | Game Points: {6}".format(player1, action, player2, points[player1], points[player2], BonusPoints, GamePoints))

print("Total Points: ", TotalPoints)
