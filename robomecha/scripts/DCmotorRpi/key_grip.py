import sys, tty, termios, os
from GripperControl import AlphaBot

bot=AlphaBot()

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

bot.setPWMA(70)
bot.setPWMB(70)
bot.setPWMC(70)
while True:
  try: 
   char = getch()
   if(char == 'q'):
      print('q')
      bot.fad()
   elif(char == 'a'):
      print('a')
      bot.backward()
   elif(char == 'z'):
      print('z')
      bot.stop()
   elif(char == "x"):
      break
   char = ""
  except ValueError:
    print('Angle out of range')                        
