# Encontrar índice: Escribe una función que reciba una lista y un valor, y devuelva el
# índice de la primera aparición de ese valor en la lista, o -1 si el valor no está presente.

# def indice(lista, valor):
#     for i, elemento in enumerate(lista):
#         if elemento == valor:
#             return i
#     return -1

def indice(lista, valor):
    con = 1
    indice = 0
    for i in lista:
        if i == valor:
            indice = con
            break
        else:
            indice = -1
        con += 1
    return indice
    

lista = [1,2,3,4,5]
valor = 3
indice_encontrado = 0

indice_encontrado = indice(lista, valor)
print("El indice del numero", valor, "es", indice_encontrado)