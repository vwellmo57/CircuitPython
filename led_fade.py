#Vann Wellmon
#Mr.H
#LED Fade
import board #gives the board functionality
from analogio 
import AnalogOut #allows you to output pwm via alanlog pins
analog_out = AnalogOut(board.A0) #pin A0
while True: #essesialy a void loop
    for i in range(0, 65535, 1): #counts from 0 to 65535 and then writes it to the LED
        analog_out.value = i
    for j in range(65535, 0, -1): #counts from 65535 down to 0 and then writes it to the LED
        analog_out.value = j
