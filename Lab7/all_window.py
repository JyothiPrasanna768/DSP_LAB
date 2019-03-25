import numpy as np
import matplotlib.pyplot as plt

M=31
n=np.linspace(0,M-1)
#balckman
whn=0.42-0.5*np.cos((2*np.pi*n)/(M-1))+0.08*np.cos((4*np.pi*n)/(M-1))
#hamming
hn=0.54-0.46*np.cos((2*np.pi*n)/(M-1))
#hanning
hn1=0.5-0.5*np.cos((2*np.pi*n)/(M-1))
#traingular
n1=np.arange(0,M-1)
hn2=1-(2*(abs((n-(M-1)*0.5))/(M-1)))
#rectangular
n2=np.arange(0,M-1)
hn3=np.ones(M-1)
plt.plot(n,whn,'r',n,hn,'b',n,hn1,'y')
#,n1,hn2,'g',n2,hn3,'black'
plt.show()
