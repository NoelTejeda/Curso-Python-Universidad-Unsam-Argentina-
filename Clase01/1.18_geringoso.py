'''Ejercicio 1.18: Geringoso rústico

Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.'''

cadena = 'geringoso'
cadena2 = ''

for c in cadena:
     print (c)
     cadena2 = cadena2 + c
   
     if c == 'a':
          cadena2 = cadena2 + 'pa'
     elif c == 'e':
          cadena2 = cadena2 + 'pe'
     elif c == 'i':
          cadena2 = cadena2 + 'pi'
     elif c == 'o':
          cadena2 = cadena2 + 'po'
     elif c == 'u':
          cadena2 = cadena2 + 'pu'

print (cadena2)