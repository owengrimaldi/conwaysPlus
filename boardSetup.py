'''
Board setup for Conway's, namely creating the data structure, its border, and conditions.
'''

#!/usr/bin/env python3

class Board:
    #Data structure for the board in Conway's

    def __init__(self, boardSize=40):

        emptyRow = [' ' for x in range(boardSize)]
        self.tiles = [emptyRow for x in range(boardSize)]
        self.boardSize = boardSize

    def printCurrentBoard(self):
        #Top Row of Board
        print("+")
        for x in range(self.boardSize): print("-")
        print("+\n")

        #Each non-border row of board
        for row in self.tiles:
            print("|")
            for tile in row:
                print(tile)
            print("| ")




