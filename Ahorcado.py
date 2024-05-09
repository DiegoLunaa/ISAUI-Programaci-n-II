import random

caracteres_aceptados = "abcdefghijklmnñopqrstuvwxyz"

palabras = [('p', 'e', 'l', 'o', 't', 'a'), ('c', 'a', 'n', 'c', 'h', 'a'), ('p', 'a', 'r', 't', 'i', 'd', 'o'), ('g', 'o', 'l')]

palabra_random = random.choice(palabras)

palabra_oculta = ["_" for _ in palabra_random]

palabra_elegida = "".join(palabra_random)

longitud_palabra = len(palabra_elegida)

intentos = 7

input("¡Juego del ahorcado!\nREGLAS Y CONDICIONES...\n- Tendrás 7 intentos, cada error te descontará 1.\n- Deberás escribir una letra por intento y no la puedes repetir.\n- Podrás escribir una palabra pero si no aciertas perderás.\nPresiona Enter para comenzar... ")

while True:
    print("\nPalabra: ", " ".join(palabra_oculta))

    print("Intentos restantes: ", intentos)

    letra_ingresada = input("Ingresar letra elegida: ").lower()

    if len(letra_ingresada) > 1:
        
        if letra_ingresada == palabra_elegida:
            print("\n¡Felicitaciones! Has adivinado la palabra.\nPalabra: ", palabra_elegida, "\nTu número de intentos restantes es: ", intentos)
            break
        else: 
            print("GAME OVER\nNo has adivinado la palabra y has perdido.")
            break

    

    if letra_ingresada not in caracteres_aceptados:
        print("\n---------¡¡¡Has ingresado un caracter no aceptado. Recuerda que solo se aceptan letras!!!---------\n---------¡¡¡Has ingresado un caracter no aceptado. Recuerda que solo se aceptan letras!!!---------")
        continue

    elif letra_ingresada in palabra_random:
        print("La letra es correcta")
        longitud_palabra -= 1
        for i in range(len(palabra_random)):
            if palabra_random[i] == letra_ingresada:
                palabra_oculta[i] = letra_ingresada

    else:
        print("La letra es incorrecta")
        intentos -= 1

    if "_" not in palabra_oculta:
        print("\n¡Felicidades! Has adivinado la palabra: ", palabra_elegida, "\nTu número de intentos restantes es ", intentos)
        break

    if intentos == 0:
        print("GAME OVER\nTu número de intentos es 0.")
        break
    

