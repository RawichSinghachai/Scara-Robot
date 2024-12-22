from adafruit_servokit import ServoKit
from time import sleep
import numpy as np

# Initialize the ServoKit for 16 channels
kit = ServoKit(channels=16)

kit.servo[0].actuation_range = 270
kit.servo[0].set_pulse_width_range(500, 2500)
kit.servo[0].angle = 0

kit.servo[1].actuation_range = 270
kit.servo[1].set_pulse_width_range(500, 2500)
kit.servo[1].angle = 0

kit.servo[2].actuation_range = 270
kit.servo[2].set_pulse_width_range(500, 2500)
kit.servo[2].angle = 0

kit.servo[4].actuation_range = 270
kit.servo[4].set_pulse_width_range(500, 2500)
kit.servo[4].angle = 0