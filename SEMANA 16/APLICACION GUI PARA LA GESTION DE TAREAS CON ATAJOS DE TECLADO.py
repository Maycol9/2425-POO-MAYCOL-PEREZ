import tkinter as tk
from tkinter import messagebox


class TaskManager:
    def __init__(self, master):
        self.master = master
        master.title("Gestión de Tareas")  # Se establece el título de la ventana principal.

        # Creación del campo de entrada para introducir nuevas tareas.
        # Se utiliza un widget Entry para que el usuario pueda escribir el texto de la tarea.
        self.entry = tk.Entry(master, width=50)
        self.entry.pack(pady=10)
        self.entry.focus()  # Coloca el foco en el campo de entrada al iniciar la aplicación.

        # Se vincula el evento <Return> (tecla Enter) al método add_task_event,
        # permitiendo que se agregue una tarea al presionar Enter.
        self.entry.bind("<Return>", self.add_task_event)

        # Creación de un Frame para organizar los botones de acción.
        # Esto permite una mejor disposición y alineación de los elementos.
        self.btn_frame = tk.Frame(master)
        self.btn_frame.pack(pady=5)

        # Botón para agregar una nueva tarea.
        # Al hacer clic, se llama al método add_task.
        self.add_btn = tk.Button(self.btn_frame, text="Agregar Tarea", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        # Botón para marcar la tarea seleccionada como completada.
        # Llama al método complete_task al hacer clic.
        self.complete_btn = tk.Button(self.btn_frame, text="Completar Tarea", command=self.complete_task)
        self.complete_btn.grid(row=0, column=1, padx=5)

        # Botón para eliminar la tarea seleccionada.
        # Llama al método delete_task al hacer clic.
        self.delete_btn = tk.Button(self.btn_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # Creación de un Listbox para mostrar las tareas.
        # Este widget permite visualizar las tareas agregadas y seleccionar alguna para modificarla.
        self.task_listbox = tk.Listbox(master, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Configuración de atajos de teclado adicionales a nivel de la ventana principal:
        # - La tecla Escape cierra la aplicación.
        master.bind("<Escape>", lambda event: master.quit())
        # - La tecla "C" marca la tarea seleccionada como completada.
        master.bind("<Key-c>", lambda event: self.complete_task())
        # - La tecla "D" y la tecla Delete eliminan la tarea seleccionada.
        master.bind("<Key-d>", lambda event: self.delete_task())
        master.bind("<Delete>", lambda event: self.delete_task())

    def add_task_event(self, event):
        """
        Método invocado al presionar la tecla Enter en el campo de entrada.
        Se delega la funcionalidad a add_task para evitar duplicación de código.
        """
        self.add_task()

    def add_task(self):
        """
        Añade la tarea ingresada en el campo de entrada al Listbox.
        Se verifica que el campo no esté vacío; de lo contrario, se muestra un mensaje de advertencia.
        """
        task = self.entry.get().strip()  # Se obtiene el contenido del Entry y se eliminan espacios innecesarios.
        if task:
            self.task_listbox.insert(tk.END, task)  # Se agrega la tarea al final del Listbox.
            self.entry.delete(0, tk.END)  # Se limpia el campo de entrada tras agregar la tarea.
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

    def complete_task(self):
        """
        Marca la tarea seleccionada en el Listbox como completada.
        La lógica consiste en agregar un prefijo "[Completado] " para diferenciar visualmente las tareas terminadas.
        Si la tarea ya posee dicho prefijo, se informa al usuario.
        """
        try:
            index = self.task_listbox.curselection()[0]  # Se obtiene el índice de la tarea seleccionada.
            task_text = self.task_listbox.get(index)  # Se obtiene el texto de la tarea.
            # Se verifica si la tarea ya está marcada como completada.
            if not task_text.startswith("[Completado] "):
                self.task_listbox.delete(index)  # Se elimina la tarea actual para poder modificarla.
                self.task_listbox.insert(index, "[Completado] " + task_text)  # Se reinserta la tarea con el prefijo.
            else:
                messagebox.showinfo("Información", "La tarea ya está marcada como completada.")
        except IndexError:
            # Captura el error en caso de que no se haya seleccionado ninguna tarea.
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

    def delete_task(self):
        """
        Elimina la tarea seleccionada del Listbox.
        Si no se ha seleccionado ninguna tarea, se muestra una advertencia.
        """
        try:
            index = self.task_listbox.curselection()[0]  # Se obtiene el índice de la tarea seleccionada.
            self.task_listbox.delete(index)  # Se elimina la tarea del Listbox.
        except IndexError:
            # Maneja el caso en que no haya una tarea seleccionada.
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")


if __name__ == "__main__":
    # Creación de la ventana principal de la aplicación.
    root = tk.Tk()
    # Instanciación de la clase TaskManager que contiene toda la lógica de la aplicación.
    app = TaskManager(root)
    # Inicia el bucle principal de la aplicación, permitiendo la interacción con la interfaz.
    root.mainloop()
