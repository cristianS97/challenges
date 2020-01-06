"""
Write a program that print pattern like this:
    12345
    23451
    34512
    45123
    51234
"""
try:
    n = int(input('Ingrese un número: '))

    for j in range(n):
        for i in range(1+j, n+1):
            print(i, end=' ')
        for i in range(j):
            print(i+1, end=' ')
        print(end='\n')
except ValueError:
    print('El valor ingresado no es un número')
finally:
    print('\nFin del programa')