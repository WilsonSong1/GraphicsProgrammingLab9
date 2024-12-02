#Import cv2 nump and matplotlib
import cv2
import numpy as np
from matplotlib import pyplot as plt

#imported ATU jpeg using cv2
img = cv2.imread('ATU1.jpg',)

#converted the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#displaying the grayscale image
cv2.imshow('Grayscale', gray_image)

cv2.waitKey(0)