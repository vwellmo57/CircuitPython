#Vann Wellmon
#Cap touch servo
#Mr. H 3rd
import time
import board
import pulseio
from adafruit_motor import servo
import touchio
 
 
touch_A1 = touchio.TouchIn(board.A1)   
touch_A2 = touchio.TouchIn(board.A2)
# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)
angle = 0
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
 
while True:
    if touch_A1.value:
        print("Touched A1!")
        if angle < 180:
            angle = angle +5
        my_servo.angle = angle
        time.sleep(0.05)
    if touch_A2.value:
        print("Touched A1!")
        if angle > 0:
            angle = angle -5
        my_servo.angle = angle
        time.sleep(0.05)
