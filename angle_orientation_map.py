
import numpy as np
import pandas as pd
import time
import os
start=time.clock()

#os.chdir('/home/shashank/Documents/ABP/Videos/Video_0111/Images_0111')
df1=pd.read_csv("circle_ellipse_map.csv")
df2=df1.as_matrix()
#d=np.zeros(61)
#i=0
row=0
while(row<164585):
	c_x=df2[row]
	c_y=df2[row+1]
	e_x=df2[row+2]
	e_y=df2[row+3]
	o_c=df2[row+4]
	#o_e_0_90=o_e<180 
	#o_e_90_180=o_e>180
	diff_y=c_y-e_y>0
	diff_x=c_x-e_x>0
	#diff_y_0=np.where(o_e==90)[0]
	#diff_180=np.where(o_e==180)[0]
	#for i in range(len(o_e)):
	#	if(o_e[i]==90):
#			continue
#		if(o_e_0_90[i]==True and diff_x[i]==True):
#			o_e[i]=o_e[i]+180
#			continue
#		if(o_e_90_180[i]==True and diff_y[i]==True):
#			o_e[i]=o_e[i]-180
#			continue
#	for i in range(len(diff_y_0)):
#		if(diff_x[diff_y_0[i]]==True):
#			o_e[diff_y_0[i]]=o_e[diff_y_0[i]]+180
#		
#	for i in range(len(diff_180)):
#		if(diff_x[diff_180[i]]==True):
#			o_e[diff_180[i]]=o_e[diff_180[i]]-180
	for i in range(len(o_c)):
		if (o_c[i]>=0 and o_c[i]<45):
			if(diff_x[i]==False):
				o_c[i]=o_c[i]+270
			if(diff_x[i]==True):
				o_c[i]=90+o_c[i]
			continue
		if(o_c[i]>=45 and o_c[i]<=90):
			if(diff_y[i]==True):
				o_c[i]=o_c[i]+90
			if(diff_y[i]==False):
				o_c[i]=270+o_c[i]
			continue
		if(o_c[i]>90 and o_c[i]<=135):
			if(diff_y[i]==True):
				o_c[i]=o_c[i]+90
			if(diff_y[i]==False):
				o_c[i]=o_c[i]-90
			continue
		if(o_c[i]>135 and o_c[i]<180):
			if(diff_x[i]==False):
				o_c[i]=o_c[i]+90
			if(diff_x[i]==True):
				o_c[i]=o_c[i]-90
	z=pd.DataFrame(np.array([c_x,c_y,o_c]))
	row=row+5
	#print(z)
	with open('angle_orientation_map_test.csv','a') as f:			
		z.to_csv(f,header=False,index=False)
	
end=time.clock()
print(end-start)

