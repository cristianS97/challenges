"""
    Crear una función que dado una lista de números y un valor, devuelva todas las parejas de números que
    sumen el valor dado, todos los numeros de la lista son enteros y pueden ser negativos

    ej:
	list = [1, 2, 2, 3, 4, 4, 6]
	sum = 8
	resp = [(2, 6), (2, 6), (4, 4)]
"""

def sum_verification(list_of_numbers, sum_to_verify):
    sums = []
    for i in range(len(list_of_numbers)):
        for j in range(i+1, len(list_of_numbers)):
            if(list_of_numbers[i] + (list_of_numbers[j]) == sum_to_verify):
                pair_sum = (list_of_numbers[i], list_of_numbers[j])
                sums.append(pair_sum)
    return sums

my_numbers = [1, 2, 2, 3, 4, 4, 6]
my_sum = 8

print(sum_verification(my_numbers, my_sum))