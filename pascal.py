"""
Crear un programa que muestre el triangulo de pascal de n pisos, resiviendo n como parametro
"""

# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1

"""
Formula:
    N                N!
    --    =   -----------------
    K           K! * (N - K)!

    N: Todos los números enteros positivos (0, 1, 2, 3, 4, 5, ..., infinito)
    K: Todos los enteros positivos hasta N (0, 1, 2, 3, 4, ..., N)

    0! = 1
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n+1):
            resultado *= i
    return resultado

def pascal(n):
    pisos = list()
    for i in range(n):
        piso = list()
        for k in range(i+1):
            numerador = factorial(i)
            denominador = (factorial(k) * factorial(i-k))
            numero = numerador / denominador
            piso.append(int(numero))
        pisos.append(piso)
    return pisos

try:
    n = int(input("Ingrese la cantidad de pisos que desea: "))
    triangulo = pascal(n+1)

    for piso in triangulo:
        for elemento in piso:
            print(elemento, end="  ")
        print(end="\n")
except ValueError:
    print("Ingrese un valor númerico")
finally:
    print("\nFin del programa")