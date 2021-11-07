#!/usr/bin/env python3
import sys, tty, termios, os
import rospy
from robomecha.msg import Angle
#from std_msgs.msg import Bool

#from GripperControl import AlphaBot
#bot=AlphaBot()
#bot.setPWMA(70)
#bot.setPWMB(70)
#bot.setPWMC(70)
control=Angle()
step_angle = 3
control.degree1 = 90
control.degree2 = 90
control.degree3 = 165
control.degree4 = 15
control.degree5 = 122
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
 rospy.init_node('pub_key')
 pub = rospy.Publisher('key',Angle , queue_size = 10)
 rate = rospy.Rate(10)
 while not rospy.is_shutdown():
   char = getch()
   if(char == 'r'):
      control.degree1 = control.degree1 + step_angle
      control.degree2 = control.degree2 - step_angle
      pub.publish(control)
     # print('increment angle joint2 ++  ',control.degree1)
   elif(char == 'f'):
      control.degree1 = control.degree1 - step_angle
      control.degree2 = control.degree2 + step_angle
      pub.publish(control)
     # print('Decrement angle joint2 -- ',control.degree1)
   elif(char == 't'):
      control.degree3 = control.degree3 + step_angle
      pub.publish(control)
      #print('increment angle joint3 ++  ',control.degree2)
   elif(char == 'g'):
      control.degree3 = control.degree3 - step_angle
      pub.publish(control)
      #print('Decrement angle joint3 -- ',control.degree2)
   elif(char == 'y'):
      control.degree4 = control.degree4 + step_angle
      pub.publish(control)
      #print('increment angle joint4 ++  ',control.degree3)
   elif(char == 'h'):
      control.degree4 = control.degree4 - step_angle
      pub.publish(control)
      #print('Decrement angle joint4 -- ',control.degree3)
   elif(char == 'u'):
      control.degree5 = control.degree5 + step_angle
      pub.publish(control)
      #print('increment angle joint5 ++  ',control.degree4)
   elif(char == 'j'):
      control.degree5 = control.degree5 - step_angle
      pub.publish(control)
      #print('Decrement angle joint5 -- ',control.degree4)
   
   ## Base robot ##
   elif(char == 'e'):     
      control.move_base = True
      pub.publish(control)
   elif(char == 'd'):
      control.move_base = False 
      pub.publish(control)  
   
   ## Gripper ##
   elif(char == 'q'):
      #print('q')
      control.grip_state = True
      pub.publish(control)
   elif(char == 'a'):
      #print('a')
      control.grip_state = False
      pub.publish(control)
  
   elif(char == "x"):
      break
   char = ""
   #pub.publish(control)
   rate.sleep()
  