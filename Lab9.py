#Import cv2 nump and matplotlib
import copy
import cv2
import numpy as np
from matplotlib import pyplot as plt

#imported ATU jpeg using cv2
img = cv2.imread('ATU1.jpg',)

#converted the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#deep copy 
imgHarris = copy.deepcopy(img)
imgShiTomasi = copy.deepcopy(img)

#Harris corner detection
dst = cv2.cornerHarris(gray_image, 2, 3, 0.04)

threshold = 0.1; #number between 0 and 1
for i in range(len(dst)):
    for j in range(len(dst[i])):
        if dst[i][j] > (threshold*dst.max()):
            cv2.circle(imgHarris,(j,i),3,(0, 0, 255),-1)

#Shi Tomasi corner detection algorithm
corners = cv2.goodFeaturesToTrack(gray_image,10 , 0.01, 10)
corners = np.int0(corners) #convert corners values to integer

for i in corners:
    x,y = i.ravel()
    cv2.circle(imgShiTomasi,(x,y),3,(0, 0, 255),-1)

#Plotting the gray scaled image
plt.subplot(2, 2, 1),plt.imshow(gray_image, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])

#HarrisCorners
plt.subplot(2, 2, 2),plt.imshow(cv2.cvtColor(imgHarris, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('HarrisCorners'), plt.xticks([]), plt.yticks([])

#Shi Tomasi Corners
plt.subplot(2, 2, 3),plt.imshow(cv2.cvtColor(imgShiTomasi, cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('ShiTomasi'), plt.xticks([]), plt.yticks([])

#displaying the image
plt.show()

cv2.waitKey(0)  
cv2.destroyAllWindows()