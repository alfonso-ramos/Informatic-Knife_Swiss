import customtkinter as ctk
from customtkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
import os

from converters import convert_images_to_webp
from downloaders import download_from_youtube
from generators import generate_qrcode

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SwissKnifeApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Swiss Knife - Herramientas Multipropósito")
        self.geometry("900x650")
        self.minsize(800, 550)

        # Grid config
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Main tabview
        self.tabview = ctk.CTkTabview(self, width=880, height=600)
        self.tabview.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.tabview.grid_columnconfigure(0, weight=1)
        self.tabview.grid_rowconfigure(0, weight=1)

        # Create tabs
        self.tab_webp = self.tabview.add("  WebP Converter  ")
        self.tab_youtube = self.tabview.add("  YouTube Downloader  ")
        self.tab_qr = self.tabview.add("  QR Code Generator  ")

        self.setup_webp_tab()
        self.setup_youtube_tab()
        self.setup_qr_tab()

    def setup_webp_tab(self):
        self.tab_webp.grid_columnconfigure(0, weight=1)

        # Title
        title = ctk.CTkLabel(
            self.tab_webp, 
            text="Convertidor de Imágenes a WebP", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.grid(row=0, column=0, pady=(30, 20))

        # Description
        desc = ctk.CTkLabel(
            self.tab_webp,
            text="Convierte imágenes individuales o carpetas completas al formato WebP",
            font=ctk.CTkFont(size=12)
        )
        desc.grid(row=1, column=0, pady=(0, 30))

        # Input frame
        input_frame = ctk.CTkFrame(self.tab_webp)
        input_frame.grid(row=2, column=0, padx=50, pady=10, sticky="ew")
        input_frame.grid_columnconfigure(0, weight=1)

        self.webp_path_var = ctk.StringVar()
        
        path_entry = ctk.CTkEntry(
            input_frame, 
            textvariable=self.webp_path_var,
            placeholder_text="Selecciona una imagen o carpeta...",
            height=40,
            font=ctk.CTkFont(size=12)
        )
        path_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        browse_btn = ctk.CTkButton(
            input_frame,
            text="📁 Buscar",
            width=100,
            height=40,
            command=self.browse_webp_path
        )
        browse_btn.grid(row=0, column=1, padx=10, pady=10)

        # Buttons frame
        btn_frame = ctk.CTkFrame(self.tab_webp, fg_color="transparent")
        btn_frame.grid(row=3, column=0, pady=30)

        convert_btn = ctk.CTkButton(
            btn_frame,
            text="🚀 Convertir a WebP",
            width=200,
            height=45,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.start_webp_conversion
        )
        convert_btn.grid(row=0, column=0, padx=10)

        # Progress bar
        self.webp_progress = ctk.CTkProgressBar(self.tab_webp, width=400)
        self.webp_progress.grid(row=4, column=0, pady=20)
        self.webp_progress.set(0)

        # Status label
        self.webp_status = ctk.CTkLabel(
            self.tab_webp,
            text="",
            font=ctk.CTkFont(size=12)
        )
        self.webp_status.grid(row=5, column=0, pady=10)

    def setup_youtube_tab(self):
        self.tab_youtube.grid_columnconfigure(0, weight=1)

        # Title
        title = ctk.CTkLabel(
            self.tab_youtube, 
            text="Descargador de YouTube", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.grid(row=0, column=0, pady=(30, 20))

        # Description
        desc = ctk.CTkLabel(
            self.tab_youtube,
            text="Descarga videos individuales o listas de reproducción de YouTube",
            font=ctk.CTkFont(size=12)
        )
        desc.grid(row=1, column=0, pady=(0, 30))

        # URL Input
        url_frame = ctk.CTkFrame(self.tab_youtube)
        url_frame.grid(row=2, column=0, padx=50, pady=10, sticky="ew")
        url_frame.grid_columnconfigure(0, weight=1)

        self.youtube_url_var = ctk.StringVar()
        
        url_entry = ctk.CTkEntry(
            url_frame, 
            textvariable=self.youtube_url_var,
            placeholder_text="Pega la URL de YouTube aquí...",
            height=40,
            font=ctk.CTkFont(size=12)
        )
        url_entry.grid(row=0, column=0, padx=10, pady=15, sticky="ew")

        # Download type
        type_frame = ctk.CTkFrame(self.tab_youtube, fg_color="transparent")
        type_frame.grid(row=3, column=0, pady=20)

        self.download_type = ctk.StringVar(value="video")

        video_radio = ctk.CTkRadioButton(
            type_frame,
            text="  Video (MP4)",
            variable=self.download_type,
            value="video",
            font=ctk.CTkFont(size=14)
        )
        video_radio.grid(row=0, column=0, padx=20)

        audio_radio = ctk.CTkRadioButton(
            type_frame,
            text="  Audio (MP3)",
            variable=self.download_type,
            value="audio",
            font=ctk.CTkFont(size=14)
        )
        audio_radio.grid(row=0, column=1, padx=20)

        # Output folder
        output_frame = ctk.CTkFrame(self.tab_youtube)
        output_frame.grid(row=4, column=0, padx=50, pady=10, sticky="ew")
        output_frame.grid_columnconfigure(0, weight=1)

        self.youtube_output_var = ctk.StringVar(value="downloads")
        
        output_entry = ctk.CTkEntry(
            output_frame, 
            textvariable=self.youtube_output_var,
            placeholder_text="Carpeta de salida...",
            height=35,
            font=ctk.CTkFont(size=11)
        )
        output_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        browse_output_btn = ctk.CTkButton(
            output_frame,
            text="📁",
            width=50,
            height=35,
            command=self.browse_youtube_output
        )
        browse_output_btn.grid(row=0, column=1, padx=10, pady=10)

        # Download button
        download_btn = ctk.CTkButton(
            self.tab_youtube,
            text="⬇️  Iniciar Descarga",
            width=220,
            height=50,
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self.start_youtube_download
        )
        download_btn.grid(row=5, column=0, pady=30)

        # Progress
        self.youtube_progress = ctk.CTkProgressBar(self.tab_youtube, width=400)
        self.youtube_progress.grid(row=6, column=0, pady=15)
        self.youtube_progress.set(0)

        # Status
        self.youtube_status = ctk.CTkLabel(
            self.tab_youtube,
            text="",
            font=ctk.CTkFont(size=12)
        )
        self.youtube_status.grid(row=7, column=0, pady=10)

    def setup_qr_tab(self):
        self.tab_qr.grid_columnconfigure(0, weight=1)

        # Title
        title = ctk.CTkLabel(
            self.tab_qr, 
            text="Generador de Códigos QR", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.grid(row=0, column=0, pady=(30, 20))

        # Description
        desc = ctk.CTkLabel(
            self.tab_qr,
            text="Genera códigos QR a partir de enlaces o texto",
            font=ctk.CTkFont(size=12)
        )
        desc.grid(row=1, column=0, pady=(0, 30))

        # URL/Content Input
        content_frame = ctk.CTkFrame(self.tab_qr)
        content_frame.grid(row=2, column=0, padx=50, pady=10, sticky="ew")
        content_frame.grid_columnconfigure(0, weight=1)

        self.qr_content_var = ctk.StringVar()
        
        content_entry = ctk.CTkEntry(
            content_frame, 
            textvariable=self.qr_content_var,
            placeholder_text="Ingresa el enlace o texto para el QR...",
            height=40,
            font=ctk.CTkFont(size=12)
        )
        content_entry.grid(row=0, column=0, padx=10, pady=15, sticky="ew")

        # Filename
        filename_frame = ctk.CTkFrame(self.tab_qr)
        filename_frame.grid(row=3, column=0, padx=50, pady=10, sticky="ew")
        filename_frame.grid_columnconfigure(0, weight=1)

        self.qr_filename_var = ctk.StringVar(value="codigo_qr.png")
        
        filename_entry = ctk.CTkEntry(
            filename_frame, 
            textvariable=self.qr_filename_var,
            placeholder_text="Nombre del archivo...",
            height=35,
            font=ctk.CTkFont(size=11)
        )
        filename_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Generate button
        generate_btn = ctk.CTkButton(
            self.tab_qr,
            text="🔳  Generar Código QR",
            width=220,
            height=50,
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self.start_qr_generation
        )
        generate_btn.grid(row=4, column=0, pady=30)

        # QR Preview frame
        self.qr_preview_frame = ctk.CTkFrame(self.tab_qr, width=250, height=250)
        self.qr_preview_frame.grid(row=5, column=0, pady=20)
        self.qr_preview_frame.grid_propagate(False)

        self.qr_preview_label = ctk.CTkLabel(
            self.qr_preview_frame,
            text="Vista previa del QR\naparecerá aquí",
            font=ctk.CTkFont(size=12)
        )
        self.qr_preview_label.place(relx=0.5, rely=0.5, anchor="center")

        # Status
        self.qr_status = ctk.CTkLabel(
            self.tab_qr,
            text="",
            font=ctk.CTkFont(size=12)
        )
        self.qr_status.grid(row=6, column=0, pady=10)

    # WebP Methods
    def browse_webp_path(self):
        path = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff")]
        )
        if not path:
            path = filedialog.askdirectory(title="Seleccionar carpeta de imágenes")
        if path:
            self.webp_path_var.set(path)

    def start_webp_conversion(self):
        input_path = self.webp_path_var.get()
        if not input_path:
            messagebox.showwarning("Advertencia", "Por favor selecciona una imagen o carpeta")
            return

        if not os.path.exists(input_path):
            messagebox.showerror("Error", "La ruta seleccionada no existe")
            return

        self.webp_status.configure(text="Convirtiendo...", text_color="yellow")
        self.webp_progress.set(0.5)
        self.webp_progress.start()

        thread = threading.Thread(target=self._convert_webp_thread, args=(input_path,))
        thread.daemon = True
        thread.start()

    def _convert_webp_thread(self, input_path):
        try:
            output_path = convert_images_to_webp(input_path)
            self.after(0, lambda: self._webp_conversion_done(output_path))
        except Exception as e:
            self.after(0, lambda: self._webp_conversion_error(str(e)))

    def _webp_conversion_done(self, output_path):
        self.webp_progress.stop()
        self.webp_progress.set(1)
        self.webp_status.configure(text=f"✅ Completado! Guardado en: {output_path}", text_color="green")
        messagebox.showinfo("Éxito", f"Conversión completada!\nArchivos guardados en:\n{output_path}")

    def _webp_conversion_error(self, error_msg):
        self.webp_progress.stop()
        self.webp_progress.set(0)
        self.webp_status.configure(text=f"❌ Error: {error_msg}", text_color="red")
        messagebox.showerror("Error", f"Error durante la conversión:\n{error_msg}")

    # YouTube Methods
    def browse_youtube_output(self):
        path = filedialog.askdirectory(title="Seleccionar carpeta de descarga")
        if path:
            self.youtube_output_var.set(path)

    def start_youtube_download(self):
        url = self.youtube_url_var.get().strip()
        if not url:
            messagebox.showwarning("Advertencia", "Por favor ingresa una URL de YouTube")
            return

        download_type = self.download_type.get()
        output_path = self.youtube_output_var.get()

        os.makedirs(output_path, exist_ok=True)

        self.youtube_status.configure(text="Descargando...", text_color="yellow")
        self.youtube_progress.start()

        thread = threading.Thread(
            target=self._youtube_download_thread, 
            args=(url, download_type, output_path)
        )
        thread.daemon = True
        thread.start()

    def _youtube_download_thread(self, url, download_type, output_path):
        try:
            download_from_youtube(url, download_type, output_path)
            self.after(0, lambda: self._youtube_download_done(output_path))
        except Exception as e:
            self.after(0, lambda: self._youtube_download_error(str(e)))

    def _youtube_download_done(self, output_path):
        self.youtube_progress.stop()
        self.youtube_progress.set(1)
        self.youtube_status.configure(text=f"✅ Descarga completada en: {output_path}", text_color="green")
        messagebox.showinfo("Éxito", f"Descarga completada!\nArchivos guardados en:\n{output_path}")

    def _youtube_download_error(self, error_msg):
        self.youtube_progress.stop()
        self.youtube_progress.set(0)
        self.youtube_status.configure(text=f"❌ Error: {error_msg}", text_color="red")
        messagebox.showerror("Error", f"Error durante la descarga:\n{error_msg}")

    # QR Methods
    def start_qr_generation(self):
        content = self.qr_content_var.get().strip()
        if not content:
            messagebox.showwarning("Advertencia", "Por favor ingresa un enlace o texto")
            return

        filename = self.qr_filename_var.get()
        if not filename.endswith('.png'):
            filename += '.png'

        self.qr_status.configure(text="Generando...", text_color="yellow")

        thread = threading.Thread(
            target=self._qr_generation_thread, 
            args=(content, filename)
        )
        thread.daemon = True
        thread.start()

    def _qr_generation_thread(self, content, filename):
        try:
            generate_qrcode(content, filename)
            self.after(0, lambda: self._qr_generation_done(filename))
        except Exception as e:
            self.after(0, lambda: self._qr_generation_error(str(e)))

    def _qr_generation_done(self, filename):
        self.qr_status.configure(text=f"✅ QR guardado como: {filename}", text_color="green")
        
        # Load and display the QR image
        try:
            img = Image.open(filename)
            img.thumbnail((230, 230))
            
            ctk_image = ctk.CTkImage(light_image=img, dark_image=img, size=(230, 230))
            
            self.qr_preview_label.configure(image=ctk_image, text="")
            self.qr_preview_label.image = ctk_image  # Keep reference
        except:
            pass

        messagebox.showinfo("Éxito", f"Código QR generado!\nGuardado como: {filename}")

    def _qr_generation_error(self, error_msg):
        self.qr_status.configure(text=f"❌ Error: {error_msg}", text_color="red")
        messagebox.showerror("Error", f"Error al generar QR:\n{error_msg}")


def main():
    app = SwissKnifeApp()
    app.mainloop()


if __name__ == "__main__":
    main()
