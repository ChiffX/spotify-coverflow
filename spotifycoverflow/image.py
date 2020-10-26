""" Generates the image for the album artwork

Functions:
    itunes_search()
    convert_image()
"""

import ctypes
import itunespy
import requests
from io import BytesIO
from PIL import Image, ImageTk

user32 = ctypes.windll.user32
MONITOR_WIDTH = user32.GetSystemMetrics(0)
MONITOR_HEIGHT = user32.GetSystemMetrics(1)


def itunes_search(song, artist):
    """Check if iTunes has a higher definition album cover and return the url if found

    :param song: currently playing song
    :param artist: artist for currently playing song
    """
    try:
        matches = itunespy.search_track(song)
    except LookupError:
        return None

    for match in matches:
        if match.artist_name == artist:
            return match.artwork_url_100.replace('100x100b', '5000x5000b')


def convert_image(src):
    '''
    Converts the image url to Tkinter compatible PhotoImage
    '''

    res = requests.get(src)
    img = Image.open(BytesIO(res.content)).resize((MONITOR_HEIGHT, MONITOR_HEIGHT), Image.ANTIALIAS)  # Square sizing
    pi = ImageTk.PhotoImage(img, size=(MONITOR_HEIGHT, MONITOR_HEIGHT))

    return pi