# Elementos mayores que un valor: Escribe una función que tome una lista de números
# y un valor n, y devuelva una nueva lista con los elementos mayores que n.
def elem_mayor_valor(lista, n):
    lista_mayores = []
    for i in lista:
        if i > n:
            lista_mayores.append(i)
    lista_mayores.sort()
    return lista_mayores

lista = []

can = int(input("Ingrese la cantidad de datos a usar: "))

for i in range(can):
    dato = int(input("Ingresar el dato número " + str(i + 1) + ": " ))
    lista.append(dato)

nro_ran = int(input("\nIngresar número para calcular los mayores a él: "))

lista_mayores = elem_mayor_valor(lista, nro_ran)

print(lista_mayores)