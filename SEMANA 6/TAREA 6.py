# TAREA: Aplicar los conceptos de POO: Clase, Objeto, Herencia, Encapsulación y Polimorfismo.

# Clase base: Persona
# Esta clase representa una persona genérica y contiene atributos comunes como nombre y edad.
# Además, demuestra la encapsulación mediante el uso de un atributo privado.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público que puede ser accedido directamente.
        self.__edad = edad  # Atributo privado que solo puede ser accedido a través de métodos específicos.

    def obtener_edad(self):
        """
        Método público para acceder al atributo privado __edad.
        Este método implementa el concepto de encapsulación.
        """
        return self.__edad

    def mostrar_informacion(self):
        """
        Método que devuelve información básica de la persona.
        Este método será sobrescrito en las clases derivadas para demostrar polimorfismo.
        """
        return f"Nombre: {self.nombre}, Edad: {self.__edad}"


# Clase derivada: Empleado (Hereda de Persona)
# Esta clase específica representa a un empleado, extendiendo las características de Persona.
class Empleado(Persona):
    def __init__(self, nombre, edad, salario, puesto):
        # Llamada al constructor de la clase base para inicializar los atributos heredados.
        super().__init__(nombre, edad)
        self.salario = salario  # Atributo adicional para el salario del empleado.
        self.puesto = puesto  # Atributo adicional para el puesto del empleado.

    # Sobrescritura del método mostrar_informacion para incluir detalles específicos del empleado.
    def mostrar_informacion(self):
        """
        Sobrescritura del método mostrar_informacion de la clase base.
        Demuestra polimorfismo al modificar el comportamiento del método en esta clase derivada.
        """
        info_persona = super().mostrar_informacion()  # Reutiliza el método de la clase base.
        return f"{info_persona}, Puesto: {self.puesto}, Salario: ${self.salario}"


# Clase adicional: Gerente (Hereda de Empleado)
# Representa un gerente, con atributos adicionales específicos como el departamento que lidera.
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, puesto, departamento):
        # Llamada al constructor de Empleado para inicializar los atributos heredados.
        super().__init__(nombre, edad, salario, puesto)
        self.departamento = departamento  # Atributo adicional para el departamento del gerente.

    # Sobrescritura del método mostrar_informacion para incluir el departamento.
    def mostrar_informacion(self):
        """
        Sobrescritura del método mostrar_informacion.
        Agrega detalles adicionales específicos del gerente, demostrando nuevamente el polimorfismo.
        """
        info_empleado = super().mostrar_informacion()  # Reutiliza el método de la clase derivada.
        return f"{info_empleado}, Departamento: {self.departamento}"


# Función principal para demostrar el uso de las clases.
def main():
    # Creación de instancias de las clases:
    # - Una instancia de Persona para representar una persona genérica.
    # - Una instancia de Empleado para un trabajador específico.
    # - Una instancia de Gerente para un líder de equipo.
    persona = Persona("Luis Fernández", 35)
    empleado = Empleado("María López", 25, 1800, "Desarrolladora")
    gerente = Gerente("Roberto Martínez", 45, 4000, "Director de Proyecto", "Innovación")

    # Demostración de las funcionalidades:
    # Mostrar información general de cada tipo de objeto, utilizando el concepto de herencia y polimorfismo.
    print("Información de la Persona:")
    print(persona.mostrar_informacion())
    print("\nInformación del Empleado:")
    print(empleado.mostrar_informacion())
    print("\nInformación del Gerente:")
    print(gerente.mostrar_informacion())

    # Ejemplo de encapsulación:
    # Accediendo al atributo privado __edad mediante el método público obtener_edad.
    print("\nDemostración de encapsulación:")
    print(f"Edad del Gerente (accediendo mediante un método): {gerente.obtener_edad()}")


# Punto de entrada del programa.
# Este bloque asegura que el código se ejecute solo si el archivo es ejecutado directamente.
if __name__ == "__main__":
    main()

