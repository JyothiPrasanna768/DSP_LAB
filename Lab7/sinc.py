import numpy as np
import matplotlib.pyplot as plt

wc=np.pi/4
n=np.arange(-50,51)
m=n*0.25
#hn=np.sin(wc*n)/(np.pi*n)
hn=(np.sinc(m))*0.25
plt.stem(n,hn)
plt.show()
