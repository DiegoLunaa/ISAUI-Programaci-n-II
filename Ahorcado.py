import random

caracteres_aceptados = "abcdefghijklmnñopqrstuvwxyz"

palabras = ['pelota', 'cancha', 'partido', 'gol']

# Elijo una palabra al azar de la lista ya predefinida
palabra_random = random.choice(palabras)

# Oculto la palabra
palabra_oculta = ["_" for _ in palabra_random]

intentos = 7

input("¡Juego del ahorcado!\nREGLAS Y CONDICIONES...\n- Tendrás 7 intentos, cada error te descontará 1.\n- Deberás escribir una letra por intento y no la puedes repetir.\n- Podrás escribir una palabra pero si no aciertas perderás.\nPresiona Enter para comenzar... ")

while True:
    # Muestro la cantidad de letras ocultas y la separo en espacios 
    print("\nPalabra: ", " ".join(palabra_oculta))
    print("Intentos restantes: ", intentos)

    letra_ingresada = input("Ingresar letra elegida: ").lower()

    # Opción por si el jugador elige una palabra 
    if len(letra_ingresada) > 1:
        
        if letra_ingresada == palabra_random:
            print("\n¡Felicitaciones! Has adivinado la palabra.\nLa palabra oculta era: ", palabra_random.capitalize())
            break
        else: 
            print("GAME OVER\nNo has adivinado la palabra y has perdido.")
            break

    
    # Aviso al jugador de qué el elemento ingresado no es válido
    if letra_ingresada not in caracteres_aceptados:
        print("\n---------¡¡¡Has ingresado un caracter no aceptado. Recuerda que solo se aceptan letras!!!---------\n---------¡¡¡Has ingresado un caracter no aceptado. Recuerda que solo se aceptan letras!!!---------")
        continue
    
    # Si la letra es correcta se le avisa y se muestra, si no pierde un intento
    elif letra_ingresada in palabra_random:
        print("La letra es correcta")
        for i in range(len(palabra_random)):
            if palabra_random[i] == letra_ingresada:
                palabra_oculta[i] = letra_ingresada

    else:
        print("La letra es incorrecta")
        intentos -= 1
    # Cuando ya no hay palabras ocultas termina el juego
    if "_" not in palabra_oculta:
        print("\n¡Felicitaciones! Has adivinado la palabra.\nLa palabra oculta era: ", palabra_random.capitalize())
        break

    if intentos == 0:
        print("GAME OVER\nTu número de intentos es 0.")
        break

