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

def main():
    try:
        cantidad_bitcoins = float(input("Ingrese la cantidad de Bitcoins que posee: "))
        if cantidad_bitcoins < 0:
            print("La cantidad de Bitcoins no puede ser negativa.")
            return

        precio_bitcoin = obtener_precio_bitcoin()

        if precio_bitcoin is not None:
            costo_en_usd = cantidad_bitcoins * precio_bitcoin
            print(f"El costo actual de {cantidad_bitcoins:.8f} Bitcoins es: ${costo_en_usd:,.4f}")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido para la cantidad de Bitcoins.")

if __name__ == "__main__":
    main()