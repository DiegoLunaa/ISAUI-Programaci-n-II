# Producto de elementos: Escribe una función que tome una lista de números y
# devuelva el producto de todos los elementos.
def producto(lista):
    producto = 1
    for i in lista:
        producto *= i
    return producto
        


# Prueba
lista = [2,3,4]
producto = producto(lista)
print("El producto de", lista, "es", producto)