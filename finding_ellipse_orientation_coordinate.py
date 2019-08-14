import cv2 as cv
import numpy as np
import skimage
import time
import os
from matplotlib import pyplot as plt
from skimage.draw import ellipse
start=time.clock()

os.chdir('/home/shashank/Documents/ABP/Videos/Video_0111/Images_0111')
name_begin='frame_'
ext='.jpg'
count=0

name_full=name_begin+str(count)+ext	
img=cv.imread(name_full,1)
cv.namedWindow('1',cv.WINDOW_NORMAL)
cv.imshow('1',img)
cv.waitKey(0)
img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
circles=cv.HoughCircles(img_gray,cv.cv.CV_HOUGH_GRADIENT,dp=1.5,minDist=200,minRadius=123,maxRadius=132)			
circles=np.uint16(np.around(circles))
centerx=circles[0,0][0]
centery=circles[0,0][1]
radius=circles[0,0][2]

#************************************************************#
#     Creating Framed Image(For the region of Interest)
#************************************************************#

frame = np.zeros(np.shape(img), np.uint8)
cv.circle(frame,(centerx,centery), radius-8, (1,1,1), -1)
	#img_gray=cv.medianBlur(img_gray,5)
framed_img=frame*img
img_gray =frame[:,:,0]*img_gray
img_r = framed_img[:,:,2]
img_g = framed_img[:,:,1]
img_b = framed_img[:,:,0]
equ = cv.equalizeHist(img_g)
res=(img_r-img_g)+50
cv.namedWindow('2',cv.WINDOW_NORMAL)
cv.imshow('2',res)
cv.waitKey(0)
ret,thresh = cv.threshold(res,150,255,0)
cv.namedWindow('Threshold',cv.WINDOW_NORMAL)
cv.imshow('Threshold',thresh)
cv.waitKey(0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
blank= np.zeros(np.shape(img_r), np.uint8)
for i in range(np.shape(contours)[0]):
	cntr=contours[i]
	area=cv.contourArea(cntr)
	if np.shape(cntr)[0] >= 5 and area < 180 and area>50 :
		ellipse = cv.fitEllipse(cntr)
		if ellipse[2]>120 and ellipse[2]<150:
			cv.ellipse(blank,ellipse,(255),-1)

cv.namedWindow('ellipse',cv.WINDOW_NORMAL)
cv.imshow('ellipse',blank)
cv.waitKey(0)	
	
end=time.clock()
print(end-start)
print(count)
cv.destroyAllWindows()

