import tkinter as tk
color_amarillo = '#feffda'
color_naranja = '#f7b7a3'
contador = 0
def incrementar():
    global contador
    contador += 1
    contador_entry.config(state='normal')
    contador_entry.delete(0, tk.END)
    contador_entry.insert(0, contador)
    contador_entry.config(state='readonly')

def decreciente():
    global contador
    # if contador > 0: Esto haría que el contador no baje de 0, es decir no sea negativo, pero como en la consigna no lo decía lo comento.
    contador -= 1
    contador_entry.config(state='normal')
    contador_entry.delete(0, tk.END)
    contador_entry.insert(0, contador)
    contador_entry.config(state='readonly')

def reset():
    global contador
    contador = 0
    contador_entry.config(state='normal')
    contador_entry.delete(0, tk.END)
    contador_entry.insert(0, contador)
    contador_entry.config(state='readonly')

ventana = tk.Tk()
ventana.title("Contador")
ventana.configure(bg=color_amarillo)
ventana.geometry("400x100")
ventana.resizable(False, False)

# Label
label = tk.Label(ventana, text="Contador", font=('Arial', 12, 'bold'), bg=color_amarillo)
label.grid(row= 0, column= 0, pady=25)

# Lineedit
contador_entry = tk.Entry(ventana, font=('Arial', 12), width=10)
contador_entry.grid(row=0, column= 1, pady=25)
contador_entry.insert(0, contador)
contador_entry.config(state='readonly')

boton = tk.Button(ventana, text="Count Up", command=incrementar, font=('Arial', 10, 'bold'), bg=color_naranja)
boton.grid(row= 0, column= 2, pady=25, padx=5)

boton1 = tk.Button(ventana, text="Count Down", command=decreciente, font=('Arial', 10, 'bold'), bg=color_naranja)
boton1.grid(row= 0, column= 3, pady=25)

boton_reset = tk.Button(ventana, text="Reset", command=reset, font=('Arial', 10, 'bold'), bg=color_naranja)
boton_reset.grid(row= 0, column= 4, pady=25, padx=5)
ventana.mainloop()

