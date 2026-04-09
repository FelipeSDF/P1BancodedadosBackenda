from fastapi import APIRouter
from schemas.movie_schema import Movie
from services.movie_service import *

router = APIRouter()

@router.get("/movies")
def list_movies():
    return get_all_movies_service()

@router.post("/movies")
def create_movie_route(movie: Movie):
    return create_movie_service(movie)

@router.get("/movies/{movie_id}")
def get_movie_route(movie_id: str):
    return get_movie_by_id_service(movie_id)

@router.put("/movies/{movie_id}")
def update_movie_route(movie_id: str, movie: Movie):
    return update_movie_service(movie_id, movie)

@router.delete("/movies/{movie_id}")
def delete_movie_route(movie_id: str):
    return delete_movie_service(movie_id)
