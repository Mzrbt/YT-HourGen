import os
import subprocess
import sys

from moviepy import AudioFileClip, VideoFileClip  # type: ignore


def loop_video_fast(input_path: str, output_path: str, duration: int):
    if input_path.endswith(".mp3"):
        clip = AudioFileClip(input_path)
    else:
        clip = VideoFileClip(input_path)

    source_duration = clip.duration
    clip.close()

    n_loops = int(duration / source_duration) + 1

    print(f"⏱️  Source video: {source_duration:.1f}s")
    print(f"🔁 Number of loops: {n_loops}")
    print("💻 CPU encoding (ultrafast)...")
    print()

    concat_file = "concat_list.txt"
    with open(concat_file, "w") as file_handle:
        for _ in range(n_loops):
            file_handle.write(f"file '{os.path.abspath(input_path)}'\n")

    try:
        if input_path.endswith(".mp4"):
            process = subprocess.Popen(
                [
                    "ffmpeg",
                    "-f",
                    "concat",
                    "-safe",
                    "0",
                    "-i",
                    concat_file,
                    "-t",
                    str(duration),
                    "-c:v",
                    "libx264",
                    "-preset",
                    "ultrafast",
                    "-crf",
                    "23",
                    "-c:a",
                    "aac",
                    "-b:a",
                    "192k",
                    "-movflags",
                    "+faststart",
                    "-progress",
                    "pipe:1",
                    output_path,
                    "-y",
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
        else:
            process = subprocess.Popen(
                [
                    "ffmpeg",
                    "-f",
                    "concat",
                    "-safe",
                    "0",
                    "-i",
                    concat_file,
                    "-t",
                    str(duration),
                    "-c:a",
                    "libmp3lame",
                    "-b:a",
                    "192k",
                    "-movflags",
                    "+faststart",
                    "-progress",
                    "pipe:1",
                    output_path,
                    "-y",
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )

        last_time = 0
        last_progress = 0

        for line in process.stdout:
            if line.startswith("out_time_ms="):
                try:
                    time_ms = int(line.strip().split("=")[1])
                    current_time = time_ms / 1000000.0
                    progress = (current_time / duration) * 100

                    if progress - last_progress >= 0.5 or current_time - last_time >= 2:
                        bar_length = 40
                        filled = int(bar_length * progress / 100)
                        bar = "█" * filled + "░" * (bar_length - filled)

                        if current_time > 5:
                            rate = current_time / (progress / 100) if progress > 0 else 0
                            remaining = rate - current_time

                            if remaining > 0:
                                eta_str = f" - ETA: {int(remaining)}s"
                            else:
                                eta_str = ""
                        else:
                            eta_str = " - Calculating ETA..."

                        sys.stdout.write(f"\r[{bar}] {progress:.1f}%{eta_str}")
                        sys.stdout.flush()

                        last_time = current_time
                        last_progress = progress

                except (ValueError, IndexError):
                    pass

        process.wait()

        if process.returncode == 0:
            file_size = os.path.getsize(output_path) / (1024 * 1024)
            print(f"\n✅ Video created: {output_path}")
            print(f"📦 Size: {file_size:.1f} MB")
        else:
            print(f"\n❌ FFmpeg error (code {process.returncode})")
            raise subprocess.CalledProcessError(process.returncode, "ffmpeg")

        if os.path.exists(concat_file):
            os.remove(concat_file)

    except subprocess.CalledProcessError:
        print("\n❌ Encoding error")
        if os.path.exists(concat_file):
            os.remove(concat_file)
        raise
    except KeyboardInterrupt:
        print("\n⚠️  Process interrupted")
        if "process" in locals():
            process.kill()
        if os.path.exists(concat_file):
            os.remove(concat_file)
        if os.path.exists(output_path):
            os.remove(output_path)
        raise


def loop_video(input_path: str, format_type: str, duration: int, output_dir: str) -> str:
    filename = os.path.basename(input_path)
    output_filename = os.path.splitext(filename)[0] + f"_{duration}s.{format_type}"
    output_path = os.path.join(output_dir, output_filename)

    loop_video_fast(input_path, output_path, duration)

    return output_path
