# Programa para realizar cálculos matemáticos y conversiones de temperatura
# Autor: [Maycol Perez]
# Descripción: Este programa permite al usuario calcular el área de un círculo proporcionando el radio,
# una tarea común en geometría, y convertir temperaturas de grados Celsius a Fahrenheit,
# una conversión útil en la vida cotidiana y científica. Además, se utiliza una estructura clara y modular
# que facilita la comprensión y el mantenimiento del código.

import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    :param radio: float - Radio del círculo
    :return: float - Área del círculo
    """
    return math.pi * (radio ** 2)

def convertir_celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.

    :param celsius: float - Temperatura en grados Celsius
    :return: float - Temperatura en grados Fahrenheit
    """
    return (celsius * 9/5) + 32

def main():
    """
    Función principal que ejecuta el programa.
    """
    print("\n--- Calculadora básica ---\n")

    # Solicitar al usuario el radio del círculo
    radio = float(input("Ingrese el radio del círculo: "))
    area_circulo = calcular_area_circulo(radio)
    print(f"El área del círculo con radio {radio} es: {area_circulo:.2f}")

    # Solicitar al usuario la temperatura en grados Celsius
    celsius = float(input("\nIngrese la temperatura en grados Celsius: "))
    fahrenheit = convertir_celsius_a_fahrenheit(celsius)
    print(f"{celsius} °C equivale a {fahrenheit:.2f} °F")

# Ejecución del programa principal
if __name__ == "__main__":
    main()
