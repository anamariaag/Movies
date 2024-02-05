from __future__ import annotations
from data.connect_db import COLLECTION_MOVIES, COLLECTION_PERSON
from abc import abstractmethod
from Movie import Movie
from Account import Account
from bson import ObjectId
import json

class Person():
    '''Person class to save user data'''
    def __init__(self, id: str, name: str, mail: str, password: str, type_account: str) -> None:
        '''Constructor for Person class'''
        self.id: str = id
        self.name: str = name
        self.mail: str = mail
        self.password: str = password
        self.type_account: str = type_account

    @abstractmethod
    def mongo_to_person(self, id) -> object:
        '''Abstract method to convert a mongo json to a person object'''
        pass


class Administrator(Person):
    '''Administrator class dor the accounts that will have special privileges'''
    def __init__(self, _id: str, name: str, mail: str, password: str) -> None:
        '''Initialize an administrator account'''
        super().__init__(_id, name, mail, password, "admin")
        admin = {"id": _id,
                 "name": name,
                 "mail": mail,
                 "password" : password,
                 "type_account": "admin"}
        COLLECTION_PERSON.insert_one(admin)
        
    @staticmethod
    def create_movie(movie: Movie) -> str:
        '''Creates movie with a Movie object'''
        movie_json = {"title" : movie.title,
                    "price" : movie.price,
                    "directors" : movie.directors,
                    "full_plot" : movie.full_plot,
                    "plot" : movie.plot,
                    "image_url": movie.image_url,
                    "status" : movie.status
                    }
        new_movie = COLLECTION_MOVIES.insert_one(movie_json)
        return f'Movie added to collection'
    
    @staticmethod
    def read_movies(filters) -> [Movie]:
        '''Returns all the movies in the page following the given filters'''
        res = COLLECTION_MOVIES.find({})
        movies = []
        for document in res:
            if document is None:
                continue
            movie = Movie.mongo_to_movie(document["_id"])
            movies.append(movie)  
        return movies
    
    @staticmethod
    def update_movie(_id: str, content_to_change: Movie) -> str:
        '''Updates a movie in the database'''
        movie_id = ObjectId(_id)
        update_movie = {
            "$set" : {
                "title" : content_to_change.title,
                "price" : content_to_change.price,
                "directors" : content_to_change.directors,
                "full_plot" : content_to_change.full_plot,
                "plot" : content_to_change.plot,
                "image_url": content_to_change.image_url,
                "status" : content_to_change.status
            }
        }

        res = COLLECTION_MOVIES.find_one_and_update({"_id" : movie_id}, update_movie, {"new" : "true"})
        if res is None:
            return f'Movie not found'
        else:
            return f'Movie updated successfully'
    
    @staticmethod
    def delete_movie(_id) -> str:
        '''Deletes a movie from the database'''
        movie_id = ObjectId(_id)
        res = COLLECTION_MOVIES.find_one_and_delete({"_id" : movie_id})
        if res  is None:
            return f'Movie not found'
        else:
            return f'Movie has been deleted succesfully'
    
    @staticmethod
    def get_user(_id) -> User:
        '''Returns the specified user from the database'''
        user_id = ObjectId(_id)
        res = COLLECTION_PERSON.find_one({"_id" : user_id})
        if res is None:
            return f'User not found'
        else:
            response_user = User.mongo_to_person(_id)
            return response_user 
    
    @staticmethod
    def get_users():
        '''Returns an array of all the users'''
        res = COLLECTION_PERSON.find({})
        users = []
        for document in res:
            if document is None:
                continue
            if document["type_account"] == "user":
                user = User.mongo_to_person(document["_id"])
                users.append(user)  
        return users
    
    @staticmethod
    def mongo_to_person(_id: str) -> str: 
        '''Converts a mongo document to a Admin object'''
        admin_id = ObjectId(_id)
        res = COLLECTION_PERSON.find_one({"_id" : admin_id})
        if res is None:
            return f'Admin not found'
        else:
            response_person = Person(res['id'], res['name'], res['mail'], res['password'], res['type_account'])
            return response_person 

class User(Person):
    '''Default user class'''
    def __init__(self, _id: str, name: str, mail: str, password: str):
        super().__init__(_id, name, mail, password, "user")
        self.accounts = []
        user = {"id": _id,
                 "name": name,
                 "mail": mail,
                 "password" : password,
                 "accounts": self.accounts,
                 "type_account": "user"}
        COLLECTION_PERSON.insert_one(user)
    
    def create_account(self, username: str) -> None:
        '''Creates an account for the user and appends it to the accounts list'''
        account = Account(username)
        self.accounts.append(account)
        accounts_dict = [account.to_dict() for account in self.accounts]
        update_user = {
            "$set" : {
                "accounts" : accounts_dict
            }
        }
        res = COLLECTION_PERSON.find_one_and_update({"id" : self.id}, update_user, return_document=True)
    
    @staticmethod
    def mongo_to_person(_id: str) -> None:
        '''Converts a Mongo document into a User object'''
        person_id = ObjectId(_id) 
        res = COLLECTION_PERSON.find_one({"_id" : person_id})
        if res is None:
            return f'User not found'
        else:
            response_person = Person(res['id'], res['name'], res['mail'], res['password'], res['type_account'])
            return response_person 


# admin = Administrator("admin_1", "Jorge", "jorge@gmail", "123")
# movie = Movie.mongo_to_movie('65bea9e0c1ecc99b1b6283da')
# movie.price = 299
# admin.update_movie('65bea9e0c1ecc99b1b6283da', movie)
# created_movie = Movie("Avengers", 199, ["Joe Russo", "Anthony Russo", "Josh Wedon"], "Avengers fight aliens that invade New York", "Avengers fight", "image.url", "available")
# admin.create_movie(created_movie)

        
# user = User("user_1", "Miguel", "miguel@gmail", "321")
# user.create_account("miguelito122")
# user.accounts[0].rent_movie('65bea9e0c1ecc99b1b6283d9')
