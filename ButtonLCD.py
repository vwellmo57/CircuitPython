import time
import board
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode
led = DigitalInOut(board.D13)
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)
switch = DigitalInOut(board.D2)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
value = 0
lcd.set_cursor_pos(0, 1)
lcd.print("ButtonPress:")
while True:
    if switch.value:
        lcd.set_cursor_pos(0, 14)
    else:
        lcd.set_cursor_pos(0, 14)
        value = value + 1
        lcd.print(str(value))
        time.sleep(0.3)
