from database import movies_collection
from bson import ObjectId

def create_movie(movie_dict):
    return movies_collection.insert_one(movie_dict)

def get_all_movies():
    return list(movies_collection.find())

def get_movie_by_id(movie_id):
    return movies_collection.find_one({"_id": ObjectId(movie_id)})

def update_movie(movie_id, movie_dict):
    return movies_collection.update_one({"_id": ObjectId(movie_id)}, {"$set": movie_dict})

def delete_movie(movie_id):
    return movies_collection.delete_one({"_id": ObjectId(movie_id)})
