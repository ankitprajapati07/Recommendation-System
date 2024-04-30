from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np


df = pd.read_csv('user_interactions.csv')

# Extract features (interaction_type)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['interaction_type'])

# Convert to dense vector
vectors = np.asarray(X.todense())

# Calculate similarity matrix
similarity_matrix = cosine_similarity(vectors)


# Get recommendations
def get_recommendations(product_id, similarity_matrix, num_recommendations):
    product_idx = df[df['product_id'] == product_id].index[0]
    similarity_scores = list(enumerate(similarity_matrix[product_idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:num_recommendations + 1]

    product_indices = [i[0] for i in similarity_scores]
    return df['product_id'].iloc[product_indices]


# Test the function
print(get_recommendations('b91e90e8-2d2e-4a31-bd83-15e54b736296', similarity_matrix, 6))
