#!/usr/bin/python

#2016_0502 Python Programming or Arduino
#          section The Python code.
from pyfirmata import Arduino, INPUT, PWM
from time import sleep
import random

# setup board
port = '/dev/cu.usbmodem1421'
board = Arduino(port)
sleep(5)
s = board.get_firmata_version()
print("Firmata version=", s)

#setup pin 3 as Digital and mode PWM

#method 1
#pin = 3 # LED on PWM pin 3
#board.digital[pin].mode= PWM

#method 2
ledPin = board.get_pin('d:3:p') #digital, pin 3, PWM

# set pin values
for i in range(0,99):
    r = random.randint(1, 100)
    #methode 1: board.digital[pin].write( r / 100.00)
    ledPin.write( r / 100.00)
    print(i,":",r/100.00)
    sleep(0.5)

#methode 1: board.digital[pin].write(0)
ledPin.write(0)

#exit
board.exit()
