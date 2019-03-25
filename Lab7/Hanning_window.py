import numpy as np
import matplotlib.pyplot as plt
M=31
n=np.linspace(0,M-1)
whn=0.5-0.5*np.cos((2*np.pi*n)/(M-1))
plt.stem(n,whn)
plt.show()
