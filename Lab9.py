#Import cv2 nump and matplotlib
import copy
import cv2
import numpy as np
from matplotlib import pyplot as plt

#imported ATU jpeg using cv2
img = cv2.imread('ATU1.jpg',)

#deep copy
imgHarris = copy.deepcopy(img)

#converted the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Harris corner detection
dst = cv2.cornerHarris(gray_image, 2, 3, 0.04)

#displaying the grayscale image
cv2.imshow('grayscale', gray_image)

cv2.waitKey(0)