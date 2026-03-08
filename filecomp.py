import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os
import subprocess
import sys


def get_ffmpeg_path():
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, "ffmpeg.exe")
    return "ffmpeg.exe"


def compress_image(input_path, output_path, quality=80):

    with Image.open(input_path) as img:
        img.save(output_path, quality=quality, optimize=True)


def compress_video(input_path, output_path):

    ffmpeg = get_ffmpeg_path()

    subprocess.run([
        ffmpeg,
        "-i", input_path,
        "-vcodec", "libx264",
        "-crf", "28",
        "-preset", "fast",
        "-c:a", "aac",
        "-b:a", "96k",
        output_path
    ])


def reduce_size():

    filepath = filedialog.askopenfilename(
        title="Select an Image or Video File"
    )

    if not filepath:
        return

    filename, file_extension = os.path.splitext(filepath)

    output_path = filename + "_compressed" + file_extension

    if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']:

        try:
            compress_image(filepath, output_path)

            messagebox.showinfo(
                "Success",
                f"Image compressed and saved to\n{output_path}"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Failed to compress image:\n{str(e)}"
            )

    elif file_extension.lower() in ['.mp4', '.avi', '.mov', '.mkv']:

        try:
            compress_video(filepath, output_path)

            messagebox.showinfo(
                "Success",
                f"Video compressed and saved to\n{output_path}"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Failed to compress video:\n{str(e)}"
            )

    else:

        messagebox.showerror(
            "Error",
            "Unsupported file type"
        )


root = tk.Tk()

root.title("File Compressor")

root.geometry("400x400")

root.resizable(False, False)

root.configure(bg="maroon")


label = tk.Label(
    root,
    text="FiLE CompressoR",
    font=("Papyrus", 24, "bold"),
    fg="yellow",
    bg="maroon"
)

label.pack(side="top")


btn = tk.Button(
    root,
    text="Select Image/Video to Compress",
    command=reduce_size,
    font=("Helvetica", 14),
    bg="orange",
    fg="white",
    bd=2,
    relief="raised",
    cursor="hand2"
)

btn.place(
    relx=0.5,
    rely=0.5,
    anchor="center",
    width=300,
    height=40
)

root.mainloop()