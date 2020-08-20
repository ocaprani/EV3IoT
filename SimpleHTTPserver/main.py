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
lightSensor = ColorSensor(Port.S3)

html = """<!DOCTYPE html>
<html>
    <head> <title>EV3 light sensor</title> </head>
    <body> <h1>EV3 light sensor value</h1>
        <p>
        Light sensor on port 3 has value %s percent.
    </body>
</html>
"""

# Write your program here.
ev3.speaker.beep()
addr = socket.getaddrinfo('0.0.0.0', 8080)[0][-1]
s = socket.socket()
print('bind to', addr)
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, cl_addr = s.accept()
    print('client connected from', cl_addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
 
    response = html % lightSensor.reflection()
    print(lightSensor.reflection())
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()