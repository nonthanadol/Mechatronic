#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool
import RPi.GPIO as GPIO
import time

IN1 = 12
IN2 = 13
IN3 = 20
IN4 = 21
IN5 = 5
IN6 = 16
ENA = 6
ENB = 26
ENC = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)
GPIO.setup(IN5,GPIO.OUT)
GPIO.setup(IN6,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(ENB,GPIO.OUT)
GPIO.setup(ENC,GPIO.OUT)

PWMA = GPIO.PWM(ENA,200) #create a PWM instance: // GPIO.PWM(channal,frequence)
PWMB = GPIO.PWM(ENB,200)
PWMC = GPIO.PWM(ENC,200)
PWMA.start(0) # start PWM where (..) is the duty cycle (0.0% <= dc <= 100.0%)
PWMB.start(0)
PWMC.start(0)

GPIO.output(IN1,GPIO.LOW)
GPIO.output(IN2,GPIO.LOW)
GPIO.output(IN3,GPIO.LOW)
GPIO.output(IN4,GPIO.LOW)
GPIO.output(IN5,GPIO.LOW)
GPIO.output(IN6,GPIO.LOW)

PWMA.ChangeDutyCycle(70)
PWMB.ChangeDutyCycle(70)
PWMC.ChangeDutyCycle(70)
def gripper_state_callback(msg):
		GPIO.output(IN1,msg.data)
		GPIO.output(IN2,not msg.data)
		GPIO.output(IN3,not msg.data)
		GPIO.output(IN4,msg.data)
		GPIO.output(IN5,msg.data)
		GPIO.output(IN6,not msg.data)
		time.sleep(2)
		GPIO.output(IN1,GPIO.LOW)
		GPIO.output(IN2,GPIO.LOW)
		GPIO.output(IN3,GPIO.LOW)
		GPIO.output(IN4,GPIO.LOW)
		GPIO.output(IN5,GPIO.LOW)
		GPIO.output(IN6,GPIO.LOW)


if __name__ == '__main__':
    rospy.init_node('sub_gripper')
    print('Start!!!')
    rospy.Subscriber('gripper_state', Bool, gripper_state_callback)

    rospy.spin()
