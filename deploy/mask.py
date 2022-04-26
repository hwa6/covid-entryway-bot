#!/usr/bin/env python3

#dispense imports
import RPi.GPIO as GPIO
import time
import model

output_pin = 33

#function to dispense mask
def dispense():
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    p = GPIO.PWM(output_pin, 250)
    #set duty cycle initial state as 0
    p.start(0)

    print("PWM running. Press CTRL+C to exit.")
    try:
        for dc in range(30, 100, 5):
            print(dc)
            p.ChangeDutyCycle(dc)
            time.sleep(.05)
        time.sleep(5)
        for dc in range(95, 25, -5):
            print(dc)
            p.ChangeDutyCycle(dc)
            time.sleep(.05)
    finally:
        p.stop()
        GPIO.cleanup()

#function to determine if user is wearing mask
#@return maskStatus : boolean, true if user is wearing mask
def detect():
    status = model.detect()
    return status

