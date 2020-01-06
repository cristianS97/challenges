"""
Escribir un script que escriba el siguiente patron

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6

para un número n
"""

try:
    n = int(input('Ingrese número de pisos: '))
    for i in range(1, n+1):
        for num in range(i):
            print(i, end=' ')
        print()
except ValueError:
    print('Se necesita ingresar un valor númerico')
finally:
    print('\nFin del programa')