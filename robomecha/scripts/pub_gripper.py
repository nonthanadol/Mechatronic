#!/usr/bin/env python3

import rospy
#from std_msgs.msg import Bool
from robomecha.msg import Angle
import sys, tty, termios, os
control=Angle()
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

if __name__ == '__main__':
    rospy.init_node('pub_gripper')
    print("Start!!!!!!")
    rate = rospy.Rate(10)
    pub = rospy.Publisher('key', Angle, queue_size = 10)
    while True:
        char = getch()
        if(char == 'q'):
           print('q')
           control.grip_state = True
        elif(char == 'a'):
           print('a')
           control.grip_state = False
        elif(char == 'z'):
           print('z')
           control.grip_state = False
        elif(char == "x"):
           break
        char = ""
        pub.publish(control)
        rate.sleep()
                      

