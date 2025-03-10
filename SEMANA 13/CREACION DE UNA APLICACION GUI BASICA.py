import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar():
    dato = entry_info.get()  # Obtener el texto ingresado
    if dato:
        listbox.insert(tk.END, dato)  # Agregar el dato a la lista
        entry_info.delete(0, tk.END)   # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un dato")

# Función para limpiar la lista
def limpiar():
    listbox.delete(0, tk.END)  # Borrar todos los elementos de la lista

# Función para convertir Fahrenheit a Celsius
def convertir():
    try:
        fahrenheit = float(entry_fah.get())  # Convertir la entrada a número
        celsius = (fahrenheit - 32) * 5 / 9  # Fórmula de conversión
        label_result.config(text=f"Resultado: {celsius:.2f} °C")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido para Fahrenheit")

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación GUI y Conversor de Temperatura")

# --- Sección para la funcionalidad de la lista ---
frame_lista = tk.Frame(root, pady=10)
frame_lista.pack()

label_info = tk.Label(frame_lista, text="Ingresa la información:")
label_info.pack(pady=5)

entry_info = tk.Entry(frame_lista, width=40)
entry_info.pack(pady=5)

btn_agregar = tk.Button(frame_lista, text="Agregar", command=agregar)
btn_agregar.pack(pady=5)

listbox = tk.Listbox(frame_lista, width=50)
listbox.pack(pady=5)

btn_limpiar = tk.Button(frame_lista, text="Limpiar", command=limpiar)
btn_limpiar.pack(pady=5)

# --- Sección para el conversor de temperatura ---
frame_conversion = tk.Frame(root, pady=10)
frame_conversion.pack()

label_conv_title = tk.Label(frame_conversion, text="Conversor de Temperatura (Fahrenheit a Celsius)")
label_conv_title.pack(pady=5)

label_fah = tk.Label(frame_conversion, text="Grados Fahrenheit:")
label_fah.pack(pady=5)

entry_fah = tk.Entry(frame_conversion, width=20)
entry_fah.pack(pady=5)

btn_convertir = tk.Button(frame_conversion, text="Convertir", command=convertir)
btn_convertir.pack(pady=5)

label_result = tk.Label(frame_conversion, text="Resultado: ")
label_result.pack(pady=5)

# Iniciar el bucle principal de la GUI
root.mainloop()
