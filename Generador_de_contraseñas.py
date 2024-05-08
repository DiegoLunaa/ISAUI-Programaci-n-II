# Ejercicio 8: Generador de Contraseñas Aleatorias 
# Escribe un programa en Python que genere una contraseña aleatoria para el usuario. 
# La contraseña debe tener una longitud de al menos 12 caracteres y debe contener una combinación de letras 
# (mayúsculas y minúsculas), números y caracteres especiales. El programa debe mostrar la contraseña generada al usuario.
import random
contraseña = []
letras = "abcdefghijklmnñopqrstuvwxyz"
letrasm = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
nums = "1234567890"
caracteres_especiales = "!@#$%^&*()_+-=[]}{|;:,.<>?`~"

# Agrega un elemento de cada uno
contraseña.append(random.choice(letras))
contraseña.append(random.choice(letrasm))
contraseña.append(random.choice(nums))
contraseña.append(random.choice(caracteres_especiales))

# Llenar el resto de la cadena
for _ in range(8):
    contraseña.append(random.choice(letras + letrasm + nums + caracteres_especiales))

# Mezclamos para que no tengan un orden
random.shuffle(contraseña)

# Unimos la contraseña
contraseña = "".join(contraseña)

# Imprimimos la contraseña
print("Tu contraseña es ", contraseña)
