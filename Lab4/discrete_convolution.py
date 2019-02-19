import numpy as np
from matplotlib import pyplot as plt
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
h=np.array(input("enter"))
n=len(x)
#functoin defined above
print(convolute(x,h)) 

#predefined function
print(np.convolve(x,h))
