def main_menu():
    while True:
        print("Seleccione una herramienta:")
        print("1. Convertidor de imagenes a WebP")
        print("2. Descargador de audio/video de Youtube")
        print("0. Slir")
        choise = input("ingrese una opción: ")

        if choise == '1':
            print("Convertidor de imagenes")
        elif choise == '2':
            print("Descargador de audio/video")
        elif choise == '0':
            print('Saliendo')
            break
        else:
            print("Opción no válida, intente de nuevo.")
if __name__ == "__main__":
    main_menu()