from pytube import YouTube
import os

def download_video(url: str, file_format: str = "mp4") -> str:
    yt = YouTube(url)
    title = yt.title.replace(" ", "_").replace("/", "_")
    
    if file_format == "mp4":
        stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
    elif file_format == "mp3":
        stream = yt.streams.filter(only_audio=True).first()
    else:
        raise ValueError("Unsupported format. Choose 'mp4' or 'mp3'.")

    output_path = stream.download(filename=f"{title}.{file_format}")

    # If mp3: convert the audio properly
    if file_format == "mp3":
        from moviepy.editor import AudioFileClip
        audio_clip = AudioFileClip(output_path)
        mp3_path = output_path.replace(".mp4", ".mp3")
        audio_clip.write_audiofile(mp3_path)
        audio_clip.close()
        os.remove(output_path)
        output_path = mp3_path

    return output_path
