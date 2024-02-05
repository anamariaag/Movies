from data.connect_db import COLLECTION_MOVIES
from Movie import Movie
from bson import ObjectId

class Account:
    '''Account class for the users'''
    def __init__(self, username) -> None:
        self.username = username
        self.rented_movies_id = []

    def rent_movie(self, _id) -> None:
        '''Changes status state to rented and adds the movie Objectid to a list'''
        movie = Movie.mongo_to_movie(_id)
        movie_id = ObjectId(_id)
        if movie.status == "available":
            self.rented_movies_id.append(movie_id)
            new_movie = COLLECTION_MOVIES.find_one_and_update({"_id" : movie_id}, {"$set" :{"status" : "rented"}})
            return f'Movie {movie.title} rented'
        else:
            return 'Movie is not available'
    
    def rented_movies(self) ->[Movie]:
        '''Returns all the rented movies in the account'''
        rented_movies = []
        for _id in self.rented_movies_id:
            movie = Movie.mongo_to_movie(_id)
            rented_movies.append(movie)
        return rented_movies
    
    def to_dict(self) -> dict:
        '''Transforms the account object to dictionary'''
        return {
            "username" : self.username,
            "rented_movies_id" : self.rented_movies_id
        }

