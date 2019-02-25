import numpy as np
import cmath as cm
import matplotlib.pyplot as plt 

def DFT(x,N):
	i=len(x) # size of x
	print(i)
	j=cm.sqrt(-1)
	X=[]
	#w=np.linspace(0,2*np.pi,N)
	for k in range(N):
		sum=0
		for n in range(i):
			sum=sum+(x[n]*(cm.exp(((-j)*2*cm.pi*n*k)/N)))
		X.append(sum)
	
	print(X)
	plt.subplot(1,2,1)
	plt.stem(np.abs(X))
	plt.title("magnitude of X[w]")
	plt.xlabel("frequency")
	plt.ylabel("|X[w]|")
	plt.subplot(1,2,2) 
	plt.stem(np.angle(X))
	plt.title("phase of X[w]")
	plt.xlabel("frequency")
	plt.ylabel("/_X[w]")
	return(X)

N=int(input("enter no. of samples"))  #choose 8-point or 4-point dft

#sine wave generate
t=np.arange(-10,10,0.1)
x=np.sin(2*np.pi*t)

DFT(x,N)

plt.show()


