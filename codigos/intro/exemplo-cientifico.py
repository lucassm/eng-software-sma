from numpy import arange, sin, exp
import matplotlib.pyplot as plt 


x = arange(0, 25, 0.01)
y = sin(x) * exp(-0.1*x)

plt.plot(x, y, 'r-')
plt.grid(True)
plt.title('Decaimento exponencial')
plt.xlabel('Tempo (s)')
plt.ylabel('Tensao (V)')
plt.show()