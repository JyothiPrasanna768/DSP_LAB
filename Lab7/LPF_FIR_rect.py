#Low pass FIR filter using windows technique
#Rectangular window 
import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
import math

M=31
#n=np.linspace(0,1,M-1)
#w=((np.sin(n))**2) +((np.cos(n))**2)
n=np.arange(0,M-1)
w=np.ones(M-1)
plt.stem(n,w)
plt.show()

#wc=math.pi/4.0
#-100<n<=100
