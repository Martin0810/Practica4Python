from pyfiglet import Figlet
import random

def obtener_fuentes_disponibles():
    figlet = Figlet()
    return figlet.getFonts()

def seleccionar_fuente_aleatoria():
    fuentes_disponibles = obtener_fuentes_disponibles()
    return random.choice(fuentes_disponibles)

def main():
    try:
        fuente_usuario = input("Ingrese el nombre de la fuente (deje en blanco para seleccionar aleatoriamente): ").strip()

        if not fuente_usuario:
            fuente_seleccionada = seleccionar_fuente_aleatoria()
        else:
            fuente_seleccionada = fuente_usuario

        figlet = Figlet(font=fuente_seleccionada)

        texto_usuario = input("Ingrese el texto que desea imprimir: ")

        texto_formateado = figlet.renderText(texto_usuario)
        print(texto_formateado)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()