"""download youtube as mp3
"""

from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    test_url = "https://www.youtube.com/watch?v=uoDGHoFVZpQ"
    ydl.download([test_url])
