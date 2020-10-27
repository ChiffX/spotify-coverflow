# SpotifyCoverFlow

[![PyPI](https://img.shields.io/badge/Python-3.8-green.svg)]()

Keys and callback URI are given with your personal Spotify developer account, register here: [Spotify Developer](https://developer.spotify.com/my-applications/#!/).

SpotifyCoverFlow is a simple script to display a full-screen & high resolution image of your current playing (or most recent) song on Spotify. The intended use is to dedicate a RaspberryPi (or similar device) and a monitor/screen to be an always on digital poster for your favorite music artwork.

![Example](https://i.imgur.com/PFJ9EfF.png)

At the time of writing this script, Spotify only supports image artwork up to `640x640`. To counteract this - the current song is then searched through iTunes to grab artwork up to `10000x10000`. If the artwork can't be found on iTunes, the lower resolution Spotify artwork will be displayed.

API information (key, callback URI, etc) is to be stored in a .env file. A sample file has been included (.env_sample), which should be renamed to .env with your specific information included.

Next Steps:
1. Change while loop to root.mainloop() to avoid unresponsiveness while waiting for next new song
2. Add keystroke/mouse click to end program
3. Display album art from "liked" songs/albums when nothing is actively playing

Forked from kylesurowiec by ChiffX