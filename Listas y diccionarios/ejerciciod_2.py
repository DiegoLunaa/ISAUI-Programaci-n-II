# Diccionario inverso: Escribe una función que tome un diccionario y devuelva uno
# nuevo que invierta las claves y los valores.
def invertir_diccionario(diccionario):
    diccionario_nuevo = {}
    for clave, valor in diccionario.items():
        diccionario_nuevo[valor] = clave
    return diccionario_nuevo

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
diccionario_reves = {}

diccionario_reves = invertir_diccionario(diccionario)
print(diccionario_reves)