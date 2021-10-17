#!/usr/bin/env python3
import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import rospy
from std_msgs.msg import Int64

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)

pca.frequency = 60

servo0 = servo.Servo(pca.channels[0])


def joint0(degree0):
	print('joint0 = '+str(degree0.data))
	servo0.angle = degree0.data



if __name__ == '__main__':
    rospy.init_node('sub_key')
    print('Start!!!')
    rospy.Subscriber('key', Int64, joint0)
    rospy.spin()