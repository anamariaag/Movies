from __future__ import annotations
from data.connect_db import COLLECTION_MOVIES, COLLECTION_PERSON
from abc import abstractmethod
from Movie import Movie
from Account import Account
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
    def mongo_to_person(self, id):
        '''Abstract method to get information of a specified user from the database'''
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
    def create_movie(movie: Movie):
        movie_json = {"id" : movie.id,
                    "title" : movie.name,
                    "price" : movie.price,
                    "directors" : movie.directors,
                    "full_plot" : movie.full_plot,
                    "plot" : movie.plot,
                    "image_url": movie.image_url,
                    "status" : movie.status
                    }
        new_movie = COLLECTION_MOVIES.insert_one(json.dumps(movie_json))
        return new_movie
    
    @staticmethod
    def read_movies(filters) -> [Movie]:
        res = COLLECTION_MOVIES.find({})
        movies = []
        for document in res:
            if document is None:
                continue
            movie = Movie.mongo_to_movie(document["_id"])
            movies.append(movie)  
        return movies
    
    @staticmethod
    def update_movie(_id, content_to_change):
        update_movie = {
            "$set" : {
                "id" : content_to_change.id,
                "title" : content_to_change.name,
                "price" : content_to_change.price,
                "directors" : content_to_change.directors,
                "full_plot" : content_to_change.full_plot,
                "plot" : content_to_change.plot,
                "image_url": content_to_change.image_url,
                "status" : content_to_change.status
            }
        }

        res = COLLECTION_MOVIES.find_one_and_update({"_id" : _id}, update_movie, {"new" : "true"})
        return res
    
    @staticmethod
    def get_user(_id) -> User:
        res = COLLECTION_PERSON.find_one({"_id" : _id})
        if res is None:
            return f'User not found'
        else:
            response_user = User.mongo_to_person(_id)
            return response_user 
    
    @staticmethod
    def get_users():
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
    def mongo_to_person(id: str) -> None: 
        res = COLLECTION_PERSON.find_one({"id" : id})
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
        res = COLLECTION_PERSON.find_one({"id" : _id})
        if res is None:
            return f'User not found'
        else:
            response_person = Person(res['id'], res['name'], res['mail'], res['password'], res['type_account'])
            return response_person 


# admin = Administrator("admin_1", "Jorge", "jorge@gmail", "123")
        
# user = User("user_1", "Miguel", "miguel@gmail", "321")
# user.create_account("miguelito122")
