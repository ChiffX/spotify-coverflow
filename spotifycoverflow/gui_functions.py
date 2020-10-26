""" Handles all display functions of the main script 

Functions:
    generate_display()
    redraw()
"""

import ctypes
import time
from tkinter import Tk, Frame, Label
from spotifycoverflow import image, spotifyinfo 


# Automatically set width and height - FOR WINDOWS ONLY
# For other systems, replace monitor_width and _height with their respective values
user32 = ctypes.windll.user32
monitor_width = user32.GetSystemMetrics(0)
monitor_height = user32.GetSystemMetrics(1)


def generate_display(token):
    """Generates the primary screen showing album artwork, artist name, and song name

    :param token: Spotify authorization token
    :type token: string
    """    

    root = Tk()
    root.configure(bg="black", cursor="none")
    root.attributes('-fullscreen', True)

    f = Frame(root, bg="black", width=monitor_width, height=monitor_height)  # Sets frame to max monitor size with black background
    f.grid(row=1, column=1)  # Generates a 2x2 grid
    f.grid_propagate(0)
    f.update()
    
    most_recent_song = ""
    while True:
        current_song = spotifyinfo.get_current_playing(token)
        try:
            if current_song["name"] != most_recent_song:
                redraw(f, root, token, current_song)
                most_ecent_song = current_song["name"]
                time.sleep(2)
            else:
                time.sleep(2)
        except TypeError:
                # To do: replace with function that alternates through album covers from user's "liked" library
                print("Nothing is playing.")  
                time.sleep(2)
        


def redraw(f, root, token, current_song):
    """
    Redraws Tkinter window
    """

    artist = current_song["artist"]
    name = current_song["name"]
    fallback_image = current_song["img_src"]
    most_recent_song = name   

    # Generates album art image
    hd_img = image.itunes_search(name, artist)
    if hd_img != None:
        pi = image.convert_image(hd_img)
    else:
        pi = image.convert_image(fallback_image)

    # Album art label creation and placement
    album_art_label = Label(
        f, 
        image = pi, 
        bd = 0
    )
    album_art_label_placement = album_art_label.grid(
        rowspan = 2, 
        row = 0, 
        column = 0
    )

    # Artist name label creation and placement
    artist_name_label = Label(
        f,
        text = artist,
        bg = "black",
        fg = "white",
        font = ("Courier New", 50),
        wraplength = ((monitor_width - monitor_height) - (monitor_width / 50) * 2)  # Compensates for internal padding
    )
    artist_name_label_placement = artist_name_label.grid(  # To do: make grid fill screen properly. currently ends too short on the right
        row = 0,
        column = 1, 
        sticky = "s", 
        ipady = (monitor_height / 50),
        ipadx = (monitor_width / 50)
    )

    # Song label creation and placement
    song_label = Label(
        f,
        text = name,
        bg = "black",
        fg = "white",
        font = ("Courier New", 50),
        wraplength = ((monitor_width - monitor_height) - (monitor_width / 50) * 2)  # Compensates for internal padding
    )
    song_label_placement = song_label.grid(
        row = 1, 
        column = 1, 
        sticky = "n", 
        ipady = (monitor_height / 50),
        ipadx = (monitor_width / 50)
    )

    root.update()
    album_art_label.destroy()
    artist_name_label.destroy()
    song_label.destroy()
    