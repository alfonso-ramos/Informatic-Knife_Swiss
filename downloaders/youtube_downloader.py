import os
from yt_dlp import YoutubeDL
from yt_dlp.utils import ExtractorError, DownloadError

def download_from_youtube(url, download_type='video', output_path='downloads'):
    """
    Descarga videos, audios o listas de reproducción de YouTube.

    Parámetros:
    - url: str -> URL del video o lista de reproducción de YouTube.
    - download_type: str -> 'video' para video, 'audio' para solo audio.
    - output_path: str -> Directorio donde se guardarán las descargas.
    """
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'noplaylist': False if 'playlist' in url else True,
        'ignoreerrors': True,
    }

    if download_type == 'audio':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        ydl_opts.update({'format': 'best/bestvideo+bestaudio'})

    os.makedirs(output_path, exist_ok=True)

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ Descarga completada exitosamente.")
    except ExtractorError as e:
        if "Video unavailable" in str(e) or "copyright claim" in str(e).lower():
            print(f"❌ Error: El video no está disponible (posiblemente eliminado o bloqueado por derechos de autor).")
        elif "region" in str(e).lower() or "not available" in str(e).lower():
            print(f"❌ Error: El video no está disponible en tu región.")
        else:
            print(f"❌ Error al extraer el video: {e}")
    except DownloadError as e:
        print(f"❌ Error de descarga: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

