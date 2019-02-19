import cmath as cm
from matplotlib import pyplot as plt
import numpy as np
import scipy.integrate as integrate
from scipy.integrate import quad
import scipy.special as special\

def integrand(w,x,e):
    return x[w]*e

def idtft(xw,N):
    x=[]
    j=cm.sqrt(-1)
    n=len(x)
    #w=np.linspace(0,2*np.pi,N)
    for i in range(0,n):
        sum=0
        for w in range(0,2*np.pi,1/N):
            x=X[k]
            e=np.exp(j*w*i)
            I=quad(integrand,0,2*np.pi,args=(x,e)

        x.append(sum)
      #xw=sum
    
    plt.plot(w,np.abs(x))
    return(xw)
xw=np.array(input("enter x[n] value"))
idtft(x,10)
plt.xlabel("frequency")
plt.ylabel("|x[w]|")
plt.show()
