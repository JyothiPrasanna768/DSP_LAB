import cmath as cm
from matplotlib import pyplot as plt
import numpy as np

def dtft(x,N):
    xw=[]
    j=cm.sqrt(-1)
    n=len(x)
    w=np.linspace(0,2*np.pi,N)
    for i in range(0,N):
        sum=0
	w_temp=w[i]
        for k in range(0,n):
            sum=(sum+(x[k]*np.exp((-j)*w_temp*k)))

        xw.append(sum)
      #xw=sum
    plt.subplot(1,2,1)
    plt.plot(w,np.abs(xw))
    plt.title("magnitude of X[w]")
    plt.xlabel("frequency")
    plt.ylabel("|x[w]|")
    plt.subplot(1,2,2) 
    plt.plot(w,np.angle(xw))
    plt.title("phase of X[w]")
    plt.xlabel("frequency")
    plt.ylabel("/_x[w]")
    return(xw)
x=np.array(input("enter x[n] value"))
dtft(x,10)

plt.show()
