# Filtrar diccionario: Escribe una función que reciba un diccionario y una lista de claves,
# y devuelva un nuevo diccionario solo con las claves especificadas.
def clave_esp(diccionario, lista):
    diccionario_nuevo = {}
    for i in lista:
        if i in diccionario.keys():
            diccionario_nuevo[i] = diccionario[i]
    return diccionario_nuevo
diccionario_nuevo = {}
lista = ["nombre", "ciudad"]
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
diccionario_nuevo = clave_esp(diccionario, lista)
print(diccionario_nuevo)