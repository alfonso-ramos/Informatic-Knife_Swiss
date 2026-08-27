import os
import shutil
import time
from yt_dlp import YoutubeDL
from yt_dlp.networking.impersonate import ImpersonateTarget
from yt_dlp.utils import ExtractorError, DownloadError

def download_from_youtube(url, download_type='video', output_path='downloads'):
    """
    Descarga videos, audios o listas de reproducción de YouTube.

    Parámetros:
    - url: str -> URL del video o lista de reproducción de YouTube.
    - download_type: str -> 'video' para video, 'audio' para solo audio.
    - output_path: str -> Directorio donde se guardarán las descargas.
    """
    node_path = shutil.which('node') or '/home/poncho/.nvm/versions/node/v24.18.0/bin/node'
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'noplaylist': False if 'playlist' in url else True,
        'ignoreerrors': True,
        'js_runtimes': {'node': {'path': node_path}},
        'remote_components': ['ejs:github'],
        'impersonate': ImpersonateTarget.from_str('chrome'),
        'sleep_interval_requests': 1.0,
        'sleep_interval': 1.0,
        'max_sleep_interval': 3.0,
        'retries': 5,
        'fragment_retries': 5,
        'http_chunk_size': 524288,
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

    is_playlist = 'playlist' in url
    max_attempts = 3 if not is_playlist else 1
    retcode = 1
    try:
        for attempt in range(1, max_attempts + 1):
            with YoutubeDL(ydl_opts) as ydl:
                retcode = ydl.download([url])
            if retcode == 0:
                break
            if attempt < max_attempts:
                wait = 15 * attempt
                print(f"⚠️  YouTube limitó temporalmente el acceso (403). Reintentando en {wait}s (intento {attempt}/{max_attempts})...")
                time.sleep(wait)

        if retcode == 0:
            print("✅ Descarga completada exitosamente.")
        else:
            print("⚠️  Algunos elementos no se pudieron descargar (posible límite temporal de YouTube).")
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

