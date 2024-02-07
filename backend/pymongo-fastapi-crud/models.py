import uuid
from typing import Optional, Union
from pydantic import BaseModel, Field      
from typing import Any
from typing import Annotated, Union
from bson import ObjectId
from typing import Annotated, Any, Callable

from bson import ObjectId
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
class _ObjectIdPydanticAnnotation:
    # Based on https://docs.pydantic.dev/latest/usage/types/custom/#handling-third-party-types.

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: Callable[[Any], core_schema.CoreSchema],
    ) -> core_schema.CoreSchema:
        def validate_from_str(input_value: str) -> ObjectId:
            return ObjectId(input_value)

        return core_schema.union_schema(
            [
                # check if it's an instance first before doing any further work
                core_schema.is_instance_schema(ObjectId),
                core_schema.no_info_plain_validator_function(validate_from_str),
            ],
            serialization=core_schema.to_string_ser_schema(),
        )

PydanticObjectId = Annotated[
    ObjectId, _ObjectIdPydanticAnnotation
]
        
class Movie(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
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
        

class Person(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
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
        
