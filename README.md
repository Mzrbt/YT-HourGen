# 🎬 YT-HourGen

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Docker](https://img.shields.io/badge/docker-ready-brightgreen)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)

Generate 1-hour looped videos from any YouTube video.

## 🚀 Quick Start

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)

### Installation

```bash
git clone https://github.com/YOUR-USERNAME/YT-HourGen.git
cd YT-HourGen
docker-compose build
```

### Usage

```bash
# Create 1-hour MP4 video
docker-compose run --rm yt-hourgen "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -f mp4

# Create 1-hour MP3 audio
docker-compose run --rm yt-hourgen "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -f mp3
```

Generated files will be in the `assets/` folder.

## 📦 Alternative: Local Installation

If you prefer not to use Docker:

```bash
# Install the package
pip install -e .

# Use directly from anywhere
yt-hourgen "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -f mp4
```

**Note:** Requires Python 3.12+ and FFmpeg installed on your system.

## 📖 Commands

```bash
docker-compose run --rm yt-hourgen <YOUTUBE_URL> [OPTIONS]

Options:
  -f, --format {mp3,mp4}  Output format (default: mp4)
  -h, --help              Show help
```

## 🛠️ Tech Stack

- **Python 3.12** - Core language
- **yt-dlp** - YouTube downloader
- **FFmpeg** - Video encoding
- **Docker** - Containerization

## 📝 License

MIT License - see [LICENSE](LICENSE) file.

---

**⭐ Star this repo if you find it useful!**
