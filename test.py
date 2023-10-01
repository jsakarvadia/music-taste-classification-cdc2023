import pandas as pd
import requests

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

client_id = '6471d3b0bc204121ac66bba63e27ab06'
client_secret = 'fe6f65cf6f2d439da586046d01a2cd19'
redirect_uri = 'http://localhost:8881/callback'

def get_token(username, scope):
    token = util.prompt_for_user_token(
        username, scope,
        client_id=client_id,
        client_secret=client_secret, redirect_uri=redirect_uri
    )
    return token


def create_top_tracks_dict(sp, period):
    list_tracks=[]
    for offset in range(0, 500, 49):
        x = sp.current_user_top_tracks(49, offset, time_range=period)
        temp = [track for track in x['items']]
        list_tracks.extend(temp)
    top_track_dict = [{'name':item['name'], 
                            'album':item['album']['name'],
                            'year':item['album']['release_date'],
                            'artists':[artist['name'] for artist in item['album']['artists']],
                            'track_id':item['id']} for item in list_tracks if item is not None]
    return top_track_dict

def all_features(sp, dictionary):
    all_features = []
    for item in dictionary:
        all_features.extend(sp.audio_features(item['track_id'])) 

    return all_features


def get_user(username):
    token = get_token(username, 'user-top-read')
    sp = spotipy.Spotify(auth=token)
    top_tracks = create_top_tracks_dict(sp, 'long_term')
    song_features = pd.DataFrame(all_features(sp, top_tracks))
    data = pd.concat([pd.DataFrame(top_tracks), song_features], axis=1)
    return data


def get_playlist(playlist_id):
    token = get_token('jay.sakarvadia', 'user-top-read')
    sp = spotipy.Spotify(auth=token)
    playlist = playlist_id
    playlist_data = sp.playlist(playlist)['tracks']['items']
    songs = [song['track'] for song in playlist_data]
    tracks = [{'name':item['name'], 
                            'album':item['album']['name'],
                            'year':item['album']['release_date'],
                            'artists':[artist['name'] for artist in item['album']['artists']],
                            'track_id':item['id'],
                            'image':item['album']['images'][0]['url']} for item in songs]
    features = all_features(sp, tracks)
    data = pd.concat([pd.DataFrame(tracks), pd.DataFrame(features)], axis=1)
    return data

