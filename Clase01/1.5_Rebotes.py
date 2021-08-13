'''  Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 de la altura desde la que cayó. Escribí un programa rebotes.py que imprima una tabla mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes.'''

rebote=0
altura=100

while rebote<10:
    rebote +=1
    altura=3/5*altura
    print(f'rebote {rebote} | , Mts altura: {round(altura,4)}')



''' sintax round: sirve para redondear tanto decimales se quieran: round (x, 2)    -donde x es el valor o la variable, 2 la cantidad de decimales. '''