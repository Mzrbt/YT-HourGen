from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
import os

path = "../assets"

##### FONCTION TO LOOP A VIDEO ####

def loop_video(input_path: str, output_path: str, duration: int = 3600):

    clip = VideoFileClip(input_path)

    target_duration = duration
    n_loops = int(target_duration // clip.duration) + 1

    final_clip = concatenate_videoclips([clip] * n_loops).subclip(0, target_duration)

    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

    print(f"Video has been looped and saved as {output_filename} in {output_path}.")

###################################

video_files = [f for f in os.listdir(path) if f.endswith('.mp4')]
if not video_files:
    raise FileNotFoundError("No video files found in the specified directory.")

print("Available video files:")
for i, filename in enumerate(video_files, start=1):
    print(f"{i}: {filename}")

while True:
    try:
        choice = int(input("Enter the number of the video file you want to loop: "))
        if 1 <= choice <= len(video_files):
            filename = video_files[choice - 1]
            break
        else:
            print("Invalid choice. Please select a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        duration = int(input("Enter loop duration in seconds (e.g., 3600 for 1 hour): "))
        if duration > 0:
            break
        else:
            print("Duration must be a positive number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

video_path = os.path.join(path, filename)
output_filename = os.path.splitext(filename)[0] + "_1h.mp4"
output_video_path = os.path.join(path, output_filename)
loop_video(video_path, output_video_path, duration=duration)