#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import required modules
import time
import subprocess
import RPi.GPIO as GPIO

# set GPIO pin with connected button
GPIOPin = 14 
GPIOPinLED = 4
GPIOPinRelay1 = 22
GPIOPinRelay2 = 27
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(GPIOPinLED, GPIO.OUT)
#GPIO.setup(GPIOPinRelay1, GPIO.OUT)
#GPIO.setup(GPIOPinRelay2, GPIO.OUT)


# main function
def main():
  value = 0

  while True:
    # increment value if button is pressed
    if not GPIO.input(GPIOPin):
      GPIO.output(GPIOPinRelay1, False)
      GPIO.output(GPIOPinRelay2, False)
      GPIO.output(GPIOPinLED, False)
      if value > 0:
        subprocess.call(["mpc", "stop"])
        value = 0
    # restart selected if value is less than 3
    elif GPIO.input(GPIOPin):
      GPIO.output(GPIOPinRelay1, True)
      GPIO.output(GPIOPinRelay2, True)
      GPIO.output(GPIOPinLED, True)
      if value < 1:
        subprocess.call(["mpc", "play"])
        value = 1
    # wait 500ms
    time.sleep(0.5)

  return 0

if __name__ == '__main__':
  # use GPIO pin numbering convention
  GPIO.setmode(GPIO.BCM)

  # set up GPIO pin for input
  GPIO.setup(GPIOPin, GPIO.IN)
  GPIO.setup(GPIOPinLED, GPIO.OUT)
  GPIO.setup(GPIOPinRelay1, GPIO.OUT)
  GPIO.setup(GPIOPinRelay2, GPIO.OUT)

  # call main function
  main()

