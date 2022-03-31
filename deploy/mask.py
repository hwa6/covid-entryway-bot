#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

#Dispense Mask
def dispense():
    print("dispense func called")
    output_pin = 33
    output_pin = output_pins.get(GPIO.model, None)
    if output_pin is None:
        raise Exception('PWM not enabled')
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    p = GPIO.PWM(output_pin, 250)
    #set duty cycle initial state as 0
    p.start(0)
    try:
        for dc in range(0, 100, 5):
            print(dc)
            p.ChangeDutyCycle(dc)
            time.sleep(.05)
        for dc in range(100, 0, -5):
            print(dc)
            p.ChangeDutyCycle(dc)
            time.sleep(.05)
    finally:
        p.stop()
        GPIO.cleanup()
def detect():
    print("detect mask")
