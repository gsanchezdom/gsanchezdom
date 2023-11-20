from PIL import Image
import secrets
import os
import requests
from io import BytesIO

def main():
    # 1) Explicación del programa
    print("Este programa modifica una imagen añadiéndole IDs aleatorios.")

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

    # 5) Modificar la imagen
    new_image_path = os.path.splitext(image_path)[0] + '_secret.png'
    image.save(new_image_path)

    print(f"La imagen modificada se ha guardado en {new_image_path}")

if __name__ == "__main__":
    main()
