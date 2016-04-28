#!/usr/bin/python

//import serial
import pyfirmata
pin = 13
port = '/dev/cu.wchusbserial1450'

board = pyfirmata.Arduino(port)

/#print('Serial setup...')
/#s = serial.Serial('/dev/cu.wchusbserial1450', 9600)
/#print('s setup...')
/#while True:
/#    print (s.readline())
