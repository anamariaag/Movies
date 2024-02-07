from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Person, PersonUpdate, Movie, MovieUpdate

router = APIRouter()


'''Routes for person'''
@router.post("/person", response_description="Create a new person", status_code=status.HTTP_201_CREATED, response_model=Person)
def create_person(request: Request, person: Person = Body(...)):
    person = jsonable_encoder(person)
    new_person = request.app.database["Person"].insert_one(person)
    created_person = request.app.database["Person"].find_one(
        {"_id": new_person.inserted_id}
    )
    return created_person

@router.get("/person", response_description="List all users", response_model=List[Person])
def list_person(request: Request):
    persons = list(request.app.database["Person"].find(limit=100))
    return persons



'''Routes for movies'''
@router.post("/movies", response_description="Create a new movie", status_code=status.HTTP_201_CREATED, response_model=Movie)
def create_book(request: Request, book: Movie = Body(...)):
    movie = jsonable_encoder(movie)
    new_movie = request.app.database["Movies"].insert_one(movie)
    created_movie = request.app.database["Movies"].find_one(
        {"_id": new_movie.inserted_id}
    )

    return created_movie

@router.get("/movies", response_description="List all movies", response_model=List[Movie])
def list_movie(request: Request):
    movies = list(request.app.database["Movies"].find(limit=100))
    return movies

@router.get("/movies/{id}", response_description="Get a single movie by id", response_model=Movie)
def find_movie(id: str, request: Request):
    if (movie := request.app.database["Movies"].find_one({"_id": id})) is not None:
        return movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {id} not found")

@router.put("/movies/{id}", response_description="Update a movie", response_model=Movie)
def update_movie(id: str, request: Request, movie: MovieUpdate = Body(...)):
    movie = {k: v for k, v in movie.dict().items() if v is not None}
    if len(movie) >= 1:
        update_result = request.app.database["Movies"].update_one(
            {"_id": id}, {"$set": movie}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {id} not found")

    if (
        existing_movie := request.app.database["Movies"].find_one({"_id": id})
    ) is not None:
        return existing_movie

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {id} not found")

@router.delete("/movies/{id}", response_description="Delete a movie")
def delete_movie(id: str, request: Request, response: Response):
    delete_result = request.app.database["Movies"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with ID {id} not found")


'''Routes for account'''