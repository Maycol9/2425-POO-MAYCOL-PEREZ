import json
# Sistema Avanzado de Gestión de Inventario
# Este programa permite administrar productos en un inventario mediante Programación Orientada a Objetos (POO).
# Utiliza colecciones como diccionarios para almacenar productos y archivos JSON para persistencia de datos.

class Producto:
    # Representa un producto con ID único, nombre, cantidad y precio.
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        # Método para actualizar la cantidad del producto
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        # Método para actualizar el precio del producto
        self.precio = nuevo_precio

    def to_dict(self):
        # Convierte el objeto Producto en un diccionario para su almacenamiento
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


class Inventario:
    # Clase que gestiona los productos dentro del inventario
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos por ID
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        # Agrega un producto al inventario si no existe
        if producto.id_producto in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()
            print("Producto agregado con éxito.")

    def eliminar_producto(self, id_producto):
        # Elimina un producto del inventario si existe
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualiza la cantidad o el precio de un producto si existe en el inventario
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_en_archivo()
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Busca productos por nombre y muestra los resultados
        resultados = [prod for prod in self.productos.values() if nombre.lower() in prod.nombre.lower()]
        if resultados:
            for prod in resultados:
                print(
                    f"ID: {prod.id_producto}, Nombre: {prod.nombre}, Cantidad: {prod.cantidad}, Precio: ${prod.precio}")
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        # Muestra todos los productos almacenados en el inventario
        if self.productos:
            for prod in self.productos.values():
                print(
                    f"ID: {prod.id_producto}, Nombre: {prod.nombre}, Cantidad: {prod.cantidad}, Precio: ${prod.precio}")
        else:
            print("El inventario está vacío.")

    def guardar_en_archivo(self):
        # Guarda el inventario en un archivo JSON para persistencia de datos
        with open("inventario.json", "w") as archivo:
            json.dump({id: prod.to_dict() for id, prod in self.productos.items()}, archivo, indent=4)

    def cargar_desde_archivo(self):
        # Carga el inventario desde un archivo JSON al iniciar el programa
        try:
            with open("inventario.json", "r") as archivo:
                datos = json.load(archivo)
                self.productos = {id: Producto(**prod) for id, prod in datos.items()}
        except FileNotFoundError:
            self.productos = {}


# Interfaz de Usuario
def menu():
    # Menú interactivo para gestionar el inventario mediante la consola
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


if __name__ == "__main__":
    menu()
