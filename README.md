# FileComp

FileComp is a simple desktop application that compresses **images and videos** through an easy-to-use graphical interface.

The application is written in Python and uses FFmpeg for video compression.

---

## Features

- Compress image files
- Compress video files
- Preserve audio in compressed videos
- Simple graphical interface
- Works as a standalone Windows executable

---

## Technologies Used

- Python
- Tkinter
- Pillow
- FFmpeg

---

## Supported File Types

### Images
- JPG
- JPEG
- PNG
- BMP
- GIF

### Videos
- MP4
- AVI
- MOV
- MKV

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Krish0030/FileComp.git
cd FileComp
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg

Download FFmpeg from:

https://www.gyan.dev/ffmpeg/builds/

Extract and place `ffmpeg.exe` in the same folder as `filecomp.py`.

---

## Run the Application

```bash
python filecomp.py
```

---

## Build Executable

To create a standalone executable using PyInstaller:

```bash
pyinstaller --onefile --windowed --icon=filecomp.ico --add-binary "ffmpeg.exe;." filecomp.py
```

The executable will be generated inside the `dist` folder.

---

## How Compression Works

### Image Compression
Images are compressed using the Pillow library with optimized quality settings.

### Video Compression
Videos are compressed using FFmpeg with the following parameters:

```
-vcodec libx264
-crf 28
-preset fast
-c:a aac
-b:a 96k
```

These settings balance compression and quality.

---

## License

This project is licensed under the MIT License.
