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
PWM works by sending lots of signals at a certain frequency and at certain intervals. I primarily used this guide https://bit.ly/2rvsclJ to help me work it all out. There was lot's of collaberation on this assignment amoung us. The wiring is RED-5V, BLACK-GND, YELLOW-DPIN. 
