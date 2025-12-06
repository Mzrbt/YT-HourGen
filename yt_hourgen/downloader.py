import yt_dlp # type: ignore
import os

def download_video(url: str, format_type: str = "mp4") -> str:
    if format_type == "mp3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'assets/%(title).50s.%(ext)s',
            'noplaylist': True,
            'extractor_args': {'youtube': {'player_client': ['default']}},
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': 'assets/%(title).50s.%(ext)s',
            'noplaylist': True,
            'extractor_args': {'youtube': {'player_client': ['default']}},
        }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        
        if format_type == "mp3":
            filename = ydl.prepare_filename(info).rsplit('.', 1)[0] + '.mp3'
        else:
            filename = ydl.prepare_filename(info)
        
        return filename