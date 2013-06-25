#!/usr/bin/python

import firmata
import time

from linux_metrics import cpu_stat

PIN_BUTTON = 11
PIN_LED = 10
PIN_METER = 9

print "Connecting to Meter..."
board = firmata.FirmataInit('/dev/cu.usbserial-A1016d5')
print "Initializing Meter..."
board.pinMode(PIN_BUTTON, firmata.MODE_INPUT)
board.digitalWrite(PIN_BUTTON, True)
board.EnableDigitalReporting(1)  # Enable digital reporting on port 1

while(True):
  cpu_pcts = cpu_stat.cpu_percents(1)
  i = int((100 - cpu_pcts['idle']) * 2.55)
  board.analogWrite(PIN_METER, i)
