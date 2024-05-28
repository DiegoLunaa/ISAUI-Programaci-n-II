# Diccionario de frecuencias: Escribe una función que reciba una lista de palabras y
# devuelva un diccionario con la frecuencia de cada palabra.
def frecuencia_palabras(lista):
    diccionario_frecuencias = {}
    for i in lista:
        if i in diccionario_frecuencias:
            diccionario_frecuencias[i] += 1
        else:
            diccionario_frecuencias[i] = 1
    return diccionario_frecuencias

lista = ["Juan", "Pablo", "Juan", "Agustín", "José", "Agustín", "Pedro"]

diccionario = frecuencia_palabras(lista)

print(diccionario)