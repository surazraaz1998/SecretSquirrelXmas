#!/usr/bin/env python

import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setmode(GPIO.BCM) # Use Broadcom numbering

FLAG='http://172.16.122.215' # Set custom message here

# Setup LED pins
led0 = 12
led1 = 16
led2 = 20
led3 = 21

ledr = 14
ledg = 15
ledb = 18

# Blink everything once to make sure it is all working at boot
for led in (led0,led1,led2,led3,ledr,ledg,ledb):
    GPIO.setup(led,GPIO.OUT)
    GPIO.output(led,GPIO.HIGH)
time.sleep(.1)
for led in (led0,led1,led2,led3,ledr,ledg,ledb):
    GPIO.output(led,GPIO.LOW)

# Swipe animation to signal begin/end of message
def swipe():
    for led in (led0,led1,led2,led3):
        GPIO.output(led,GPIO.HIGH)
        time.sleep(.1)
    for led in (led0,led1,led2,led3):
        GPIO.output(led,GPIO.LOW)
        time.sleep(.1)
    for led in (led3,led2,led1,led0):
        GPIO.output(led,GPIO.HIGH)
        time.sleep(.1)
    for led in (led3,led2,led1,led0):
        GPIO.output(led,GPIO.LOW)
        time.sleep(.1)

# Accept 4 bits and blink the lights accordingly		
def blink(nibble,delay):
    for i in range(0,3):
      if nibble[0] == '1':
        GPIO.output(led0,GPIO.HIGH)
      else:
        GPIO.output(led0,GPIO.LOW)
      if nibble[1] == '1':
        GPIO.output(led1,GPIO.HIGH)
      else:
        GPIO.output(led1,GPIO.LOW)
      if nibble[2] == '1':
        GPIO.output(led2,GPIO.HIGH)
      else:
        GPIO.output(led2,GPIO.LOW)
      if nibble[3] == '1':
        GPIO.output(led3,GPIO.HIGH)
      else:
        GPIO.output(led3,GPIO.LOW)
    time.sleep(delay)
    for led in (led3,led2,led1,led0):
        GPIO.output(led,GPIO.LOW)
    time.sleep(2*delay)

while True:
    swipe()
    swipe()

	# Take the flag and iterate through it converting the ASCII
	# to ordinal numbers and then binary.
    for ch in range(len(FLAG)):
      k = bin(ord(FLAG[ch]))[2:].zfill(8)
      print k
	  # Break each byte into 2 nibbles and send them out to blink
      n1 = k[:4]
      n2 = k[4:]
      blink(n1,1)
      blink(n2,1)

GPIO.cleanup()