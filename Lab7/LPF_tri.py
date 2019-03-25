import cmath as cm
from matplotlib import pyplot as plt
import numpy as np

def dtft(hn,N):
    xw=[]
    j=cm.sqrt(-1)
    n=len(hn)
    n1=np.arange(0,31)
    w=np.linspace(0,np.pi,30)
    whn=(1-(2*(abs((n1-(30)*0.5))/(30))))
    for i in range(0,30):
        sum=0
        w_temp=w[i]
        for k in range(0,n):
            sum=(sum+(hn[k]*np.exp((-j)*w_temp*k)))

        xw.append(sum)

    plt.plot(w,np.abs(xw))
    plt.title("magnitude of X[w]")
    plt.xlabel("frequency")
    plt.ylabel("|x[w]|")
    return(xw)
n=np.arange(0,31)
#w=1-(2*(abs((n-(M-1)*0.5))/(M-1)))
m=n*0.25
hn=(np.sinc(m))*0.25
dtft(hn,40)

plt.show()
