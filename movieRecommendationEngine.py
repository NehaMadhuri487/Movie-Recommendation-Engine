import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from fuzzywuzzy import fuzz

# Load dataset
movies = pd.read_csv('movies.csv')

# --- Helper functions ---
def extract_title(title):
    year = title[len(title)-5:len(title)-1]
    if year.isnumeric():
        return title[:len(title)-7]
    else:
        return title

def extract_year(title):
    year = title[len(title)-5:len(title)-1]
    if year.isnumeric():
        return int(year)
    else:
        return np.nan

# Clean and preprocess
movies.rename(columns={'title': 'title_year'}, inplace=True)
movies['title_year'] = movies['title_year'].apply(lambda x: x.strip())
movies['title'] = movies['title_year'].apply(extract_title)
movies['year'] = movies['title_year'].apply(extract_year)
movies = movies[~(movies['genres'] == '(no genres listed)')].reset_index(drop=True)
movies['genres'] = movies['genres'].str.replace('|', ' ')
movies['genres'] = movies['genres'].str.replace('Sci-Fi', 'SciFi')
movies['genres'] = movies['genres'].str.replace('Film-Noir', 'Noir')

# TF-IDF and similarity matrix
tfidf_vector = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vector.fit_transform(movies['genres'])
sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)

# --- Utility functions ---
def get_title_year_from_index(index):
    return movies[movies.index == index]['title_year'].values[0]

def get_index_from_title(title):
    return movies[movies.title == title].index.values[0]

def matching_score(a, b):
    return fuzz.ratio(a, b)

def get_title_from_index(index):
    return movies[movies.index == index]['title'].values[0]

def find_closest_title(title):
    leven_scores = list(enumerate(movies['title'].apply(matching_score, b=title)))
    sorted_leven_scores = sorted(leven_scores, key=lambda x: x[1], reverse=True)
    closest_title = get_title_from_index(sorted_leven_scores[0][0])
    distance_score = sorted_leven_scores[0][1]
    return closest_title, distance_score

# --- Recommender function (unchanged logic) ---
def contents_based_recommender(movie_user_likes, how_many):
    closest_title, distance_score = find_closest_title(movie_user_likes)

    if distance_score == 100:
        movie_index = get_index_from_title(closest_title)
        movie_list = list(enumerate(sim_matrix[int(movie_index)]))
        similar_movies = list(
            filter(lambda x: x[0] != int(movie_index),
                   sorted(movie_list, key=lambda x: x[1], reverse=True))
        )
        print(f"Here's the list of movies similar to {closest_title}:\n")
        for i, s in similar_movies[:how_many]:
            print(get_title_year_from_index(i))
    else:
        print(f"Did you mean {closest_title}?\n")
        movie_index = get_index_from_title(closest_title)
        movie_list = list(enumerate(sim_matrix[int(movie_index)]))
        similar_movies = list(
            filter(lambda x: x[0] != int(movie_index),
                   sorted(movie_list, key=lambda x: x[1], reverse=True))
        )
        print(f"Here's the list of movies similar to {closest_title}:\n")
        for i, s in similar_movies[:how_many]:
            print(get_title_year_from_index(i))
