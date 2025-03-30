import tkinter as tk
from tkinter import messagebox


class TareasApp:
    def __init__(self, master):
        # Configuración inicial de la ventana principal
        self.master = master
        self.master.title("Lista de Tareas")

        # Campo de entrada de texto para las tareas
        # Decidimos usar un Entry ya que es ideal para capturar una línea de texto (como una tarea).
        self.entry_tarea = tk.Entry(self.master, width=40)
        self.entry_tarea.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="ew")
        # Asociamos el evento "Return" (presionar Enter) con la acción de añadir tarea.
        self.entry_tarea.bind("<Return>", lambda event: self.añadir_tarea())

        # Botón para añadir tareas
        # Al presionarlo, se llama a la función "añadir_tarea", que agrega el texto al Listbox.
        self.btn_añadir = tk.Button(self.master, text="Añadir Tarea", command=self.añadir_tarea)
        self.btn_añadir.grid(row=0, column=2, padx=10, pady=10)

        # Botón para marcar tareas como completadas
        # Llama a una función que cambia el estado de la tarea seleccionada en el Listbox.
        self.btn_completar = tk.Button(self.master, text="Marcar como Completada", command=self.marcar_completada)
        self.btn_completar.grid(row=1, column=0, padx=10, pady=5)

        # Botón para eliminar tareas
        # Llama a una función que elimina el elemento seleccionado del Listbox.
        self.btn_eliminar = tk.Button(self.master, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=1, column=1, padx=10, pady=5)

        # Listbox para mostrar las tareas
        # Elegimos un Listbox porque permite mostrar una lista de elementos y gestionar la selección.
        self.listbox_tareas = tk.Listbox(self.master, selectmode=tk.SINGLE, width=50, height=15)
        self.listbox_tareas.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

    def añadir_tarea(self):
        # Esta función toma el texto del Entry y lo añade al Listbox.
        # Si el texto está vacío, muestra un mensaje de advertencia.
        tarea = self.entry_tarea.get().strip()
        if tarea:
            # Insertamos la tarea al final del Listbox
            self.listbox_tareas.insert(tk.END, tarea)
            # Limpiamos el Entry para que quede listo para la siguiente entrada
            self.entry_tarea.delete(0, tk.END)
        else:
            # Mostramos un aviso si el Entry está vacío
            messagebox.showwarning("Aviso", "No puedes añadir una tarea vacía.")

    def marcar_completada(self):
        # Cambia el estado de la tarea seleccionada agregando "[Completada]" delante del texto.
        try:
            # Obtenemos el índice de la tarea seleccionada
            seleccion = self.listbox_tareas.curselection()[0]
            # Obtenemos el texto de esa tarea
            tarea = self.listbox_tareas.get(seleccion)
            # Eliminamos la tarea actual de la lista
            self.listbox_tareas.delete(seleccion)
            # Volvemos a añadir la tarea con el prefijo "[Completada]"
            self.listbox_tareas.insert(tk.END, f"[Completada] {tarea}")
        except IndexError:
            # Mostramos una advertencia si no hay ninguna tarea seleccionada
            messagebox.showwarning("Aviso", "No hay ninguna tarea seleccionada.")

    def eliminar_tarea(self):
        # Elimina la tarea seleccionada del Listbox.
        try:
            # Obtenemos el índice de la tarea seleccionada
            seleccion = self.listbox_tareas.curselection()[0]
            # Eliminamos la tarea del Listbox
            self.listbox_tareas.delete(seleccion)
        except IndexError:
            # Mostramos una advertencia si no hay ninguna tarea seleccionada
            messagebox.showwarning("Aviso", "No hay ninguna tarea seleccionada.")


# Este es el punto de entrada del programa.
# Creamos la ventana principal (Tk) y pasamos su referencia al constructor de nuestra clase TareasApp.
if __name__ == "__main__":
    root = tk.Tk()
    app = TareasApp(root)
    root.mainloop()
