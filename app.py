from flask import Flask, jsonify
from flask_cors import CORS
from test import get_user
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
import math


app = Flask(__name__)

CORS(app)

def get_distance(point1, point2, top3):
    return math.sqrt((point1[top3[0]] - point2[top3[0]])**2 + (point1[top3[1]] - point2[top3[1]])**2 + (point1[top3[2]] - point2[top3[2]])**2)

def get_user_profile():
    jay_music = get_user('jay.sakarvadia')
    jay_music.reset_index(inplace=True)
    return jay_music

def get_strong_features(user_playlist):
    
    key_features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    r2 = []

    for feature in key_features:
        X = user_playlist[feature]
        y = user_playlist['index']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()

        X_train = np.array(X_train).reshape(-1, 1)
        X_test = np.array(X_test).reshape(-1, 1)  

        # Fit the model to the training data
        model.fit(X_train, y_train)

        # Make predictions on the testing data
        y_pred = model.predict(X_test)
        r2.append(r2_score(y_test, y_pred))

    r2_comb = {key: abs(value) for key, value in zip(key_features, r2)}
    strong_features = dict(sorted(r2_comb.items(), key=lambda item: item[1], reverse=True))
    return list(strong_features.keys())[:3]

def get_comparisons(user_playlist, top3_features):
    user_point = user_playlist[top3_features].mean()

    directory_path = './character_datasets'
    top3_characters = []

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        char_df = pd.read_csv(file_path)
        char_df = char_df[top3_features].mean()
        char_df['Character'] = filename.replace("_", " ").replace(".csv", "")
        # print(char_df.head())
        top3_characters.append(char_df)

    comparison = pd.DataFrame(top3_characters)
    comparison['distance'] = comparison.apply(lambda x: get_distance(x, user_point, top3_features), axis=1)
    comparison['percentage'] = (comparison['distance'].max() - comparison['distance']) / comparison['distance'].max()

    final = comparison.sort_values('distance', ascending=True)
    return final.to_json(orient='records')

@app.route('/')
def hello_world():
    user_profile = get_user_profile()
    top3 = get_strong_features(user_profile)
    print('yes!')

    return jsonify({'data': get_comparisons(user_profile, top3)})

if __name__ == '__main__':
    app.run(debug=True)
