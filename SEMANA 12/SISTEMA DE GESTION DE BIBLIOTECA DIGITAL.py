import json

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def to_dict(self):
        return {"titulo": self.titulo, "autor": self.autor, "categoria": self.categoria, "isbn": self.isbn}

class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.prestamos = []

    def to_dict(self):
        return {"nombre": self.nombre, "user_id": self.user_id, "prestamos": [libro.isbn for libro in self.prestamos]}

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios = {}
        self.ids_usuarios = set()
        self.cargar_datos()

    def guardar_datos(self):
        datos = {
            "libros": {isbn: libro.to_dict() for isbn, libro in self.libros_disponibles.items()},
            "usuarios": {user_id: usuario.to_dict() for user_id, usuario in self.usuarios.items()}
        }
        with open("biblioteca.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)

    def cargar_datos(self):
        try:
            with open("biblioteca.json", "r") as archivo:
                datos = json.load(archivo)
                for isbn, info in datos.get("libros", {}).items():
                    self.libros_disponibles[isbn] = Libro(**info)
                for user_id, info in datos.get("usuarios", {}).items():
                    usuario = Usuario(info["nombre"], user_id)
                    usuario.prestamos = [self.libros_disponibles[isbn] for isbn in info["prestamos"] if isbn in self.libros_disponibles]
                    self.usuarios[user_id] = usuario
                    self.ids_usuarios.add(user_id)
        except FileNotFoundError:
            pass

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        self.guardar_datos()
        print(f"Libro '{libro.titulo}' agregado.")

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.user_id] = usuario
        self.ids_usuarios.add(usuario.user_id)
        self.guardar_datos()
        print(f"Usuario '{usuario.nombre}' registrado.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros_disponibles:
            usuario = self.usuarios[user_id]
            libro = self.libros_disponibles.pop(isbn)
            usuario.prestamos.append(libro)
            self.guardar_datos()
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.prestamos:
                if libro.isbn == isbn:
                    usuario.prestamos.remove(libro)
                    self.libros_disponibles[isbn] = libro
                    self.guardar_datos()
                    print(f"Libro '{libro.titulo}' devuelto.")
                    return

    def buscar_libro(self, criterio, valor):
        return [libro.titulo for libro in self.libros_disponibles.values() if getattr(libro, criterio, None) == valor]

    def listar_libros_prestados(self):
        libros_prestados = []
        for usuario in self.usuarios.values():
            for libro in usuario.prestamos:
                libros_prestados.append(f"{libro.titulo} - {usuario.nombre}")
        return libros_prestados

    def mostrar_libros(self):
        return "\n".join([f"{libro.titulo} - {libro.autor} ({libro.categoria})" for libro in self.libros_disponibles.values()])

    def mostrar_usuarios(self):
        return [f"{usuario.nombre} (ID: {usuario.user_id})" for usuario in self.usuarios.values()]

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n1. Agregar libro")
        print("2. Registrar usuario")
        print("3. Mostrar libros")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Mostrar usuarios")
        print("7. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblioteca.agregar_libro(Libro(titulo, autor, categoria, isbn))
        elif opcion == "2":
            nombre = input("Nombre del usuario: ")
            user_id = input("ID del usuario: ")
            biblioteca.registrar_usuario(Usuario(nombre, user_id))
        elif opcion == "3":
            print("\nLibros disponibles:")
            print(biblioteca.mostrar_libros())
            print("\nLibros prestados:")
            libros_prestados = biblioteca.listar_libros_prestados()
            print("\n".join(libros_prestados) if libros_prestados else "No hay libros prestados.")
        elif opcion == "4":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.prestar_libro(user_id, isbn)
        elif opcion == "5":
            user_id = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.devolver_libro(user_id, isbn)
        elif opcion == "6":
            print("Usuarios registrados:")
            print("\n".join(biblioteca.mostrar_usuarios()))
        elif opcion == "7":
            biblioteca.guardar_datos()
            print("Datos guardados. Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()

