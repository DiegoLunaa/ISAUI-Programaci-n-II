# Intercambiar valores: Crea una función que tome un diccionario y dos claves, e
# intercambie los valores de esas dos claves en el diccionario.
def intercambiar_dos_claves(diccionario, clave1, clave2):
    temp = diccionario[clave1]
    diccionario[clave1] = diccionario[clave2]
    diccionario[clave2] = temp
    return diccionario

diccionario = {
    "Color 1": "Azul",
    "Color 2": "Rojo",
    "Color 3": "Amarillo"
}

diccionario = intercambiar_dos_claves(diccionario, 'Color 1', 'Color 2')
print(diccionario)