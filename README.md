# CircuitPython
## My CircuitPython assignments

### LEDFade:
#### Objective
Make a LED fade from full brightness (255) to 


#### Lessons
In this assignment we learned how to use the new metro express board as well as CircuitPython using Mu.
#### Important Code
`LEDFade.py`
``` python
    
while True: #essesialy a void loop
    for i in range(0, 65535, 1): #counts from 0 to 65535 and then writes it to the LED
        analog_out.value = i
    for j in range(65535, 0, -1): #counts from 65535 down to 0 and then writes it to the LED
        analog_out.value = j
```
Our variable counts up, but once it reaches 6000, it multiplies it by a negative and it counts down until it reaches 2000, where it begins to count up. 

### Circuit Python Servo:
#### Objective
Use capacitive touch to move a servo back and forth.
#### Picture
![](Downloads/WiringForServoTouch.png)
#### Lessons
Learned how to use pwm(pulse width modulation) as well as capacitive touch on the Metro Express. 
#### Important Code
`Servo.py`
``` python
    
def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle
```
PWM works by sending lots of signals at a certain frequency and at certain intervals. I primarily used this guide (https://bit.ly/2rvsclJ) to help me work it all out. There was lot's of collaberation on this assignment amoung us. The wiring is RED-5V, BLACK-GND, YELLOW-DPIN. I would reccomend getting your servo working before touching capacitive touch. I used this (https://bit.ly/2X8vuXP) guide to learn how to use capacitive touch. It was a lot easier than the pwm for me. 

### LCD:
#### Objective
Count the amount of times a button has been pressed on an LCD.
#### Lessons
How to use and LCD with the Metro Express as well as how to use a button
#### Important Code
`ButtonLCD.py`
``` python
    
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
```
Our variable counts up, but once it reaches 6000, it multiplies it by a negative and it counts down until it reaches 2000, where it begins to count up. 
