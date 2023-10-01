# CDC2023
----------
This project was completed collabratively between Jay Sakarvadia and Jack Pamukci. Both individuals took lead on a portion of the project, but still worked collabratively with each other to contribute to the other parts as well.
----------------
Project Overview
----------------
## Inspiration
Our inspiration came from the theme of nostalgia and our core memories watching sitcoms of the late 90s and 2000s. Given that music plays such a large part in the lives of people and that there is publicly available APIs such as Spotify, we can harness our patterns of listening to give us a bit more insight and comparison to some of our favorite TV characters.
## Objective
This app takes a users most listened to songs and classifies them as one of many sitcom characters from the following shows:
- Friends
- How I Met Your Mother
- The Office
The only input needed from the user would be to log into Spotify.
## Build Process
With the Spotify API we are able to do two things:
1. Pull a user's top 100 tracks
2. Pull all tracks from any specific playlist 
This means that we can create feature vectors for both and compare them using both cosine similarity and euclidean distance. We decided to compare our user tracks with pre-selected playlists on Spotify which are created with a certain tv show character in mind, and from there give classifications.
## Challenges
The Spotify API is a bit challenging to work with because of two things:
1. Token and User Authentication
- Given that we are still in development mode (which limits capabilities from the API), any user that would like to login through our app to see which tv show character they are would need to be added to the list of users with access to creating a token. This severely neuters the scope of which we would like our application to be ran.
2. Running out of API calls
- The most crippling issue we came across was running out of API calls for our accounts. Through testing and debugging, we would go over our limit which was very small and would have to create a new Spotify account to get a fresh account. This was very time consuming. 
## Accomplishments
We are very proud of the goals and management we partook throughout the project. Our original idea ended up working exactly as we planned and we are very proud and grateful that it turned out this way.
## Takeaways
We learned much about not only authorization and tokens for APIs, but also the mathematical nature of recommendation systems as well as the differences between Content-Based Filtering and Collaborative Filtering. Overall the experience was very rewarding and fruitful for us!
## What's Next?
Our next goal would be to create a nice front end and hopefully ask Spotify for better API access which would allow anyone to use the app and to also use it without running into any limits!
----------------
General Outline
---------------
1 - Connect to Spotify API (created subsequent methods for API connection)

2 - Build get_user (audio feature data given users top 100 long-term songs) & get_playlist (audio feature data given selected playlist) methods to pull relevent audio feature data

Cosine Similarity - Jay (Lead)
------------------
3 - Code method to preprocess data by dropping categorical variables (one-hot encoding proved to be inefficent), and by using max-min normalization for all numeric features

4 - Code method to consolidate both user and playlist audio feature data into a single mean feature vector
![image](https://github.com/JaySakarvadia/CDC2023/assets/107783145/14bdcda4-d622-4dee-a167-9325d02839bf)
![image](https://github.com/JaySakarvadia/CDC2023/assets/107783145/e85b0cc1-cf83-434f-ac62-1f635e4f94d2)

5 - Code method to calculate cosine similarities (angle between two vectors in space; user vector and playlist vector)
using equation, then converting output to radians, and then degrees in order to eventually be able to understand
![image](https://github.com/JaySakarvadia/CDC2023/assets/107783145/285f7a01-f816-46dd-b03c-115664d014a6)



6 - Implement all methods in algorithmic analysis notebook to see results
% Similarity Breakdown
![image](https://github.com/JaySakarvadia/CDC2023/assets/107783145/c0e91244-5e89-49ad-8ad9-b17d31ccbb30)




Euclidean Distance - Jack (Lead)
------------------
3 - Regression analysis for audio feature selection; take 3 most correlative features 


(below represents strong correlation between ranking of song and the feature)
![image](https://github.com/JaySakarvadia/CDC2023/assets/111033138/180a8230-a7ab-4846-8998-efc4a7a35746)


4 - Consolidated user audio correlative feature data into a single mean feature vector
![image](https://github.com/JaySakarvadia/CDC2023/assets/111033138/6ec7c9ae-59a5-4309-85e3-c3b274cf03d5)


5 - Collected distance between user vector and playlist vector across 3D linear space using distance formula and converting distance to % using inverse normalization formula: (1  / actual_distance) * 100

![image](https://github.com/JaySakarvadia/CDC2023/assets/111033138/bc36047d-9074-4619-a605-90ae0f61b60f)

