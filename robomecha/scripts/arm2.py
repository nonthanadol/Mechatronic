import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685



#0-0
#2-125
#4-45
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)

pca.frequency = 60

servo0 = servo.Servo(pca.channels[1])
servo0.angle = 45
time.sleep(2)
#pca.deinit()

