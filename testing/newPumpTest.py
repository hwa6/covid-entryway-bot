#!/usr/bin/env python
#new flash test

import RPi.GPIO as GPIO
import time

# Pin Definitions
output_pin = 11  # BOARD pin 11

#GRND -> DC-
#5v -> DC+
#GPIO (Pin ) -> IN
#COM -> black termnal of battery
#NO -> black terminal of pump
#red terminal of battery -> red terminal of pump

def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BCM pin-numbering scheme from Raspberry Pi
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)

    print("Starting demo now! Press CTRL+C to exit")
    curr_value = GPIO.HIGH
    try:
        while True:
            time.sleep(1)
            # Toggle the output every second
            print("Outputting {} to pin {}".format(curr_value, output_pin))
            GPIO.output(output_pin, curr_value)
            curr_value ^= GPIO.HIGH
            time.sleep(1000)
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
