import numpy as np
import pandas as pd

def cosine_calc(user_df, playlist_df):
    # Convert dataframes to numpy arrays
    vec1 = user_df.values.flatten()
    vec2 = playlist_df.values.flatten()

    # Compute the dot product
    dot_product = np.dot(vec1, vec2)
    
    # Compute the magnitudes of the vectors
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    
    # Compute the cosine similarity
    similarity = dot_product / (norm_vec1 * norm_vec2)
    
    #Covert cosine similarity to degrees
    similarity_rad = np.arccos(np.clip(similarity, -1.0, 1.0))
    similarity_deg = np.degrees(similarity_rad)
    
    return similarity_deg




# # Example usage
# user_df = pd.DataFrame({'features': [1, 2, 3]})
# playlist_df = pd.DataFrame({'features': [3, 2, 1]})
# print(cosine_calc(user_df, playlist_df))





