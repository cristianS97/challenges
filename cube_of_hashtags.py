"""
    Escribir una función que escriba el siguiente patrón usando ciclos:

    ##########
    ##      ##  ==> espacios = 0; 3; 3; 0
    # #    # #  ==> espacios = 1; 2; 2; 1
    #  #  #  #  ==> espacios = 2; 1; 1; 2
    #   ##   #  ==> espacios = 3; 0; 0; 3
    #   ##   #  ==> espacios = 3; 0; 0; 3
    #  #  #  #  ==> espacios = 2; 1; 1; 2
    # #    # #  ==> espacios = 1; 2; 2; 1
    ##      ##  ==> espacios = 0; 3; 3; 0
    ##########
"""

print("# # # # # # # # # #")

for i in range(4):
    print("# ", end="")
    print("  " * i, end="")
    print("# ", end="")
    print("  " * (3 - i), end="")
    print("  " * (3 - i), end="")
    print("# ", end="")
    print("  " * i, end="")
    print("# ")

for i in range(4):
    print("# ", end="")
    print("  " * (3 - i), end="")
    print("# ", end="")
    print("  " * i, end="")
    print("  " * i, end="")
    print("# ", end="")
    print("  " * (3 - i), end="")
    print("# ")

print("# # # # # # # # # #")