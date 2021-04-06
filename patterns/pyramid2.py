"""
Dado un número, generar una piramide como la del ejemplo
1
1 2
1 2 3
1 2 3 4
1 2 3
1 2
1
"""

def piramide(n):
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end=" ")
        print(end="\n")
    for i in range(n - 1):
        for j in range(n - (i + 1)):
            print(j + 1, end=" ")
        print(end="\n")

piramide(9)