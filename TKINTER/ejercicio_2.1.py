import tkinter as tk
color_amarillo = '#feffda'
color_naranja = '#f7b7a3'

def validar_solo_numeros(char):
    if char.isdigit() or char == ".":
        return True
    return False

def sumar():
    try:
        num1 = float(entry_pn.get())
        num2 = float(entry_sn.get())
        resultado = num1 + num2
        entry_resultado.config(state='normal')
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, resultado)
        entry_resultado.config(state='readonly')
    except ValueError:
        entry_resultado.config(state='normal')
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, "Error")
        entry_resultado.config(state='readonly')

def restar():
    try:
        num1 = float(entry_pn.get())
        num2 = float(entry_sn.get())
        resultado = num1 - num2
        entry_resultado.config(state='normal')
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, resultado)
        entry_resultado.config(state='readonly')
    except ValueError:
        entry_resultado.config(state='normal')
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, "Error")
        entry_resultado.config(state='readonly')

def multiplicar():
    try:
        num1 = float(entry_pn.get())
        num2 = float(entry_sn.get())
        resultado = num1 * num2
        entry_resultado.config(state='normal')
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, resultado)
        entry_resultado.config(state='readonly')
    except ValueError:
        entry_resultado.config(state='normal')
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, "Error")
        entry_resultado.config(state='readonly')

def dividir():
    try:
        num1 = float(entry_pn.get())
        num2 = float(entry_sn.get())
        resultado = num1 / num2
        entry_resultado.config(state='normal')
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, resultado)
        entry_resultado.config(state='readonly')
    except ValueError:
        entry_resultado.config(state='normal')
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, "Error")
        entry_resultado.config(state='readonly')

def porcentaje():
    try:
        num1 = float(entry_pn.get())
        num2 = float(entry_sn.get())
        resultado = (num1 * num2) / 100
        entry_resultado.config(state='normal')
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, resultado)
        entry_resultado.config(state='readonly')
    except ValueError:
        entry_resultado.config(state='normal')
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, "Error")
        entry_resultado.config(state='readonly')

def clear():
    entry_pn.delete(0, tk.END)
    entry_sn.delete(0, tk.END)
    entry_resultado.config(state='normal')
    entry_resultado.delete(0, tk.END)
    entry_resultado.config(state='readonly')
    
    

# Creación de ventana
ventana = tk.Tk()
ventana.title('Calculadora')
ventana.configure(bg=color_amarillo)
ventana.geometry("300x350")
ventana.resizable(False, False)

# Labels y entrys
validacion = ventana.register(validar_solo_numeros)

label_pn = tk.Label(ventana, text='Primer número', font=('Arial', 10, 'bold'), bg=color_amarillo)
label_pn.grid(row=0, column=0, pady=25)

entry_pn = tk.Entry(ventana, font=('Arial', 10), validate="key", validatecommand=(validacion, '%S'))
entry_pn.grid(row=0, column=1, pady=25, padx=5)

label_sn = tk.Label(ventana, text='Segundo número', font=('Arial', 10, 'bold'), bg=color_amarillo)
label_sn.grid(row=1, column=0, pady=25)

entry_sn = tk.Entry(ventana, font=('Arial', 10), validate="key", validatecommand=(validacion, '%S'))
entry_sn.grid(row=1, column=1, pady=25, padx=5)

label_resultado = tk.Label(ventana, text='Resultado', font=('Arial', 10, 'bold'), bg=color_amarillo)
label_resultado.grid(row=2, column=0, pady=25)

entry_resultado = tk.Entry(ventana, font=('Arial', 10))
entry_resultado.grid(row=2, column=1, pady=25, padx=5)
entry_resultado.config(state="readonly")

# Botones 
button_suma = tk.Button(ventana, command=sumar, text="+", height=1, width=15, font=('Arial', 10, 'bold'), bg=color_naranja)
button_suma.grid(row=3,column=0, pady=5)

button_resta = tk.Button(ventana, command=restar, text="-", height=1, width=15, font=('Arial', 10, 'bold'), bg=color_naranja)
button_resta.grid(row=3,column=1, pady=5)

button_multiplicacion = tk.Button(ventana, command=multiplicar, text="*", height=1, width=15, font=('Arial', 10, 'bold'), bg=color_naranja)
button_multiplicacion.grid(row=4,column=0, pady=5)

button_division = tk.Button(ventana, command=dividir, text="/", height=1, width=15, font=('Arial', 10, 'bold'), bg=color_naranja)
button_division.grid(row=4,column=1, pady=5, padx= 5)

button_porcentaje = tk.Button(ventana, command=porcentaje, text="%", height=1, width=15, font=('Arial', 10, 'bold'), bg=color_naranja)
button_porcentaje.grid(row=5,column=0, pady=5, padx= 5)

button_clear = tk.Button(ventana, command=clear, text="CLEAR", height=1, width=15, font=('Arial', 10, 'bold'), bg=color_naranja)
button_clear.grid(row=5,column=1, pady=5, padx= 5)

ventana.mainloop()