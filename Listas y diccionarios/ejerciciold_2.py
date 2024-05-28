# Agrupar por longitud: Escribe una función que reciba una lista de palabras y devuelva
# un diccionario donde las claves son las longitudes de las palabras y los valores son
# listas de palabras con esa longitud.
def agrupar_por_longitud(lista):
    diccionario = {}
    palabras = []
    for cadena in lista:
        palabras += cadena.split()
    for i in palabras:
        longitud = len(i)
        if longitud not in diccionario:
                diccionario[longitud] = []
        diccionario[longitud].append(i)
    return diccionario
lista = [
    "Juan",
    "Pablo",
    "Pedro",
    "Josefina"
]

diccionario = agrupar_por_longitud(lista)
print(diccionario)






















# def agrupar_por_longitud(lista):
#     palabras = " ".join(lista)
#     palabras = palabras.split()
#     longitudes = []
#     diccionario = {}
#     for i in palabras:
#         if len(i) not in longitudes:
#             longitudes.append(len(i))
#         for x in longitudes:
#             if x not in diccionario:
#                 diccionario[x] = []
#             if len(i) == x:
#                 diccionario[x].append(i)
#     return diccionario
# lista = [
#     "Juan pablo",
#     "Pablo pedro",
#     "Pedro pablo"
# ]

# diccionario = agrupar_por_longitud(lista)
# print(diccionario)
