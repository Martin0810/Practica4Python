import requests
from io import BytesIO
from zipfile import ZipFile

def descargar_imagen(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        raise Exception(f"No se pudo descargar la imagen. Código de estado: {response.status_code}")

def almacenar_imagen_como_zip(imagen_bytes, nombre_zip):
    with ZipFile(nombre_zip, 'w') as zip_file:
        zip_file.writestr('imagen_descargada.jpg', imagen_bytes.getvalue())

def extraer_zip(nombre_zip, directorio_destino='.'):
    with ZipFile(nombre_zip, 'r') as zip_file:
        zip_file.extractall(directorio_destino)

def main():
    url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    nombre_zip = "imagen_zip.zip"

    try:
        imagen_bytes = descargar_imagen(url_imagen)
        almacenar_imagen_como_zip(imagen_bytes, nombre_zip)

        print(f"Imagen descargada y almacenada como '{nombre_zip}'")

        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()