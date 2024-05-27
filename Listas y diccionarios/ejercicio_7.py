# Invertir lista: Escribe una función que tome una lista y devuelva una nueva lista con los
# elementos en orden inverso.
def invertir(lista):
    lista_inv = []
    can = len(lista) - 1
    for i in lista:
        if can >= 0:
            lista_inv.append(lista[can]) 
            can -= 1
    return lista_inv

# Prueba
lista = [1,2,3,4,5,6,7,8,9,10]

lista_inv = invertir(lista)

print(lista_inv)