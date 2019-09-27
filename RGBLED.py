 
# main.py

import time
import board
from rgb import RGB   # import the RGB class from the rgb module

r1 = board.D3
g1 = board.D4
b1 = board.D5
r2 = board.D10
g2 = board.D11
b2 = board.D12

myRGB1 = RGB(r1, g1, b1)   # create a new RGB object, using pins 3, 4, and 5
myRGB2 = RGB(r2, g2, b2)   # create a new RGB object, using pins 8, 9, and 10

myRGB1.red()          # Glow red
myRGB2.green()        # Glow green
time.sleep(1)
myRGB1.blue()         # Glow blue
myRGB2.cyan()         # Glow... you get it...
time.sleep(1)
myRGB1.magenta()      # Did you know magenta isn't in the rainbow?
myRGB2.yellow()
# Like you learned in first grade, red and green make... huh?
time.sleep(1)
# extra spicy (optional) part
# myRGB1.rainbow(rate1)
# Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
# myRGB2.rainbow(rate2)
# Fade through the colors of the rainbow at the given rate.  Oooooh, pretty!
time.sleep(1)

____________________________________________________________

# rgb.py


import pulseio

class RGB():
    print("Colors")

    full = 65535

    def __init__(self, r, g, b):
        print(str(r))
        self.r = pulseio.PWMOut(r, frequency=5000, duty_cycle=0)
        self.g = pulseio.PWMOut(g, frequency=5000, duty_cycle=0)
        self.b = pulseio.PWMOut(b, frequency=5000, duty_cycle=0)

    def red(self):
        print("Red")
        self.r.duty_cycle = self.full
        self.g.duty_cycle = self.full
        self.b.duty_cycle = self.full

    def green(self):
        print("Green")
        self.r.duty_cycle = self.full
        self.g.duty_cycle = 0
        self.b.duty_cycle = self.full

    def cyan(self):
        print("Cyan")
        self.r.duty_cycle = 0
        self.g.duty_cycle = 0
        self.b.duty_cycle = self.full

    def blue(self):
        print("Blue")
        self.r.duty_cycle = self.full
        self.g.duty_cycle = 55535
        self.b.duty_cycle = 35535

    def magenta(self):
        print("Magenta")
        self.r.duty_cycle = self.full
        self.g.duty_cycle = 0
        self.b.duty_cycle = self.full

    def yellow(self):
        print("Yellow")
        self.r.duty_cycle = self.full
        self.g.duty_cycle = self.full
        self.b.duty_cycle = 26214
