import requests
import cv2
import numpy as np


URL = "http://10.254.88.168:8080/video"
cam = cv2.VideoCapture(URL)

while True:
    check, img = cam.read()
    cv2.imshow('IPWebcam', ing)
    height, width, channels = img.shape
    print(height, width, channels)
    if cv2.waitKey(1) == 27:
      break