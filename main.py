""" This script acquires the currently playing track in Spotify and displays
    its artwork alongside the artist and song names
"""

from spotifycoverflow import authorization, gui_functions


def main():
    '''
    Main event loop, draw the image and text to tkinter window
    '''
    token = authorization.get_token()
    gui_functions.generate_display(token)


if __name__ == "__main__":
    main()
