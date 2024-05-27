# Contar elementos: Escribe una función que reciba una lista y un valor, y devuelva
# cuántas veces aparece ese valor en la lista.
def contador_lista(lista, valor):
    con = 0
    for i in lista:
        if i == valor:
            con += 1
    if con == 0:
        con = "El valor no está en la lista"
    return  con  
    
lista = []

can = int(input("Ingrese la cantidad de datos a usar: "))

for i in range(can):
    dato = int(input("Ingresar el dato número " + str(i + 1) + ": " ))
    lista.append(dato)

valor = int(input("Ingrese el valor para calcular las veces que se repite: "))

cantidad = contador_lista(lista, valor)

print("El valor aparece", cantidad, "veces")