# Inventario de productos : Escribe una función que recibe un diccionario donde las claves
# son los nombres de los productos y los valores son listas de precios históricos de esos productos.
# La función debe devolver un nuevo diccionario donde las claves son los nombres de los productos
# y los valores son el precio promedio de cada producto.
def inventario(diccionario):
    diccionario_promedio = {}
    for clave, valor in diccionario.items():
        promedio = sum(valor) / len(valor)
        diccionario_promedio[clave] = promedio
    return diccionario_promedio

diccionario = {
    "Tomate": [100, 200, 300],
    "Naranja": [300, 100, 300]

}
diccionario_promedio = inventario(diccionario)
print(diccionario_promedio)
