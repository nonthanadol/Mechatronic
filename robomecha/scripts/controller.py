import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)

pca.frequency = 60

servo0 = servo.Servo(pca.channels[0])
servo1 = servo.Servo(pca.channels[1])
servo2 = servo.Servo(pca.channels[2])
servo3 = servo.Servo(pca.channels[3])
servo4 = servo.Servo(pca.channels[4])
servo5 = servo.Servo(pca.channels[5])

def home_pos(degree0,degree1,degree2,degree4):
    servo0.angle = degree0
    servo1.angle = degree1
    servo2.angle = degree2
    servo4.angle = degree4

def joint0(degree0):
	servo0.angle = degree0
def joint1(degree1):
	servo1.angle = degree1
def joint2(degree2):
	servo2.angle = degree2
def joint3(degree3):
	servo3.angle = degree3
def joint4(degree4):
	servo4.angle = degree4
def joint5(degree5):
	servo5.angle = degree5
