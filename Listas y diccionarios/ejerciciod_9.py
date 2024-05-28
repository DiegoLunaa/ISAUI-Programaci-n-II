# Actualizar diccionario: Escribe una función que tome un diccionario y una lista de
# tuplas (clave, valor) y actualice el diccionario con esas tuplas.
def actualizar_diccionario(diccionario, tupla):
    for clave, valor in tupla:
        diccionario[clave] = valor

    return diccionario
diccionario = {
    "Color 1": "Azul",
    "Color 2": "Rojo",
    "Color 3": "Amarillo"
}
tupla = [("Color 2", "Azul"), ("Color 3", "Violeta"), ("Color 4", "Naranja")]
diccionario = actualizar_diccionario(diccionario, tupla)
print(diccionario)