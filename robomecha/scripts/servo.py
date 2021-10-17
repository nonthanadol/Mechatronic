import time

from board import SCL, SDA
import busio


from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)


servo7 = servo.Servo(pca.channels[7])

# We sleep in the loops to give the servo time to move into position.
for i in range(180):
    servo7.angle = i
    time.sleep(0.03)
for i in range(180):
    servo7.angle = 180 - i
    time.sleep(0.03)

# You can also specify the movement fractionally.
fraction = 0.0
while fraction < 1.0:
    servo7.fraction = fraction
    fraction += 0.01
    time.sleep(0.03)

pca.deinit()
