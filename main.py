import argparse
import os
from yt_hourgen.downloader import download_video
from yt_hourgen.looper import loop_video

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
    parser.add_argument(
        "-d", "--duration",
        type=int,
        default=3600,
        help="Target the duration in seconds. Default: 3600s (= 1 hour)"
    )
    
    args = parser.parse_args()

    print(f"\033[0;33m[INFO]\033[0m Downloading video from {args.url} in {args.format.upper()} format for {args.duration} seconds...")

    downloaded_path = download_video(args.url, args.format)

    print(f"\033[0;33m[INFO]\033[0m Downloaded to: {downloaded_path}")
    print(f"\033[0;33m[INFO]\033[0m Processing to create a {args.duration}-seconds file...")

    output_path = loop_video(downloaded_path, args.format, args.duration, ASSETS_DIR)

    print(f"\033[0;32m[DONE]\033[0m {args.duration}-seconds {args.format.upper()} created at: {output_path}")

if __name__ == "__main__":
    if not os.path.exists(ASSETS_DIR):
        os.makedirs(ASSETS_DIR)
    main()