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