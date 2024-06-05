# Notas de estudiantes : Escribe una función que recibe un diccionario donde
# las claves son nombres de estudiantes y los valores son listas de sus
# calificaciones. La función debe devolver un nuevo diccionario con las
# mismas claves pero donde los valores son la calificación promedio de cada estudiante.
def notas_estudiantes(diccionario):
    calificaciones = {}
    for clave, valor in diccionario.items():
        suma = 0
        prom = 0
        for i in valor:
            suma += i
        prom = suma / len(valor)
        calificaciones[clave] = prom
    return calificaciones


estudiantes_promedio = {}

estudiantes = {
    "Juan": [5, 7, 2],
    "Pedro": [8, 7, 9],
    "Pablo": [9, 4, 7],
    "Oscar": [2, 4, 1],
    "Mateo": [10, 10, 6]
}

estudiantes_promedio = notas_estudiantes(estudiantes)
print(estudiantes_promedio)