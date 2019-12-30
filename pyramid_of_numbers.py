"""
    Escribir un código que escriba el siguinte patron según un numero dado.

    ej: n=6

    1 7 12 16 19 21
     2 8 13 17 20
      3 9 14 18
       4 10 15
        5 11
         6
"""

def inverted_pyramid(n):
    for i in range(n):
        number = i + 1
        print(' ' * i, end='')
        for j in range(n-i):
            print(number, end=' ')
            number += (n-j)
        print(end='\n')

inverted_pyramid(6)