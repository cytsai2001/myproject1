import csv
import tmdbsimple as tmdb
import datetime
import json
import os
import numpy as np

# Set up API key and initialize TMDb object
tmdb.API_KEY = '58ab053e5128c03492cebf4e5439ed72'

# Set up cache directory and file name
cache_dir = './cache'
cache_file = os.path.join(cache_dir, 'movies_cache.json')

# Define function to retrieve movies with a specific genre, release date range, and language
def get_movies(genre_id=None, start_date=None, end_date=None, language=None):
    # Initialize cache data
    cache_data = {
        'expires': datetime.datetime.now().timestamp() + 86400, # Cache for 1 day
        'movies': []
    }

    # Build query parameters based on provided criteria
    params = {}
    if genre_id:
        params['with_genres'] = str(genre_id)
    if start_date:
        params['primary_release_date.gte'] = start_date
    if end_date:
        params['primary_release_date.lte'] = end_date
    if language:
        params['language'] = language

    # Retrieve movie data and cache it
    discover = tmdb.Discover()
    page = 1
    total_pages = 1
    while page <= total_pages:
        params['page'] = page
        response = discover.movie(**params)
        movies = response['results']
        cache_data['movies'] += movies
        total_pages = response['total_pages']
        page += 1

    os.makedirs(cache_dir, exist_ok=True)
    with open(cache_file, 'w') as f:
        json.dump(cache_data, f)

    return cache_data['movies']


def get_movie_genres(movie_i_dot_genres):
    return_list = []
    for i in movie_i_dot_genres:
        for j in i.items():
            if type(j[1]) != int:
                return_list.append(j[1])
    return return_list


def get_production_companies(movie_i_dot_production_companies):
    return_list = []
    for i in movie_i_dot_production_companies:
        for j in i.items():
            if j[0] == "name":
                return_list.append(j[1])
    return return_list


def get_watch_provider(movie_i_dot_watch_providers):
    try:
        return_list = [i['provider_name'] for i in movie_i_dot_watch_providers["results"]["TW"]["flatrate"]]
    except KeyError:
        return_list = []
    return return_list


# Retrieve movies with specific criteria and write them to a CSV file
genre_id = 28
start_date = '2018-01-01'
end_date = '2023-05-30'
language = 'en'
movies = get_movies(genre_id=genre_id, start_date=start_date, end_date=end_date, language=language)

print("cache done")

# Define header row for CSV file
header = ['Title', 'Release Date', 'Popularity', 'Budget', 'Revenue', 'vote_average', 'vote_count', 'adult', 'runtime', 'genre']

# Write movie data to CSV file
with open('act_movies_2018-_new1.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for movie in movies:
        # Convert movie to a tmdb.Movies object and retrieve required properties
        movie_obj = tmdb.Movies(movie['id'])
        movie_obj.info()
        row = [movie_obj.title, movie_obj.release_date, movie_obj.popularity, movie_obj.budget, movie_obj.revenue,
               movie_obj.vote_average, movie_obj.vote_count, movie_obj.adult, movie_obj.runtime]

        writer.writerow(row)
