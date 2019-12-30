# Crear un programa que reciba el tamaño de un range y cree una lista con todos los números que sean pares y que su
# antecesor sea multiplo de 3

n = int(input('Ingrese el tamaño del objeto range: '))

lista = [x for x in range(n) if x % 2 == 0 and (x-1) % 3 == 0]

print(lista)