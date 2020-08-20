#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import socket

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()
s = socket.socket()
addr_info = socket.getaddrinfo("towel.blinkenlights.nl",23)
addr = addr_info[0][-1]

# Write your program here.
ev3.speaker.beep()
s.connect(addr)
print(addr_info)
print(addr)

while True:
    data = s.recv(500)
    print(str(data, 'utf8'), end = '')