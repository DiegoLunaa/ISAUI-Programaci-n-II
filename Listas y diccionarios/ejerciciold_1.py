# Contar palabras en frases: Escribe una función que reciba una lista de frases y
# devuelva un diccionario donde las claves son las palabras y los valores son las
# frecuencias de esas palabras en todas las frases.
def contador_palabras(lista):
    diccionario = {}
    # El .join une todas las cadenas en una lista separadas por el argumento dado en " "
    palabras = " ".join(lista)
    # El split separa cada palabra en subcadenas
    palabras = palabras.split()

    for i in palabras:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    #  Sorted convierte el diccionario en una lista de tuplas (clave, valor) utilizando diccionario.items().
    #  Luego se usa el método lambda, el cual toma una variable como argumento (por ejemplo, clave_valor) 
    #  que representa cada tupla. La lambda accede al índice 1 (clave_valor[1]), que es el valor.
    #  Se usa reverse=True porque sorted ordena en orden ascendente por defecto.
    #  Finalmente, dict convierte la lista ordenada de tuplas de nuevo en un diccionario.

    diccionario_ordenado = dict(sorted(diccionario.items(), key = lambda clave_valor: clave_valor[1], reverse=True))
        
    return diccionario_ordenado


lista = ["Hola todo bien?", "Hola todo bien", "Hola soy Juan", "Un gusto Juan"]
diccionario = contador_palabras(lista)
print(diccionario)