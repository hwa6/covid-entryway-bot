#!/usr/bin/env python3
import cv2 as cv
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

filepath = '/home/team7/covid-entryway-bot/deploy/model.pth'
model = torch.load(filepath)


class_names = ['with mask',
 'without mask'
]

#helper function for @classify_face()
#@params image : PIL image
#@return img : image transform of PIL image
def process_image(image):
    ''' Scales, crops, and normalizes a PIL image for a PyTorch model,
        returns an Numpy array
    '''
    
    # TODO: Process a PIL image for use in a PyTorch model
    #pil_image = Image.open(image)
    image_transforms = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    pil_image = image_transforms(image)
    return pil_image

#helper function for @detect()
#@params image : PIL image
#@return class_names[index] : label corresponding to PIL image
def classify_face(image):

    #not sure what this line does tbh
    device = torch.device("cpu")

    #convert from BGR to RGB for PIL processing
    image_cv = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    #convert safely to PIL
    image_pil = Image.fromarray(image_cv)

    #demonstrating images (optional)
    #cv.imshow("CV Image after Color Conversion", image_cv)
    #image_pil.show()
    #cv.waitKey(0)
    #cv.destroyAllWindows()

    print('Processing Image')
    image_pil = process_image(image_pil)
    print('Image Processed')
    #img_processed = np.asarray(image_processed)
    image_pil = image_pil.unsqueeze_(0)
    image_pil = image_pil.float()

    model.eval()
    model.cpu()
    output = model(image_pil)
    #print(output,'##############output###########')
    _, predicted = torch.max(output, 1)
    #print(predicted.data[0],"predicted")


    classification1 = predicted.data[0]
    index = int(classification1)
    return class_names[index]

def getImage():
    cam_port = 0
    cam = cv.VideoCapture(cam_port)  
    # reading the input using the camera
    result, image = cam.read()
    if result:
        print("Image has been captured")
        label = classify_face(image)
        print("User is " + label)
        return label
    else:
        print("Error reading from camera :(")
       
def detect(): 
    print("Detecting mask")
    status = getImage()
    if(status == "with mask"):
        return True
    return False
