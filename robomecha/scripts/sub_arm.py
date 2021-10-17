#!/usr/bin/env python3
import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import rospy
from robomecha.msg import Angle

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)

pca.frequency = 60

#servo0 = servo.Servo(pca.channels[0])
servo1 = servo.Servo(pca.channels[1])
servo2 = servo.Servo(pca.channels[2])
servo3 = servo.Servo(pca.channels[3])
servo4 = servo.Servo(pca.channels[4])
servo5 = servo.Servo(pca.channels[5])
def printscreen():
    print('################################################')
    #print('angle joint1 = {0:.2f}'.format(servo0.angle))
    print('angle joint1 = {0:.2f}'.format(servo1.angle))
    print('angle joint2 = {0:.2f}'.format(servo3.angle))
    print('angle joint3 = {0:.2f}'.format(servo4.angle))
    print('angle joint4 = {0:.2f}'.format(servo5.angle))
    #print('angle joint5 = {0:.2f}'.format(servo6.angle))
    print('################################################')

def joint(msgs):
 try:
    #servo0.angle = msgs.degree0
    servo1.angle = msgs.degree1
    servo2.angle = msgs.degree2
    servo3.angle = msgs.degree3
    servo4.angle = msgs.degree4
    servo5.angle = msgs.degree5
    printscreen()
 except ValueError:
    print('Angle out of range')   
   

if __name__ == '__main__':
    rospy.init_node('sub_arm')
    print('Start!!!')
    rospy.Subscriber('key', Angle, joint)
    rospy.spin()