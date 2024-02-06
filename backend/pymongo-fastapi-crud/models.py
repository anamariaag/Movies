import uuid
from typing import Optional, Union
from pydantic import BaseModel, Field

class Person(BaseModel):
    id: Optional[str] = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    email: str = Field(...)
    pasword: str = Field(...)
    type: str = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "Don Quixote",
                "email": "Miguel de Cervantes",
                "password": "...",
                "type": "USER"
            }
        }
        
class PersonUpdate(BaseModel):
    name: str = Field(...)
    email: str = Field(...)
    pasword: str = Field(...)
    type: str = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "Don Quixote",
                "email": "Miguel de Cervantes",
                "password": "...",
                "type": "USER"
            }
        }
        
        
class Movie(BaseModel):
    title: str = Field(...)
    price: float = Field(...)
    directors: list[str] = Field(...)
    cast:  list[str] = Field(...)
    fullplot: Union[None, str] = Field(...)
    genres: list[str] = Field(...)
    plot: Union[None, str] = Field(...)
    image_url: Union[None, str] = Field(...)
    status: str = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Don Quixote",
                "price": 65.3,
                "directors": "Miguel de Cervantes",
                "full_ploat": "jflsdkjlf",
                "plot": "",
                "image_url": "",
                "status": "Rented"
            }
        }
        
        
class MovieUpdate(BaseModel):
    title: str = Field(...)
    price: float = Field(...)
    directors: list[str] = Field(...)
    cast:  list[str] = Field(...)
    fullplot: str = Field(...)
    genres: list[str] = Field(...)
    plot: str = Field(...)
    image_url: str = Field(...)
    status: str = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "title": "Don Quixote",
                "price": 65.3,
                "directors": "Miguel de Cervantes",
                "full_ploat": "jflsdkjlf",
                "plot": "",
                "image_url": "",
                "status": "Rented"
            }
        }