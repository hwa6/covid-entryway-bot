#!/usr/bin/env python

#DOCUMENTATION
#
# As it stands, pump runs continuously on PWM configured pin.
# Circuitry configuration: 

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


def main():
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.LOW)
    #p = GPIO.PWM(output_pin, 250)
    #set duty cycle initial state as 0
    #p.start(0)

    print("PWM running. Press CTRL+C to exit.")
    try:
        while True:
	    print("Writing HIGH to pin", output_pin)
            GPIO.output(output_pin, GPIO.HIGH)
	    time.sleep(10)
            print("Writing LOW to pin", output_pin)
	    GPIO.output(output_pin, GPIO.LOW)
            time.sleep(10)
    finally:
        #p.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    main()
