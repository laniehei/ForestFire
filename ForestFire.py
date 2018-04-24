import turtle
import random
from Forest import *
from Tree import *


def main():
    myt = turtle
    forest = Forest()
    gridSize = 40

    density, percent, wetness = forest.parameters()
    forest.initforest(density, percent, wetness, gridSize)
    forest.initialmatch(gridSize)
    scr = turtle.Screen()
    myt = turtle
    scr.setworldcoordinates(-1, -1, gridSize, gridSize)
    forest.redraw()
    ashes = False  # represents forest is done burning
    while ashes == False:
        forest.update()
        forest.redraw()
        if forest.isBurning() == False:
            ashes = True
    myt.goto(gridSize/4, gridSize/2)
    myt.write("FOREST IS TOAST (CLICK TO EXIT)", font=("Arial", 16, "normal"))
    myt.exitonclick()


main()
