#!/usr/bin/env python3

import rospy
from robomecha.msg import Angle
import RPi.GPIO as GPIO
from time import sleep
enable_pin = 12
step_pin = 17
dir_pin = 18
mode_pins = (22, 23, 24)

# Stepper motor setup
step_type = '1/32'
fullstep_delay = .005

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(mode_pins, GPIO.OUT)
GPIO.output(enable_pin, not True)
resolution = {'Full':(0, 0, 0),
                    'Half':(1, 0, 0),
                    '1/4':(0, 1, 0),
                    '1/8':(1, 1, 0),
                    '1/16':(0, 0, 1),
                    '1/32':(1, 0, 1)}
microsteps =  {'Full':1,
                    'Half':2,
                    '1/4':4,
                    '1/8':8,
                    '1/16':16,
                    '1/32':32}
delay = .005/microsteps[step_type]
GPIO.output(mode_pins, resolution[step_type])
def move_base(msg):
    GPIO.output(dir_pin, msg.move_base)
    for i in range(32):
        GPIO.output(step_pin, GPIO.HIGH)
        sleep(delay)
        GPIO.output(step_pin, GPIO.LOW)
        sleep(delay)
    GPIO.output(enable_pin, not False)
if __name__ == '__main__':
    rospy.init_node('sub_base')
    rospy.Subscriber('key', Angle, move_base)

    rospy.spin()