import pandas as pd
import requests

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

print("yooo")
client_id = '5ee25f7022604f25bd114950a6437995'
client_secret = '7137f0a04815452c991d20c21a18dae6'
redirect_uri = 'http://localhost:8881/callback'

def call_api(username, scope):
    token = util.prompt_for_user_token(
        username, scope,
        client_id=client_id,
        client_secret=client_secret, redirect_uri=redirect_uri
    )
    return token

token = call_api('jay.sakarvadia', 'user-top-read')

sp = spotipy.Spotify(auth=token)

class Track:
    def __init__(self, name, album, release, artist, id, image):
        self.name = name
        self.album = album
        self.release = release
        self.artist = artist
        self.id = id
        self.image = image

def create_top_tracks_dict(period):
    list_tracks=[]
    for offset in range(0, 500, 49):
        x = sp.current_user_top_tracks(49, offset, time_range=period)
        temp = [track for track in x['items']]
        list_tracks.extend(temp)
    top_track_dict = [Track(item['name'], 
                            item['album']['name'],
                            item['album']['release_date'],
                            [artist['name'] for artist in item['album']['artists']],
                            item['id'],
                            item['album']['images'][0]['url']) for item in list_tracks]
    return top_track_dict, len(list_tracks)
    
    
print(create_top_tracks_dict('long_term'))
