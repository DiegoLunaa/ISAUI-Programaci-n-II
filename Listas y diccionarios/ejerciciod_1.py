# Contar letras: Escribe una función que reciba una cadena y devuelva un diccionario
# con la frecuencia de cada letra en la cadena.
def cadena_a_diccionario(lista):
    diccionario = {}
    for i in lista:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    return diccionario

cadena = "asdasdas"
diccionario = {}

diccionario = cadena_a_diccionario(cadena)
print(diccionario)
