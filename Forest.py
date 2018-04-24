from Tree import *
import random
import turtle
import sys


class Forest():
    ## adds trees to the forest, removes trees, updates status, redraws forest ##
    def __init__(self):
        self.forest = []

    def parameters(self):  # prompts user for user defined parameters
        # prompts user for the density of trees in the forest (1.0 to 100.0)
        density = float(
            input("Please Enter the Density of the Forest (0.0 to 1.0): "))
        if density > 1.0 or density < 0.0:
            print("Please enter a density between 0.0 and 1.0")
            sys.exit()
        # prompts user for percentage of pine trees in the forest (0 to 1)
        percentage = float(
            input("Please Enter the Percentage of Pine Trees (0.0 to 1.0): "))
        if percentage > 1.0 or percentage < 0.0:
            print("Please enter a percentage of pines between 0.0 and 1.0")
            sys.exit()
        # prompts user for the relative wetness of the forest (1 to 100)
        wetness = float(
            input("Please Enter the Wetness of the Forest (1 to 100): "))
        if wetness > 100 or wetness < 1:
            print("Please enter a wetness between 1 and 100")
            sys.exit()
        return density, percentage, wetness

    def initforest(self, density, percentage, wetness, gridSize):
        ## creates an initial forest in the empty forest ##
        # calculates the total number of pine trees, rounds down to nearest number
        pines = int(percentage*gridSize**2)
        for x in range(gridSize-1):
            for y in range(gridSize-1):
                self.randDensity = random.uniform(
                    0, 1)  # creates random number
                # if random value is less than (or equal to) density, then add tree
                if density >= self.randDensity:
                    # taking random number (0 or 1) and if we have met quota for pine trees to determinee if tree is pine
                    if random.randint(0, 1) == 1 and pines > 0:
                        tree = Pine(False, wetness, x, y)
                        self.addTree(tree)
                        pines -= 1
                    else:
                        tree = Oak(False, wetness, x, y)
                        self.addTree(tree)
                else:  # else adds none object to list
                    self.addTree(None)

    def addTree(self, tree):
        ## adds the tree to the forest ##
        self.forest += [tree]

    def initialmatch(self, gridSize):
        ## sets initial tree on fire ##
        done = False
        while not done:
            rand = random.randint(0, gridSize)
            if self.forest[rand] == None:
                pass
            else:
                # selects random tree to catch aflame
                self.forest[rand].setBurning(True)
                done = True

    def isBurning(self):
        ## informs whether a tree is burning in the forest - utilized to terminate the program ##
        for trees in self.forest:
            if trees != None:
                if trees.burning == True:
                    return True
        return False

    def update(self):
        ## updates the status of the forest ##
        currentlyburning = []
        futureburning = []
        forest = self.getForestList()
        for x in range(len(forest)):
            arbor = forest[x]
            if arbor != None:  # skips the None values
                if arbor.burning == True:  # checks if tree was burning previously
                    # appends indice to list for future deletion
                    currentlyburning += [x]
                else:
                    rand = random.random()  # random number between 0.0 and 1.0
                    if rand < arbor.probCatch:
                        if self.checksurrounding(arbor) == True:
                            # appends indice to list for future burning
                            futureburning += [x]
        for each in currentlyburning:
            forest[each] = None
        for each in futureburning:
            tree = forest[each]
            tree.burning = True
        self.forest = forest

    def getForestList(self):
        ## returns the forest list ##
        return self.forest

    def checksurrounding(self, tree):
        ## checks surrounding trees to see if they are burning ##
        for x in self.forest:
            # checks if object in list or current tree object is equal to None
            if (x != None) and (tree != None):
                if x == tree:  # checks if the tree is being compared to itself
                    pass
                elif ((x.xpos - tree.xpos) in range(-1, 2)) and ((x.ypos - tree.ypos) in range(-1, 2)):
                    if x.burning == True:
                        return True

    def redraw(self):
        ## update graphics display by clearing all trees and redrawing ##
        turtle.clearstamps()  # clears the board
        for each in self.forest:
            if each != None:
                each.draw()  # draws the new forest
        turtle.update()  # updates the screen
