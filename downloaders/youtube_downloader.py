import os
from yt_dlp import YoutubeDL

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
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://www.youtube.com/'
        }
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
        ydl_opts.update({'format': 'bestvideo+bestaudio/best'})

    os.makedirs(output_path, exist_ok=True)

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

