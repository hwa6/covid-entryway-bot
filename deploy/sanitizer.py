#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

# Pin Definitions
output_pin = 11  # BOARD pin 11

def dispense():
    print("Dispensing Sanitizer")
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BCM pin-numbering scheme
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)

    curr_value = GPIO.HIGH
    print("Outputting {} to pin {}".format(curr_value, output_pin))
    GPIO.output(output_pin, curr_value)
    curr_value ^= GPIO.HIGH
    time.sleep(1)
    GPIO.output(output_pin, curr_value)

    GPIO.cleanup()

