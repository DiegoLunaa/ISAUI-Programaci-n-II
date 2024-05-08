# Ejercicio 7: Juego de Adivinar el Número 
# Desarrolla un juego en el que el programa selecciona aleatoriamente un número entre 1 y 100 y el jugador debe adivinarlo. 
# El programa debe proporcionar pistas al jugador si el número ingresado es demasiado alto o demasiado bajo.
# El juego debe continuar hasta que el jugador adivine correctamente el número.

import random



numeroR = random.randint(1, 100)

while True:
    numero = int(input("Adivina el número entre el 1 y el 100: "))
    if numero == numeroR:
        print("Has adivinado el número, ¡felicitaciones!")
        break
    elif numero > numeroR:
        print("El número es más bajo")
    elif numero < numeroR:
        print("El número es más alto")
    else:
        print("Número equivocado")
    

