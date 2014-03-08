#!/usr/bin/env python
# -*- coding: utf-8 -*-


import gaugette.rotary_encoder
import gaugette.switch
import subprocess
import StepperControl.stepper
import RPi.GPIO as GPIO
 
A_PIN  = 12
B_PIN  = 13
 
encoder = gaugette.rotary_encoder.RotaryEncoder.Worker(A_PIN, B_PIN)
encoder.start()
doubletrue = 0;
 
stepper = StepperControl.stepper.Stepper(24,25,8,7)
steps = 250
try:
 while 1:
    delta = encoder.get_delta()
    if delta!=0:
        if doubletrue > 0:
	 if delta > 0:
	 	stepper.rotate_clockwise(steps)
		subprocess.call(["mpc", "next"])
	 else:
		stepper.rotate_counterwise(steps)
		subprocess.call(["mpc", "prev"])
	 doubletrue = 0
	else:
	 doubletrue = 1
  # reset GPIO settings if user pressed Ctrl+C
except KeyboardInterrupt:
 print("Execution stopped by user")
 GPIO.cleanup() 
