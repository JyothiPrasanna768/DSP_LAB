import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
#fs,data=wav.read('prasanna.wav')
fs1,d8k=wav.read('/home/rgukt/Desktop/prasanna.wav')
print(fs1,len(d8k))
print(d8k)
t=np.arange(0,len(d8k)/fs1,1.0/fs1)
plt.plot(d8k)
plt.show()
wav.write('prasu_slow.wav',fs1*0.5,d8k)  #expand
#wav.write('prasu_fast.wav',np.float(fs1*2),d8k)   #compress
