# Validación de Contraseña 
# Escribe un programa en Python que valide una contraseña ingresada por el usuario. La contraseña debe cumplir con los 
# siguientes requisitos:
# Debe tener al menos 8 caracteres de longitud.
# Debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (por ejemplo, !, @, #, $, %, etc.). 
# El programa debe informar al usuario si la contraseña es válida o no.

# def VerificarContraseña(contraseña):
#     correcta = len(contraseña) > 7 and any(caracter.isupper() for caracter in contraseña) and any(caracter.islower() for caracter in contraseña) and any(caracter.isdigit() for caracter in contraseña) and any(caracter in "!@#$%^&*()-_+=[]{}|\\:;\"'<>?,./" for caracter in contraseña)
#     if correcta:
#         print("La contraseña es valida")
#     else:
#         print("La contraseña no es valida, la contraseña debe tener:\nAl menos 8 caracteres de longitud, una letra mayúscula, una letra minúscula y un carácter especial")
    
while True: 
    contraseña = input("Insertar contraseña ")
    if len(contraseña) > 7 and any(caracter.isupper() for caracter in contraseña) and any(caracter.islower() for caracter in contraseña) and any(caracter.isdigit() for caracter in contraseña) and any(caracter in "!@#$%^&*()-_+=[]{}|\\:;\"'<>?,./" for caracter in contraseña):
        print("La contraseña es valida")
        break
    else:
        print("La contraseña no es valida, la contraseña debe tener:\nAl menos 8 caracteres de longitud, una letra mayúscula, una letra minúscula y un carácter especial")