# Diccionario de listas: Escribe una función que tome un diccionario donde los valores
# son listas y devuelva una lista que contenga todos los elementos de las listas del
# diccionario.
def diccionario_listas(diccionario):
    lista = []
    for clave, valor in diccionario.items():
        lista += valor
    return lista

diccionario = {
    "Nombres": ["Matias", "Pedro", "Martín"],
    "Edades": [10, 20, 30],
    "Deporte": ["Futbol", "Rugby", "Handball"]
}
lista = diccionario_listas(diccionario)
print(lista)
