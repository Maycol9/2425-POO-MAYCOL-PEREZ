import json

# Definición de la clase Producto
class Producto:
    # Constructor de la clase Producto con ID, nombre, cantidad y precio
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Método para actualizar la cantidad de un producto
    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    # Método para actualizar el precio de un producto
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Método para convertir un objeto Producto a un diccionario para su almacenamiento
    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


# Definición de la clase Inventario para gestionar los productos
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar los productos
        self.cargar_desde_archivo()  # Cargar productos desde un archivo al iniciar

    # Método para agregar un producto al inventario
    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()  # Guardar los cambios en el archivo
            print("Producto agregado con éxito.")

    # Método para eliminar un producto del inventario
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()  # Guardar cambios en el archivo
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    # Método para actualizar la cantidad o el precio de un producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_en_archivo()  # Guardar los cambios en el archivo
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    # Método para buscar productos por nombre
    def buscar_producto(self, nombre):
        resultados = [prod for prod in self.productos.values() if nombre.lower() in prod.nombre.lower()]
        if resultados:
            for prod in resultados:
                print(
                    f"ID: {prod.id_producto}, Nombre: {prod.nombre}, Cantidad: {prod.cantidad}, Precio: ${prod.precio}")
        else:
            print("No se encontraron productos con ese nombre.")

    # Método para mostrar todos los productos del inventario
    def mostrar_productos(self):
        if self.productos:
            for prod in self.productos.values():
                print(
                    f"ID: {prod.id_producto}, Nombre: {prod.nombre}, Cantidad: {prod.cantidad}, Precio: ${prod.precio}")
        else:
            print("El inventario está vacío.")

    # Método para guardar los productos en un archivo JSON
    def guardar_en_archivo(self):
        with open("inventario.json", "w") as archivo:
            json.dump({id: prod.to_dict() for id, prod in self.productos.items()}, archivo, indent=4)

    # Método para cargar los productos desde un archivo JSON
    def cargar_desde_archivo(self):
        try:
            with open("inventario.json", "r") as archivo:
                datos = json.load(archivo)
                self.productos = {id: Producto(**prod) for id, prod in datos.items()}
        except FileNotFoundError:
            self.productos = {}


# Función que maneja el menú interactivo en la consola
def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no desea cambiar): ")
            precio = input("Nuevo precio (dejar en blanco si no desea cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


# Punto de entrada principal del programa
if __name__ == "__main__":
    menu()
