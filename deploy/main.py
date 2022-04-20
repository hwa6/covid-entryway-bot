#!/usr/bin/env python3

import time
import pir
import mask
import sanitizer
import display
import model



while(1):
    if(True):
        ##person detected, get label from model
        if(mask.detect() == False):
            ##no mask, dispense masks
            display.displayStatus("No Mask Detected, Dispensing Mask.")
            mask.dispense()
            time.sleep(3)
        else:
            ##mask on
            display.displayStatus("Mask Detected.")
            time.sleep(1)
        ##dispense hand sanitizer
        display.displayStatus("Dispensing Sanitizer")
        sanitizer.dispense()
        time.sleep(5)
    else:
        #no one near sensor, wait a second before checking again
        time.sleep(3)
