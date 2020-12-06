from pytube import YouTube
from pytube import Playlist
import os
import re

playlist = Playlist('https://www.youtube.com/playlist?list=PLR-LN9NY_iuK9_TdWQ2Df8r1MqxaVqgc8')

# prints each video url, which is the same as iterating through playlist.video_urls
for url in playlist:
    print(url)
# prints address of each YouTube object in the playlist
for vid in playlist.videos:
    print(vid)

# downloads videos in the playlist
# playlist.download_all(resolution="1080p")
