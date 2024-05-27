# Eliminar duplicados: Crea una función que tome una lista y devuelva una nueva lista
# sin elementos duplicados.
def lista_sin_duplicados(lista):
   lista_sind = []
   for i in lista:
      if i not in lista_sind:
         lista_sind.append(i)
   lista_sind.sort()
   return lista_sind

lista = []
can = int(input("Ingrese la cantidad de datos a usar: "))

for i in range(can):
    dato = int(input("Ingresar el dato número " + str(i + 1) + ": " ))
    lista.append(dato)

listasin = lista_sin_duplicados(lista)

print(listasin)