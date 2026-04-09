from repositories.movie_repository import *
from bson import ObjectId

def format_movie(movie):
    movie["_id"] = str(movie["_id"])
    return movie

def create_movie_service(movie):
    result = create_movie(movie.model_dump())
    return {"message": "Movie created", "id": str(result.inserted_id)}

def get_all_movies_service():
    movies = get_all_movies()
    return [format_movie(m) for m in movies]

def get_movie_by_id_service(movie_id):
    try:
        movie = get_movie_by_id(movie_id)
    except:
        return {"error": "Invalid ID"}
    if not movie:
        return {"error": "Movie not found"}
    return format_movie(movie)

def update_movie_service(movie_id, movie):
    try:
        result = update_movie(movie_id, movie.model_dump())
    except:
        return {"error": "Invalid ID"}
    if result.matched_count == 0:
        return {"error": "Movie not found"}
    return {"message": "Movie updated"}

def delete_movie_service(movie_id):
    try:
        result = delete_movie(movie_id)
    except:
        return {"error": "Invalid ID"}
    if result.deleted_count == 0:
        return {"error": "Movie not found"}
    return {"message": "Movie deleted"}
