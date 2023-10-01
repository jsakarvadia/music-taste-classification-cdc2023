import numpy as np
import pandas as pd

def cosine_similarity(df1, df2):
    # Convert dataframes to numpy arrays
    vec1 = df1.values.flatten()
    vec2 = df2.values.flatten()

    # Compute the dot product
    dot_product = np.dot(vec1, vec2)
    
    # Compute the magnitudes of the vectors
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    
    # Compute the cosine similarity
    similarity = dot_product / (norm_vec1 * norm_vec2)
    
    return similarity

# Example usage
df1 = pd.DataFrame({'features': [1, 2, 3]})
df2 = pd.DataFrame({'features': [1, 2, 3]})
print(cosine_similarity(df1, df2))

