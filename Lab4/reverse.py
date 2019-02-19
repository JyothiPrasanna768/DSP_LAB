import numpy as np
n=int(input("ENTER "))
y=[]
for i in range(0,n,1):
	a=input("enter")
	y.append(a)
x=[]
for i in range(0,n,1):
	a=y[n-i-1]
	x.append(a)
print(x)	
