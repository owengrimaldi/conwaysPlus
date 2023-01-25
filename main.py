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

import curses


def getch():
    screen = curses.initscr()
    print(screen.getch())


getch()

'''
import sys
from boardSetup import Board


testBoard = Board(30)

testBoard.printCurrentBoard()

get = _Getch()
if get == 'v': print("yup!")