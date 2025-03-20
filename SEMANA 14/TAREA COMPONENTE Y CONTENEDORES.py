import tkinter as tk
from tkinter import ttk, messagebox

# Importar el DateEntry desde tkcalendar para el selector de fecha
try:
    from tkcalendar import DateEntry
except ImportError:
    messagebox.showerror("Error",
                         "El módulo tkcalendar no está instalado. Por favor, instálalo con: pip install tkcalendar")
    raise


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.crear_widgets()

    def crear_widgets(self):
        # --- Frame para la entrada de datos ---
        frame_entrada = ttk.Frame(self.root, padding="10")
        frame_entrada.pack(fill=tk.X)

        # Etiqueta y widget para la fecha (DatePicker)
        ttk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.fecha_entry = DateEntry(frame_entrada, date_pattern='dd/mm/yyyy')
        self.fecha_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # Etiqueta y widget para la hora
        ttk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        self.hora_entry = ttk.Entry(frame_entrada, width=10)
        self.hora_entry.grid(row=0, column=3, sticky=tk.W, padx=5, pady=5)

        # Etiqueta y widget para la descripción
        ttk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.descripcion_entry = ttk.Entry(frame_entrada, width=50)
        self.descripcion_entry.grid(row=1, column=1, columnspan=3, sticky=tk.W, padx=5, pady=5)

        # Botón para agregar un evento
        self.btn_agregar = ttk.Button(frame_entrada, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.grid(row=2, column=0, columnspan=2, pady=10)

        # Botón para eliminar el evento seleccionado
        self.btn_eliminar = ttk.Button(frame_entrada, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.btn_eliminar.grid(row=2, column=2, columnspan=2, pady=10)

        # --- Frame para mostrar la lista de eventos (TreeView) ---
        frame_tree = ttk.Frame(self.root, padding="10")
        frame_tree.pack(fill=tk.BOTH, expand=True)

        # Configuración del TreeView: columnas para Fecha, Hora y Descripción
        self.tree = ttk.Treeview(frame_tree, columns=("fecha", "hora", "descripcion"), show="headings")
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.column("fecha", width=100)
        self.tree.column("hora", width=80)
        self.tree.column("descripcion", width=300)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Botón para salir de la aplicación
        self.btn_salir = ttk.Button(self.root, text="Salir", command=self.root.quit)
        self.btn_salir.pack(pady=10)

    def agregar_evento(self):
        """Función para agregar un nuevo evento a la agenda."""
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        # Validar que todos los campos se hayan completado
        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        # Insertar el evento en el TreeView
        self.tree.insert("", tk.END, values=(fecha, hora, descripcion))

        # Limpiar los campos de entrada (excepto la fecha)
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

    def eliminar_evento(self):
        """Función para eliminar el evento seleccionado tras confirmación."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")
            return
        confirm = messagebox.askyesno("Confirmar eliminación",
                                      "¿Está seguro de que desea eliminar el evento seleccionado?")
        if confirm:
            self.tree.delete(selected_item)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
