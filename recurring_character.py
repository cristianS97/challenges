"""
    Crear una función que reciba un string y devuelva el primer caracter que se repita,
    de no haber caracter que se repita, devolver un None
"""

def recurring_character(given_string):
	letters = {}
	for letter in given_string:
		if letter.upper() in letters:
			return letter
		else:
			letters[letter.upper()] = 1
	return None

cadena = "acBdccDe"

print(recurring_character(cadena))