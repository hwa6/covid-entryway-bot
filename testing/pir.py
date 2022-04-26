#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

pin = 18

def main():
    prev_value = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    try:
        value = GPIO.input(pin)
        if value == GPIO.HIGH:
            value_str = "HIGH"
            print("true")
            return True
        else:
            value_str = "low"
            print("false")
            return False
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
