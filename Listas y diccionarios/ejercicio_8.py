# Concatenar listas: Escribe una función que reciba dos listas y devuelva una nueva lista
# que sea la concatenación de ambas.
def concatenar_lista(lista1, lista2):
    lista_nueva = []
    lista_nueva = lista1 + lista2
    return lista_nueva

lista_concatenada = []
num_1_5 = [1,2,3,4,5]
num_6_10 = [6,7,8,9,10]

lista_concatenada = concatenar_lista(num_1_5, num_6_10)

print(lista_concatenada)