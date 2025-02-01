import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'SEMANA 2/TAREA 2.py',
        '2': 'SEMANA 3/TAREA EJEMPLO DE PROGRAMACION ORIENTADAS A OBJETOS.py',
        '3': 'SEMANA 3/TAREA EJEMPLO DE PROGRAMACION TRADICIONAL.py',
        '4': 'SEMANA 4/EJEMPLO MUNDO REAL1.py',
        '5': 'SEMANA 5/CREACION DE UN PROGRAMA.py',
        '6': 'SEMANA 6/APLICAR CONCEPTOS BASICOS DE POO.py',
        '7': 'SEMANA 7/DETALLAR  EL USO DE CONSTRUCTURES Y DESTRUCTORES EN PYTHON.py'

    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()