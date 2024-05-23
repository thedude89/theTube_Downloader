import tkinter as tk
from tkinter import ttk, messagebox
from pytube import YouTube
import moviepy.editor as mp
import os
from pathlib import Path

def download_video(url, file_type):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        if file_type == "mp4":
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            output_path = Path.home() / "Downloads"
            stream.download(output_path=output_path)
            messagebox.showinfo("Erfolg", "Video wurde erfolgreich heruntergeladen!")
        elif file_type == "mp3":
            stream = yt.streams.filter(only_audio=True).first()
            output_path = Path.home() / "Downloads"
            out_file = stream.download(output_path=output_path)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            
            # Verwenden von moviepy zur Umwandlung in MP3
            clip = mp.AudioFileClip(out_file)
            clip.write_audiofile(new_file)
            clip.close()
            
            # Entfernen der ursprünglichen Datei
            os.remove(out_file)
            
            messagebox.showinfo("Erfolg", "Audio wurde erfolgreich heruntergeladen!")
    except Exception as e:
        messagebox.showerror("Fehler", f"Es ist ein Fehler aufgetreten: {str(e)}")
    finally:
        progress_var.set(0)
        progress_bar.update()

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    progress_var.set(percentage_of_completion)
    progress_bar.update()

def start_download():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Fehler", "Bitte geben Sie eine URL ein")
        return
    file_type = file_type_var.get()
    download_video(url, file_type)

# GUI Setup
root = tk.Tk()
root.title("YouTube Downloader")

tk.Label(root, text="YouTube URL:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Label(root, text="Format wählen:").pack(pady=10)
file_type_var = tk.StringVar(value="mp4")
tk.Radiobutton(root, text="MP4", variable=file_type_var, value="mp4").pack()
tk.Radiobutton(root, text="MP3", variable=file_type_var, value="mp3").pack()

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(pady=20)

tk.Button(root, text="Download", command=start_download).pack(pady=20)

root.mainloop()
