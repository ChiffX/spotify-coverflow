import time
import requests
import ctypes
import itunespy

import spotipy
from io import BytesIO
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Label
from spotifycoverflow import authentication

from pprint import pprint

user32 = ctypes.windll.user32
MONITOR_WIDTH = user32.GetSystemMetrics(0)
MONITOR_HEIGHT = user32.GetSystemMetrics(1)


def get_current_playing(token):
    '''
    Returns information about the current playing song. If no song is currently
    playing the most recent song will be returned.
    '''

    spotify = spotipy.Spotify(auth=token)
    results = spotify.current_user_playing_track()

    img_src = results["item"]["album"]["images"][0]["url"]
    artist = results["item"]["album"]["artists"][0]["name"]
    album = results["item"]["album"]["name"]
    name = results["item"]["name"]
    isrc = results["item"]["external_ids"]["isrc"]

    return {
        "img_src": img_src,
        "artist": artist,
        "album": album,
        "name": name,
        "id": isrc
    }


def itunes_search(song, artist):
    '''
    Check if iTunes has a higher definition album cover and
    return the url if found
    '''

    try:
        matches = itunespy.search_track(song)
    except LookupError:
        return None

    for match in matches:
        if match.artist_name == artist:
            return match.artwork_url_100.replace('100x100b', '5000x5000b')


def convert_image(src):
    '''
    Convert the image url to Tkinter compatible PhotoImage
    '''

    res = requests.get(src)
    img = Image.open(BytesIO(res.content)).resize(
        (MONITOR_HEIGHT, MONITOR_HEIGHT), Image.ANTIALIAS)
    pi = ImageTk.PhotoImage(img, size=(MONITOR_HEIGHT, MONITOR_HEIGHT))

    return pi


def main():
    '''
    Main event loop, draw the image and text to tkinter window
    '''
    token = authentication.get_token()

    root = Tk()
    root.configure(bg="black", cursor="none")
    root.attributes('-fullscreen', True)

    f = Frame(root, bg="black", width=MONITOR_WIDTH, height=MONITOR_HEIGHT)
    f.grid(row=0, column=0)
    f.grid_propagate(0)
    f.update()

    most_recent_song = ""
    while True:
        redraw = True

        
        current_song = get_current_playing(token)

        if current_song["name"] != most_recent_song:
            redraw = True
        else:
            redraw = False

        if redraw:
            artist = current_song["artist"]
            name = current_song["name"]
            most_recent_song = name
            hd_img = itunes_search(
                current_song["name"], current_song["artist"])

            if hd_img != None:
                pi = convert_image(hd_img)
            else:
                pi = convert_image(current_song["img_src"])

            img_x = 0
            img_y = MONITOR_HEIGHT / 2

            label = Label(f, image=pi, highlightthickness=0, bd=0)
            label.place(x=img_x, y=img_y, anchor="w")

            artist_label = Label(
                f,
                text=artist,
                bg="black",
                fg="white",
                font=("Courier New", 30)
            )

            artist_x = MONITOR_WIDTH - (MONITOR_WIDTH / 5)
            artist_y = (MONITOR_HEIGHT / 2) - 50
            artist_label.place(x=artist_x, y=artist_y, anchor="center")

            song_label = Label(
                f,
                text=name,
                bg="black",
                fg="white",
                font=("Courier New", 50),
            )

            song_x = MONITOR_WIDTH - (MONITOR_WIDTH / 5)
            song_y = (MONITOR_HEIGHT / 2) + 50
            song_label.place(x=song_x, y=song_y, anchor="center")

            root.update()

            label.destroy()
            artist_label.destroy()
            song_label.destroy()
            time.sleep(2)

if __name__ == "__main__":
    main()
