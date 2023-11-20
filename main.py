from PIL import Image
import secrets
import os

def main():
    # 1) Explicación del programa
    print("Este programa modifica una imagen añadiéndole IDs aleatorios.")

    # 2) Preguntar al usuario la ruta de la imagen
    image_path = input("Por favor, introduce la ruta de la imagen que quieres modificar: ")

    # 3) Crear IDs aleatorios
    random_id = secrets.token_hex(5)

    
    with open('image_ids.txt', 'a') as f:
        f.write(f'ID: {random_id}, Image Path: {image_path}\n')

    # 5) Modificar la imagen
    image = Image.open(image_path)
    new_image_path = os.path.splitext(image_path)[0] + '_secret.png'
    image.save(new_image_path)

    print(f"La imagen modificada se ha guardado en {new_image_path}")


continuar = True

while continuar:
    if __name__ == "__main__":
        try:
            main()
        
        except:
            print("\nIntroduce una ruta correcta")
            input("\nPulsa cualquier tecla para continuar...\n")
