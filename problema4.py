import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status() 
        data = response.json()
        precio_bitcoin = data["bpi"]["USD"]["rate_float"]
        return precio_bitcoin
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

def guardar_precio_en_archivo(precio, nombre_archivo="precio_bitcoin.txt"):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(f"Precio de Bitcoin: ${precio:,.4f}\n")

def main():
    try:
        precio_bitcoin = obtener_precio_bitcoin()

        if precio_bitcoin is not None:
            guardar_precio_en_archivo(precio_bitcoin)
            print(f"Precio actual de Bitcoin guardado en el archivo 'precio_bitcoin.txt'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()