def contar_lineas_codigo(ruta_archivo):
    try:
        if not ruta_archivo.endswith('.py'):
            raise ValueError("El archivo no tiene extensión .py")

        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()

        contador_lineas = 0

        for linea in lineas:
            linea = linea.strip()
            
            if linea != '' and not linea.startswith('#'):
                contador_lineas += 1

        return contador_lineas

    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

    return 0

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    cantidad_lineas = contar_lineas_codigo(ruta_archivo)

    if cantidad_lineas > 0:
        print(f"El archivo {ruta_archivo} tiene {cantidad_lineas} líneas de código.")
    else:
        print("No se pudo determinar la cantidad de líneas de código.")

if __name__ == "__main__":
    main()