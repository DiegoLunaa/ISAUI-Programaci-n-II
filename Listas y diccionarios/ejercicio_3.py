# Promedio de una lista: Crea una función que calcule el promedio de los números en
# una lista dada.
def suma_lista(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

def promedio_lista(lista):
    can = len(lista)
    sumalista = suma_lista(lista)
    promedio = sumalista / can
    return promedio

lista = []

can = int(input("Ingrese la cantidad de datos a usar: "))

for i in range(can):
    dato = int(input("Ingresar el dato número " + str(i + 1) + ": " ))
    lista.append(dato)

promedio = promedio_lista(lista)

print("\nEl promedio es: ", promedio)