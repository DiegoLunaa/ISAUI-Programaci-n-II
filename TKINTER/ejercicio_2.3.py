import tkinter as tk
import random

color_amarillo = '#feffda'
color_naranja = '#f7b7a3'

def generar():
    try:
        numero1 = int(num1.get())
        numero2 = int(num2.get())

        if numero1 > numero2:
            numero1, numero2 = numero2, numero1

        aleatorio = random.randint(numero1, numero2)
        entry.config(state='normal')
        entry.delete(0, tk.END)
        entry.insert(0, aleatorio)
        entry.config(state='readonly')

    except ValueError:
        entry.config(state='normal')
        entry.delete(0, tk.END)
        entry.insert(0, "Solo números")
        entry.config(state='readonly')
        
# Creación de ventana
ventana = tk.Tk()
ventana.title("Generado de números")
ventana.configure(bg=color_amarillo)
ventana.geometry("480x300")
ventana.resizable(False, False)

label1 = tk.Label(ventana, text='Número 1:', font=('Arial', 12, 'bold'), bg=color_amarillo)
label1.grid(row=0,column=0,pady=25)

num1 = tk.Spinbox(ventana, from_=1, to=100, font=('Arial', 12))
num1.grid(row=0,column=1,pady=25, padx=10)

label2 = tk.Label(ventana, text='Número 2:', font=('Arial', 12, 'bold'), bg=color_amarillo)
label2.grid(row=1,column=0,pady=25)

num2 = tk.Spinbox(ventana, from_=1, to=100, font=('Arial', 12))
num2.grid(row=1,column=1,pady=25, padx=10)

label3 = tk.Label(ventana, text='Número generado:', font=('Arial', 12, 'bold'), bg=color_amarillo)
label3.grid(row=2,column=0,pady=25)

entry = tk.Entry(ventana, font=('Arial', 12), state='readonly')
entry.grid(row=2,column=1,pady=25)


button = tk.Button(ventana, command=generar, text="Generar", height=1, width=7, font=('Arial', 10, 'bold'), bg=color_naranja)
button.place(x=210, y=225, width=80, height=40)



ventana.mainloop()