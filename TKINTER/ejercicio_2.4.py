import tkinter as tk
color_amarillo = '#feffda'
color_naranja = '#f7b7a3'

def validar_solo_numeros(char):
    if char.isdigit() or char == ".":
        return True
    return False

def calculo():
    try:
        operacion = opcion_operacion.get()
        num1 = float(entry_pn.get())
        num2 = float(entry_sn.get())

        if operacion == 1:
            resultado = num1 + num2
        elif operacion == 2:
            resultado = num1 - num2
        elif operacion == 3:
            resultado = num1 * num2
        elif operacion == 4:
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "No se puede dividir por 0."
            
        
        entry_resultado.config(state='normal')
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, resultado)
        entry_resultado.config(state='readonly')
        
    except ValueError:
        entry_resultado.config(state='normal')
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, 'ERROR Verificar los datos.')
        entry_resultado.config(state='readonly')
    

    
    

# Creación de ventana
ventana = tk.Tk()
ventana.title('Calculadora')
ventana.configure(bg=color_amarillo)
ventana.geometry("500x350")
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

button = tk.Button(ventana, command=calculo, text="Generar", height=1, width=7, font=('Arial', 10, 'bold'), bg=color_naranja)
button.grid(row=3, column=1)

label_op = tk.Label(ventana, text='Operaciones', font=('Arial', 10, 'bold'), bg=color_amarillo)
label_op.place(x=350, y= 10)

opcion_operacion = tk.IntVar()

rd1 = tk.Radiobutton(ventana, text='Suma', variable=opcion_operacion, value=1,  font=('Arial', 10, 'bold'), bg=color_amarillo)
rd1.place(x=350, y=40)

rd2 = tk.Radiobutton(ventana, text='Resta', variable=opcion_operacion, value=2,  font=('Arial', 10, 'bold'), bg=color_amarillo)
rd2.place(x=350, y=80)

rd3 = tk.Radiobutton(ventana, text='Multiplicar', variable=opcion_operacion, value=3,  font=('Arial', 10, 'bold'), bg=color_amarillo)
rd3.place(x=350, y=120)

rd4 = tk.Radiobutton(ventana, text='Dividir', variable=opcion_operacion, value=4,  font=('Arial', 10, 'bold'), bg=color_amarillo)
rd4.place(x=350, y=160)


ventana.mainloop()