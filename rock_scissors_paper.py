# Se importa el modulo choice del pauqete random para hacer la selección aleatoria de la jugada
from random import choice
# Importamos os para limpiar la consola
import os

# Declaramos las vaiables con las opciones ara la cpu
options = ['r', 'p', 's']
# Texto a mostrar al momento de dar a elegir una opción
text = "r - Rock\np - Paper\ns - Scissors\n\nWhat is your choice >"
# Variable en donde se almacenara el puntaje
scores = {'player' : 0, 'CPU' : 0}
# Variable para poder mostrar la opción seleccionada
equivalents = {'r': 'Rock', 's': 'Scissors', 'p': 'Paper'}

# Inicio del programa
while True:
    os.system('cls')
    # Preguntamos si quiere una partida
    answer = input('Do you want to play? (y/n): ')[0].lower()
    # Terminamos la ejecución del programa si no quiere jugar
    if answer == 'n':
        break
    # Recibimos la opción a elegir por parte del jugador
    answer = input(text)[0].lower()

    # Seleccionamos de manera aleatoria una opción para la cpu
    cpu = choice(options)

    # Imprimimos las opciones seleccionadas
    print(f'\nPlayer: {equivalents[answer]}\nCPU: {equivalents[cpu]}\n\n')

    # Imprimimos al ganador o el empate en caso de que se de
    if cpu == 'r' and answer == 's':
        print('CPU win this game')
        scores['CPU'] += 1
    elif cpu == 'r' and answer == 'p':
        print('Player win this game')
        scores['player'] += 1
    elif cpu == 'r' and answer == 'r':
        print('Tie')

    elif cpu == 'p' and answer == 's':
        print('Player win this game')
        scores['player'] += 1
    elif cpu == 'p' and answer == 'p':
        print('Tie')
    elif cpu == 'p' and answer == 'r':
        print('CPU win this game')
        scores['CPU'] += 1

    elif cpu == 's' and answer == 's':
        print('Tie')
    elif cpu == 's' and answer == 'p':
        print('CPU win this game')
        scores['CPU'] += 1
    elif cpu == 's' and answer == 'r':
        print('Player win this game')
        scores['player'] += 1

    input('Press enter to continue...')

# Borramos la consola para mostrar los resultados
os.system('cls')

# Extraemos los puntajes para hacer uso de ellos
player_points = scores['player']
cpu_points = scores['CPU']

# Imprimimos los puntajes por pantalla
print(f'Player: {player_points}')
print(f'CPU: {cpu_points}')
print(end='\n')

# Indicamos al ganador o empate del juego
if player_points == cpu_points:
    print('A tie has ocurred')
elif player_points > cpu_points:
    print('Player wins')
else:
    print('CPU wins')