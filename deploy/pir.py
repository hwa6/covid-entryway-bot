#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

pin = 18

def detect():
    print("enter func")
    prev_value = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    print("setup")
    try:
        value = GPIO.input(pin)
        if value == GPIO.HIGH:
            value_str = "HIGH"
            print("Value read from pin {} : {}".format(pin, value))
            return True
        else:
            value_str = "low"
            print("Value read from pin {} : {}".format(pin, value))
            return False
    finally:
        GPIO.cleanup()
