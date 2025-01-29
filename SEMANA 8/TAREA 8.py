import os
import subprocess


def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_codigo(ruta_script):
    """Muestra el contenido del script."""
    ruta_script = os.path.abspath(ruta_script)
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
        print(f"\n--- Código de {ruta_script} ---\n")
        print(codigo)
        return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    """Ejecuta el script en una nueva ventana de terminal."""
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Sistemas Unix (Linux, macOS, etc.)
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


def mostrar_menu():
    """Muestra el menú principal con las opciones de semana."""
    # Se toma la ruta base del directorio donde se encuentra este script
    ruta_base = os.path.dirname(os.path.abspath(__file__))

    # Diccionario con las semanas (del 2 al 8)
    semanas = {
        '1': 'Semana 2',
        '2': 'Semana 3',
        '3': 'Semana 4',
        '4': 'Semana 5',
        '5': 'Semana 6',
        '6': 'Semana 7',
        '7': 'Semana 8'
    }

    while True:
        limpiar_pantalla()
        print("=== Menú Principal - Dashboard ===")
        for key, semana in semanas.items():
            print(f"{key} - {semana}")
        print("0 - Salir")

        eleccion = input("Elige una semana o '0' para salir: ")
        if eleccion == '0':
            print("Saliendo del programa.")
            break
        elif eleccion in semanas:
            ruta_semana = os.path.join(ruta_base, semanas[eleccion])
            if os.path.exists(ruta_semana) and os.path.isdir(ruta_semana):
                mostrar_sub_menu(ruta_semana)
            else:
                print(f"La carpeta '{semanas[eleccion]}' no existe en la ruta base.")
                input("Presiona Enter para continuar...")
        else:
            print("Opción no válida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")


def mostrar_sub_menu(ruta_semana):
    """
    Muestra el submenú correspondiente a la carpeta de la semana seleccionada,
    listando las subcarpetas disponibles.
    """
    # Se listan las subcarpetas y se ordenan alfabéticamente
    subcarpetas = sorted([entry.name for entry in os.scandir(ruta_semana) if entry.is_dir()])

    while True:
        limpiar_pantalla()
        print(f"=== {os.path.basename(ruta_semana)} - Submenú ===")
        for idx, carpeta in enumerate(subcarpetas, start=1):
            print(f"{idx} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion = input("Elige una opción: ")
        if eleccion == '0':
            break
        try:
            indice = int(eleccion) - 1
            if 0 <= indice < len(subcarpetas):
                ruta_subcarpeta = os.path.join(ruta_semana, subcarpetas[indice])
                mostrar_scripts(ruta_subcarpeta)
            else:
                print("Opción no válida.")
                input("Presiona Enter para continuar...")
        except ValueError:
            print("Opción no válida.")
            input("Presiona Enter para continuar...")


def mostrar_scripts(ruta_subcarpeta):
    """
    Muestra los scripts (archivos .py) disponibles en la subcarpeta
    y permite visualizarlos y ejecutarlos.
    """
    # Se listan los scripts y se ordenan alfabéticamente
    scripts = sorted([entry.name for entry in os.scandir(ruta_subcarpeta)
                      if entry.is_file() and entry.name.endswith('.py')])

    while True:
        limpiar_pantalla()
        print(f"=== {os.path.basename(ruta_subcarpeta)} - Scripts ===")
        for idx, script in enumerate(scripts, start=1):
            print(f"{idx} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion = input("Elige un script: ")
        if eleccion == '0':
            break
        elif eleccion == '9':
            return  # Regresa al menú principal
        try:
            indice = int(eleccion) - 1
            if 0 <= indice < len(scripts):
                ruta_script = os.path.join(ruta_subcarpeta, scripts[indice])
                limpiar_pantalla()
                codigo = mostrar_codigo(ruta_script)
                if codigo is not None:
                    ejecutar = input("\n¿Desea ejecutar el script? (1: Sí, 0: No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta_script)
                    elif ejecutar == '0':
                        print("No se ejecutó el script.")
                    else:
                        print("Opción no válida. Regresando al menú de scripts.")
                    input("\nPresiona Enter para continuar...")
            else:
                print("Opción no válida.")
                input("Presiona Enter para continuar...")
        except ValueError:
            print("Opción no válida.")
            input("Presiona Enter para continuar...")


if __name__ == "__main__":
    mostrar_menu()

