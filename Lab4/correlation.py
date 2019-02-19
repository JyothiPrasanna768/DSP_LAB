import numpy as np
from matplotlib import pyplot as plt

n=int(input("ENTER "))
y=[]
for i in range(0,n,1):
	a=input("enter")
	y.append(a)
h=[]
for i in range(0,n,1):
	a=y[n-i-1]
	h.append(a)
print(h)	

def convolute(x,h):
    n1=len(x)
    n2=len(h)
    print(n1,n2)
    y=[]
    for n in range(n1+n2-1):
          sum=0
          for k in range(n1):
             if n-k>=0 and n-k<=n2-1:
                   sum=sum+x[k]*h[n-k]
          y=np.append(y,sum)
    return y
x=np.array(input("enter"))
print(convolute(x,h))
print(np.convolve(x,h))
