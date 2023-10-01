# CDC2023

1 - Connect to Spotify API (created subsequent methods for API connection)
2 - Build get_user (audio feature data given users top 100 long-term songs) & get_playlist (audio feature data given selected playlist) methods to pull relevent audio feature data

Cosine Similarity
------------------
3 - Method to preprocess data by dropping categorical variables (one-hot encoding proved to be inefficent), and by using max-min normalization for all numeric features
4 - Method to consolidate both user and playlist audio feature data into a single mean feature vector
5 - Method to calculate cosine similarities (angle between two vectors in space; user vector and playlist vector) using equation, then converting output to radians, and then degrees in order to eventually be able to understand % Similarity Breakdown
6 - Implement all methods in algorithmic analysis notebook to see results



Euclidian Distance
------------------
3 - Regression analysis for audio feature selection; take 3 most correlative features 


(below represents strong correlation between ranking of song and the feature)
![image](https://github.com/JaySakarvadia/CDC2023/assets/111033138/180a8230-a7ab-4846-8998-efc4a7a35746)


4 - Consolidated user audio correlative feature data into a single mean feature vector
![image](https://github.com/JaySakarvadia/CDC2023/assets/111033138/1744a779-3d88-4812-a8fd-3232e4d9c369)


5 - Collected distance between user vector and playlist vector across 3D linear space using distance formula across

6 - Coverted distance to % using normalization formula: (max_distance-actual_distance)/max_distance
