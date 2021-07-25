import sys, tty, termios, os
import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)

pca.frequency = 60

servo0 = servo.Servo(pca.channels[0])
servo4 = servo.Servo(pca.channels[4])
servo2 = servo.Servo(pca.channels[2])
degree0 = 0 
degree4 = 0 
degree2 = 0 

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


while True:
   char = getch()
   #print(char)
   if(char == 'r'):
       print('increment angle joint0 '+str(degree0))
       degree0 = degree0 + 1
       servo0.angle = degree0
   if(char == 'f'):
       print('Decrement angle joint0 {}'.format(degree0))
       degree0 = degree0 - 1
       servo0.angle = degree0
   if(char == 't'):
      print('increment angle joint2 {} '.format(degree2))
      degree2 = degree2 + 1
      servo2.angle = degree2
   if(char == 'g'):
      print('Decrement angle joint2 {}'.format(degree2))
      degree2 = degree2 - 1
      servo2.angle = degree2
   if(char == 'y'):
      print('increment angle joint4 {}'.format(degree4)) 
      degree4 = degree4 + 1
      servo4.angle = degree4
   if(char == 'h'):
      print('Decrement angle joint4 {}'.format(degree4))
      degree4 = degree4 - 1
      servo4.angle = degree4
   if(char == "x"):
       break
   char = ""