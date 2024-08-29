import tkinter as tk
contador_n = 1
def factorial(x):
    resultado = 1
    for i in range(1, x + 1):
        resultado *= i

    entry_factorial.config(state='normal')    
    entry_factorial.delete(0, tk.END)
    entry_factorial.insert(0, resultado)
    entry_factorial.config(state='readonly')
    

def siguiente():
    global contador_n
    contador_n += 1
    entryn.config(state='normal')
    entryn.delete(0, tk.END)
    entryn.insert(0, contador_n)
    entryn.config(state='readonly')
    factorial(contador_n)



color_amarillo = '#feffda'
color_naranja = '#f7b7a3'

ventana = tk.Tk()
ventana.title("Factorial")
ventana.configure(bg=color_amarillo)
ventana.geometry("400x100")
ventana.resizable(False, False)


label1 = tk.Label(ventana, text="n", font=('Arial', 10, 'bold'), bg=color_amarillo)
label1.grid(row=0, column=0, pady=25)

entryn = tk.Entry(ventana, font=('Arial', 10), width=8)
entryn.grid(row=0, column=1, pady=25)
entryn.insert(0, contador_n)
entryn.config(state='readonly')


label2 = tk.Label(ventana, text="Factorial(n)", font=('Arial', 10, 'bold'), bg=color_amarillo)
label2.grid(row=0, column=2, pady=25, padx=10)

entry_factorial = tk.Entry(ventana, font=('Arial', 10), width=20)
entry_factorial.grid(row=0, column=3, pady=25)
entry_factorial.insert(0, '1')
entry_factorial.config(state='readonly')

button = tk.Button(ventana, text="Siguiente", font=('Arial', 10, 'bold'), command= siguiente, bg=color_naranja)
button.grid(row=0,column=4, pady=25, padx= 10)


ventana.mainloop()