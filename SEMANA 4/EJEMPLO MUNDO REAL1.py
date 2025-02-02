# Sistema de reservas para el hotel "El Gran Emperador"

# Clase que representa una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        """
        Inicializa los atributos de la habitación.
        :param numero: Número de la habitación
        :param tipo: Tipo de habitación (Ej. Simple, Doble, Suite)
        :param precio: Precio por noche
        """
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.esta_disponible = True  # Por defecto, todas las habitaciones están disponibles

    def __str__(self):
        return f"Habitación {self.numero} ({self.tipo}) - ${self.precio}/noche"

# Clase que representa un cliente
class Cliente:
    def __init__(self, nombre, identificacion):
        """
        Inicializa los atributos del cliente.
        :param nombre: Nombre del cliente
        :param identificacion: ID único del cliente
        """
        self.nombre = nombre
        self.identificacion = identificacion

    def __str__(self):
        return f"Cliente: {self.nombre} (ID: {self.identificacion})"

# Clase que representa una reserva
class Reserva:
    def __init__(self, habitacion, cliente, dias):
        """
        Inicializa una nueva reserva.
        :param habitacion: Objeto de tipo Habitacion reservado
        :param cliente: Objeto de tipo Cliente que realiza la reserva
        :param dias: Cantidad de noches reservadas
        """
        self.habitacion = habitacion
        self.cliente = cliente
        self.dias = dias
        self.total = habitacion.precio * dias

    def __str__(self):
        return (f"Reserva: {self.habitacion} por {self.cliente.nombre} "
                f"durante {self.dias} noche(s). Total: ${self.total}")

# Clase que representa el sistema de reservas del hotel
class SistemaDeReservas:
    def __init__(self):
        """Inicializa el sistema de reservas con listas de habitaciones y reservas."""
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        """Agrega una habitación al sistema."""
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        """Muestra todas las habitaciones disponibles para reserva."""
        print("Habitaciones disponibles:")
        for habitacion in self.habitaciones:
            if habitacion.esta_disponible:
                print(habitacion)

    def reservar_habitacion(self, numero_habitacion, cliente, dias):
        """
        Reserva una habitación para un cliente.
        :param numero_habitacion: Número de la habitación a reservar
        :param cliente: Objeto de tipo Cliente
        :param dias: Cantidad de noches
        """
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion and habitacion.esta_disponible:
                habitacion.esta_disponible = False
                reserva = Reserva(habitacion, cliente, dias)
                self.reservas.append(reserva)
                print("Reserva realizada con éxito:")
                print(reserva)
                return
        print("La habitación no está disponible o no existe.")

# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear el sistema de reservas
    sistema = SistemaDeReservas()

    # Agregar habitaciones al sistema
    sistema.agregar_habitacion(Habitacion(1, "Simple", 40))
    sistema.agregar_habitacion(Habitacion(2, "Doble", 60))
    sistema.agregar_habitacion(Habitacion(3, "Suite", 95))

    # Crear un cliente
    cliente1 = Cliente("Matias Lopez", "1724452559")

    # Mostrar habitaciones disponibles
    sistema.mostrar_habitaciones_disponibles()

    # Realizar una reserva
    sistema.reservar_habitacion(2, cliente1, 3)

    # Mostrar habitaciones disponibles nuevamente
    sistema.mostrar_habitaciones_disponibles()
