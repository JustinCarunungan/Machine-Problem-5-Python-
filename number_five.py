import matplotlib.pyplot as plt
import numpy as np
import math as m

n = np.arange(0,200)
x = np.sin((3*m.pi*n)/100)
x = eval(input('Please enter a value for x(n) : '))
y = np.zeros((x.shape))
#y = np.zeros(x)

for i in range(len(n)):
    if n[i]==0:
        y[i] = -1.5*x[i]+2*x[i+1]-0.5*x[i+2]
    elif n[i]<199:
        y[i] = 0.5*x[i+1]-0.5*x[i-1]
    else:
        y[i] = 1.5*x[i]-2*x[i-1]+0.5*x[i-2]
        
plt.plot(n,x,'g-',label='x')
plt.plot(n,y,'m-',label='y')
plt.title('Plot of x(n) and y(n)')
plt.xlabel('n')
plt.xlim(0,200)
plt.ylim(-1,1)
plt.legend()
plt.show()





