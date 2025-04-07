import argparse
import os
from yt_hourgen.downloader import download_video
from yt_hourgen.looper import make_video_one_hour

ASSETS_DIR = "assets"

def main():
    parser = argparse.ArgumentParser(
        description="Generate a 1-hour version of a YouTube video (mp3 or mp4)."
    )
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "-f", "--format",
        choices=["mp3", "mp4"],
        default="mp4",
        help="Output format: mp3 (audio only) or mp4 (video). Default: mp4"
    )
    args = parser.parse_args()

    print(f"[INFO] Downloading video from {args.url} in {args.format.upper()} format...")

    # Step 1: Download video/audio
    downloaded_path = download_video(args.url, args.format)

    print(f"[INFO] Downloaded to: {downloaded_path}")
    print("[INFO] Processing to create a 1-hour file...")

    # Step 2: Make 1 hour version
    output_path = make_video_one_hour(downloaded_path, args.format, ASSETS_DIR)

    print(f"[✅ DONE] 1-hour {args.format.upper()} created at: {output_path}")


if __name__ == "__main__":
    if not os.path.exists(ASSETS_DIR):
        os.makedirs(ASSETS_DIR)
    main()
