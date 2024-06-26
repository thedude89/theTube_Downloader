# YouTube Downloader

Ein einfaches Tool zum Herunterladen von YouTube-Videos als MP4 oder MP3 mit einer benutzerfreundlichen Tkinter-GUI.

## Funktionen

- Herunterladen von YouTube-Videos als MP4.
- Herunterladen von YouTube-Audios als MP3.
- Fortschrittsanzeige während des Downloads.

## Installation

1. Klone das Repository:
   ```bash
   git clone https://github.com/thedude89/theTube_Downloader.git
   cd youtube-downloader
   ```
2. Erstelle eine virtuelle Umgebung und aktiviere sie:
   ```bash
   python -m venv venv
   # Aktivieren der virtuellen Umgebung
   venv\Scripts\activate  # Für Windows
   # source venv/bin/activate  # Für MacOS/Linux
   ```
3. Installiere die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```
4. Stelle sicher, dass die folgenden Pakete in requirements.txt enthalten sind:
   - pytube
   - moviepy
## Verwendung
- Skript ausführen und Popup verwenden
- Andwendung ausführen und Popup verwenden
## Anwendung
Um eine Anwendung zu machen, muss zuertst Windowssicherheit ausgeschalten werden. 
Man muss sicherstellen, dass man PyInstaller auf dem Gerät heruntergeladen hat. 
```bash
pip install pyinstaller
```
Dann muss man folgenden Befehl ausführen
```bash
pyinstaller --onefile youtube_downloader.py
```
## Lizenz
Dieses Projekt steht unter der MIT Lizenz
