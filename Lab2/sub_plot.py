import numpy as np
import matplotlib.pyplot as plt
t=np.arange(-10,10,0.1)
x=np.sin(2*np.pi*t)
x1=np.cos(2*np.pi*t)

fig = plt.figure()
ax1 = fig.add_subplot(1,3,1)
ax1.plot(t,x)
ax1=fig.add_subplot(2,3,2)
ax1.plot(t,x1)
plt.show()
