# Suma de elementos: Escribe una función que tome una lista de números y devuelva la
# suma de todos los elementos en la lista.
def suma_lista(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

lista = []

can = int(input("Ingrese la cantidad de datos a usar: "))

for i in range(can):
    dato = int(input("Ingresar el dato número " + str(i + 1) + ": " ))
    lista.append(dato)

sumalista = suma_lista(lista)

print("\n La suma de los números es: ", sumalista)