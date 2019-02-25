import cmath as cm
import matplotlib.pyplot as plt
import numpy as np
def DFT(X):
	N=len(X) # size of x
	print(N)
	j=cm.sqrt(-1)
	x=[]
	i=3
	for n in range(N):
		sum=0
		for k in range(N):
			sum=sum+(X[k]*(cm.exp((j*2*cm.pi*n*k)/N)))
		x.append(sum/N)
	
	print(x)
	plt.subplot(1,2,1)
	plt.stem(np.abs(x))
	plt.title("magnitude of X[w]")
	plt.xlabel("frequency")
	plt.ylabel("|X[w]|")
	plt.subplot(1,2,2) 
	plt.stem(np.angle(x))
	plt.title("phase of X[w]")
	plt.xlabel("frequency")
	plt.ylabel("/_X[w]")
	return(x)

#N=int(input("enter no. of samples"))  #choose 8-point or n-point dft
X=np.array(input("enter values of x[n]"))
DFT(X)

plt.show()


