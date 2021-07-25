# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
#SPDX-License-Identifier: MIT

"""Simple test for a standard servo on channel 0 and a continuous rotation servo on channel 1."""
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=8)

kit.servo[0].angle =0
#time.sleep(1)
#kit.servo[1].angle =90
#time.sleep(1)
#kit.servo[2].angle =180
#kit.servo[3].angle =180
#kit.servo[4].angle =180
#kit.continuous_servo[1].throttle = 0
#time.sleep(2)
#kit.continuous_servo[2].throttle = 0
#time.sleep(1)
#kit.servo[2].angle = 90
#kit.continuous_servo[4].throttle = 1
while True:
  for i in range(0,181,10):
    kit.servo[0].angle = i
    time.sleep(1)
  for i in range(0,181,10):
    kit.servo[0].angle = 180-i
    time.sleep(1)
  time.sleep(1)