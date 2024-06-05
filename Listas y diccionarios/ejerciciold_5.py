# Palabras por letra inicial : Escribe una función que tome una lista de
# palabras y devuelva un diccionario donde las claves son las letras iniciales
# de las palabras y los valores son listas de palabras que comienzan con esa letra.
def palabra_letra_inicial(lista):
    diccionario = {}
    for palabra in lista:
        primera_letra = palabra[0]
        if primera_letra not in diccionario:
            diccionario[primera_letra] = []
        diccionario[primera_letra].append(palabra)
    
    return diccionario

lista = ["Abigail", "Estito", "Juan", "Emanuel", "Auto", "Pedro"]


diccionario = palabra_letra_inicial(lista)
print(diccionario)