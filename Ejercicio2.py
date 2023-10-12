import os
import hashlib
from stegano import lsb
import stegano

carpeta_imagenes = '/home/mikel/n'

for archivo_nombre in os.listdir(carpeta_imagenes):
    archivo_ruta = os.path.join(carpeta_imagenes, archivo_nombre)

    with open(archivo_ruta, 'rb') as archivo_imagen:
        bytes_imagen = archivo_imagen.read()
        md5_hash = hashlib.md5(bytes_imagen).hexdigest()
        
    if md5_hash == 'e5ed313192776744b9b93b1320b5e268':
        print("Imagen encontrada! Es la imagen: " + archivo_nombre)

        with open(archivo_ruta, 'rb') as archivo_imagen:
            mensaje = stegano.red.reveal(archivo_imagen)
        print("El mensaje oculto es: " + mensaje)
        break
