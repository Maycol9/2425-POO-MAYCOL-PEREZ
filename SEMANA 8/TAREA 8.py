import os
import subprocess
import datetime


def registrar_log(mensaje):
    """Registra un mensaje en un archivo de log con la fecha y hora actual."""
    with open("dashboard_log.txt", "a") as log:
        log.write(f"[{datetime.datetime.now()}] {mensaje}\n")


def mostrar_codigo(ruta_script):
    """Muestra el código fuente de un script dado."""
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
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


def ejecutar_codigo(ruta_script, argumentos=""):
    """Ejecuta un script de Python con opción de agregar argumentos."""
    try:
        comando = f"python {ruta_script} {argumentos}" if os.name == 'nt' else f"python3 {ruta_script} {argumentos}"
        subprocess.Popen(comando, shell=True)
        registrar_log(f"Ejecutado: {ruta_script} con argumentos: {argumentos}")
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")
        registrar_log(f"Error al ejecutar {ruta_script}: {e}")


def mostrar_menu():
    """Muestra el menú principal del dashboard."""
    ruta_base = os.path.dirname(__file__)
    unidades = {'1': 'Unidad 1', '2': 'Unidad 2'}

    print("\n========== BIENVENIDO AL DASHBOARD DE PROYECTOS ==========")
    while True:
        print("\nMenú Principal")
        for key, nombre in unidades.items():
            print(f"{key} - {nombre}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("⚠ Opción no válida. Inténtalo de nuevo.")


def mostrar_sub_menu(ruta_unidad):
    """Muestra el submenú de carpetas dentro de una unidad."""
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        try:
            indice = int(eleccion_carpeta) - 1
            if 0 <= indice < len(sub_carpetas):
                mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[indice]))
            else:
                print("⚠ Opción no válida. Inténtalo de nuevo.")
        except ValueError:
            print("⚠ Entrada inválida. Introduce un número válido.")


def mostrar_scripts(ruta_sub_carpeta):
    """Muestra los scripts disponibles y permite ejecutarlos."""
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\nScripts disponibles:")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar")

        eleccion_script = input("Elige un script o '0' para regresar: ")
        if eleccion_script == '0':
            break
        try:
            indice = int(eleccion_script) - 1
            if 0 <= indice < len(scripts):
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
                mostrar_codigo(ruta_script)
                ejecutar = input("¿Deseas ejecutar el script? (1: Sí, 0: No): ")
                if ejecutar == '1':
                    argumentos = input("Introduce argumentos si es necesario (o deja en blanco): ")
                    ejecutar_codigo(ruta_script, argumentos)
                input("Presiona Enter para continuar...")
            else:
                print("⚠ Opción no válida.")
        except ValueError:
            print("⚠ Entrada inválida.")


if __name__ == "__main__":
    mostrar_menu()
