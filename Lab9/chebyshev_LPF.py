#IIR Low Pass Filter 

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
N_o=math.acosh(sq)/math.acosh(x)
N=math.ceil(N_o)
print('N',N)

#epslon
E=math.sqrt(d_p-1)
print('Epslon',E)

#YN
a=math.sqrt(1+(1/(E**2)))+(1/E)
Y_N=1/2*(((a)**(1/N)) - (1/(a)**(1/N)))
print('Y_N',Y_N)

#b_k
k=1
b_k=2*Y_N*(np.sin((2*k-1)*np.pi/(2*N)))
print('b_k',b_k)

#c_k
c_k=(Y_N**2)+((np.cos((2*k-1)*np.pi/(2*N)))**2)
print('c_k',c_k)

#s
w=np.linspace(0,np.pi,100)
print('w',w)
z=np.exp((j*w))
print('z',z)
s=(2/T)*((1-(1/z))/(1+(1/z)))

#H_s
H_s=((1/np.sqrt(1+(E**2))*(wo_p**N)*c_k)/((s**2)+b_k*wo_p*s+(wo_p**2)*c_k))
print('H_s',H_s)
plt.plot(w,abs(H_s))
plt.show()
