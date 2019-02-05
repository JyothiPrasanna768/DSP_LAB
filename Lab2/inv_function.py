import numpy as np
import matplotlib.pyplot as plt
#x=int(input("x="))
#y=int(input("y="))
t=np.arange(-10,10,1)
z=np.arctan(t)
#z=np.arcsin(x/y)
#z=np.sinh(x/y)
#z=np.arctan(x/y)
#print(z)
plt.plot(t,z)
plt.show()
