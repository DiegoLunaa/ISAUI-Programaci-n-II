# Merge de diccionarios: Crea una función que tome dos diccionarios y devuelva uno
# nuevo que combine ambos (en caso de conflicto, usa los valores del segundo
# diccionario).
def combinar_diccionarios(diccionario1, diccionario2):
    diccionario_nuevo = diccionario1 | diccionario2
    return diccionario_nuevo
diccionario_n = {}
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

diccionario2 = {
    "nombre": "Pedro",
    "edad": 35,
    "ciudad": "Madrid"
}

diccionario_n = combinar_diccionarios(diccionario, diccionario2)
print(diccionario_n)