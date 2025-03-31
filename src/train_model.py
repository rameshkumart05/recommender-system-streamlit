'''Data pipeline & model training function for KNN movie recommendation system.'''

import pickle
import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load the movie data
movies=pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/k-nearest-neighbors-project-tutorial/main/tmdb_5000_movies.csv')
credits=pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/k-nearest-neighbors-project-tutorial/main/tmdb_5000_credits.csv')

# Join movies and credits dataframes
credits.rename({'movie_id': 'id'}, axis=1, inplace=True)
data_df=pd.merge(movies, credits, on='id', how='outer')
data_df.drop(['title_x', 'title_y'], axis=1, inplace=True)
data_df.rename({'original_title': 'title'}, axis=1, inplace=True)

# Encode features
data_df['cast']=data_df['cast'].apply(lambda x: [item['name'] for item in json.loads(x)][:3] if pd.notna(x) else None)
data_df['keywords']=data_df['keywords'].apply(lambda x: [item['name'] for item in json.loads(x)][:3] if pd.notna(x) else 'none')
data_df['genres']=data_df['genres'].apply(lambda x: [item['name'] for item in json.loads(x)][:3] if pd.notna(x) else 'none')
data_df['overview']=data_df['overview'].apply(lambda x: [x if pd.notna(x) else 'none'])
data_df['tags']=data_df['overview'] + data_df['genres'] + data_df['keywords'] + data_df['cast']
data_df['tags']=data_df['tags'].apply(lambda x: ', '.join(x))

# Vectorize the 'tags' string feature using TF-IDF (text frequency, inverse document frequency)
vectorizer=TfidfVectorizer()
tfidf_matrix=vectorizer.fit_transform(data_df['tags'])

# Instantiate and train the nearest neighbors model
model=NearestNeighbors(n_neighbors=5, algorithm='brute', metric='cosine')
fit_result=model.fit(tfidf_matrix)

# Save the assets
pickle.dump(model, open('models/model.pkl', 'wb'))
pickle.dump(tfidf_matrix, open('data/tfidf_matrix.pkl', 'wb'))
pickle.dump(data_df, open('data/encoded_features_df.pkl', 'wb'))