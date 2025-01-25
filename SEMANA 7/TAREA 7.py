# Ejemplo detallado de uso de constructores (__init__) y destructores (__del__) en Python

class BaseDeDatos:
    def __init__(self, nombre_bd):
        """
        Constructor de la clase BaseDeDatos.
        Este método inicializa una conexión ficticia a una base de datos.

        :param nombre_bd: Nombre de la base de datos a la que se "conectará".
        """
        self.nombre_bd = nombre_bd
        print(f"[INFO] Inicializando conexión a la base de datos '{self.nombre_bd}'.")
        # Simulamos la conexión a la base de datos
        self.conectado = True
        print(f"[INFO] Conexión a la base de datos '{self.nombre_bd}' establecida.")

    def realizar_consulta(self, consulta):
        """
        Método para simular la ejecución de una consulta en la base de datos.

        :param consulta: La consulta SQL que se va a ejecutar.
        """
        if self.conectado:
            print(f"[INFO] Ejecutando consulta en '{self.nombre_bd}': {consulta}")
        else:
            print("[ERROR] No se puede ejecutar la consulta. No hay conexión a la base de datos.")

    def __del__(self):
        """
        Destructor de la clase BaseDeDatos.
        Este método se encarga de "cerrar" la conexión a la base de datos de forma segura.
        """
        if self.conectado:
            print(f"[INFO] Cerrando conexión a la base de datos '{self.nombre_bd}'.")
            self.conectado = False
        print(f"[INFO] Objeto BaseDeDatos para '{self.nombre_bd}' destruido.")

# Demostración del uso de la clase BaseDeDatos
def main():
    """
    Función principal que muestra cómo funciona el constructor y destructor.
    Nombre del ejercicio: "Simulación de conexión a base de datos"
    """
    # Creamos una instancia de la clase BaseDeDatos
    base_datos = BaseDeDatos('mi_base_de_datos')

    # Realizamos algunas consultas simuladas
    base_datos.realizar_consulta("SELECT * FROM usuarios;")
    base_datos.realizar_consulta("INSERT INTO usuarios(nombre, edad) VALUES ('maycol', 28);")

    # Eliminamos el objeto manualmente para invocar el destructor
    del base_datos

    print("[INFO] Fin del programa.")

if __name__ == "__main__":
    main()
