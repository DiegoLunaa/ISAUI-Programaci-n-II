import tkinter as tk
color_amarillo = '#feffda'
color_naranja = '#f7b7a3'

def agregar():
    pelicula = pelicula_entry.get()
    
    if pelicula_entry.get() == "":
        modalerror = tk.Toplevel(ventana)
        modalerror.title("¡El campo no puede estar vacío!")
        modalerror.geometry("300x120")
        modalerror.configure(bg=color_amarillo)
        modalerror.resizable(False, False)

        label_modal_error = tk.Label(modalerror, text='¡El campo no puede estar vacío!', font=('Arial', 10, 'bold'), bg=color_naranja)
        label_modal_error.grid(row=0, column=0, pady=25, padx=25)

        button_error1 = tk.Button(modalerror, command=modalerror.destroy, text="Volver", height=1, width=7, font=('Arial', 10, 'bold'), bg=color_naranja)
        button_error1.grid(row=1, column=0)
        pelicula_entry.delete(0, tk.END)
    elif pelicula in lista.get(0, tk.END):
        modal = tk.Toplevel(ventana)
        modal.title("Error: La película ya ha sido ingresada")
        modal.geometry("350x120")
        modal.configure(bg=color_amarillo)
        modal.resizable(False, False)

        label_modal = tk.Label(modal, text='La película ya fue ingresada, intente con otra.', font=('Arial', 10, 'bold'), bg=color_naranja)
        label_modal.grid(row=0, column=0, pady=25, padx=25)

        button_error = tk.Button(modal, command=modal.destroy, text="Volver", height=1, width=7, font=('Arial', 10, 'bold'), bg=color_naranja)
        button_error.grid(row=1, column=0)
        pelicula_entry.delete(0, tk.END)
    else:
        lista.insert(0, pelicula)
        pelicula_entry.delete(0, tk.END)
        

# Creación de ventana
ventana = tk.Tk()
ventana.title("Contador")
ventana.configure(bg=color_amarillo)
ventana.geometry("480x300")
ventana.resizable(False, False)


# Label
label1 = tk.Label(ventana, text="Escribe el título de una película:", font=('Arial', 12, 'bold'), bg=color_amarillo)
label1.grid(row= 0, column= 0, pady=25)

button = tk.Button(ventana, command=agregar, text="Añadir", height=1, width=5, font=('Arial', 10, 'bold'), bg=color_naranja)
button.grid(row=0,column=2, pady=5)


# Lineedit
pelicula_entry = tk.Entry(ventana, font=('Arial', 12), width=15, validate="key")
pelicula_entry.grid(row=0, column= 1, pady=25, padx= 10)
# contador_entry.insert(0)


label2 = tk.Label(ventana, text="Películas", font=('Arial', 12, 'bold'), bg=color_amarillo)
label2.place(x=150, y=80)

lista = tk.Listbox(ventana, bg=color_naranja)
lista.place(x=50, y=100, width=350, height=180)



ventana.mainloop()