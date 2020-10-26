""" Gets the song information for the currently playing song

Functions:
    get_currently_playing()
"""

import spotipy


def get_current_playing(token):
    '''
    Returns information about the current playing song. If no song is currently
    playing the most recent song will be returned.
    '''

    spotify = spotipy.Spotify(auth=token)
    results = spotify.current_user_playing_track()

    try:
        if results != None:
            img_src = results["item"]["album"]["images"][0]["url"]
            artist = results["item"]["album"]["artists"][0]["name"]
            album = results["item"]["album"]["name"]
            name = results["item"]["name"]
            isrc = results["item"]["external_ids"]["isrc"]
        if results == None:
            return False
    except TypeError:
        return False

    return {
        "img_src": img_src,
        "artist": artist,
        "album": album,
        "name": name,
        "id": isrc
    }
