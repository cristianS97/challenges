try:
    pisos = abs(int(input("Ingrese la cantidad de pisos de la piramide: ")))
except ValueError:
    print("El valor ingresa no es un número, se usara el valor 3")
    pisos = 3

print("Manera clásica")

for piso in range(pisos):
    for espacio in range(pisos - piso):
        print(" ", end="")
    for asterisco in range((2*piso)+1):
        print("*", end="")
    print()

print("\n")

for piso in range(pisos):
    for espacio in range(piso + 1):
        print(" ", end="")
    for asterisco in range(((pisos * 2) - ((2 * piso) + 1))):
        print("*", end="")
    print()

print("\n")

print("Manera resumida")

for piso in range(pisos):
    print(" " * (pisos - piso), end="")
    print("*" * ((2*piso)+1))

print("\n")

for piso in range(pisos):
    print(" " * (piso + 1), end = "")
    print("*" * ((pisos * 2) - ((2 * piso) + 1)))

print("\n")

print("Diamante")

for piso in range(pisos):
    print(" " * (pisos - piso), end="")
    print("*" * ((2*piso)+1))

print("*" * ((2*pisos)+1))

for piso in range(pisos):
    print(" " * (piso + 1), end = "")
    print("*" * ((pisos * 2) - ((2 * piso) + 1)))

input("Presione una tecla para continuar...")
