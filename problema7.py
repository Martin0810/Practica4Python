import requests
import sqlite3

url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
response = requests.get(url)
data = response.json()

dolar_compra = data['compra']
dolar_venta = data['venta']

try:
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            compra REAL,
            venta REAL
        )
    ''')

    for fecha, valores in data['historico'].items():
        cursor.execute('''
            INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)
        ''', (fecha, valores['compra'], valores['venta']))

    conn.commit()

    print("Datos almacenados en la base de datos 'base.db'.")

except sqlite3.Error as e:
    print(f"Error al interactuar con la base de datos: {e}")

finally:
    if conn:
        conn.close()

try:
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM sunat_info')
    rows = cursor.fetchall()

    print("\nContenido de la tabla 'sunat_info':")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print(f"Error al interactuar con la base de datos: {e}")

finally:
    if conn:
        conn.close()