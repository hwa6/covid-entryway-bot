#!/usr/bin/env python

# Setting the frequency higher allows for the servo to make more changes.
# Time sleep also seems to need to be quite miniscule for rapid changes.

import RPi.GPIO as GPIO
import time

output_pins = {
    'JETSON_XAVIER': 18,
    'JETSON_NANO': 33,
    'JETSON_NX': 33,
    'CLARA_AGX_XAVIER': 18,
    'JETSON_TX2_NX': 32,
}
output_pin = output_pins.get(GPIO.model, None)
if output_pin is None:
    raise Exception('PWM not supported on this board')


def getAngle(angle):
    duty = angle / 18 + 3
    return duty

def main():
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
        while True:
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

if __name__ == '__main__':
    main()
