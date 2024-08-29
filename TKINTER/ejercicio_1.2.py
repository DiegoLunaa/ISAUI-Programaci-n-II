import tkinter as tk
color_amarillo = '#feffda'
color_naranja = '#f7b7a3'
contador = 88
def decreciente():
    global contador
    # if contador > 0: Esto haría que el contador no baje de 0, es decir no sea negativo, pero como en la consigna no lo decía lo comento.
    contador -= 1
    # Hacer el Entry editable temporalmente
    contador_entry.config(state='normal')
    # Borrar el contenido actual del Entry
    contador_entry.delete(0, tk.END)
    # Insertar el nuevo valor del contador
    contador_entry.insert(0, contador)
    # Volver a hacer el Entry no editable
    contador_entry.config(state='readonly')

# Creación de la ventana
ventana = tk.Tk()
ventana.title("ContDecreciente")
ventana.configure(bg=color_amarillo)

# Tamaño inicial ventana
ventana.geometry("200x100")

# Hacer que solo tenga un tamaño
ventana.resizable(False, False)

# Label
label = tk.Label(ventana, text="Contador", font=('Arial', 12, 'bold'), bg=color_amarillo)
label.grid(row= 0, column= 0, pady=25)

# Lineedit
contador_entry = tk.Entry(ventana, font=('Arial', 12), width=10)
contador_entry.grid(row=0, column= 1, pady=25)
contador_entry.insert(0, contador)  # Insertar texto predeterminado
contador_entry.config(state='readonly')        # Hacer que el Entry sea no editable

# Botón
boton = tk.Button(ventana, text="-", command=decreciente, font=('Arial', 12, 'bold'), bg=color_naranja)
boton.grid(row= 0, column= 2, pady=25)
ventana.mainloop()