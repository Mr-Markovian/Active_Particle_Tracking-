import numpy as np
import pandas as pd
import time
import os
start=time.clock()

#os.chdir('/home/shashank/Documents/ABP/Videos/Video_0111/Images_0111')
df1=pd.read_csv("angle_orientation_map_test.csv")
df2=df1.as_matrix()
c_x_temp=df2[0]
c_y_temp=df2[1]
o_c_temp=df2[2]
z=pd.DataFrame(np.array([c_x_temp,c_y_temp,o_c_temp]))
with open('particle_frame_map.csv','a') as f:			
		z.to_csv(f,header=False,index=False)
i=3
while(i<164585):#2917):
	c_x_o=df2[i]
	c_y_o=df2[i+1]
	o_c_o=df2[i+2]
	c_x_n,c_y_n,o_c_n=np.zeros(61),np.zeros(61),np.zeros(61)
	for j in range(61):
		d=(c_x_o-c_x_temp[j])**2+(c_y_o-c_y_temp[j])**2
		ind=np.argmin(d)
		c_x_n[j]=c_x_o[ind]
		c_y_n[j]=c_y_o[ind]
		o_c_n[j]=o_c_o[ind]	
	z=pd.DataFrame(np.array([c_x_n,c_y_n,o_c_n]))
	c_x_temp,c_y_temp,o_c_temp=c_x_n,c_y_n,o_c_n
	i=i+3
	with open('particle_frame_map_test.csv','a') as f:			
		z.to_csv(f,header=False,index=False)
	
end=time.clock()
print(end-start)
