'''
Board setup for Conway's, namely creating the data structure, its border, and conditions.
'''

#!/usr/bin/env python3

class Board:
    #Data structure for the board in Conway's

    def __init__(self, boardSize=40):

        emptyRow = [' ' for x in range(boardSize)] #empty space to show an empty tile
        self.tiles = [emptyRow for x in range(boardSize)]
        self.boardSize = boardSize

    def printCurrentBoard(self):
        #Top row of board
        print("+", end="")
        for x in range(self.boardSize): print("--", end="")
        print("-+") #extra dash added to account for spacing tiles out in tile rows

        #Each non-border row of board
        for row in self.tiles:
            print("| ", end="")
            for tile in row:
                print(tile + " ", end="")
            print("|")

        #Bottom row of board
        print("+", end="")
        for x in range(self.boardSize): print("--", end="")
        print("-+") #extra dash added to account for spacing tiles out in tile rows


