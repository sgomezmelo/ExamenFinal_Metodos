#Ejercicio4
# 'y' es una senal en funcion del tiempo 't' con las unidades descritas en el codigo.
# a. Grafique la senal en funcion del tiempo en la figura 'senal.png' ('y' vs. 't')
# b. Calule la transformada de Fourier (sin utilizar funciones de fast fourier transform) y
# grafique la norma de la transformada en funcion de la frecuencia (figura 'fourier.png')
# c. Lleve a cero los coeficientes de Fourier con frecuencias mayores que 10000 Hz y calcule 
# la transformada inversa para graficar la nueva senal (figura 'filtro.png')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


n = 512 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 128 ) #128 samples per frequency
t = np.linspace( 0, (n-1)*dt, n) 
y = np.sin(2 * np.pi * f * t) + np.cos(2 * np.pi * f * t * t)
noise = 1.4*(np.random.rand(n)+0.7)
y  =  y + noise

plt.figure()
plt.plot(t,y)
plt.savefig('senal.png')

fourier = np.zeros(n)
fourier_Re = np.zeros(n)
fourier_Im = np.zeros(n)

for i in range(n):
    suma_RE = 0
    suma_IM = 0
    for j in range(n):
        suma_RE += y[j]*np.cos(-2*np.pi*i*j/n)/n
        suma_IM += y[j]*np.sin(-2*np.pi*i*j/n)/n
    fourier[i] = np.sqrt(suma_RE**2 + suma_IM**2)
    fourier_Re[i] = suma_RE
    fourier_Im[i] = suma_IM

omega = np.array(range(n))/(n*dt)

plt.figure()
plt.plot(omega,fourier)
plt.savefig('fourier.png')

RE_filt = np.zeros(n)
IM_filt = np.zeros(n)

for i in range(n):
    w = omega[i]
    if(w <= 10):
        RE_filt[i] = fourier_Re[i]
        IM_filt[i] = fourier_Im[i]


filtro = np.zeros(n)
for i in range(n):
    suma = 0
    for j in range(n):
        suma += (RE_filt[j]+1j*IM_filt[j])*np.exp(2*np.pi*i*j*1j/n)/n
    filtro[i] = np.real(suma)

print(filtro)
plt.figure()
plt.plot(t,filtro)
plt.savefig('filtro.png')

    
        
    
