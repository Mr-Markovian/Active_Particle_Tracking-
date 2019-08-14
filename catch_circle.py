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

for i in range(2,4):
	name_full=name_begin+str(i)+ext	
	img=cv.imread(name_full,1)
	img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
	circles=cv.HoughCircles(img_gray,cv.cv.CV_HOUGH_GRADIENT,dp=1.5,minDist=200,minRadius=123,maxRadius=132)
	circles=np.uint16(np.around(circles))
	centerx=circles[0,0][0]
	centery=circles[0,0][1]
	radius=circles[0,0][2]

	frame = np.zeros(np.shape(img), np.uint8)
	cv.circle(frame,(centerx,centery), radius-8, (1,1,1), -1)
	
	framed_img=frame*img
	img_gray =frame[:,:,0]*img_gray

	img_r = framed_img[:,:,2]
	img_g = framed_img[:,:,1]
	img_b = framed_img[:,:,0]
	
	cv.namedWindow('3',cv.WINDOW_NORMAL)
	cv.imshow('3',img_g)
	cv.waitKey(0)
	#center_x = particles[0,:,0]                                         #Size of this array =no of particles
	#center_y = particles[0,:,1]
	#print(np.shape(center_x),i)
end=time.clock()
print(end-start)
cv.destroyAllWindows()

