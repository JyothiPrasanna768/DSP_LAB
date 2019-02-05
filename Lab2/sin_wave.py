import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,10,0.1)
x=np.sin(2*np.pi*t)
plt.plot(t,x,'green') # in continuous domain
#plt.stem(t,x)    # if you wanna print plot in discrete domain , this command is used
plt.title("Sinwave")
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.show()
