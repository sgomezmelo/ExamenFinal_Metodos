# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares y que pare de imprimir al encontrar un numero mayor a 800

import numpy as np

x = np.int_(np.random.random(100)*1000)

i = 0
while(x[i] <= 800):
    if(x[i]%2 != 0):
        print(x[i])
    i = i+1
    



