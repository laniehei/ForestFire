import random
import turtle

class Tree():
    ##defines attributes of specific trees##
    ## attributes: probCatch, burning, wetness, xpos, ypos
    def __init__(self, burning = False, wetness = 1.0, xpos = 0, ypos = 0):
        self.burning = burning #is the tree burning? T/F
        self.wetness = wetness  #user input data, 100 is wet
        self.xpos = xpos #x position on turtle grid
        self.ypos = ypos #y position on turtle grid 

    def setBurning(self, burning): #allows user to change whether the tree is burning
        self.burning = burning

class Oak(Tree):
    ## inherits attributes from Tree class, creates oak tree objects ##
    def __init__(self, burning = False, wetness = 1.0, xpos = 0, ypos = 0):
        super().__init__(burning, wetness, xpos,ypos) #parent class Tree handles these parameters
        self.probCatch = 0.45/wetness #the chance of object Oak catching fire is default 0.45/ user input wetness
        
    def draw(self): #draws circle on screen, representing oak
        myt = turtle
        myt.penup()
        myt.goto(self.xpos, self.ypos)
        myt.shape("circle")
        myt.tracer(0,0)
        if self.burning == False:
            myt.color('green')
            myt.shapesize(0.5)
            myt.pendown()
            myt.stamp()
        elif self.burning == True:
            myt.color('red')
            myt.shapesize(0.5)
            myt.pendown()
            myt.stamp()
        else:
            return None


class Pine(Tree):
## inherits attributes from Tree class, creates pine tree objects ##
    def __init__(self, burning = False, wetness = 1.0, xpos = 0, ypos = 0):
        super().__init__(burning, wetness, xpos,ypos) #parent class Tree handles these parameters
        self.probCatch = 0.45/wetness #the chance of object Pine catching fire is default 0.95/ user input wetness

    def draw(self): #stamps triangle on screen, representing pine tree
        myt = turtle
        myt.penup()
        myt.goto(self.xpos, self.ypos)
        myt.shape("triangle")
        myt.tilt(90)
        myt.tracer(0,0)
        if self.burning == False:
            myt.color('green')
            myt.shapesize(0.5)
            myt.pendown()
            myt.stamp()
            myt.tilt(270)
        elif self.burning == True:
            myt.color('red')
            myt.shapesize(0.5)
            myt.pendown()
            myt.stamp()
            myt.tilt(270)
        else:
            return None