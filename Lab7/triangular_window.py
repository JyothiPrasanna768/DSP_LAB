import numpy as np
import matplotlib.pyplot as plt

M=31
n=np.arange(0,M-1)
w=1-(2*(abs((n-(M-1)*0.5))/(M-1)))
plt.stem(n,w)
plt.show()
#print(abs(x))
