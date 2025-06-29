from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
import os

path = "../assets"

video_files = [f for f in os.listdir(path) if f.endswith('.mp4')]
if not video_files:
    raise FileNotFoundError("No video files found in the specified directory.")
filename = video_files[0]

video_path = os.path.join(path, filename)
output_filename = os.path.splitext(filename)[0] + "_1h.mp4"
output_video_path = os.path.join(path, output_filename)

clip = VideoFileClip(video_path)

target_duration = 3600
n_loops = int(target_duration // clip.duration) + 1

final_clip = concatenate_videoclips([clip] * n_loops).subclip(0, target_duration)

final_clip.write_videofile(output_video_path, codec='libx264', audio_codec='aac')

print(f"Video has been looped and saved as {output_filename} in {path}.")