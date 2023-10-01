#https://www.section.io/engineering-education/building-spotify-recommendation-engine/#creating-playlist-vector

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def get_feature_list(data): #this is raw API data
    columns = ['track_id',
             'acousticness',
             'danceability',
             'duration_ms',
             'energy',
             'instrumentalness',
             'liveness',
             'loudness',
             'speechiness',
             'tempo',
             'valence']
    spotify_features_df = data[columns]

    scaled_features = MinMaxScaler().fit_transform([
    spotify_features_df['acousticness'].values,
    spotify_features_df['danceability'].values,
    spotify_features_df['duration_ms'].values,
    spotify_features_df['energy'].values,
    spotify_features_df['instrumentalness'].values,
    spotify_features_df['liveness'].values,
    spotify_features_df['loudness'].values,
    spotify_features_df['speechiness'].values,
    spotify_features_df['tempo'].values,
    spotify_features_df['valence'].values,
    ])

    spotify_features_df[['acousticness','danceability','duration_ms','energy','instrumentalness','liveness','loudness','speechiness','tempo','valence']] = scaled_features.T
    return spotify_features_df #This is cleaned API data with only audio features