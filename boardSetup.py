'''
Board setup for Conway's, namely creating the data structure, its border, and conditions.
'''
'''
Conway's Rules per Turn:
    1.) Any live cell with two or three live neighbours survives.
    2.) Any dead cell with three live neighbours becomes a live cell.
    3.) All other live cells die in the next generation. Similarly, all other dead cells stay dead.

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

    def addTile(self, posRow, posCol):
        #what if tile is already alive? ping user in higher level func
        #sets tile to alive on board position given, row and col
        self.tiles[posRow][posCol] = 'x'


    def executeTurn(self):
    #A call performs the algorithm that occurs each turn of Conway's
    #Evaluates current board for neighbors, creates new board, replaces old

    newBoard = self.tiles

        for currRow in range(self.boardSize):
            for currCol in range(self.boardSize):
                

                
                


