### Documentación del Programa: SwissKnife

#### Versión en Español

# SwissKnife

SwissKnife es una herramienta multifuncional desarrollada en Python que ofrece una variedad de utilidades para tareas relacionadas con la informática. Actualmente, incluye un convertidor de imágenes a formato WebP y un descargador de audio/video de YouTube.

## Instalación

### Dependencias

Para que SwissKnife funcione correctamente, necesitas instalar las siguientes bibliotecas de Python:

- `pillow`
- `pytube`
- `tqdm`

Puedes instalarlas usando `pip`. Abre una terminal y ejecuta:

```sh
pip install pillow pytube tqdm
```

## Uso

### Convertidor de Imágenes a WebP

Esta herramienta permite convertir imágenes de cualquier formato al formato WebP. Puedes ingresar la ruta de una imagen individual o de una carpeta que contenga múltiples imágenes.

#### Ejemplo de Uso

1. Ejecuta el programa principal:

   ```sh
   python main.py
   ```

2. Selecciona la opción "Convertidor de imágenes a WebP" ingresando `1`.

3. Ingresa la ruta de la imagen o carpeta de imágenes cuando se te solicite.

4. El programa mostrará una barra de progreso mientras convierte las imágenes y te indicará la ubicación de las imágenes convertidas.

### Descargador de Audio/Video de YouTube

Esta herramienta permite descargar audio o video de YouTube proporcionando la URL del video.

#### Ejemplo de Uso

1. Ejecuta el programa principal:

   ```sh
   python main.py
   ```

2. Selecciona la opción "Descargador de audio/video de YouTube" ingresando `2`.

3. Ingresa la URL del video de YouTube.

4. Selecciona el tipo de descarga:
   - Ingresa `1` para descargar solo el audio.
   - Ingresa `2` para descargar el video.

5. El programa mostrará una barra de progreso mientras descarga el contenido y te indicará la ubicación del archivo descargado.

---

#### English Version

# SwissKnife

SwissKnife is a multifunctional tool developed in Python that offers various utilities for tasks related to computing. Currently, it includes an image converter to WebP format and a YouTube audio/video downloader.

## Installation

### Dependencies

To ensure SwissKnife functions correctly, you need to install the following Python libraries:

- `pillow`
- `pytube`
- `tqdm`

You can install them using `pip`. Open a terminal and run:

```sh
pip install pillow pytube tqdm
```

## Usage

### Image Converter to WebP

This tool allows you to convert images from any format to WebP format. You can input the path of an individual image or a folder containing multiple images.

#### Usage Example

1. Run the main program:

   ```sh
   python main.py
   ```

2. Select the "Image Converter to WebP" option by entering `1`.

3. Enter the path of the image or image folder when prompted.

4. The program will display a progress bar while converting the images and will indicate the location of the converted images.

### YouTube Audio/Video Downloader

This tool allows you to download audio or video from YouTube by providing the URL of the video.

#### Usage Example

1. Run the main program:

   ```sh
   python main.py
   ```

2. Select the "YouTube Audio/Video Downloader" option by entering `2`.

3. Enter the URL of the YouTube video.

4. Select the type of download:
   - Enter `1` to download only the audio.
   - Enter `2` to download the video.

5. The program will display a progress bar while downloading the content and will indicate the location of the downloaded file.
