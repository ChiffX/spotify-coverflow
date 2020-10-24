import dotenv
import os
import sys
import spotipy.util as util

dotenv.load_dotenv()
USERNAME = os.getenv('USERNAME')
SECRET = os.getenv('SECRET')
SCOPE = os.getenv('SCOPE')
URI = os.getenv('URI')
ID = os.getenv('ID')


def get_token():
    '''
    This will open a new browser window if the developer account information
    above is correct. Follow the instructions that appear in the console dialog.
    After doing this once the token will auto refresh as long as the .cache file exists
    in the root directory.
    '''

    token = util.prompt_for_user_token(USERNAME, SCOPE, ID, SECRET, URI)
    return token