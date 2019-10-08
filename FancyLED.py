from board import *
import random
import digitalio
import simpleio
import time
class fancyled:
     kind = "color" # class variable shared by all instances

     # you don't need an __init__ method, but it is common for stuff that runs at instantiaion
     def __init__(self, p1, p2, p3):
        self.fancy1 = digitalio.DigitalInOut(p1) #sets temp values for p1/2/3
        self.fancy2 = digitalio.DigitalInOut(p2)
        self.fancy3 = digitalio.DigitalInOut(p3)
        self.fancy1.direction = digitalio.Direction.OUTPUT #defines them as outputs
        self.fancy2.direction = digitalio.Direction.OUTPUT
        self.fancy3.direction = digitalio.Direction.OUTPUT

     def alternate(self):
        print("alternate") #runs alternate function
        self.fancy1.value = True
        self.fancy2.value = False
        self.fancy3.value = True
        time.sleep(.15)
        self.fancy1.value = False
        self.fancy2.value = True
        self.fancy3.value = False
        time.sleep(.15)
     def blink(self): #runs blink function
        print("blink")
        time.sleep(.15)
        self.fancy1.value = False
        self.fancy2.value = False
        self.fancy3.value = False
        time.sleep(.15)
        self.fancy1.value = True
        self.fancy2.value = True
        self.fancy3.value = True
     def chase(self): #runs chase function
        print("chase")
        self.fancy1.value = True
        self.fancy2.value = False
        self.fancy3.value = False
        time.sleep(.15)
        self.fancy1.value = False
        self.fancy2.value = True
        self.fancy3.value = False


        time.sleep(.15)
        self.fancy1.value = False

        self.fancy2.value = False
        self.fancy3.value = True
        time.sleep(.15)
     def sparkle(self): #runs sparkle function
        print("sparkle")

        rand = random.randrange(4, 10, 1) #randomly selects a pin
        uptime = random.randrange(0, 20, 1)#randomly selects a time
        uptime = uptime/150 #divides time to get a smaller number

       # print(uptime)
        if rand == 4: #run sparkle for each pin with random values
           self.fancy1.value= True
           self.fancy2.value = False

           self.fancy3.value = False
           time.sleep(uptime)
        if rand == 5:
           self.fancy2.value= True
           self.fancy1.value = False
           self.fancy3.value = False
           time.sleep(uptime)
        if rand == 6:
           self.fancy3.value= True
           self.fancy1.value = False
           self.fancy2.value = False
           time.sleep(uptime)
        if rand > 6:
           self.fancy1.value = False
           self.fancy2.value = False
           self.fancy3.value = False
           time.sleep(uptime)

_____________________________________________________

from fancyled import fancyled
import board  #pylint: disable-msg=import-error
import time

fancy1 = fancyled(board.D2,board.D3,board.D4) #defines different pins for each function
fancy2 = fancyled(board.D5,board.D6,board.D7)

while True: #runs functions
    fancy1.alternate()
    fancy2.blink()
    fancy1.chase()
    fancy2.sparkle()
