from digitalio import DigitalInOut, Direction, Pull
import board
import time
max = 4 #the time delay
start = time.time()
photo = DigitalInOut(board.D2) #digital pin 2
photo.direction = Direction.INPUT
photo.pull = Pull.UP #pulling up, using internal resistor
photo_state = False #setting the states to be false on the loops first run
last_state = False
value = 0
limit = 0
while True:
    photo_state = photo.value
    if photo_state and not last_state: #if the photo state is true but the last state is false, do x
        value = value + 1
        # print("# of interrupts:")
        # print(value)
    last_state = photo_state
    remaining = max + start - time.time() #calculates the time
    if remaining <= 0: #if time is over
        print("# of interrupts:", (value))
        max += 4 #sets the variables back to default
        value = 0
