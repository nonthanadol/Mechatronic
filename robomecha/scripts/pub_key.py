#!/usr/bin/env python3
import sys, tty, termios, os
import rospy
from std_msgs.msg import Int64


degree0 = 90

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
 rospy.init_node('key')
 pub = rospy.Publisher('key',Int64 , queue_size = 10)
 rate = rospy.Rate(10)
 while not rospy.is_shutdown():
   char = getch()
   if(char == 'r'):
      degree0 = degree0 + 1
      print('increment angle joint0 ++  '+str(degree0))
   elif(char == 'f'):
      degree0 = degree0 - 1
      print('Decrement angle joint0 -- {}'.format(degree0))
   elif(char == "x"):
      break
   char = ""
   pub.publish(degree0)
   rate.sleep()