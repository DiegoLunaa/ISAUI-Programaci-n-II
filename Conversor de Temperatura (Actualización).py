eleccion = int(input("Si desea convertir de Celsius a Fahrenheit introduzca 1\nSi desea convertir de Fahrenheit a Celsius introduzca 2\n"))
grados = float(input("Ahora ingrese los grados a convertir: "))

if eleccion == 1:
    eleccion = "Fahrenheit"
    grados = grados * (9/5) + 32
elif eleccion == 2:
    eleccion = "Celsius"
    grados = (grados - 32) * (5/9)
    
print("La temperatura es de " + str(grados) + " Grados " + eleccion)

