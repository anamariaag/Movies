from data.connect_db import COLLECTION_MOVIES
class Movie():
    '''Movie class to create and get movies from the database'''
    def __init__(self, id: str, title: str, price: int, directors: [str], fullplot: str, plot: str, image_url: str, status: str) -> None:
        '''Initialize the Movie object'''
        self.id = id
        self.title = title
        self.price = price
        self.directors = directors
        self.full_plot = fullplot
        self.plot = plot
        self.image_url = image_url
        self.status = status
    
    @staticmethod
    def mongo_to_movie(_id):
        res = COLLECTION_MOVIES.find_one({"_id" : _id})
        if res is None:
            return f'Movie not found'
        else:
            response_movie = Movie(res['_id'], res['title'], res['price'], res['directors'], res['fullplot'], res['plot'], res['image_url'], res['status'])
            return response_movie 

