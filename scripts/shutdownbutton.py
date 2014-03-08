#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import required modules
import time
import subprocess
import RPi.GPIO as GPIO

# set GPIO pin with connected button
GPIOPin = 18 
GPIOPinLED = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIOPinLED, GPIO.OUT)

# main function
def main():
  value = 0

  GPIO.output(GPIOPinLED, True)
  while True:
    # increment value if button is pressed
    if not GPIO.input(GPIOPin):
      value += 0.5

    # restart or shutdown selected
    if value > 0:

      # shutdown selected if value is larger than 3 or equal
      if value >= 3:
	GPIO.output(GPIOPinLED, False)
        subprocess.call(["shutdown", "-h", "now"])
        return 0

      # restart selected if value is less than 3
      elif GPIO.input(GPIOPin):
	GPIO.output(GPIOPinLED, False)
        subprocess.call(["shutdown", "-r", "now"])
        return 0

    # wait 500ms
    time.sleep(0.5)

  return 0

if __name__ == '__main__':
  # use GPIO pin numbering convention
  GPIO.setmode(GPIO.BCM)

  # set up GPIO pin for input
  GPIO.setup(GPIOPin, GPIO.IN)

  # call main function
  main()

