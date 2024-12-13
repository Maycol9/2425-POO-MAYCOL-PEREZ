#PROGRAMACION ORIENTADAS AOBJETOS
class Clima:
    """
    La Clase base que define comportamientos genéricos para datos del clima.
    Incluye un método genérico para calcular el promedio de una lista de valores.
    """

    def calcular_promedio(self, valores):
        # Verifica si la lista de valores está vacía.
        # Si es así, retorna 0.0 para evitar divisiones entre cero.
        if len(valores) == 0:
            return 0.0
        # Calcula el promedio sumando todos los valores y dividiéndolos
        # entre la cantidad de elementos en la lista.
        return sum(valores) / len(valores)


class ClimaSemanal(Clima):
    """
    Clase que representa el clima de una semana (7 días).
    Hereda de la clase 'Clima' para reutilizar el método calcular_promedio.
    """

    def __init__(self):
        # Se utiliza un atributo privado (__temperaturas) para almacenar las
        # temperaturas de los 7 días, manteniendo así la encapsulación.
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        """
        Método para ingresar las temperaturas diarias de una semana (7 días).
        Cada temperatura se solicita por teclado y se valida que sea un valor numérico.
        De no ser numérico, se vuelve a solicitar hasta obtener un valor válido.
        Todas las temperaturas ingresadas se guardan en __temperaturas.
        """
        for i in range(7):
            while True:
                try:
                    # Pide al usuario que ingrese la temperatura del día (i+1).
                    temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                    # Si es válido, se agrega a la lista de temperaturas.
                    self.__temperaturas.append(temp)
                    break
                except ValueError:
                    # Si ocurre un error de conversión (no es un número),
                    # se notifica y se solicita un nuevo ingreso.
                    print("Por favor, ingrese un valor numérico válido.")

    def obtener_promedio_semanal(self):
        """
        El método para obtener el promedio de las temperaturas de la semana.
        Se aprovecha el método 'calcular_promedio' heredado de la clase base 'Clima'.
        """
        # Invocamos el método de la clase padre para calcular el promedio
        # de la lista interna __temperaturas.
        return self.calcular_promedio(self.__temperaturas)


if __name__ == "__main__":
    # Se crea una instancia de ClimaSemanal
    clima_semana = ClimaSemanal()

    # Se ingresan las temperaturas por teclado
    clima_semana.ingresar_temperaturas()

    # Se calcula y muestra el promedio semanal de las temperaturas
    promedio = clima_semana.obtener_promedio_semanal()
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

