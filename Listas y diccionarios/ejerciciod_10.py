# Valores únicos: Escribe una función que reciba un diccionario y devuelva una lista de
# valores únicos en el diccionario.
def valores_unicos(diccionario):
    lista_unica = []
    for valor in diccionario.values():
        if valor not in lista_unica:
            lista_unica.append(valor)
    return lista_unica
diccionario = {
    1: "Argentina",
    2: "Brasil",
    3: "Argentina",
    4: "Brasil",
    5: "Uruguay"
}

lista_unica = valores_unicos(diccionario)
print(lista_unica)
