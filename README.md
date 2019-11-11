# CircuitPython
## My CircuitPython assignments

### LEDFade:
#### Objective
Make a LED fades in and out.


#### Lessons
In this assignment we learned how to use our new metro board and how to use CircuitPython on Mu.
#### Important Code
`LED.py`
``` python
    
while True:
    led.value = holder     #Sets the LED to a value
    time.sleep(0.1)
    holder += changer      #adds brightness (or subtracts)
    print(holder)          #prints to serial monitor


    if holder >= 60000:
        changer *= -1       #if the led is at the threshold, it makes the changer negative

    if holder <= 2000:
        changer *= -1
```
Our variable counts up, but once it reaches 6000, it multiplies it by a negative and it counts down until it reaches 2000, where it begins to count up. 
