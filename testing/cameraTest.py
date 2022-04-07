#!/usr/bin/env python3
# importing OpenCV library
import cv2 as cv
  
# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
cam_port = 0
cam = cv.VideoCapture(cam_port)
  
# reading the input using the camera
result, image = cam.read()
  
# If image will detected without any error, 
# show result
if result:
    cv.namedWindow("cam-test")
    cv.imshow("cam-test",image)
    cv.waitKey(0)
    cv.destroyWindow("cam-test")
    cv.imwrite("filename.jpg",image)
  
# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")
