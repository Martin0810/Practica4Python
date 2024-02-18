def guardar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", 'w') as archivo:
            for i in range(1, 11):
                resultado = numero * i
                archivo.write(f"{numero} x {i} = {resultado}\n")
        print(f"Tabla de multiplicar {numero} guardada en tabla-{numero}.txt")
    except Exception as e:
        print(f"Error al guardar la tabla de multiplicar: {e}")

def mostrar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", 'r') as archivo:
            contenido = archivo.read()
            print(f"Tabla de multiplicar {numero}:\n{contenido}")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")
    except Exception as e:
        print(f"Error al mostrar la tabla de multiplicar: {e}")

def mostrar_linea_tabla_multiplicar(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", 'r') as archivo:
            lineas = archivo.readlines()
            if 1 <= linea <= len(lineas):
                print(f"Línea {linea}: {lineas[linea - 1].strip()}")
            else:
                print(f"Línea {linea} no válida para la tabla de multiplicar {numero}")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")
    except Exception as e:
        print(f"Error al mostrar la línea de la tabla de multiplicar: {e}")

def main():
    while True:
        print("\nMenú:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= numero <= 10:
                guardar_tabla_multiplicar(numero)
            else:
                print("Número no válido. Debe estar entre 1 y 10.")
        elif opcion == "2":
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            mostrar_tabla_multiplicar(numero)
        elif opcion == "3":
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea a mostrar: "))
            mostrar_linea_tabla_multiplicar(numero, linea)
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()