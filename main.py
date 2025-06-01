# Importa las funciones correctamente
from converters import convert_images_to_webp
from downloaders import download_from_youtube
from generators import generate_qrcode

def main_menu():
    while True:
        print("\nSeleccione una herramienta:")
        print("1. Convertidor de imágenes a WebP")
        print("2. Descargador de audio/video de YouTube")
        print("3. Generador de código QR")
        print("0. Salir")
        choice = input("Ingrese su opción: ")

        if choice == '1':
            image_converter_menu()
        elif choice == '2':
            youtube_downloader_menu()
        elif choice == '3':
            qrcode_generator_menu()
        elif choice == '0':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

def image_converter_menu():
    input_path = input("Ingrese la ruta de la imagen o carpeta de imágenes: ")
    output_path = convert_images_to_webp(input_path)
    print(f"Imágenes convertidas guardadas en: {output_path}")

def youtube_downloader_menu():
    url = input("Ingrese la URL del video o lista de reproducción de YouTube: ")
    print("Seleccione el tipo de descarga:")
    print("1. Audio")
    print("2. Video")
    download_choice = input("Ingrese su opción: ")
    
    if download_choice == '1':
        download_type = 'audio'
    elif download_choice == '2':
        download_type = 'video'
    else:
        print("Opción no válida, regresando al menú principal.")
        return
    
    output_path = "downloads/audio" if download_type == 'audio' else "downloads/videos"
    download_from_youtube(url, download_type, output_path)
    print(f"Descarga completada en: {output_path}")

def qrcode_generator_menu():
    enlace = input("Ingrese el enlace para generar el código QR: ")
    generate_qrcode(enlace)

if __name__ == "__main__":
    main_menu()
