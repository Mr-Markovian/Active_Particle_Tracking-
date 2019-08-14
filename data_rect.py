import numpy as np
import pandas as pd
import time
import os
start=time.clock()

#os.chdir('/home/shashank/Documents/ABP/Videos/Video_0111')
df1=pd.read_csv('particle_frame_map_test.csv')
df2=df1.as_matrix()
c_x_temp=df2[0]
c_y_temp=df2[1]
o_c_temp=df2[2]
flag=np.zeros(61)
z=pd.DataFrame(np.array([c_x_temp,c_y_temp,o_c_temp]))
with open('rect_particle_frame_map_test.csv','a') as f:			
		z.to_csv(f,header=False,index=False)
i=3
while(i<164585):#2917):
	c_x_o=df2[i]
	c_y_o=df2[i+1]
	o_c_o=df2[i+2]
	
	for j in range(61):
		if(np.abs(o_c_temp[j]-o_c_o[j])>90 and np.abs(o_c_temp[j]-o_c_o[j])<270):
	
			
			if(o_c_temp[j]-o_c_o[j]>90):			
				o_c_o[j]=o_c_o[j]+180
			
			if(o_c_o[j]-o_c_temp[j]>90):
				o_c_o[j]=o_c_o[j]-180
				
		if(o_c_o[j]>360):
			o_c_o[j]=o_c_o[j]-360
	z=pd.DataFrame(np.array([c_x_o,c_y_o,o_c_o]))
	c_x_temp,c_y_temp,o_c_temp=c_x_o,c_y_o,o_c_o
	i=i+3
	with open('rect_particle_frame_map_test.csv','a') as f:			
		z.to_csv(f,header=False,index=False)
	
end=time.clock()
print(end-start)
