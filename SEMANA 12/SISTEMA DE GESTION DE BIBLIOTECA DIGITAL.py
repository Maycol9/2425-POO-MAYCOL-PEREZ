# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Se utiliza una tupla para almacenar los atributos inmutables: título y autor.
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        # Devuelve una cadena con la información relevante del libro.
        return f"Libro: {self.info[0]} de {self.info[1]} | Categoría: {self.categoria} | ISBN: {self.isbn}"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        # ID de usuario único.
        self.id_usuario = id_usuario
        # Lista de libros actualmente prestados.
        self.libros_prestados = []

    def __str__(self):
        # Muestra la información del usuario y la cantidad de libros prestados.
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}) | Libros prestados: {len(self.libros_prestados)}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        # Diccionario para almacenar los libros disponibles con ISBN como clave.
        self.libros = {}
        # Diccionario para almacenar usuarios registrados con el ID como clave.
        self.usuarios = {}
        # Conjunto para asegurar que los IDs de usuario sean únicos.
        self.ids_usuarios = set()

    # Función para añadir un libro a la biblioteca.
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.info[0]}' agregado exitosamente.")

    # Función para quitar un libro de la biblioteca.
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)
            print(f"Libro '{libro.info[0]}' eliminado de la biblioteca.")
        else:
            print("No se encontró el libro con ese ISBN.")

    # Función para registrar un nuevo usuario.
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado exitosamente.")

    # Función para dar de baja a un usuario.
    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print("El usuario tiene libros prestados. Debe devolverlos antes de darse de baja.")
            else:
                del self.usuarios[id_usuario]
                self.ids_usuarios.remove(id_usuario)
                print(f"Usuario '{usuario.nombre}' dado de baja.")
        else:
            print("No se encontró un usuario con ese ID.")

    # Función para prestar un libro a un usuario.
    def prestar_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios:
            print("El usuario no está registrado en la biblioteca.")
            return

        if isbn not in self.libros:
            print("El libro no está disponible para préstamo.")
            return

        # Se retira el libro del diccionario de libros disponibles.
        libro = self.libros.pop(isbn)
        self.usuarios[id_usuario].libros_prestados.append(libro)
        print(f"El libro '{libro.info[0]}' ha sido prestado al usuario '{self.usuarios[id_usuario].nombre}'.")

    # Función para devolver un libro.
    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios:
            print("El usuario no está registrado.")
            return

        usuario = self.usuarios[id_usuario]
        # Se busca el libro en la lista de libros prestados del usuario.
        libro_encontrado = None
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                libro_encontrado = libro
                break

        if libro_encontrado:
            usuario.libros_prestados.remove(libro_encontrado)
            # Se vuelve a agregar el libro a la colección de libros disponibles.
            self.libros[isbn] = libro_encontrado
            print(f"El libro '{libro_encontrado.info[0]}' ha sido devuelto a la biblioteca.")
        else:
            print("El usuario no tiene este libro en préstamo.")

    # Función para buscar libros por título.
    def buscar_libro_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros.values() if libro.info[0].lower() == titulo.lower()]
        return resultados

    # Función para buscar libros por autor.
    def buscar_libro_por_autor(self, autor):
        resultados = [libro for libro in self.libros.values() if libro.info[1].lower() == autor.lower()]
        return resultados

    # Función para buscar libros por categoría.
    def buscar_libro_por_categoria(self, categoria):
        resultados = [libro for libro in self.libros.values() if libro.categoria.lower() == categoria.lower()]
        return resultados

    # Función para listar todos los libros prestados a un usuario.
    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios:
            print("El usuario no está registrado.")
            return []
        return self.usuarios[id_usuario].libros_prestados


# --- Ejemplo de uso del sistema de biblioteca digital ---
if __name__ == "__main__":
    # Crear instancia de Biblioteca
    biblioteca = Biblioteca()

    # Crear algunos libros con los nuevos nombres
    libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "ISBN001")
    libro2 = Libro("Don Quijote", "Miguel de Cervantes", "Novela", "ISBN002")
    libro3 = Libro("Domina tus emosiones", "Thibaut Meurisse", "Autoayuda", "ISBN003")

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Registrar usuarios con nuevos nombres
    usuario1 = Usuario("Carlos", "U001")
    usuario2 = Usuario("Mariana", "U002")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar un libro a Carlos
    biblioteca.prestar_libro("ISBN001", "U001")
    # Intentar prestar un libro que no está disponible (ya prestado)
    biblioteca.prestar_libro("ISBN001", "U002")

    # Listar libros prestados a Carlos
    libros_carlos = biblioteca.listar_libros_prestados("U001")
    print("\nLibros prestados a Carlos:")
    for libro in libros_carlos:
        print(libro)

    # Devolver el libro por Carlos
    biblioteca.devolver_libro("ISBN001", "U001")

    # Buscar libros por categoría (por ejemplo, 'Novela')
    resultados_novela = biblioteca.buscar_libro_por_categoria("novela")
    print("\nLibros disponibles en la categoría 'Novela':")
    for libro in resultados_novela:
        print(libro)

    # Quitar un libro de la biblioteca
    biblioteca.quitar_libro("ISBN002")

    # Intentar dar de baja a un usuario que tiene libros en préstamo
    biblioteca.prestar_libro("ISBN003", "U002")
    biblioteca.dar_de_baja_usuario("U002")  # Mariana tiene un libro prestado, no podrá darse de baja

    # Devolver el libro para poder dar de baja al usuario
    biblioteca.devolver_libro("ISBN003", "U002")
    biblioteca.dar_de_baja_usuario("U002")
