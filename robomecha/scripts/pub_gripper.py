#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool
import sys, tty, termios, os
control=Bool()
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
    pub = rospy.Publisher('gripper_state', Bool, queue_size = 10)
    while True:
        char = getch()
        if(char == 'q'):
           print('q')
           control.data = True
        elif(char == 'a'):
           print('a')
           control.data = False
        elif(char == 'z'):
           print('z')
           control.data = False
        elif(char == "x"):
           break
        char = ""
        pub.publish(control)
        rate.sleep()
                      

