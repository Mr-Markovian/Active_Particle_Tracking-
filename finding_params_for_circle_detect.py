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
for j in range(15000,25000):
	name_full=name_begin+str(j)+ext	
	img=cv.imread(name_full,1)
	img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
	circles=cv.HoughCircles(img_gray,cv.cv.CV_HOUGH_GRADIENT,dp=1.5,minDist=200,minRadius=123,maxRadius=132)
	if(circles is None):
		continue			
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
	equ = cv.equalizeHist(img_g)#img_g
	particles =cv.HoughCircles(equ,cv.cv.CV_HOUGH_GRADIENT,dp=1.9,param1=115,param2=23,minDist=20,minRadius=7,maxRadius=13)
	center_x = particles[0,:,0] 
	if (np.shape(center_x)[0]!=61):
		particles =cv.HoughCircles(equ,cv.cv.CV_HOUGH_GRADIENT,dp=2.1,param1=90,param2=25,minDist=20,minRadius=7,maxRadius=13)
	 #white =(255,255,255)
		
	particles=np.uint16(np.around(particles))
	
	#for i in particles[0,:]:
	#	cv.circle(img,(i[0],i[1]),i[2],(255,255,255),2)  #white =(255,255,255)
	#cv.namedWindow('3',cv.WINDOW_NORMAL)
	#cv.imshow('3',img)	
#cv.namedWindow('3',cv.WINDOW_NORMAL)
	#cv.imshow('3',img)


	center_x = particles[0,:,0]                                         #Size of this array =no of particles
	center_y = particles[0,:,1]
	#print(np.shape(center_x),i)
	print(np.shape(center_x)[0],j)
	if(np.shape(center_x)[0]!=61):
		count=count+1		
	
end=time.clock()
print(end-start)
print(count)
cv.destroyAllWindows()

