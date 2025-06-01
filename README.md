# Swiss Knife Project Documentation

```
 .d8888b.                d8b                        888    d8P           d8b  .d888         
d88P  Y88b               Y8P                        888   d8P            Y8P d88P"          
Y88b.                                               888  d8P                 888            
 "Y888b.   888  888  888 888 .d8888b  .d8888b       888d88K     88888b.  888 888888 .d88b.  
    "Y88b. 888  888  888 888 88K      88K           8888888b    888 "88b 888 888   d8P  Y8b 
      "888 888  888  888 888 "Y8888b. "Y8888b.      888  Y88b   888  888 888 888   88888888 
Y88b  d88P Y88b 888 d88P 888      X88      X88      888   Y88b  888  888 888 888   Y8b.     
 "Y8888P"   "Y8888888P"  888  88888P'  88888P'      888    Y88b 888  888 888 888    "Y8888  
                                                                                            
                                                                                                                                                                                     
```

## Description
This project includes tools for image conversion to WebP and downloading videos/audio from YouTube. It also allows managing these functions through an interactive menu.

## Installation
### 1. Clone the repository
```bash
git clone <REPO_URL>
cd <REPO_NAME>
```

### 2. Create and activate a virtual environment
#### On Windows
```bash
python -m venv venv
venv\Scripts\activate
```
#### On Linux/Mac
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install yt-dlp pillow tqdm qrcode matplotlib
```

**Note:** `yt-dlp` requires `ffmpeg` to function properly. Install it with:
- **Windows**: Download and install `ffmpeg` from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) and add it to the PATH.
- **Linux (Debian/Ubuntu)**: `sudo apt install ffmpeg`
- **MacOS**: `brew install ffmpeg`

## Usage
Run the main menu with:
```bash
python main.py
```

## Features
### 1. Image Converter to WebP
Converts individual images or entire folders to WebP format.

### 2. YouTube Video and Audio Downloader
- Downloads individual videos or playlists.
- Supports downloading in video format or audio-only.
- Uses `yt-dlp` instead of `pytube`.

## Project Structure
```
<project root>/
│── converters/              # Image conversion module
│── downloaders/             # YouTube download module
│── downloads/               # Folder for downloaded files
│── venv/                    # Virtual environment (not included in Git)
│── main.py                  # Main menu
│── .gitignore               # Files and folders ignored by Git
│── README.md                # Project documentation
```

## Additional Notes
- Updated the download system to replace `pytube`.
- Added support for downloading entire playlists.
- Documented virtual environment setup.
- Simplified dependency installation into a single command.
- Included `ffmpeg` installation as a requirement for `yt-dlp`.

If you find any issues or have suggestions, feel free to contribute! 😊

---

# Documentación del Proyecto Swiss Knife 

```
 .d8888b.                d8b                        888    d8P           d8b  .d888         
d88P  Y88b               Y8P                        888   d8P            Y8P d88P"          
Y88b.                                               888  d8P                 888            
 "Y888b.   888  888  888 888 .d8888b  .d8888b       888d88K     88888b.  888 888888 .d88b.  
    "Y88b. 888  888  888 888 88K      88K           8888888b    888 "88b 888 888   d8P  Y8b 
      "888 888  888  888 888 "Y8888b. "Y8888b.      888  Y88b   888  888 888 888   88888888 
Y88b  d88P Y88b 888 d88P 888      X88      X88      888   Y88b  888  888 888 888   Y8b.     
 "Y8888P"   "Y8888888P"  888  88888P'  88888P'      888    Y88b 888  888 888 888    "Y8888  
                                                                                            
  
```

## Descripción
Este proyecto incluye herramientas para la conversión de imágenes a WebP y la descarga de videos/audio desde YouTube. Además, permite gestionar estas funciones desde un menú interactivo.

## Instalación
### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

### 2. Crear y activar un entorno virtual
#### En Windows
```bash
python -m venv venv
venv\Scripts\activate
```
#### En Linux/Mac
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install yt-dlp pillow tqdm qrcode matplotlib
```

**Nota:** Para que `yt-dlp` funcione correctamente, es necesario tener `ffmpeg` instalado. Puedes instalarlo con:
- **Windows**: Descarga e instala `ffmpeg` desde [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) y agrégalo al PATH.
- **Linux (Debian/Ubuntu)**: `sudo apt install ffmpeg`
- **MacOS**: `brew install ffmpeg`

## Uso
Ejecuta el menú principal con:
```bash
python main.py
```

## Funcionalidades
### 1. Convertidor de imágenes a WebP
Convierte imágenes individuales o en carpetas al formato WebP.

### 2. Descargador de videos y audio de YouTube
- Descarga videos individuales o listas de reproducción.
- Soporta descarga en formato de video o solo audio.
- Se utiliza `yt-dlp` en lugar de `pytube`.

## Estructura del Proyecto
```
<raíz del proyecto>/
│── converters/              # Módulo para conversión de imágenes
│── downloaders/             # Módulo para descargas de YouTube
│── downloads/               # Carpeta donde se almacenan los archivos descargados
│── venv/                    # Entorno virtual (no se sube a Git)
│── main.py                  # Menú principal
│── .gitignore               # Archivos y carpetas a ignorar en Git
│── README.md                # Documentación del proyecto
```

## Notas Adicionales
- Se ha actualizado el sistema de descargas para evitar el uso de `pytube`.
- Se agregó soporte para descargar listas de reproducción completas.
- Se documentó la configuración del entorno virtual.
- Ahora la instalación de dependencias se hace en un solo comando.
- Se añadió la instalación de `ffmpeg` como requisito para el funcionamiento de `yt-dlp`.

Si encuentras errores o tienes sugerencias, ¡contribuye al proyecto! 😊
