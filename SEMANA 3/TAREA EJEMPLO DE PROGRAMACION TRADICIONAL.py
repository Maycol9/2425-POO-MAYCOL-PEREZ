#PROGRAMACION TRADICIONAL
def ingresar_temperaturas():
    """
    Esta es la función para ingresar las temperaturas diarias
    donde se Solicita al usuario las temperaturas para 7 días mediante un bucle que se repite 7 veces.
    Cada temperatura ingresada se valida para asegurarse de que sea un valor numérico.
    En caso de un valor no válido, se vuelve a pedir el dato.
    Finalmente, se retorna una lista con las 7 temperaturas.
    """
    temperaturas = []
    for i in range(7):
        while True:
            try:
                # Se solicita la temperatura del día i+1
                temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                # Si es válida, se agrega a la lista y se rompe el bucle interno
                temperaturas.append(temp)
                break
            except ValueError:
                # Si hay error al convertir a float, se pide nuevamente el dato
                print("Por favor, ingrese un valor numérico válido.")
    return temperaturas


def calcular_promedio(temperaturas):
    """
    Función para calcular el promedio de una lista de temperaturas.
    Primero comprueba si la lista está vacía. De estarlo, retorna 0.0.
    De lo contrario, realiza la suma de todos los valores y divide entre la cantidad de elementos.
    Devuelve el promedio calculado
    """
    if len(temperaturas) == 0:
        return 0.0
    return sum(temperaturas) / len(temperaturas)


# Programa principal
if __name__ == "__main__":
    # Se obtienen las temperaturas de los 7 días de la semana mediante la función ingresar_temperaturas
    temps = ingresar_temperaturas()

    # Se calcula el promedio semanal de la lista de temperaturas obtenidas
    promedio_semana = calcular_promedio(temps)

    # Se muestra el promedio semanal con dos decimales
    print(f"El promedio semanal de las temperaturas es: {promedio_semana:.2f}°C")
