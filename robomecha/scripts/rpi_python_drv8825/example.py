from stepper import StepperMotor
from time import sleep
import sys, tty, termios, os
# GPIO setup
enable_pin = 12
step_pin = 17
dir_pin = 18
mode_pins = (22, 23, 24)

# Stepper motor setup
step_type = '1/32'
fullstep_delay = .005

# create object
motor = StepperMotor(enable_pin, step_pin, dir_pin, mode_pins, step_type, fullstep_delay)
motor.enable(True)        # enables stepper driver
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
while(True):   
    char = getch()
    if(char == 'e'):
        motor.run(32, True)     # run motor 6400 steps clowckwise
    elif(char == 'd'):
       motor.run(32, False)    # run motor 6400 steps counterclockwise
    elif(char == 'c'):
        break
    else:
        pass
motor.enable(False)       # disable stepper driver
