import cv2 as cv
import numpy as np
import pandas as pd
import skimage
import time
import os
from matplotlib import pyplot as plt
from skimage.draw import ellipse
from skimage.measure import label,regionprops
from skimage.color import label2rgb
start=time.clock()
os.chdir("/home/shashank/Documents/ABP/Videos/Video_0111/Images_0111")
#cap=cv2.VideoCapture("Video path")
#totalFrames = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)) 
#==================================================================================
#Functions defined here
#=================================================================================
#def findframe(img_g):
#	circles=cv.HoughCircles(img_g,cv.cv.CV_HOUGH_GRADIENT,dp=1.5,minDist=200,minRadius=123,maxRadius=132)
#	circles=np.uint16(np.around(circles))
#	frame_=np.zeros(np.shape(img_g),np.uint8)
#	centerx=circles[0,0][0]
#	centery=circles[0,0][1]
#	radius=circles[0,0][2]
#	cv.circle(frame_,(centerx,centery),radius-8,(1),-1)
#	return frame_


def particle_position(img_green):                                       #function to compute particle position
	equ = cv.equalizeHist(img_green)
	particles =cv.HoughCircles(equ,cv.cv.CV_HOUGH_GRADIENT,dp=1.9,param1=115,param2=23,minDist=20,minRadius=7,maxRadius=13)
	center_x = particles[0,:,0] 
	if (np.shape(center_x)[0]!=61):
		particles =cv.HoughCircles(equ,cv.cv.CV_HOUGH_GRADIENT,dp=2.1,param1=90,param2=25,minDist=20,minRadius=7,maxRadius=13)
	particles =np.uint16(np.around(particles))
        return particles[0,:,0],particles[0,:,1]  #(x,y)

                                                      
def orientation(input_img):
	contours,hierarchy=cv.findContours(input_img, 1, 2)
	count=0
	ellipsex,ellipsey,ellipse_angle=np.arange(0,61),np.arange(0,61),np.arange(0,61)
	for i in range(0,np.shape(contours)[0]):
		cntr=contours[i]
		area=cv.contourArea(cntr)	
		if np.shape(cntr)[0] >= 5 and area < 180 and area>50:	
			ellipse = cv.fitEllipse(cntr)
			(x,y)=ellipse[0]
			angle=ellipse[2]
			ellipsex[count],ellipsey[count]=x,y
			ellipse_angle[count]=angle
			count=count+1
	return np.around(ellipsex),np.around(ellipsey),ellipse_angle


#=======================================================================================
#           Functions End here
#=======================================================================================
t=np.ones(61)
name_begin='frame_'
ext='.jpg'
success=0
for j in range(0,35963):#total=35964,next run from 10000 to 25000 and then 25000 to 35964
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

	frame = np.zeros(np.shape(img_gray), np.uint8)
	cv.circle(frame,(centerx,centery), radius-8, (1), -1)			
	#frame=findframe(img_gray)                            # ROI gray scale img
	                                               # Equalization to enhance contrast
	img_r = img[:,:,2]
	img_g = img[:,:,1]
	r_g=(img_r-img_g)*frame+50
	img_g=img_g*frame 
	thresh=cv.threshold(r_g,150,255,cv.THRESH_BINARY)[1]
	kernel=np.ones((3,3))	
	#dilation=cv.dilate(thresh,kernel,iterations=1)
	particle_x,particle_y=particle_position(img_g)
	if(np.shape(particle_x)[0]!=61):
		continue
	success=success+1
	ellipse_x,ellipse_y,ellipse_orient=orientation(thresh)    # Image to be sent for ellipse detection
	z=pd.DataFrame(np.array([particle_x,particle_y,ellipse_x,ellipse_y,ellipse_orient]))	
	#z=list(zip(particle_x,particle_y,ellipse_x,ellipse_y,ellipse_orient))
	with open('data_re.csv','a') as f:			
		z.to_csv(f,header=False,index=False)
	

end=time.clock()
print(end-start)
print("framed stored",success)
cv.destroyAllWindows()
