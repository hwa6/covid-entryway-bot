#!/usr/bin/env python3

#dispense imports
import RPi.GPIO as GPIO
import time
#detect imports
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import os
import pandas as pd
from sklearn.model_selection import train_test_split
import shutil
import time
import copy
from PIL import Image
import glob
import cv2

filepath = '/home/team7/covid-entryway-bot/deploy/model.pth'
model = torch.load(filepath)


class_names = ['with_mask',
 'without_mask'
]



#function to dispense mask
def dispense():
    print("dispense func called")
    output_pin = 33
    output_pin = output_pins.get(GPIO.model, None)
    if output_pin is None:
        raise Exception('PWM not enabled')
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    p = GPIO.PWM(output_pin, 250)
    #set duty cycle initial state as 0
    p.start(0)
    try:
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

#function to determine if user is wearing mask
#@return maskStatus : boolean, true if user is wearing mask
def detect():
    print("Detecting Mask.")
    count = 0

    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if count % 20 == 0 :
            label = classify_face(frame)
            # print("the label is", label)
        if key == 27: # exit on ESC
            break
        count += 1

    vc.release()
    cv2.destroyWindow("preview")

#helper function for @detect()
#@params image : PIL image
#@return class_names[index] : label corresponding to PIL image
def classify_face(image):
    device = torch.device("cpu")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #im_pil = image.fromarray(image)
    #image = np.asarray(im)
    im = Image.fromarray(image)
    image = process_image(im)
    # print('image_processed')
    img = image.unsqueeze_(0)
    img = image.float()

    model.eval()
    model.cpu()
    output = model(image)
    # print(output,'##############output###########')
    _, predicted = torch.max(output, 1)
    # print(predicted.data[0],"predicted")


    classification1 = predicted.data[0]
    index = int(classification1)
    print(class_names[index])
    return class_names[index]

#helper function for @classify_face()
#@params image : PIL image
#@return img : image transform of PIL image
def process_image(image):
    ''' Scales, crops, and normalizes a PIL image for a PyTorch model,
        returns an Numpy array
    '''
    
    # TODO: Process a PIL image for use in a PyTorch model
    #pil_image = Image.open(image)
    pil_image = image
   
    image_transforms = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    img = image_transforms(pil_image)
    return img

