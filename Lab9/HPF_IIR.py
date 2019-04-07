High Pass Filter using IIR   

import numpy as np
import cmath as cm
import math
import matplotlib.pyplot as plt
del_p=0.6
del_s=0.1
w_s=0.35*np.pi
w_p=0.7*np.pi
T=0.1
j=cm.sqrt(-1)
wo_p=(2/T)*(np.tan(w_p/2))
print('omega_p',wo_p)
wo_s=(2/T)*(np.tan(w_s/2))
print('omega_s',wo_s)
d_s=1/(del_s**2)
d_p=1/(del_p**2)
sq=np.sqrt((d_s-1)/(d_p-1))

wo_s1=wo_p/wo_s
wo_p1=wo_p/wo_p
x=wo_s1/wo_p1

#order
N_o=(math.log(sq,10))/(math.log(x,10))
N=math.ceil(N_o)
print('N',N)
a=1/(2*N)
#omega_c value using butterworth approximation
w_c=(wo_s1)/((d_s-1)**a)
print(w_c)

#b_k
w=np.linspace(0,np.pi,1000)
print('w',w)
z=np.exp((j*w))
print('z',z)
s=(2/T)*((1-(1/z))/(1+(1/z)))
s_dash=wo_p/s
print('s_dash',s_dash)

k=1
b_k=2*(np.sin((2*k-1)*np.pi/(2*N)))
print('b_k',b_k)
#H(s) filter

Hs_dash=((w_c)**N)/((s_dash**2)+b_k*w_c*s_dash+(w_c**2))
print('Hs_dash',Hs_dash)

plt.plot(w,abs(Hs_dash))
plt.show()
