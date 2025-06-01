import qrcode
import matplotlib.pyplot as plt

def generate_qrcode(enlace, nombre_archivo="codigo_qr.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(enlace)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(nombre_archivo)

    # Mostrar el código QR gráficamente
    plt.imshow(img, cmap='gray')
    plt.axis("off")
    plt.show()

    print(f"Código QR generado y guardado como {nombre_archivo}")

if __name__ == "__main__":
    enlace = input("Ingresa el enlace para generar el código QR: ").strip()
    generate_qrcode(enlace)
