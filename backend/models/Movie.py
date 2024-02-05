from __future__ import annotations
from data.connect_db import COLLECTION_MOVIES
from bson import ObjectId
class Movie():
    '''Movie class to create and get movies from the database'''
    def __init__(self, title: str, price: int, directors: [str], fullplot: str, plot: str, image_url: str, status: str) -> None:
        '''Initialize the Movie object'''
        self.title = title
        self.price = price
        self.directors = directors
        self.full_plot = fullplot
        self.plot = plot
        self.image_url = image_url
        self.status = status
    
    @staticmethod
    def mongo_to_movie(_id) -> Movie:
        movie_id = ObjectId(_id)
        res = COLLECTION_MOVIES.find_one({"_id" : movie_id})
        if res is None:
            return f'Movie not found'
        else:
            response_movie = Movie(res['title'], res['price'], res['directors'], res['fullplot'], res['plot'], res['image_url'], res['status'])
            return response_movie 

