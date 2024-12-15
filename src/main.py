## Color Palette: https://colorhunt.co/palette/89a8b2b3c8cfe5e1daf1f0e8

## Maybe:
#   That cursor thingy
#   Another square next to spotify displaying projects
#   If spotify not playing display anime pfp (like that anime girl drinking coffee)

from flask import Flask, render_template
import requests
import spotipy
from spotipy import SpotifyClientCredentials, SpotifyOAuth
import pprint
from dotenv import load_dotenv
import os

load_dotenv()

REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URL")

sp_auth = SpotifyOAuth(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        redirect_uri=REDIRECT_URI)

app = Flask(__name__)

def get_access_token():
    res = sp_auth.refresh_access_token(REFRESH_TOKEN)
    return res["access_token"]


@app.route("/")
def hello_world():
    my_spotify = spotipy.Spotify(auth=get_access_token())

    curr_playing = my_spotify.current_user_playing_track()
    if curr_playing:
        if curr_playing["is_playing"]:
            name    = curr_playing["item"]["name"]
            href    = curr_playing["item"]["external_urls"]["spotify"]
            img     = curr_playing["item"]["album"]["images"][1]["url"]
            artists = ", ".join([i["name"] for i in curr_playing["item"]["album"]["artists"]])
            # return curr_playing["item"]
            return render_template("index.html/", name=name, href=href, img=img, artists=artists)
        else:
            return "No track currently playing..."
    else:
        return "No track currently playing..."
    

    # return "hi"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))