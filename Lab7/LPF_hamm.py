import cmath as cm
from matplotlib import pyplot as plt
import numpy as np

def dtft(hn,N):
    xw=[]
    j=cm.sqrt(-1)
    n=len(hn)
    w=np.linspace(0,np.pi,31)
    n1=np.arange(0,31)
    whn=(0.54-0.46*np.cos((2*np.pi*n1)/(30)))
    for i in range(0,31):
        sum=0
        w_temp=w[i]
        for k in range(0,n):
            sum=(sum+(hn[k]*np.exp((-j)*w_temp*k)))

        xw.append(sum)
    y=xw*whn
    plt.plot(w,np.abs(y))
    plt.title("magnitude of X[w]")
    plt.xlabel("frequency")
    plt.ylabel("|x[w]|")
    return(xw)
n=np.arange(0,31)

m=n*0.25
hn=(np.sinc(m))*0.25
dtft(hn,40)

plt.show()
