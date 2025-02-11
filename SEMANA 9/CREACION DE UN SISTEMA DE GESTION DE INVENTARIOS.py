#Sistema de Gestion de Inventrios#
# La clase Producto representa un producto individual en el inventario.
# Cada producto tiene un identificador único (id_producto), un nombre, una cantidad en existencia
# y un precio unitario. Se proporcionan métodos *getter* para acceder a sus atributos y
# métodos *setter* para modificarlos de forma controlada.
# Además, el método especial __str__ define la representación en cadena del producto.
# ============================================================#

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        Inicializa el producto con los siguientes atributos:
        - id_producto: Identificador único del producto.
        - nombre: Nombre descriptivo del producto.
        - cantidad: Cantidad en existencia.
        - precio: Precio unitario del producto.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        """Devuelve el identificador único del producto."""
        return self.id_producto

    def get_nombre(self):
        """Devuelve el nombre del producto."""
        return self.nombre

    def get_cantidad(self):
        """Devuelve la cantidad en existencia del producto."""
        return self.cantidad

    def get_precio(self):
        """Devuelve el precio unitario del producto."""
        return self.precio

    def set_cantidad(self, cantidad):
        """Actualiza la cantidad en existencia del producto."""
        self.cantidad = cantidad

    def set_precio(self, precio):
        """Actualiza el precio unitario del producto."""
        self.precio = precio

    def __str__(self):
        """
        Representación en cadena del producto.
        Muestra el ID, nombre, cantidad y precio (formateado a dos decimales).
        """
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"


# ============================================================
# Clase Inventario#
# ============================================================
# La clase Inventario gestiona una colección de productos.
# Proporciona métodos para añadir, eliminar, actualizar, buscar y mostrar productos.
# Se asegura de que no se puedan agregar productos con IDs duplicados y maneja
# las operaciones con mensajes informativos para el usuario.
# ============================================================

class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa la lista 'productos' para almacenar objetos de tipo Producto.
        """
        self.productos = []

    def añadir_producto(self, producto):
        """
        Añade un producto al inventario.
        Antes de añadirlo, verifica que no exista ya otro producto con el mismo ID.
        Si el ID ya existe, se muestra un mensaje de error; de lo contrario, se añade el producto.
        """
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario identificándolo por su ID.
        Recorre la lista de productos y, si encuentra el producto, lo elimina y muestra un mensaje de éxito.
        Si no se encuentra el producto, se imprime un mensaje de error.
        """
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                print("Producto eliminado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza los atributos de un producto (cantidad y/o precio) identificado por su ID.
        Si se encuentra el producto:
          - Actualiza la cantidad si se proporciona un nuevo valor.
          - Actualiza el precio de manera similar.
        Si el producto no se encuentra, se muestra un mensaje de error.
        """
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """
        Busca productos cuyo nombre contenga la cadena proporcionada.
        La búsqueda no distingue entre mayúsculas y minúsculas.
        Devuelve una lista con todos los productos que coinciden con el criterio de búsqueda.
        """
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        """
        Muestra todos los productos presentes en el inventario.
        Si no hay productos, informa que el inventario se encuentra vacío.
        """
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos:
                print(producto)


# ============================================================
# Función menu
# ============================================================
# La función menu implementa una interfaz de usuario en modo consola para gestionar el inventario.
# Permite al usuario:
# 1. Añadir un producto.
# 2. Eliminar un producto.
# 3. Actualizar un producto.
# 4. Buscar productos por nombre.
# 5. Mostrar todos los productos.
# 6. Salir del sistema.
#
# Cada opción solicita los datos necesarios al usuario y llama al método correspondiente
# del objeto Inventario para realizar la acción solicitada.
# ============================================================

def menu():
    """
    Función principal que ejecuta el menú interactivo de gestión de inventario.
    """
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Se solicitan los datos necesarios para crear un nuevo producto.
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            # Se solicita el ID del producto a eliminar.
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            # Se solicita el ID del producto a actualizar y los nuevos valores para cantidad y/o precio.
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje vacío si no desea cambiar): ")
            precio = input("Ingrese el nuevo precio (deje vacío si no desea cambiar): ")
            # Se convierten los valores a int/float si el usuario ingresó datos, de lo contrario se asigna None.
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == '4':
            # Se solicita el nombre del producto a buscar.
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos.")

        elif opcion == '5':
            # Se muestran todos los productos existentes en el inventario.
            inventario.mostrar_productos()

        elif opcion == '6':
            # Se finaliza la ejecución del programa.
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# ============================================================
# Bloque principal
# ============================================================
# La siguiente condición verifica que el script se ejecute directamente.
# Si se ejecuta, se llama a la función menu() para iniciar el sistema de gestión de inventarios.
# ============================================================

if __name__ == "__main__":
    menu()
