import sys, tty, termios, os
import controller as ctrl


degree0 = 20
degree1 = 160
degree2 = 130
degree4 = 160

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


while True:
  try: 
   char = getch()
   if(char == 'r'):
      degree0 = degree0 + 1
      ctrl.joint0(degree0)
      print('increment angle joint0 ++  '+str(degree0))
   elif(char == 'f'):
      degree0 = degree0 - 1
      ctrl.joint0(degree0)
      print('Decrement angle joint0 -- {}'.format(degree0))
   
   elif(char == 't'):
      degree1 = degree1 + 1
      ctrl.joint1(degree1)
      print('increment angle joint1 ++  '+str(degree1))
   elif(char == 'g'):
      degree1 = degree1 - 1
      ctrl.joint1(degree1)
      print('Decrement angle joint1 -- {}'.format(degree1))

   elif(char == 'y'):
      degree2 = degree2 + 1
      ctrl.joint2(degree2)
      print('increment angle joint2 ++  '+str(degree2))
   elif(char == 'h'):
      degree2 = degree2 - 1
      ctrl.joint2(degree2)
      print('Decrement angle joint2 -- {}'.format(degree2))
   
   elif(char == 'u'):
      degree4 = degree4 + 1
      ctrl.joint4(degree4)
      print('increment angle joint4 ++  '+str(degree4))
   elif(char == 'j'):
      degree4 = degree4 - 1
      ctrl.joint4(degree4)
      print('Decrement angle joint4 -- {}'.format(degree4))
   
   elif(char == "z"):
      degree0 = 20
      degree1 = 160
      degree2 = 130
      degree4 = 160
      print('set home position ')
      ctrl.home_pos(degree0,degree1,degree2,degree4)
   
   elif(char == "x"):
      break
   char = ""
  except ValueError:
    print('Angle out of range')                        

   
