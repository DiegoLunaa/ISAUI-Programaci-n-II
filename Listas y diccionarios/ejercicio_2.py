# Máximo y mínimo: Escribe una función que reciba una lista de números y devuelva el
# valor máximo y el mínimo de la lista.
# def min_max(lista):
#     maximo = 0
#     minimo = 0
#     maximo = (max(lista))
#     minimo = (min(lista))
#     return minimo, maximo

def min_max(lista):
    if not lista:
        return "No hay números para calcular el máximo y el mínimo."

    maximo = minimo = lista[0]

    for i in lista:
        if i > maximo:
            maximo = i
        if i < minimo:
            minimo = i
    
    return minimo, maximo

lista = []

can = int(input("Ingrese la cantidad de datos a usar: "))

for i in range(can):
    dato = int(input("Ingresar el dato número " + str(i + 1) + ": " ))
    lista.append(dato)

minimo, maximo = min_max(lista)

print("El número más bajo es", minimo, "y el número más alto es", maximo)

