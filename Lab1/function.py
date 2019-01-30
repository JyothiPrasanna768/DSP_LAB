import numpy as np
import math
def sigmoid(x):
	y=1/(1+math.exp(x))
	return(y)
x=int(input("enter a number"))
z=sigmoid(x)
print(z)
