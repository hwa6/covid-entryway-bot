#!/usr/bin/env python3

import time
import pir
import mask
import sanitizer
import display

while(1):
    if(pir.detect):
        ##face detected, get label from model
        if(mask.detect == False):
            ##no mask, dispense mask
            display.displayStatus("No Mask Detected, Dispensing Mask.")
            mask.dispense
        else:
            ##mask on
            display.displayStatus("Mask Detected.")
        time.sleep(1)
        ##dispense hand sanitizer
        display.displayStatus("Dispensing Sanitizer")
        sanitizer.dispense
        time.sleep(5)
    else:
        time.sleep(1)
