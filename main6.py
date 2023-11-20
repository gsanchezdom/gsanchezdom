import stepic
from PIL import Image
import secrets
import os
import requests
from io import BytesIO
import uuid

def main():
    # 1) Explicación del programa
    print("Este programa modifica una imagen añadiéndole IDs aleatorios y utiliza la esteganografía para ocultar los IDs en la imagen.")

    # Preguntar al usuario si quiere modificar una imagen de un path o de una URL
    source = input("¿Quieres modificar una imagen de un path o de una URL? (Escribe 'path' o 'URL'): ")

    if source.lower() == 'path':
        # 2) Preguntar al usuario la ruta de la imagen
        image_path = input("Por favor, introduce la ruta de la imagen que quieres modificar: ")
        image = Image.open(image_path)
    elif source.lower() == 'url':
        # Preguntar al usuario la URL de la imagen
        image_url = input("Por favor, introduce la URL de la imagen que quieres modificar: ")
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        image_path = image_url
    else:
        print("Entrada no válida. Por favor, escribe 'path' o 'URL'.")
        return

    # 3) Crear IDs aleatorios
    random_id = secrets.token_hex(5)

    # 4) Guardar los IDs y la ruta de la imagen en un archivo txt
    with open('image_ids.txt', 'a') as f:
        f.write(f'ID: {random_id}, Image Path: {image_path}\n')

    # 5) Utilizar la esteganografía para ocultar el ID en la imagen
    stego_image = stepic.encode(image, random_id.encode())

    # 6) Leer el recuento de la ejecución del programa desde un archivo
    with open('count.txt', 'r') as f:
        count_str = f.read().strip()
        count = int(count_str) if count_str else 0

    # 7) Incrementar el recuento
    count += 1

    # 8) Guardar el recuento incrementado en el archivo
    with open('count.txt', 'w') as f:
        f.write(str(count))

    # 9) Guardar la imagen modificada con el nombre "Eladio Carrion" seguido del recuento
    new_image_path = f'Eladio Carrion {count}.png'
    stego_image.save(new_image_path)

    print(f"La imagen modificada se ha guardado en {new_image_path}")

if __name__ == "__main__":
    while True:
        main()
        input("Presiona Enter para reiniciar el programa...")
