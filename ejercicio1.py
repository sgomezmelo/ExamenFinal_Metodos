# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while'.
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.linspace(0,2.,10)
dx = x[1] - x[0]
fx = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])
primera_derivada = (fx[1:] - fx[:-1])/dx
x_pd = x[1:]

segunda_derivada = (primera_derivada[1:] - primera_derivada[:-1])/dx
xsd = x_pd[1:]

plt.figure()
plt.plot(xsd,segunda_derivada)
plt.savefig('segunda.png')





