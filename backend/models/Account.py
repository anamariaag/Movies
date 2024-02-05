from data.connect_db import COLLECTION_MOVIES
import Movie

class Account:
    '''Account class for the users'''
    def __init__(self, username) -> None:
        self.username = username
        self.rented_movies_id = []

    def rent_movie(self, movie_id) -> None:
        movie = Movie.mongo_to_movie(movie_id)
        if movie["status"] == "available":
            self.rented_movies.append(movie_id)
            new_movie = COLLECTION_MOVIES.find_one_and_update({"id" : movie_id}, {"status" : "Rented"})
            return f'Movie {movie["title"]} rented'
        else:
            return 'Movie is not available'
    
    def rented_movies(self):
        rented_movies = []
        for id in self.rented_movies_id:
            movie = Movie.mongo_to_movie(id)
            rented_movies.append(movie)
        return rented_movies
    
    def to_dict(self):
        return {
            "username" : self.username,
            "rented_movies_id" : self.rented_movies_id
        }

