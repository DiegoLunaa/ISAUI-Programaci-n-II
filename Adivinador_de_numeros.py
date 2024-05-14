# Crea un juego que le pida al usuario que piense un número entre 1 y 100. 
# Luego, el programa debe intentar adivinar ese número utilizando la estrategia de búsqueda binaria. 
# En cada intento, el programa debe preguntar al usuario si el número a adivinar es mayor, 
# menor o igual al número propuesto por el programa. 
# El juego debe terminar cuando el programa adivine el número correcto.

import random
numero_maximo = 100
numero_minimo = 1

print("Este juego consiste en que pienses en un número del 1 al 100."
      "\nArenita tratará de adivinarlo, ella te preguntará si el número es mayor, menor o igual al que pensaste."
      "\nSí el número es mayor escribe 'mayor' o '>', si es menor, 'menor' o '<', y si es igual, 'igual' o '='. ")
input("Para comenzar presionar Enter..")

while True:
    
    nro = (numero_minimo + numero_maximo) // 2

    es = input("Arenita pregunta: ¿El número es mayor, menor, o igual a " + str(nro) + " ? ")
    
    if es == 'igual' or es == '=':
       print("Arenita exclama: Adiviné, el número en el que pensabas es", nro)
       break
    
    elif es == 'mayor' or es == '>':
       numero_minimo = nro + 1

    elif es == 'menor' or es == '<':
       numero_maximo = nro - 1

    
