import numpy as np
import pandas as pd
import time
import os
start=time.clock()

#os.chdir('/home/shashank/Documents/ABP/Videos/Video_0111/Images_0111')
df1=pd.read_csv("data_re.csv")
df2=df1.as_matrix()
i=1
while(i<164585):#2917):
	c_x=df2[i]
	c_y=df2[i+1]
	e_x=df2[i+2]
	e_y=df2[i+3]
	o_e=df2[i+4]
	#o_e=np.radians(o_e)
	o_c,e_x_n,e_y_n=np.zeros(61),np.zeros(61),np.zeros(61)
	for j in range(61):
		d=(e_x-c_x[j])**2+(e_y-c_y[j])**2
		ind=np.argmin(d)
		o_c[j]=o_e[ind]
		e_x_n[j]=e_x[ind]
		e_y_n[j]=e_y[ind]
	z=pd.DataFrame(np.array([c_x,c_y,e_x_n,e_y_n,o_c]))
	with open('circle_ellipse_map.csv','a') as f:			
		z.to_csv(f,header=False,index=False)
	i=i+5

end=time.clock()
print(end-start)
