#!/usr/bin/python

import firmata
import time

PIN_BUTTON = 11
PIN_LED = 10
PIN_METER = 9

print "Connecting to Meter..."
board = firmata.FirmataInit('/dev/cu.usbserial-A1016d5')
print "Initializing Meter..."
board.pinMode(PIN_BUTTON, firmata.MODE_INPUT)
board.digitalWrite(PIN_BUTTON, True)
board.EnableDigitalReporting(1)  # Enable digital reporting on port 1

i = 0
d = 1

while(True):
  if(d):
    i += 1
  else:
    i -= 1

  if(i<1):
    d = 1
  if(i>254):
    d = 0

  board.analogWrite(PIN_LED, i)
  board.analogWrite(PIN_METER, i)
  time.sleep(0.01)
