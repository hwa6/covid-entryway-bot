#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

pin = 18

def detect():
    prev_value = None
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    try:
        value = GPIO.input(pin)
        if value != prev_value:
            if value == GPIO.HIGH:
                value_str = "HIGH"
                print("Value read from pin {} : {}".format(pin, value_str))
                return True
            else:
                value_str = "low"
                print("Value read from pin {} : {}".format(pin, value_str))
                return False
            prev_value = value
        time.sleep(1)
    finally:
        GPIO.cleanup()
