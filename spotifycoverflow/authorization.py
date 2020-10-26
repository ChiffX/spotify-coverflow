""" Acquires authorization token from Spotify

Functions:
    get_token()
"""

import dotenv
import os
import sys
import spotipy.util as util


def get_token():
    '''
    This will open a new browser window if the developer account information
    above is correct. Follow the instructions that appear in the console dialog.
    After doing this once the token will auto refresh as long as the .cache file exists
    in the root directory.
    '''

    # Load sensitive API data from local .env file
    dotenv.load_dotenv()
    USERNAME = os.getenv('USERNAME')
    SECRET = os.getenv('SECRET')
    SCOPE = os.getenv('SCOPE')
    URI = os.getenv('URI')
    ID = os.getenv('ID')

    # Acquire token
    token = util.prompt_for_user_token(USERNAME, SCOPE, ID, SECRET, URI)
    return token