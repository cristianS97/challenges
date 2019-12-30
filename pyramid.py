def piramide(n):
    for i in range(n):
        print(' ' * (n-i), end='')
        for j in range(2*i+1):
            if j % 2 == 0:
                print('*', end='')
            else:
                print('A', end='')
        print(end='\n')

n = int(input('Ingresa la cantidad de pisos: '))

piramide(n)
