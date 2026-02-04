import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

user_movie_matrix = ratings.pivot_table(
    index='userId',
    columns='movieId',
    values='rating'
).fillna(0)

user_similarity = cosine_similarity(user_movie_matrix)

def recommend_movies(user_id, n_recommendations=5):
    user_index = user_movie_matrix.index.tolist().index(user_id)

    sim_scores = user_similarity[user_index]

    weighted_ratings = user_movie_matrix.T.dot(sim_scores)

    scores = pd.Series(weighted_ratings, index=user_movie_matrix.columns)

    watched = ratings[ratings['userId'] == user_id]['movieId']
    scores = scores.drop(watched)

    recommended_movie_ids = scores.sort_values(ascending=False).head(n_recommendations).index

    return movies[movies['movieId'].isin(recommended_movie_ids)][['movieId', 'title']]

try:
    uid = int(input("Enter user ID (1-610): ").strip())
    print(recommend_movies(uid))
except ValueError:
    print(" Please enter a valid number between 1 and 610")
except Exception as e:
    print("Error:", e)

