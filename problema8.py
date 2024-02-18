import requests
import sqlite3
from datetime import datetime

url_bitcoin = "https://api.coindesk.com/v1/bpi/currentprice.json"
response_bitcoin = requests.get(url_bitcoin)
data_bitcoin = response_bitcoin.json()

url_sunat = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
response_sunat = requests.get(url_sunat)
data_sunat = response_sunat.json()

bitcoin_usd = data_bitcoin['bpi']['USD']['rate_float']

tipo_cambio_pen = data_sunat['venta']

bitcoin_pen = bitcoin_usd * tipo_cambio_pen

conn = sqlite3.connect('base.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS bitcoin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT,
        precio_usd REAL,
        precio_gbp REAL,
        precio_eur REAL,
        precio_pen REAL
    )
''')

fecha_actual = datetime.now().strftime("%Y-%m-%d")

cursor.execute('''
    INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen)
    VALUES (?, ?, ?, ?, ?)
''', (fecha_actual, bitcoin_usd, 0, 0, bitcoin_pen))

conn.commit()

cursor.execute('SELECT * FROM bitcoin')
rows = cursor.fetchall()

print("\nContenido de la tabla 'bitcoin':")
for row in rows:
    print(row)

precio_compra_10_bitcoins_pen = 10 * row[4]  
precio_compra_10_bitcoins_eur = 10 * row[3]  

print(f"\nPrecio de comprar 10 bitcoins en PEN: {precio_compra_10_bitcoins_pen}")
print(f"Precio de comprar 10 bitcoins en EUR: {precio_compra_10_bitcoins_eur}")

conn.close()