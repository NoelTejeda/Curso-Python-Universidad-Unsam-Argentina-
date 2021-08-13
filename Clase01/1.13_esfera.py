'''Ejercicio 1.13: El volumen de una esfera

En tu directorio de trabajo de esta clase, escribí un programa llamado esfera.py que le pida al usuario que ingrese por teclado el radio r de una esfera y calcule e imprima el volumen de la misma. Sugerencia: recordar que el volúmen de una esfera es 4/3 πr^3.

Finalmente, ejecutá el programa desde la línea de comandos para responder ¿cuál es el volumen de una esfera de radio 6? Debería darte 904.7786842338603.'''

print ('calculadora de radio de una esfera')
print (' ')

from math import pi
radio=int(input('Por favor indique el radio de la esfera:  '))
print(f'el volumen de la esfera es: {4/3 * pi * radio**3}')
