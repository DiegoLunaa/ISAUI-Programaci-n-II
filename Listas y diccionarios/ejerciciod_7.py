# Sumar valores: Escribe una función que reciba un diccionario con valores numéricos y
# devuelva la suma de todos los valores.

# Otra forma
# def suma_valores(diccionario):
#     suma = 0
#     for i in diccionario.values():
#         suma += i
#     return suma

def suma_valores(diccionario):
    suma = 0
    for clave, valor in diccionario.items():
        suma += valor
    return suma

diccionario = {
    1: 2,
    2: 4,
    3: 6
}

suma = suma_valores(diccionario)
print(suma)