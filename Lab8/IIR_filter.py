import numpy as np
import cmath as cm
import math
import matplotlib.pyplot as plt
del_p=0.6
del_s=0.1
w_p=0.35*np.pi
w_s=0.7*np.pi
T=0.1
j=cm.sqrt(-1)
wo_p=(2/T)*(np.tan(w_p/2))
print('omega_p',wo_p)
wo_s=(2/T)*(np.tan(w_s/2))
print('omega_s',wo_s)
d_s=1/(del_s**2)
d_p=1/(del_p**2)
sq=np.sqrt((d_s-1)/(d_p-1))
x=wo_s/wo_p

#order
N_o=(math.log(sq,10))/(math.log(x,10))
N=math.ceil(N_o)
print(N)
a=1/(2*N)

#omega_c value using butterworth approximation
wo_c=(wo_s)/((d_s-1)**a)
print(wo_c)

#b_k
w=np.linspace(0,np.pi,100)
print('w',w)
z=np.exp((j*w))
print('z',z)
s=(2/T)*((1-(1/z))/(1+(1/z)))
k=1
b_k=2*(np.sin((2*k-1)*np.pi/(2*N)))
print('b_k',b_k)

#H(s) filter
H_s=((wo_c)**N)/((s**2)+b_k*wo_c*s+(wo_c**2))
print('H_s',H_s)
plt.plot(w,abs(H_s))
plt.show()
