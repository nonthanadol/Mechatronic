#!/usr/bin/env python3
import sys, tty, termios, os
import rospy
from robomecha.msg import Angle
control=Angle()
control.degree0 = 20
control.degree1 = 160
control.degree2 = 130
control.degree3 = 130
control.degree4 = 160
control.degree5 = 130
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
 pub = rospy.Publisher('key',Angle , queue_size = 10)
 rate = rospy.Rate(10)
 while not rospy.is_shutdown():
   char = getch()
   if(char == 'r'):
      control.degree0 = control.degree0 + 1
      #print('increment angle joint1 ++  ',control.degree0)
   elif(char == 'f'):
      control.degree0 = control.degree0 - 1
      #print('Decrement angle joint1 -- ',control.degree0)
   elif(char == 't'):
      control.degree1 = control.degree1 + 1
      #print('increment angle joint2 ++  ',control.degree1)
   elif(char == 'g'):
      control.degree1 = control.degree1 - 1
      #print('Decrement angle joint2 -- ',control.degree1)
   elif(char == 'y'):
      control.degree2 = control.degree2 + 1
      #print('increment angle joint3 ++  ',control.degree2)
   elif(char == 'h'):
      control.degree2 = control.degree2 - 1
      #print('Decrement angle joint3 -- ',control.degree2)
   elif(char == 'u'):
      control.degree3 = control.degree3 + 1
      #print('increment angle joint4 ++  ',control.degree3)
   elif(char == 'j'):
      control.degree3 = control.degree3 - 1
      #print('Decrement angle joint4 -- ',control.degree3)
   elif(char == 'i'):
      control.degree4 = control.degree4 + 1
      #print('increment angle joint5 ++  ',control.degree4)
   elif(char == 'k'):
      control.degree4 = control.degree4 - 1
      #print('Decrement angle joint5 -- ',control.degree4)
   elif(char == 'o'):
      control.degree5 = control.degree5 + 1
      #print('increment angle joint6 ++  ',control.degree5)
   elif(char == 'l'):
      control.degree5 = control.degree5 - 1
      #print('Decrement angle joint6 -- ',control.degree5)
   elif(char == "x"):
      break
   char = ""
   pub.publish(control)
   rate.sleep()
  