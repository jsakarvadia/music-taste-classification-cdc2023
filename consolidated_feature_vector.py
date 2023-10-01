import pandas as pd

def consolidated_feature_vector(spotify_features_df):
    consolidated_feature_vector = spotify_features_df.mean()
    return consolidated_feature_vector #this is consolidated single vector of spotify features