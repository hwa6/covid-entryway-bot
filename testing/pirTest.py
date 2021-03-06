#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

input_pin = 18

def main():
    prev_value = None


    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(input_pin, GPIO.IN)
    print("Starting")
    try:
        while True:
            value = GPIO.input(input_pin)
            #if True:
            if value != prev_value:
                if value == GPIO.HIGH:
                    value_str = "HIGH"
                else:
                    value_str = "LOW"
                print("Value read from pin {} : {}".format(input_pin, value_str))
            prev_value = value
            #prev_val = value
            time.sleep(1)
    finally:
            GPIO.cleanup()

if __name__ == '__main__':
    main()
