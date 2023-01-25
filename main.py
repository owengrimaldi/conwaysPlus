#!/usr/bin/env python3

'''
Remaking Conway's Game of Life
To-Do:
1.) Board borders DONE
2.) Surrounding tile algorithm
3.) Turn movement
4.) Menu
5.)

https://pypi.org/project/getch/
Test usage for input handling

'''
import sys
from boardSetup import Board
import msvcrt

testBoard = Board(30)

testBoard.printCurrentBoard()

get = msvcrt.getch()
if get is 'v': print("yup!")