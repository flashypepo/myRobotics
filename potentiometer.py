#!/usr/bin/python

# Python Programming or Arduino
# 2016_0502 Prototyping templates using Firmata
#           potentiometer -> brightness of led

from pyfirmata import Arduino, util, PWM
from time import sleep
import os

# setup board
port = '/dev/cu.usbmodem1421'
board = Arduino(port)
sleep(5)
#s = board.get_firmata_version()
#print("Firmata version=", s)
it = util.Iterator(board) # iterate over the board
it.start() #start

# setup pin A0 which is connected to potentiometer
# setup pin 3 for LED - PWM
a0 = board.get_pin('a:0:i')
ledPin = board.get_pin('d:3:p') #digital, pin 3, PWM

# main section, interruptable gracefully with Ctrl-c
try:
    # read A0 and set brightness...
    while True:
        p = a0.read() # 0.0 < p < 1.0
        #print(p)  #debugging
        ledPin.write(p)
except KeyboardInterrupt:
    board.exit() #exit board
    os._exit(0) #exit program
