# Diccionario de cuadrados: Escribe una función que reciba un número n y devuelva un
# diccionario con los números de 1 a n como claves y sus cuadrados como valores.
def diccionario_cuadrado(n):
    con = 1
    diccionario_cuadrado = {}
    while con <= n:
        diccionario_cuadrado[con] = (con * con)
        con += 1
    return diccionario_cuadrado

diccionario_nuevo = diccionario_cuadrado(10)
print(diccionario_nuevo)